import asyncio
import websockets

async def communicate_with_ai():
    uri = "ws://localhost:8000/ws"  # WebSocket server URL
    try:
        async with websockets.connect(uri, ping_interval=20, ping_timeout=60) as websocket:
            while True:
                message = input("You: ")  # Get user input
                await websocket.send(message)  # Send message to server
                response = await websocket.recv()  # Receive response from server
                print(f"AI: {response}")  # Print the response
    except websockets.ConnectionClosedError as e:
        print(f"Connection closed with error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

async def stream_communicate_with_ai():
    uri = "ws://localhost:8000/ws/stream"  # WebSocket server URL
    try:
        async with websockets.connect(uri, ping_interval=20, ping_timeout=60) as websocket:
            while True:
                message = input("You: ")  # Get user input
                await websocket.send(message)  # Send message to server
                while True:
                    try:
                        response = await websocket.recv()  # Receive response from server
                        print(f"AI: {response}")  # Print the response
                    except websockets.ConnectionClosedError as e:
                        print(f"Connection closed during stream with error: {e}")
                        break
    except websockets.ConnectionClosedError as e:
        print(f"Connection closed with error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    choice = input("Choose mode: 1 for normal, 2 for streaming: ")
    if choice == "1":
        asyncio.run(communicate_with_ai())
    else:
        asyncio.run(stream_communicate_with_ai())
