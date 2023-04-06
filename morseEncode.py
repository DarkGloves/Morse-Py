####################
# MORSE DICTIONARY #
####################

morseEncoder = {
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
  ' ': ' ', 
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
  '&': '.-...', 
  "'": '.----.', 
  '@': '.--.-.', 
  ')': '-.--.-', 
  '(': '-.--.',
  ':': '---...', 
  ',': '--..--', 
  '=': '-...-', 
  '!': '-.-.--', 
  '.': '.-.-.-',
  '-': '-....-', 
  '+': '.-.-.', 
  '"': '.-..-.', 
  '?': '..--..', 
  '/': '-..-.',
  '' : ''
}
morseDecoder = {v: k for k, v in morseEncoder.items() } #reverse the previous dictionary
morseDecoder['space'] = ' ' # Check line 81

############
# FUNCTION #
############

def encode(str):
    output = '' #define output as an string without characters
    try:
        str = [*str.upper()] #get the string, uppercase it and split each letter in a touple
        for letter in str:
            output = output + morseEncoder[letter] + " " #search the matching characters for each letter & separate them via spaces
    except :
        output = "Your string isn't compatible with morse code "
    return output


def decode(str):
    output = ''
    try:
        str = str.replace('   ', ' space ') #replace real spaces with the string 'space' for preventing trouble in the 'split(' ')' function
        str = str.split(' ') #separate each group of morse characters into a list
        
        for char in str:
            output = output + morseDecoder[char]
    except:
        output = "Your string isn't a morse code"
    return output

