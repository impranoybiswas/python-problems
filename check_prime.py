import math

def check_prime(num):
    if(num < 2) :
        return False
    for n in range(2, int(math.sqrt(num)) + 1):
        if(num % n == 0):
            return False
    return True