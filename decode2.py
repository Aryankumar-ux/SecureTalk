import os

def decode():
    print('Enter 0 for switch to encode\n')
    print('Enter 00 to main menu\n')
    text = input('Enter the text to decode: ')
    if text == '0':
        os.system('python3 encode2.py')
    if text == '00':
        os.system('python3 Start.py')
        return

    decode_dict = {
        "$": "a", "@": "b", "#": "c", "&": "d", "_": "e", "-": "f",
        "+": "g", "(": "h", ")": "i", "{": "j", "}": "k", "*": "l",
        ";": "m", ":": "n", "!": "o", "?": "p", ",": "q", "~": "r",
        "=": "s", "[": "t", "]": "u", ".": "v", "×": "w", "%": "x",
        "¥": "y", "|": "z"
    }

    decoded = ''
    for ch in text:
        decoded += decode_dict.get(ch, ch)

    print('\n\tDecoded text:', decoded)

decode()
