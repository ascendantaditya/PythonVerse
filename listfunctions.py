##list Functions ##
lucky_numbers = [4,8,15,16]
friends = ["Aditya" , "Pavithra" , "Rudra" ,"Arohi" , "Pavithra"]

#if you want to appends another list in a list 
friends.extend(lucky_numbers)

##for adding an element in the list
friends.append("Shivani")

##for adding  any element at indexing position
friends.insert(3,"Himanshu")

##if you want to remove any value 
friends.remove("Himanshu")

##if you want to delete or clear the whole list


##if you want to get rid of the last element of the list
friends.pop()

##if you want to sort a list in ascending  order or alphabets or nums
lucky_numbers.sort()
print(lucky_numbers)

##if you want to reverse this list 
lucky_numbers.reverse()
print(lucky_numbers)

##if you want to copy a list
friends2 = friends.copy()
print(friends2)

##if you want to check wheather the indexing position of elements in your list
print(friends.index("Arohi"))

##if you want to count that how much times it comes in your way
print(friends.count("Pavithra"))



