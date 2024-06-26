#Setting the Specific Data Type
#If you want to specify the data type, you can use the following constructor functions:

x = str ("Hello World")
print(type(x))

x =int (20)
print(type(x))

x = float (20.5)
print(type(x))

x = complex (1j)
print(type(x))

x = list(("apple", "banana", "cherry"))
print(type(x))

x = tuple (("apple", "banana", "cherry"))
print(type(x))

x = range (6)
print(type(x))

x = dict(name="John", age=36)
print(type(x))

x = set(("apple", "banana", "cherry"))
print(type(x))

x = frozenset (("apple", "banana", "cherry"))
print(type(x))

x = bool (5)
print(type(x))

x = bytes (5)
print(type(x))

x = bytearray (5)
print(type(x))

x = memoryview (bytes(5))
print(type(x))