# Strings are immutable but python provides a set of build-in methods that we can use to alter and modify the string. 
a = 'Harry'
print(len(a))
print(a.upper()) # Here it will print the string of a in upper case. It is not changing the string of a it only operate existing on string and return the new string.
print(a.lower()) # Here it will print the string of a in lower case.


# rstrip() 
# rstrip() method is removes any trelling character 
str1 = "Hello !!!!"
print(str1.rstrip("!"))

str2 = "!!!! Hello !!!!" # Here it will not remove the starting characters because it only remove the ending characters
print(str2.rstrip("!"))


# replace()
# replace() methode replace all occurences of string with another string
nm = "Lilly"
print(nm)
print(nm.replace("Lilly","Hermione"))
print(nm.replace("L","H"))

st = "Harry is the friend of Weasley. Also Harry is friend of hermione"
print(st)
print(st.replace("Harry","Hagrid"))


# split()
# split() method split the given string at the specified instance and returns the seprated strings in list items
slt = "Harry is son of Lilly" 
print(slt)
print(slt.split(" "))


# capitalize()
# The capitalize() method turns only the first character of string to uppercase and rest other character of the string are turn to lowercase. String has no effect if the first character is already in uppercase.

cap = "hello word"
print(cap)
print(cap.capitalize())

cap2 = "here it will print the capital letter at start and If There is Capital letter at middle or anywhere it will make it small"

print(cap2.capitalize())


# center()
# The center() method aligns the string to the center as per the parameters given by the user

cen = "welcome to the pythn series"

print(cen.center(50))

# we can also give the padding character, It will fill the rest of the fill characters provided by the user

cen2 = "welcome to the programe series"

print(cen2.center(50,"*"))

# count()
# The count() method returns the number of times the given value has occurred within the given string

cnt = "method returns the number of times the given value has occurred within the given string"
print(cnt.count("r"))


#endswith()
# endswith() method checks if the string ends with a given value. If yes then it return true else return false

str1 = "Hello word !!!"
print(str1.endswith("!!!"))
print(str1.endswith("."))

# we can even also chack for a value in-between the string by providing the start and end index positions as follow

str2 = "Welcome to the console !!!"
print(str2.endswith("to",4,10))
print(str2.endswith("to",4,8))


# find()
# The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then returns -1

fnd = "He's name is Dan. He is an honest man"
print(fnd.find("is"))
print(fnd.find("she"))

# index()
# The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception (error)

ind = "He's name is Dan. He is an honest man"
print(ind.index("is"))
# print(ind.index("she"))


# isalnum()
# The isalnum() method retrns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

num = "Helloword"
print(num.isalnum())

num2 = "Hello Word"
print(num2.isalnum())


#isalpha()
# The isalpha() method retrns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

num = "Hello word"
print(num.isalpha())

num2 = "HelloWord"
print(num2.isalpha())

num3 = "welcometo45"
print(num3.isalpha())




