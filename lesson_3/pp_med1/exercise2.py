# Alan wrote the following function, which was intended to return all of the factors of number:

def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

print(factors(-9))

# bonus: line 7 evaluates if number divided by the devisor divides evenly which modulo will return 0 remainder
# suggesting divisibility
