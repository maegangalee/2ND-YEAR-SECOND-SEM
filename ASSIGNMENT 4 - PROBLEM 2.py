fb=int(input("How many Fibonacci numbers you want: "))

a=1 
b=1

for i in range(fb):
    print(a)
    temp=a
    a=b
    b=temp+b
    