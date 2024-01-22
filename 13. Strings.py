print("Hello") #Double Quotes
print('Hello') #Single Quotes

a = "Hello"
print(a)

a = """This code is practise is number 13. I need to learn Python and SQL to gain a better
job at Amazon, be able to work again from home, set a good example for my kids and encourage them to do better."""
print(a)

a = "Hello, World!"
print(len(a)) #The len() function returns the length of a string

a = "Hello, World!"
print(a[1]) #Get the character at position 1 (remember that the first character has the position 0):


#Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "Banana": #Loop through the letters in the word "banana":
    print(x)
    
#To get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a))

#To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in Life are Free!"
print("free" in txt)

#Print only if "free" is present:
txt = "The best things in Life are Free!"
if "free" in txt:
    print("Yes, 'free' is present.")


#Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)


#Use it in an if statement.
#Print only if "expensive" is NOT present.
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
    

