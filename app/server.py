from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn
from .langchain_client import get_langchain_response, stream_langchain_response

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    session_id = websocket.client.host  # Use client IP as session ID
    try:
        while True:
            data = await websocket.receive_text()
            response = get_langchain_response(data, session_id=session_id)
            await websocket.send_text(response)
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {e}")
        await websocket.close()
    finally:
        print("connection closed")

@app.websocket("/ws/stream")
async def websocket_stream_endpoint(websocket: WebSocket):
    await websocket.accept()
    session_id = websocket.client.host  # Use client IP as session ID
    try:
        while True:
            data = await websocket.receive_text()
            async for chunk in stream_langchain_response(data, session_id=session_id):
                await websocket.send_text(chunk)
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {e}")
        await websocket.close()
    finally:
        print("connection closed")

def run_server():
    uvicorn.run(app, host="0.0.0.0", port=8000, ws_ping_interval=20, ws_ping_timeout=20)

if __name__ == "__main__":
    while True:
        try:
            run_server()
        except Exception as e:
            print(f"Server error: {e}")
        print("Restarting server...")
