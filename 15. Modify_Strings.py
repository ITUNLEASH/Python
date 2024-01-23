#The upper() method returns the string in upper case letters.
#This is could be useful when creating important messages. 
a = "Hello, World!"
print(a.upper())

#The upper() method returns the string in lower case letters.
a = "Hello, World!"
print(a.lower())

#Remove Whitespace.
#Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
a = " Hello, World! "  #Notice the space after the quotes.
print(a.strip())

#The replace() method replaces a string with another string.
a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method returns a list where the text between the specified separator becomes the list items.
a = "Hello, Wolrd!"
print(a.split(",")) #This code returns ['Hello', 'World!']

