import locale
from time import sleep
locale.setlocale(locale.LC_ALL, 'uk_UA.utf-8')



def pop(string:str):
    ret = str()
    list1 = list(string)
    list1.pop()
    for i in list1:
        ret += i
    return ret

#RLE - run length encoding
def rle(filename) -> str:
    decoded_file = str()
    with open(filename, 'r', encoding='utf-8') as f:
        last_symbol = None
        for symbol in f.read():
            try:
                times = int(last_symbol)
                decoded_file = pop(decoded_file)
                for i in range(times):
                    decoded_file += symbol
            except:
                decoded_file += symbol

            last_symbol = symbol
        
    return decoded_file

def main(filename:str, output_file_name:str):
    decoded_file = rle(filename)
    # print(decoded_file)

    with open(output_file_name, 'w', encoding='utf-8') as f:
        f.write(decoded_file)

if __name__ == "__main__":
    main('tour3/file.compress', 'tour3/decoded.txt')

    