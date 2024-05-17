i=5

while i > 0:
    rpw=input("Enter Password: ")
    i -= 1

    if rpw == "jeonpogi":
        print("Logged in.")
        break
        
    elif i == 0:
        print("You are kicked off to the system.")
        
    else:
        print("Try again. You have", i, "attempt/s left.")