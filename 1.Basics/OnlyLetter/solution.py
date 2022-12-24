
alphabet = "abcdefghijklmnopqrstuvwxyz"
request = input() 

for letter in alphabet:
    for symbol in request.lower():
        if letter == symbol:
            print(letter, end = "")
            break
    