#functions use to organise our code properly 
##writing an function which will says "hello"
def sayHello():
    print("Hello User!") #it gives nothing as in the ouput here
#bcoz it's exceuted by the default

#for printing the function we need to call the function
print("Good")
sayHello()
print("Morn")

##we can make functions powerful by doing what ; by providing them the data they need so that thing is known as "Parameters"
#1st Method
def sayHello(name,age): ##by giving function a value it can print it to get easily 
    print("Hello " + name + " , you're " + age)
sayHello("Aditya ",  "18")
sayHello("Pavithra " ,  "17")

##by using my method(2nd)
def sayHello(name,age):
    print("Hello" + name +" , you're " + str(age))
sayHello("Aditya ", 18)
sayHello("Pavithra ", 17)