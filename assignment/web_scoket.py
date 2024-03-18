import websocket
import threading

# WebSocket server URL
ws_url = "ws://assemblix:8383"

# Message to send
message = "Hello, WebSocket!"

# Function to handle WebSocket open
def on_open(ws):
    print("Connected to WebSocket server")
    # Send the message
    ws.send(message)
    print("Sent message:", message)

# Function to handle received message
def on_message(ws, message):
    # new_m = []
    new_m= message.split(',')
    print("Received message:",new_m)

# Function to handle WebSocket close
def on_close(ws):
    print("Connection to WebSocket server closed")

def run_websocket(): 
    
# Create WebSocket connection
    ws = websocket.WebSocketApp(ws_url,
                            on_message=on_message,
                            on_open=on_open,
                            on_close=on_close)


# Run WebSocket connection
    ws.run_forever()  

wet = threading.Thread(target=run_websocket)
wet.start()