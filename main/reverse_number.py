n = int(input("Enter the number:- "))

rn = 0

while(n>0):
  rem = n%10
  rn = (rn*10)+rem
  n = n//10

print("Reversed Number is:- {}".format(rn))
