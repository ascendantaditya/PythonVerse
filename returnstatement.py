##Return : This statement is used in a function to end the exceution of the function and to send a result back to the caller if required.

#for finding a cube of a number
def cube(num):
    num*num*num
                 ##as for now this shows "none" as output so what will gonna happen in we will use return there so it can execute the code 
print(cube(3))

#finding cube using "return" statement 
def cube(num):
    return num*num*num #"return" breaks the statement 
print(cube(8))

#here whathappens ki we give information to user using def function and we use return statement to get information back from the user