import sys

from random import randint

winners_count = int(input())

number, letters = input().split()

numbers = set()

for idx in range(0, len(number)):
    if number[idx] != '0':
        number[idx:];
        break
    
if int(number) <= int(winners_count):
    winners_count = number
  
while len(numbers) != int(winners_count):
    numbers.add(randint(1, int(number)))

winner = 1

for m in numbers:
    if len(str(m)) < 6 :
        print("Победитель номер ", winner, " - ",  "\"", "0" * (6 -len(str(m))) + str(m), " ", letters.upper(), "\"", sep='') 
    else:
        print("Победитель номер ", winner, " - ", "\"", str(m), " ",  letters.upper(), "\"", sep = '')
    winner += 1