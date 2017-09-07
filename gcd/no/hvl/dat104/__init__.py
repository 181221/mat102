def gcd(a, b):
    if b == 0:
        return a
    else:
        print(a, b)
        return gcd(b, a % b)

print(gcd(2178309, 3524578))
