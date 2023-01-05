import sys

alphabet = "abcdefghijklmnopqrstuvwxyzab"

cryption_request = input().lower()
decryption_table = input().lower()

for symbol in cryption_request:
    pos = decryption_table.find(symbol)

    if pos != -1 :
        print(alphabet[pos], end='')
    else:
        print(symbol, end = '')
        
