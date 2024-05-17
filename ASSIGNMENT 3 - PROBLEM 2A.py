print("Problem: Find the last digit of 2 raised to that power.")

a=eval(input("Enter a Number: "))
b=eval(input("Enter its Power: "))

r=a**b
p=2**b
ld=p%10


print("Result of the input numbers: ", r)
print("2 raised to the input power: ", p)
print("Answer to the problem: ", ld)

