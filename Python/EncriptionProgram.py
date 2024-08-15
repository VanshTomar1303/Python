import random
import string

char=" "+string.punctuation+string.digits+string.ascii_letters
char=list(char)
key=char.copy()

random.shuffle(key)

#ENCRYPT
text=input("ENTER A MESSAGE TO ENCRYPT:")
cipher_text=" "

for l in text:
    index=char.index(l)
    cipher_text+=key[index]

print(f"ORIGINAL MESSGE:{text}")
print(f"ENCRYPTED MESSGE:{cipher_text}")

#DECRYPT
cipher_text=input("ENTER A MESSAGE TO DECRYPT:")
text=" "

for l in cipher_text:
    index=key.index(l)
    text+=char[index]

print(f"ORIGINAL MESSGE:{cipher_text}")
print(f"DECRYPTED MESSGE:{text}")
