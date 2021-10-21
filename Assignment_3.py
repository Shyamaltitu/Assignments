# Write a Python Program to implement your own myreduce() function which works exactly
# like Python's built-in function reduce()

def my_reduce(sum1,a):
    b=0
    for i in a:
        b = sum1(b,i)
    return b

def sum1(x,y):
    z=x+y
    return z

def main():
    n=int(input("How many numbers you want to compute?\t"))
    a=[int(input("Enter List Values\t")) for i in range(n)]
    b=my_reduce(sum1,a)
    print(b)

main()

# Write a Python program to implement your own myfilter() function which works exactly
# like Python's built-in function filter()

def my_filter(f,a):
    b=-99999999999999
    for i in a:
        b=f(b,i)
    return b

def f(x,y):
    if x>y:
        return x
    elif x<y:
        return y
    elif x==y:
        return x

def main():
    n=int(input("How many numbers you want to compute?\t"))
    a=[float(input("Enter List Values\t")) for i in range(n)]
    b=my_filter(f,a)
    print("Largest number is\t",b)

main()

# Implement List comprehensions to produce the following lists
#['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
#[[2], [3], [4], [3], [4], [5], [4], [5], [6]] 
# [[2, 3, 4, 5], [3, 4, 5, 6],[4, 5, 6, 7], [5, 6, 7, 8]]
#[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]


l=[j*chr(ord('x')+i) for i in range(3) for j in range(5) if j>0]
print(l)
 
l=[i*chr(ord('x')+j) for i in range(5) if i>0 for j in range(3)]
print(l)

m=[[2+i+j] for i in range(3) for j in range(3)]
print(m)

m=[[2+i+j for i in range(4)] for j in range(4)]
print(m)

n=[(j,i) for i in range(1,4) for j in range(1,4)]
print(n)