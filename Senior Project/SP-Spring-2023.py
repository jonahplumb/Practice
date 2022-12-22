#!/usr/bin/python3

import argparse
import hashlib
import base64


# Below are the 3 hashing algorithms (MD5, SHA256, SHA512)
# SHA256
def generateHashSHA256(hashInput): # Generating SHA256 Hash
    shaResult = hashlib.sha256(hashInput.encode())
    print("\nHere is your SHA256 hash: ", shaResult.hexdigest())

# SHA512
def generateHashSHA512(hashInput): #Generating SHA512 Hash
    shaResult = hashlib.sha512(hashInput.encode())
    print("\nHere is your SHA512 hash: ", shaResult.hexdigest())

# MD5
def generateHashMD5(hashInput): # Generating MD5 Hash
    md5Result = hashlib.md5(hashInput.encode())
    print("\nHere is your MD5 hash: ", md5Result.hexdigest())


# Below is function for decryption (caesar brute force)
def caesarBruteForce(cipherText):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = 0
    print("Starting Caesar Cipher Brute Force:")
    while key < 26:
        key += 1
        decryptString = cipherText.lower()
        shiftValue = int(key)
        result = ""
        for character in decryptString:
            position = alphabet.find(character)
            nextPosition = position - shiftValue
            if character in alphabet:
                result = result + alphabet[nextPosition]
            else:
                result = result + character

        shiftValueString = str(shiftValue)
        print("\nShift Value of " + shiftValueString +": " + result)


# Below is function for encryption (caesar)
def caesarEncryption(plainText, shiftValue):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plainText = plainText.upper()
    # Shift should already be integer but this is here just to make sure
    shiftValue = int(shiftValue)
    encryptedString=""
    for character in plainText:
        position = alphabet.find(character)
        newposition = position+shiftValue
        if character in alphabet:
            encryptedString = encryptedString + alphabet[newposition]
        else:
            encryptedString = encryptedString + character
    print("Your encrypted message with a cipher shift of " + str(shiftValue) + " is below")
    print(encryptedString)

# Base64 Encryption
def base64Encryption(plainText):
    text_bytes = plainText.encode('ascii')
    base_bytes = base64.b64encode(text_bytes)
    message = base_bytes.decode('ascii')
    print(message)

# Base64 Decryption
def base64Decryption(cipherText):
    text_bytes = cipherText.encode('ascii')
    base_bytes = base64.b64decode(text_bytes)
    message = base_bytes.decode('ascii')
    print(message)


