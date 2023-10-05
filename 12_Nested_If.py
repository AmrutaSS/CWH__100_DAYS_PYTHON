num = int(input("Enter the value of num : "))

if(num < 0) :
    print("The number is negative")
elif(num > 0) : 
    if(num <= 10):
        print("The number is in between 1-10")
    elif(num > 10 and num < 20) :
        print("The number is in between 11-20")
    else :
        print("The number is greater than 20")
else :
    print("The number is equal to zero")