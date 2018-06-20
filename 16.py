def Power(base,exponent):
    result = 1
    if base == 0:
        return 0
    if exponent == 0:
        return 1
    elif exponent < 0:
        for i in range(-exponent):
            result = result*base
        return 1/result
    else:
        for i in range(exponent):
            result = result*base
        return result

print(Power(2,3))
print(Power(-2,3))
print(Power(2,0))
print(Power(2,-3))
print(Power(0,3))
print(4%3)
