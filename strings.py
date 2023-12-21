#1st Method to Print A  String 
print("The\nAscendants")

#2nd Method to Print A String by creating a Variable and concatening a new string
phrase = "The Ascendants"
print(phrase + " are  cool ")

#For Capatalize in Lower Case
phrase = "The Ascendants"
print(phrase.lower())

#For Capatalize in Upper Case 
phrase = "The Ascendants"
print(phrase.upper()) 

#For Checking Whether the string is UpperCase or LowerCase
phrase = "The Ascendants"
print(phrase.isupper())

#Using Function in combination with each other 
phrase = "The Ascendants"
print(phrase.upper().isupper())

#for finding the length of the given phrase of statement inside the string
phrase = "The Ascendants"
print(len(phrase))

#for finding the length of the given list using len function
phrase = []
print(len(phrase))

#for figuring out whats the letter of string or whether what the letter
phrase = "The Ascendants"
print(phrase[0])

#figuring out the indexing of the letter
phrase = "The Ascendants"
print(phrase.index("A"))

#for replacing the text of phrase while printing
phrase = "The Ascendants"
print(phrase.replace("Ascendants","Conquerors"))
