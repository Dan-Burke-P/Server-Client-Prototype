# Holds flags used to define message types inside of a packet
import struct
from enum import IntEnum
from socket import socket


class MsgType(IntEnum):
    INVALID = -1
    SINGLE_IMAGE = 1
    TEXT_MESSAGE = 2
    COMMAND = 3


# Abstraction meant to separate and encapsulate the data needed for the header
class Header:
    HEADER_SIZE = 8

    def __init__(self):
        # The length of the data in the packet
        self.data_length = 0
        self.messageType = MsgType.INVALID

    # Create the byte array for the header
    def encode_header(self):
        pass


# Unified system for holding messages, gives a standard interface
# through which we can serialize and deserialize data
class MessagePack:
    HEADER_SIZE = 0

    def __init__(self, message_type):
        self.length = 0
        self.message_type = message_type

    def send_message(self, connection: socket):
        msg = bytearray()
        # TODO verify the data is good to go before sending it
        message_type_bytes = struct.pack('i', int(self.message_type))
        length_bytes = struct.pack('i', self.length)
        msg = length_bytes + message_type_bytes
        connection.sendall(msg)
