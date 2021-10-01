plaintext = input("Enter PlainText: ")
shift = input("Enter Shift Key: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
ciphertext = ""

shift = int(shift)

new_index = 0
for i in plaintext:
    if i.lower() in alphabet:
        new_index = alphabet.index(i) - shift
        ciphertext += alphabet[new_index % 26]
    else:
        ciphertext += i
print("Ciphertext: " + ciphertext)