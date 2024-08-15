import random

low=1
high=100
guess=0
start=True

Random=random.randint(low,high)
while start:
    num=int(input("Enter a number b/w ({low}-{high}):"))
    if(num>Random):
        guess+=1
        print("TOO HIGH! TRY AGAIN.....")
    elif(num<Random):
        guess+=1
        print("TOO LOW! TRY AGAIN......")
    else:
        print("Correct!")
        start=False
        
print(f"YOU GUESS IN {guess} ATTEMPT")
