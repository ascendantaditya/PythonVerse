#Building a Basic Translator In Python
##1st Method
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "p"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a Phrase :")))

##2nd Method
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":#chnages here for lowercase
            translation = translation + "p"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a Phrase :")))

##by using a boolean trajectory
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower in "aeiou":
            if letter.isupper():
                translation = translation + "P"
            else:
                translation = translation + "p"

        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a Phrase :")))
