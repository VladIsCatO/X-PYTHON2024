from math import floor, ceil

def lzw_encode(string:str) -> bytes:
    string.encode('utf-8')
    n_keys = 256
    compressed = []
    start = 0
    length = len(string) + 1
    while True:
        pass