number=""
count=0
num=0


while number != 0:
    number=eval(input("Enter number (0 to end): "))
    count += 1
    num=num+number
    
    if number == 0:
        break

print("Count: ", (count)-1)
print("Sum: ", num)
print("Mean: ", num/(count-1))