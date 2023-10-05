x = int(input("Enter the value of x : "))

match x :
# if x is 0
    case 0 :
        print("x is zero")
    # Case with if condition 
    case 4 :
        print("case is 4")
    case _ if(x < 10):
        print(x, "is less than 10")
    case _ :
        print(x)
