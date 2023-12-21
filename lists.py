dost = ["Aditya", "Sushant", "Pavithra" , "Arohi"]
#######["0"     ,    "1"   ,      "2"   ,     "3"] 
#######["-4"     ,    "-3"   ,      "-2"   ,     "-1"] 
print(dost[0]) #access the list using index values of words storing in it
#By using from -ve side 
print(dost[-2])

## If i want to use last two names of list only
print(dost[1:3]) #here it will grab only the indexing[1] and [2] positioning elements

#If you want to modify  any name or value  from list
dost[1] = "Sungjinwoo"
print(dost[1])