# Vigenere Keygen from keyword/phrase
def generateVigKey(phrase, key):
    key = list(key)
    if len(phrase) == len(key):
        return(key)
    else:
        for i in range(len(phrase) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

# Credit majority of this code for vigenere to 
# https://github.com/geektechdude/Python_Encryption/blob/master/geektechstuff_vigenere_cipher.py
# Vigenere Encrypt
def vigEncrypt(plainText, key: str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    enc_key = ""
    cipherText = ""
    enc_key = str(key).lower() # Not sure why but was incurring error so put this here alongwith str for parameter and it fixed it.
    plainText = plainText.lower()
    text_length = len(plainText)


    extended_key  = enc_key
    extended_key_len = len(extended_key)

    while extended_key_len < text_length:
        extended_key = extended_key + enc_key
        extended_key_len = len(extended_key)

    key_position = 0

    for letter in plainText:
        if letter in alphabet:
            position = alphabet.find(letter)
            key_character = extended_key[key_position]
            key_character_position = alphabet.find(key_character)
            key_position = key_position + 1

            new_position = position + key_character_position
            if new_position > 26:
                new_position = new_position - 26
            new_character = alphabet[new_position]
            cipherText = cipherText + new_character
        else:
            cipherText = cipherText + letter
    print(cipherText)


# Vigenere Decrypt
def vigDecrypt(cipherText, key: str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    dec_key = ""
    plainText = ""
    dec_key = str(key).lower() # Not sure why but was incurring error so put this here alongwith str for parameter and it fixed it.

    cipherText = cipherText.lower()
    string_length = len(cipherText)

    extended_key  = dec_key
    extended_key_len = len(extended_key)

    while extended_key_len < string_length:
        extended_key = extended_key + dec_key
        extended_key_len = len(extended_key)

    key_position = 0

    for letter in cipherText:
        if letter in alphabet:
            # cycles through each letter to find it's numeric position in the alphabet
            position = alphabet.find(letter)
            # moves along key and finds the characters value
            key_character = extended_key[key_position]
            key_character_position = alphabet.find(key_character)
            key_position = key_position + 1
            # changes the original of the input string character
            new_position = position - key_character_position
            if new_position > 26:
                new_position = new_position + 26
            new_character = alphabet[new_position]
            plainText = plainText + new_character
        else:
            plainText = plainText + letter
    print(plainText)


# ASCII to Binary
def stringToBinary(string):

    userInput = string.encode()
    binary= int.from_bytes(userInput, "big") # Create Bianry Array
    output = bin(binary)
    print(output.replace("0b", "")) # To remove 0b at begining of string

# Binary to ASCII
def binaryToString(binary):

    input=int(binary, 2);
    total_bytes= (input.bit_length() +7) // 8 # Get number of bytes
    input_array = input.to_bytes(total_bytes, "big")
    decodedString=input_array.decode()
    print(decodedString)



def main():
# Banner
    print(""" 
```````````````````````````````````````````````````
(╯°□°）╯   Jonah Plumb Senior Project   (╯°□°）╯ 
```````````````````````````````````````````````````
          """)


    parser = argparse.ArgumentParser(description='Jonah Plumb Senior Project')

    # Arguments to flag whether the user wants to encrypt or decrypt
    parser.add_argument("-d", "--decrypt", action="store_true", help="decrypt the following algorithms (caesar, vigenere, base64, binary)") # Decrypt Argument
    parser.add_argument("-e", "--encrypt", action="store_true", help="encrypt the following algorithms (caesar, vigenere, base64, binary)") # Encrypt Argument

    # Possible Arguments for decryption/encryption
    parser.add_argument("--caesar", help="Caesar Cipher")
    parser.add_argument("--vigenere", help="Vigenere Cipher")
    parser.add_argument("--binary", help="Binary")
    parser.add_argument("--keyword", help="Vigenere Cipher keyword")
    # parser.add_argument("--des", help="Data Encryption Standard")
    parser.add_argument("--base64", help="Base64")
    parser.add_argument("--shift", type=int, help="Specify Caesar Cipher Encrypt Shift Value")

    # Arguments for hashing algorithms 
    parser.add_argument("--sha256", help="Generate SHA256 Hash")
    parser.add_argument("--sha512", help="Generate SHA512 Hash")
    parser.add_argument("--md5", help="Generate MD5 Hash")

    args = parser.parse_args()


# If statements to continue program based on user input for hashes, not separated, only want one program output. 
    if args.sha256: # Generate SHA256 Hash
        generateHashSHA256(args.sha256)
    elif args.md5: # Generate MD5 Hash
        generateHashMD5(args.md5)
    elif args.sha512: # Generate SHA512 Hash
        generateHashSHA512(args.sha512)
    elif args.caesar and args.decrypt == True: # Decrypt Caesar Cipher (Brute)
        caesarBruteForce(args.caesar)
    elif args.shift and args.caesar and args.encrypt == True: # Encrypt Caesar Cipher with shift
        caesarEncryption(args.caesar, args.shift)
    elif args.base64 and args.encrypt == True: # Base64 Encrypt
        base64Encryption(args.base64)
    elif args.base64 and args.decrypt == True: # Base64 Decrypt
        base64Decryption(args.base64)
    elif args.binary and args.encrypt == True: # Convert to Binary
        stringToBinary(args.binary)
    elif args.binary and args.decrypt == True: # Convert from Binary
        binaryToString(args.binary)
    elif args.keyword and args.vigenere and args.encrypt == True: # Encrypt using Vigenere with keyword
        key = generateVigKey(args.vigenere,args.keyword) # Generate key from keyword, then encode
        vigEncrypt(args.vigenere,key)
    elif args.keyword and args.vigenere and args.decrypt == True: # Decrypt Vigenere with keyword
        key = generateVigKey(args.vigenere,args.keyword) # Generate key from keyword, then decode
        vigDecrypt(args.vigenere,key)



if __name__ == "__main__":
    main()