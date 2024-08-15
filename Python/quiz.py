questions = ("How many elements are in the periodic table?: ",
            "Which animal lays the largest eggs?: ",
            "What is the most abundant gas in Earth's atmosphere?: ",
            "How many bones are in the human body?: ",
            "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for x in questions:
    print("------------------------")
    print(x)
    print("------------------------")
    for option in options[question_num]:
        print(option)
    guess=input("Enter (A,B,C,D):")
    guesses.append(guess)
    if(guess==answers[question_num]):
        score+=1
        print("CORRECT")
    else:
        print("Wrong ")
        print(answers[question_num])

    question_num+=1
print("------------------------")
print("          RESULT        ")
print("------------------------")
print("ANSWER:")
for i in answers:
    print(i,end=" ")
print()
print("GUSSES:")
for i in guesses:
    print(i,end=" ")
print()
score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
        
