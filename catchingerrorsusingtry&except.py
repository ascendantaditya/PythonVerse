##Catching Errors using try and except
#so here we used try except block : it allows to tryout the code block
#Using "Try" Block
try:
    value = 10 / 0
    number = int(input("Enter a number : "))
    print(number)

#Using "Except" Block
except ZeroDivisionError:
    print("Invalid Input")
except ValueError:
    print("Invalid Input")