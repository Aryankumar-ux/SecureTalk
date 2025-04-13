import os
def encode():
	print('Enter 0 for switch to decode\n')
	print('Enter 00 to main menu\n')
	text=input('Enter the text to encode:- ')
	if text=='0':
		os.system('python3 decode2.py')
	if text == '00':
		os.system('python3 Start.py')
		return
	encode_dict={
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
	new=''
	for letter in text:
	            	if letter.lower() in encode_dict.keys():
	            		new+=encode_dict[letter.lower()]
	            	else:
	            		new+=letter
	print('\tEncoded text: ',new)
encode()          	