# Length of string
# we can find a length of string usin len() function

fruit = "Mango"
length = len(fruit)

print("Mango is", length, "letter word")

# String slicing
print(fruit[0:4])  # It will print the string including 0 but not 4 index

print(fruit[1:3]) # It will print the string including 1 but not 3 index

print(fruit[:4]) # It will print the string including 0 but not 4 index here it will take 0 index by default

print(fruit[:]) # It will print the string including 0 but not 5 index here it will print whole string from start to end

print(fruit[0:-3]) # It will print the string including 0 but not 2 index here it will take -3 as len(fruit)-3 and lenght of string is 5 so 5-3 = 2  

print(fruit[-1:-3]) # Here it will be like 5-1 = 4 and 5-3 = 2 so it is like 4:2 this will print blank because this is not a scence to count array including 4 but not 3

print(fruit[-3:-1]) # Here it will be like 5-3 = 2 and 5-1 = 4 so it is like 2:4 this will print the string including 2 but not 4

nm = "Harry"
print(nm[-4:-2]) # Here it will be like 5-4 = 1 and 5-2 = 3 so it is like 1:3 this will print the string including 1 but not 3
