import os, random

def encode():
    print('Enter 0 for switch to decode\n')
    print('Enter 00 to main menu\n')
    text = input("Enter the text to encode : ").lower()
    
    if text == "0":
        print("Switch to decode")
        while True:
            os.system('python Decode.py')
    
    if text == '00':
        os.system('python3 Start.py')
        return

    encode_dict = {
        "a": "$",
        "b": "@",
        "c": "#",
        "d": "&",
        "e": "_",
        "f": "-",
        "g": "+",
        "h": "(",
        "i": ")",
        "j": "{",
        "k": "}",
        "l": "*",
        "m": ";",
        "n": ":",
        "o": "!",
        "p": "?",
        "q": ",",
        "r": "~",
        "s": "=",
        "t": "[",
        "u": "]",
        "v": ".",
        "w": "×",
        "x": "%",
        "y": "¥",
        "z": "|"
    }

    new = ''
    for letter in text:
        if letter.lower() in encode_dict.keys():
            new += encode_dict[letter.lower()]
        else:
            new += letter

    new = new.split(' ')
    key1 = int(input("Create a key : "))
    key1 = str((key1 * 2 + 40) * 3)
    
    key_dict = {
        "1": "@",
        "2": "#",
        "3": "$",
        "4": "&",
        "5": "+",
        "6": "!",
        "7": "?",
        "8": "/",
        "9": "*",
        "0": "="
    }
    
    l = '@#$_&-+!?=×*(/'

    if len(new) >= len(key1):
        for mixy in range(len(key1)):
            new[mixy] = key_dict[key1[mixy]] + new[mixy]
        mix = 0
        for rd in new:
            new[mix] = "".join(random.sample(l, 3)) + new[mix] + "".join(random.sample(l, 3))
            mix += 1
    else:
        for rdm in range(len(new)):
            new[rdm] = "".join(random.sample(l, 3)) + new[rdm] + "".join(random.sample(l, 3))
        for key_space in range(len(key1) - len(new)):
            new.append("".join(random.sample(l, 4)))
        mix = 0
        for mixy in new:
            if len(new[mix]) == 4:
                new[mix] = key_dict[key1[mix]] + new[mix]
            else:
                new[mix] = new[mix][:3] + key_dict[key1[mix]] + new[mix][3:]
            mix += 1

    print("Encoded text:", " ".join(new))

encode()
