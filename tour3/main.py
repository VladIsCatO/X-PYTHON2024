"""Client Side, just giving the file to the server and creating compressed file"""

import socket
import os
from math import ceil


class Client:
    """Client class"""

    def main(self, filename, output, mode="encode") -> str:
        """Main function,
        mode='encode' or 'decode'"""
        self.file_stats = os.stat(filename)
        with open(filename, "r", encoding="utf-8") as file:
            data = file.read()
        if mode == "encode":
            final = self.communicate(mode, data, 1000)

        elif mode == "decode":
            final = self.communicate(mode, data)
        else:
            raise AttributeError('Attribute "mode" must be "encode" or "decode".')
        print(final.decode())
        with open(output, "wb") as f:
            f.write(final)
        self.ready_file_stats = os.stat(output)
        return (
            final.decode(),
            {"before": self.file_stats, "after": self.ready_file_stats},
        )

    def communicate(self, mode: str, data, size=1):
        """Communicating with server"""
        host = "localhost"
        data_to_send = []
        final = bytes()
        for i in data:
            data_to_send += i
        for i in range(ceil(len(data) / size)):
            sock = socket.socket()
            sock.connect((host, 9090))
            data_ = mode + "|"
            for i in range(size):
                if len(data_to_send) != 0:
                    data_ += data_to_send.pop(0)
            sock.send(data_.encode())
            final += sock.recv(1024)
            sock.close()
        return final


if __name__ == "__main__":
    client = Client()
    client.main("tour3/server.py", "tour3/finish.enc")  # enc is from the word 'encoded'

    print(client.main("tour3/finish.enc", "tour3/finish.txt", "decode"))
