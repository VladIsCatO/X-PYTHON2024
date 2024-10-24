"""In this project i will mix some text file compressing methods, and create my own"""
from rle import rle_encode as rle
from lzw import lzw_encode as lzw


def main(filename:str, output_file_name:str):
    compressed_file = rle(filename)
    print(compressed_file)
    with open(output_file_name, 'w', encoding='utf-8') as f:
        f.write(compressed_file)

if __name__ == "__main__":
    main('tour3/file.txt', 'tour3/file.compress')

    