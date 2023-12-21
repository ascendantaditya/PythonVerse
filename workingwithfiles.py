##Working with Them ##
myfile = open("aditya.txt","r")
#by using "readline()" function
print(myfile.readline())#readline : will read only the first line

#by using "readlines()" function
print(myfile.readlines()[0]) #readlines: we can read to all lines by using indexing positions
myfile.close()
