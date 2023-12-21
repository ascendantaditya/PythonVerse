#For Loop : which allows us to loop over different collections of items.
#it executes a block of statements as long as the condition is "True"
for letter in "Pavithra":
    print(letter)
##using for loop in an array
friends = ["Aditya", "Pavithra" ,"Dua"]
for name in friends:
    print(name) 
##we can use indexing in looping
for index in range(3,10):#  it starts with '3' and end at '9'
    print(index)

#for printing the all the elements in the array
for index in range(len(friends)):
    print(friends[index])#it doesn't indexed the value it just indexed the words inside the "array"

#if i want to do something special in these
for index in range(5):
    if index == 0 :
        print("first Iteration")
    else:
        print("Not funny")
