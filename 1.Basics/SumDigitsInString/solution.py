import sys

digit_string = sys.argv[1]

summ = 0

for i in digit_string:
    summ += int(i)
    
print(summ)