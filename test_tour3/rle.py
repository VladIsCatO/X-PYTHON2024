"""RLE - run length encoding"""

def rle_encode(filename:str) -> str:
    compressed_file = str()
    with open(filename, 'r', encoding='utf-8') as f:
        last_symbol = None
        count = 1
        for i in f.readlines():
            for symbol in i:
                if last_symbol == symbol:
                    count += 1
                else:
                    if count == 1 and last_symbol is not None:
                        compressed_file += last_symbol
                    elif last_symbol is not None:
                        compressed_file += str(count) + last_symbol
                    count = 1
                last_symbol = symbol
    return compressed_file