import time
import subprocess
import os

def start_server():
    return subprocess.Popen(["python", "-m", "app.server"])

def start_client(mode):
    return subprocess.Popen(["python", "websocket_client.py", mode])

def monitor_log_and_restart(mode):
    server_process = start_server()
    client_process = start_client(mode)

    log_file_path = 'server.log'
    last_position = 0

    while True:
        with open(log_file_path, "r") as log_file:
            log_file.seek(last_position)
            lines = log_file.readlines()
            last_position = log_file.tell()

            for line in lines:
                if "Client disconnected" in line or "connection closed" in line:
                    print("Detected client disconnection or connection closure. Restarting server and client...")
                    server_process.terminate()
                    client_process.terminate()
                    server_process = start_server()
                    client_process = start_client(mode)
                    time.sleep(1)  # Prevent rapid restart

        time.sleep(5)  # Check the log file every 5 seconds

if __name__ == "__main__":
    mode = input("Choose mode: 1 for normal, 2 for streaming: ")

    if not os.path.exists('server.log'):
        open('server.log', 'w').close()  # Create the log file if it doesn't exist

    monitor_log_and_restart(mode)
