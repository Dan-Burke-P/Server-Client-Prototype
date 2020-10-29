import socket
import struct
import time
from MessagePack import MessagePack, MsgType

if __name__ == '__main__':
    # Global variables
    node_name = "Test_name"
    central_server_name = "NOT SET"


# Attempt to establish connection to central server
def connect_to_server():
    # give global access to the central server name
    global central_server_name
    # give global access to the nodes name
    global node_name

    # Create and configure the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("\n")
    # Loop around to establish connection while using timeout to allow for interruption
    while True:
        print("Attempting to connect....")
        try:
            s.connect((socket.gethostname(), 1234))
        except socket.timeout:
            continue

        print("\nConnection established\n\nWaiting for next message....\n")
        break

    # Loop around receiving and sending messages to the server

    try:
        print("Establishing connection with central server...")
        msg_len = s.recv(4)
        msg_len = struct.unpack('i', msg_len)[0]
        central_server_name = s.recv(msg_len).decode("utf-8")
        print("RECEIVED - Central server name: ", central_server_name)
        print("SENDING - Node Client Name: ", node_name)
        msg_len = struct.pack('i', len(node_name))
        s.send(msg_len)
        s.send(bytes(node_name, "utf-8"))

        msg = MessagePack(MsgType.COMMAND)
        msg.send_message(s)


    except KeyboardInterrupt:
        s.close()
        exit(0)


if __name__ == '__main__':
    connect_to_server()
