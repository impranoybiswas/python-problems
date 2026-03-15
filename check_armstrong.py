def check_armstrong(num):
    digits = str(num)
    power = len(digits)
    
    total = sum(list(int(d)**power for d in digits))
    return total == num