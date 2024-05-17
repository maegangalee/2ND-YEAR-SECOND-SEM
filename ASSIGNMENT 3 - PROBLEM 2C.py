print("Problem: Find the last that many digits of 2 raised to the power the user entered.")

a=eval(input("Enter Power: "))
b=eval(input("Enter how many digits you want: "))

p=2**a

ld=p%(10**b)

print("2 raised to the input power: ", p)
print("Answer to the problem: ", ld)

