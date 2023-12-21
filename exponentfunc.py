##Exponent Number: It allows a certain number and raise it to a specific power
#Using "for loop" for creating exponent function

def raise_to_power(base_num,pow_num):
    result = 1 #where we store the actual result of doing the math
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(3,4))
