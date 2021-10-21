# Write a function to compute 5/0 and use try/except to catch the exceptions.

def do_math(a,b):
    if b==0:
        raise Exception("Error!!!Division by Zero")
    else:
        x=a/b
    return x

def main():
    a=int(input("Enter Numerator\t"))
    b=int(input("Enter Denomenator\t"))
    try:
        y=do_math(a,b)
        print("Result is: ",y)
    except Exception as e:
        print(e)

main()

# Implement a Python program to generate all sentences where subject is in
# ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
# ["Baseball","cricket"].

def form_sentance(subjects,verbs,objects):
    for i in subjects:
        for j in verbs:
            for k in objects:
                print(i,j,k)

def main():
    subjects=[]
    verbs=[]
    objects=[]

    for i in range(100):
        s=input("Enter Subject\t")
        if s!="end":
            subjects.append(s)
        else:
            break
    for j in range(100):
        v=input("Enter Verb\t")
        if v!="end":
            verbs.append(v)
        else:
            break
    for k in range(100):
        o=input("Enter Objects\t")
        if o!="end":
            objects.append(o)
        else:
            break
    form_sentance(subjects,verbs,objects)

main()