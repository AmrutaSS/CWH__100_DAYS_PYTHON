st = "Frozen"

for i in st :
       print(i)
    #    we can also print the the string in one line by using "," between every alphabates like below
    #    print(i, end = ",")
       if(i == "r"):
              print("hello")


# for loop on list 
colors = ['Red','Green','Yellow','Purple']
for clr in colors :
       print(clr)
    #    if we want to apply loop in clr then we can write it as below
       for i in clr :
              print(i)


# When we want use the for loop for a specific number of times then we can write it as below
num = int(input("Enter the number : "))
for i in range(num) :
    # print(i)   # it will print from 0 to 4
    print(i+1)      #it will print from 1 to 5

# We can also give range from to as we want as below

for k in range(11 , 21) :
      print(k)       

# Third parameter of range if we want the number of gap between the range then we can give the third parameter for how much we want the gap between the range 
for k in range(1 , 21 , 3) :    # Here it will print the numbers from 1 to 20 with the gap of 3
      print(k)       