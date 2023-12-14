import pygame
import time

pygame.init()
dot=pygame.mixer.Sound('dot.wav')
dash=pygame.mixer.Sound('dash.wav')


'''
#test
for i in range(5):
    dot.play()
    time.sleep(0.20)
    dash.play()
    time.sleep(0.40)
    '''
    
morse_table = {
		'A': '.-',
		'B': '-...',
		'C': '-.-.',
		'D': '-..',
		'E': '.',
		'F': '..-.',
		'G': '--.',
		'H': '....',
		'I': '..',
		'J': '.---',
		'K': '-.-',
		'L': '.-..',
		'M': '--',
		'N': '-.',
		'O': '---',
		'P': '.--.',
		'Q': '--.-',
		'R': '.-.',
		'S': '...',
		'T': '-',
		'U': '..-',
		'V': '...-',
		'W': '.--',
		'X': '-..-',
		'Y': '-.--',
		'Z': '--..',

		'a': '.-',
		'b': '-...',
		'c': '-.-.',
		'd': '-..',
		'e': '.',
		'f': '..-.',
		'g': '--.',
		'h': '....',
		'i': '..',
		'j': '.---',
		'k': '-.-',
		'l': '.-..',
		'm': '--',
		'n': '-.',
		'o': '---',
		'p': '.--.',
		'q': '--.-',
		'r': '.-.',
		's': '...',
		't': '-',
		'u': '..-',
		'v': '...-',
		'w': '.--',
		'x': '-..-',
		'y': '-.--',
		'z': '--..',

		'0': '-----',
		'1': '.----',
		'2': '..---',
		'3': '...--',
		'4': '....-',
		'5': '.....',
		'6': '-....',
		'7': '--...',
		'8': '---..',
		'9': '----.',

		'.': '.-.-.-',
		',': '--..--',
		'?': '..--..',
		"'": '.----.',
		'!': '-.-.--',
		'/': '-..-.',
		'(': '-.--.',
		')': '-.--.-',
		'&': '.-...',
		':': '---...',
		';': '-.-.-.',
		'=': '-...-',
		'+': '.-.-.',
		'-': '-....-',
		'_': '..--.-',
		'"': '.-..-.',
		'$': '...-..-',
		'@': '.--.-.',
        ' ': ' '
	}

text=input('Input text to be encoded...:')

for char in text:
    for signal in morse_table[char]:
        print(signal, end=' ')
        if signal=='.':
            dot.play()
            time.sleep(0.2)
        elif signal=='-':
            dash.play()
            time.sleep(0.35)
        else:
            time.sleep(0.4)
            print('/', end=' ')
    time.sleep(0.2)
    print(' ', end=' ')
