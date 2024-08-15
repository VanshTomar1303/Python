import random

comp=["ROCK","PAPER","SCISSOR"]

win=0
lose=0
draw=0

print(".......THIS GAME RUN FIVE TIME.......")
for x in range(1,6):
    print("---------------------------------------")
    print(f"CHANCE {x}")
    player1=input("ENTER (ROCK,PAPER,SCISSOR):")
    comp_chance=random.choice(comp)
    print(f"COMPUTER MOVE:{comp_chance}")

    if comp_chance==player1:
        draw+=1
        print("DRAW")
    elif comp_chance=="SCISSOR" and player1=="ROCK":
        win+=1
        print("YOU WIN!")
    elif comp_chance=="ROCK" and player1=="PAPER":
        win+=1
        print("YOU WIN!")
    elif comp_chance=="PAPER" and player1=="SCISSOR":
        win+=1
        print("YOU WIN!")
    else:
        lose+=1
        print("COMPUTER WIN!")

print("-------------------------------------")
print(f"WIN:{win}")
print(f"LOSE:{lose}")
print(f"DRAW:{draw}")