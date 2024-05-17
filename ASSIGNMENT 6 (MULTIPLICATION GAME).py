print("\t\t\t\t MULTIPLICATION GAME")

from random import randint 

player_score=0

for i in range (1,11):
    n1=randint(1,10)
    n2=randint(1,10)
    correct_ans=n1*n2

    
    print("\nQuestion ", i, ":", n1, "x", n2, "=", end="")
    player_ans = int(input(""))
    
    if player_ans == correct_ans:
        print("Right!")
        player_score = player_score + 1
        
    else:
        print("Wrong. The answer is ", correct_ans)
        

print("\n\n\nYou got ", player_score, "out of ten.")
    
    
    
