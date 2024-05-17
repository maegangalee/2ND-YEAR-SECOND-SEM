a=eval(input("Price of the meal: "))
b=eval(input("Tip Percentage: "))
c=eval(input("Number of People: "))


TP=b/100
TP2=TP+1

TIP=a*TP
NP=TIP/c

ALLTotal=a*TP2

print("Total Tip: ",TIP)
print("Tip divided per person: ",NP)
print("All Total Amount: ", ALLTotal)