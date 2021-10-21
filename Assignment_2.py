# Create the below pattern using nested for loop in Python

#*
#* *
#* * *
#* * * *
#* * * * *
#* * * *
#* * *
#* *
#*

n=5
for i in range(2*n-1):
    for j in range(n):
        if j<=i and i<n:
            print("*",end="")
        elif j<=(2*(n-1)-i) and i>=n:
            print("*",end="")
        else:
            print(" ",end="")
    print("")


# Write a Python program to reverse a word after accepting the input from the user.

a=input("Enter the string to reverse\t")
print(a[::-1])