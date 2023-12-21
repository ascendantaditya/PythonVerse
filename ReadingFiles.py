#if you want to "read" the content inside the file
open("aditya.txt","r")
#if you want to write something and want to change anything
open("aditya.txt","w")
#if you want to add something or i  mean append something
open("aditya.txt","a")
#if you want to read and write you should use
open("aditya.txt","r+")

##Working with Them ##
my_file = open("aditya.txt","r")

print(my_file.read())
my_file.close()
