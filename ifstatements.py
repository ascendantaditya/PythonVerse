#Creating a boolean Variable
#mike's code
is_male = False
is_tall = False

if is_male or is_tall:
    print("You're a Tall Male")
elif is_male and not(is_tall):
    print("You're a Female and you're short")
elif not(is_male) and is_tall:
    print("You're Gay but taal gay")
else :
    print("You're a Short Girl\nand You'll Fucked in " )



##If statements using comparison operators and functions
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(69,40,5))