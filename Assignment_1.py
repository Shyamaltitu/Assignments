# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
# between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

low= 2000
high= 3200

for i in range(low, high+1):
    if i%7==0 and i%5 !=0:
        print(i, end=",")


# Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order 
# with a space between first name and last name.

First_Name=input("Enter First Name\t") #Reading First Name
Last_Name=input("Enter Last Name\t") #Reading Last Name
Full_Name= First_Name + " " + Last_Name # Concatanating First and Last Names
Reverse_Name=Full_Name[::-1] # Reversing String
print(Reverse_Name) # Printing Reverse 


# Write a Python program to find the volume of a sphere with diameter 12 cm. V=4/3 * π * r 3

Diameter=12
Volume= (4/3)*3.14*(Diameter/2)**3
print(Volume)