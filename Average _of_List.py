mylist = []
lenoflist =int(input("Enter the length of the list: "))
for i in range(lenoflist):
    element=int(input("Enter element " + str(i+1) + ": "))
    mylist.append(element)
print(mylist)

sumoflist = sum(mylist)
average = float(sumoflist/lenoflist)
print(f"The average of the list is {average}")

