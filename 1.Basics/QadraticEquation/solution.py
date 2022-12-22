import sys 

a = int(sys.argv[1]) 
b = int(sys.argv[2]) 
c = int(sys.argv[3])

Discr = b **2 - 4 * a * c

print(int((-b + Discr ** 0.5) / (2 * a)))
print(int((-b - Discr ** 0.5) / (2 * a)))

