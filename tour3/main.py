"""Client Side, just giving the file to the server and creating compressed file"""

import socket
from math import ceil


def main(filename, output, mode="encode") -> str:
    """Main function,
    mode='encode' or 'decode'"""
    host = "localhost"
    with open(filename, "r", encoding="utf-8") as file:
        data = file.read()
    if mode == "encode":
        data_to_send = []
        final = bytes()
        for i in data:
            data_to_send += i
        for i in range(ceil(len(data) / 1000)):
            sock = socket.socket()
            sock.connect((host, 9090))
            data_ = mode + "|"
            for i in range(1000):
                if len(data_to_send) != 0:
                    data_ += data_to_send.pop(0)
            sock.send(data_.encode())
            final += sock.recv(1024)
            sock.close()
    elif mode == "decode":
        data_to_send = []
        final = bytes()
        for i in data:
            data_to_send += i
        for i in range(len(data)):
            sock = socket.socket()
            sock.connect((host, 9090))
            data_ = mode + "|"
            if len(data_to_send) != 0:
                data_ += data_to_send.pop(0)
            sock.send(data_.encode())
            final += sock.recv(1024)
            sock.close()
    else:
        raise AttributeError('Attribute "mode" must be "encode" or "decode".')
    print(final.decode())
    with open(output, "wb") as f:
        f.write(final)
    return final.decode()


# main('tour3/server.py', 'tour3/finish.enc') #enc is from the word 'encoded'

print(main("tour3/finish.enc", "tour3/finish.txt", "decode"))
