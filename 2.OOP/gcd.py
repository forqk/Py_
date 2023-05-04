def gcd(a, b):
    assert(isinstance(a, int))
    assert(isinstance(b, int))
    assert(a > 0 and b > 0)
    while b:
        a, b = b, a % b
    return a

# def main():
#     print(gcd(974, 164))
    
# main()