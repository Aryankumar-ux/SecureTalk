import os
def decode():
    print('Enter 0 for switch to decode\n')
    print('Enter 00 to main menu\n')
    encoded_text = input("Enter the text to decode : ").lower()
    
    if encoded_text == "0":
        print("Switch to Encode")
        while True:
            os.system('python Encode.py')
    
    if encoded_text == '00':
        os.system('python3 Start.py')
        return

    key_dict={
    "@": "1",
    "#": "2",
    "$": "3",
    "&": "4",
    "+": "5",
    "!": "6",
    "?": "7",
    "/": "8",
    "*": "9",
    "=": "0"
    }
    decode_dict={
        "$": "a",
        "@": "b",
        "#": "c",
        "&": "d",
        "_": "e",
        "-": "f",
        "+": "g",
        "(": "h",
        ")": "i",
        "{": "j",
        "}": "k",
        "*": "l",
        ";": "m",
        ":": "n",
        "!": "o",
        "?": "p",
        ",": "q",
        "~": "r",
        "=": "s",
        "[": "t",
        "]": "u",
        ".": "v",
        "×": "w",
        "%": "x",
        "¥": "y",
        "|": "z",
        }
    encoded_text=encoded_text.split(' ')
    key1=int(input("Enter key: "))
    key1=int((key1*2+40))*3
    check=''
    for find_key in range(len(str(key1))):
        if len(encoded_text[find_key]) >= 8:
                check+=key_dict[encoded_text[find_key][3]]
                encoded_text[find_key] = encoded_text[find_key][:3] + encoded_text[find_key][4:]
        else:
                check+=key_dict[encoded_text[find_key][0]]
    if int(check) != key1:
        print("Invalid key\nSorry i am not going to decode it")
        decode()
    fresh=''
    f=0
    for filter in encoded_text:
        if (len(filter)) >= 7:
                fresh+=filter[3:-3]
                fresh+=' '

    fn=''
    for final in fresh:
        if final.lower() in decode_dict.keys():
                fn+=decode_dict[final.lower()]
        elif final == ' ':
                fn+=' '
        else:
                fnl+=final
    print("Orignal text :",fn)
decode()
