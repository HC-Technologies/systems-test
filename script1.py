limit = 3210

def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

sum = 0
num = 2
for i in xrange(limit):
    while not is_prime(num):
        num += 1
    print(num)
    num += 1