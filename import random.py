import random
import string

# Just usei a short word you'll remember!
def encrypt(text, key):
    if len(key) > 6:
        print("Sorry, your key is too long!")
        return

    key = key.upper()

    for c in key:
        if c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("The key may only contain english letters!")
            return

    ciphertext = ""

    for i in range(0, len(text)):
        code = hex(ord(text[i]) ^ ord(key[i % len(key)]))[2:]
        if len(code) < 2:
            code = "0" + code
        ciphertext += code
    print(ciphertext)


# The key is the same word you used for encrypt!
def decrypt(text, key):
    if len(key) > 6:
        #print("Sorry, your key is too long! Are you sure it's the same key you used to encrypt?")
        return False

    key = key.upper()

    if len(key) == 0:
        return False

    for c in key:
        if c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            #print("The key may only contain english letters! Are you sure it's the same key you used to encrypt?")
            return False

    plaintext = ""

    for i in range(0, len(text), 2):
        code = chr(int(text[i:i+2], 16) ^ ord(key[int(i / 2) % len(key)]))
        if code not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*_ ;":
            return False

        plaintext += code

    print(plaintext)
    
    return True

def start():
    # for i1 in range(65, 91):
    #     for i2 in range(65, 91):
    #         for i3 in range(65, 91):
    #             for i4 in range(65, 91):
    #                 for i5 in range(65, 91):
    #                     for i6 in range(65, 91):
    #
    #                         guessKey=''.join(chr(i1)).join(chr(i2)).join(chr(i3)).join(chr(i4)).join(chr(i5)).join(chr(i6))
    #                         decrypt(
    #                             "0c3b36317e621f343f206221202620622b3a21376222342736353d27303662332731652e3d3b3365273c3a21222a73750d2a37207532292335753d366230272131270d333b3721370a363727333e271a3537343f1a32332627322d203127",
    #                             guessKey)
    #
    #return false
    fo = open("words.txt","r")
    tempLine = "a"
    i = 0
    for line in fo:
        i+= 1
        line = line[0:line.find("\n")]
        decrypt("0c3b36317e621f343f206221202620622b3a21376222342736353d27303662332731652e3d3b3365273c3a21222a73750d2a37207532292335753d366230272131270d333b3721370a363727333e271a3537343f1a32332627322d203127", line)
    print(i)

start()