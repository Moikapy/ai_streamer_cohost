import asyncio
import threading
import uvicorn
import signal
import sys
from websocket_client import communicate_with_ai, stream_communicate_with_ai

def start_fastapi():
    uvicorn.run("app.server:app", host="0.0.0.0", port=8000, ws_ping_interval=20, ws_ping_timeout=20)

async def main(mode):
    loop = asyncio.get_event_loop()
    executor = threading.Thread(target=start_fastapi)
    executor.start()

    # Run the WebSocket client in the main thread
    if mode == "1":
        await communicate_with_ai()
    else:
        await stream_communicate_with_ai()

def signal_handler(sig, frame):
    print("Signal received, shutting down...")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    mode = input("Choose mode: 1 for normal, 2 for streaming: ")
    try:
        asyncio.run(main(mode))
    except (KeyboardInterrupt, SystemExit):
        print("Process interrupted, shutting down...")
