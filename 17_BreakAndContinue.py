# Break statement is enables a program to skip over a part of the code. A break statement terminates the very loop it lies within. 
# for i in range(12):
#     if(i == 10):
#         break
#     print("5x", i+1, "=", 5*(i+1))
# print("The break will break the loop after 10")


# Continue statement skip the rest of the loop statement and causes the next iteration to occur.
for i in range(12):
    if(i == 10):
        print("Skip the iteration")
        continue
    print("5x", i, "=", 5*i)

