import socket
import time
sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
sock.connect(("FC:A8:9A:00:14:9C",1))
# sock.bind(("FC:A8:9A:00:14:9C", 1)) # Use port 1 for Bluetooth
# sock.listen(1) # Listen for incoming connections
def read_switch_state():
    switch_state = 1 # Assuming the switch is ON initially
    return switch_state
def handle_client(client_socket):
    while True:
        switch_state = read_switch_state()
        client_socket.send(str(switch_state))
        time.sleep(1) # Sleep for 1 second before sending the next state
while True:
    client_socket, client_address = sock.accept()
    print(f"Accepted connection from {client_address}")
    handle_client(client_socket)