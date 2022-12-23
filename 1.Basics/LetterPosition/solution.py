import sys

original = input().lower()
request = input().lower()

request_without_repeat = ""

for letter in request:
    if letter not in request_without_repeat and letter.isalpha():
        request_without_repeat += letter

for letter in range(0, len(request_without_repeat)):
    print(request_without_repeat[letter], end=" ")
    is_missing = True
    for symbol in range(0, len(original)):
        if(request_without_repeat[letter] == original[symbol]):
            print(symbol+1, end= " ")
            is_missing = False
    if(is_missing):
        print ("None", end = '')    
    print()