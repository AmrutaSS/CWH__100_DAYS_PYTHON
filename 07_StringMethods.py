# In python, anything that you enclosed between single or double quotation is a string
name = "Harry"
frd = "John"

# If we want to print a statement then we can write it as follow
statement = 'He said, "I want eat an apple"'
print(statement, "\n")

# Multiline Sting
Multist = """A multiline string in Python begins and ends with either three single quotes or three double quotes. Any quotes, tabs, or newlines in between the “triple quotes” are considered part of the string."""

print(Multist,"\n")

# Accessing characters in string 
# In python, string is like an array of characters we can access parts of string by using it's index which starts from 0

print(Multist[5])
print(name[0],"\n")

# Looping through the string we can use loop through string using a for loop like follow
print("Let's use a for loop for name\n")
for character in name :
    print(character)

print("Let's use a for loop for Multist\n")
for character in Multist :
    print(character)