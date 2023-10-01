# Integer
num1 = 10
num2 = 20
print(num1)
print(num2)

# If we want to see the data type of any variable then write as below like type(variable) 
print("type of num1 is : ", type(num1))
print(num1 + num2)

# String
nm1 = "Radha"
nm2 = "Krishn"

print(nm1)
print(nm2)

print("type of nm1 is : ", type(nm1))
print("type of nm2 is : ", type(nm2))
print(nm1 + nm2)

# Float
Fnum1 = 1.2986
Fnum2 = 3.14

print(Fnum1)
print(Fnum2)

print("type of Fnum1 is : ", type(Fnum1))
print("type of Fnum2 is : ", type(Fnum2))
print(Fnum1 + Fnum2)

# Boolean
a = True
print(a, "and it's type is", type(a))

# Complex Number
real = 8
imagenary = 2

comp = complex(real + imagenary)
print(comp)

print("type of comp is : ", type(comp))

# List
# List is mmutable we can change the list 
lst = [8,2,1.5,[-4,16],["apple", "orange"]]
print(lst)

lst1 = [8,2,4,-74,2.5,"hello"]


lst1[0] = 424724
print(lst1)

print("type of lst is : ", type(lst))



# Tuple
# Tuple is immutable we can't change it once we declare it 
tup = (82,20,3.14,(-14,6),("fruits","vegitables"))
print(tup)

print(tup[0])

print("type of tup is : ", type(tup))

# Dictionary
disc = {"name" : "kartik", "age" : 27, "canVote" : True}
print(disc)
print("type of disc is : ", type(disc))



