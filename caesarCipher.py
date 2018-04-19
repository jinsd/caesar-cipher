# Caesar Cipher
# www.nostarch.com/crackingcodes (BSD Licensed)

import pyperclip

# The string to be encrypted/decrypted
message = 'XCBSw88S18A1S 2SB41SE .8zSEwAS50D5A5x81V'

# encryption/decryption key
key = 22

mode = 'decrypt'

# every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# store the encrypted/decrypted form of the message:
translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # encrypt or decrypt
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        # handle wraparound if needed
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        # append symbol without encrypting/decrypting
        translated = translated + symbol

# output translated string
print(translated)
pyperclip.copy(translated)
