# Here the a and b are the string because we took it in quotes so this addition will be 12
a = "1"
b = "2"

print(a+b)

# if we want to store string as a number then we can write it as follow by converting string into a number but we can do it with numbers only not with words meanse the string should be valid it we want to do it with float, double then string should be in fload,double and integers.
a = "1"
b = "2"

print(int(a) + int(b))

# the following code will give us the error because the string of a is not valid
# a = "Harry12"
# b = "20"
# print(int(a) + int(b))


# Explicite typecasting is conversion from one data type into another data type by a devoloper or programmer's 
num = "15"
str_num = 7
print(int(num) + str_num)

# Implicite typecasting is conversion of data type from one data type into another data type by paython itself
a = 1.8
b = 8

print(a + b) # Here the value of be will be taken as float by defaul by python itself