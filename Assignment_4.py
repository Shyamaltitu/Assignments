# Write a Python Program(with class concepts) to find the area of the triangle using the below formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# Function to take the length of the sides of triangle from user should be defined in the parent class 
# and function to calculate the area should be defined in subclass.

class main():
    x=int(input("Enter length of side 1\t"))
    y=int(input("Enter length of side 2\t"))
    z=int(input("Enter length of side 3\t"))

class area(main):
    def tri_area(self):
        s=(self.x+self.y+self.z)/2
        a=(s*(s-self.x)*(s-self.y)*(s-self.z)) ** 0.5
        return a

t = area()
print("Area is", t.tri_area())

# Write a function filter_long_words() that takes a list of words and an integer n and returns
# the list of words that are longer than n.


def filter_long_words(a,n):
    b=[]
    for i in a:
        if len(i)>n:
            b.append(i)
    return b

def main():
    a=[]
    for i in range(100):
        b= input("Enter the word\t")
        if b!="End":
            a.append(b)
        else:
            break
    n= int(input("Enter number of characters required\t"))
    print(a)
    b=filter_long_words(a,n)
    print(b)

main()

# Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words.

def maptolen(a):
    b=[]
    for i in a:
        n=int(len(i))
        b.append(n)
    return b

def main():
    a=[]
    for i in range(10000):
        x=input("Enter Word\t")
        if x!="end":
            a.append(x)
        else:
            break
    b=maptolen(a)
    print(b)

main()

# Write a Python function which takes a character (i.e. a string of length 1) and returns True if
# it is a vowel, False otherwise.


def checkvowel(a):

    if a in "aeiouAEIOU":
        print("True")
    else:
        print("False")

def main():
    for i in range(100):
        a=input("Enter character to check\t")
        if a=="|":
            break
        elif len(a) > 1 :
            print("It's a String!!! enter character")
            continue
        elif len(a) == 1 :
            checkvowel(a)
        else:
            print("Enter something :)")

main()