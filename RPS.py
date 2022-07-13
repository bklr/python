import random

name = input("What is your name?: ")
print("Welcome", name)

while (True):
    c = random.choice(['rock','paper','scissors'])

    s = input("Select the following: 'rock', 'paper' , or 'scissors': ").lower()
    while(True):
        if(s == "rock" or s == "paper" or s == "scissors"):
            break
        else:
            print("Sorry! Looks like you did not choose rock, paper, OR scissors! Your selection", s + ", by default, does not beat my choice", c + "... you lose!")
            s = input("Please select a valid choice: 'rock', 'paper', or 'scissors' ").lower()

    if(s == c):
        print(f"You chose {s} and I chose {c}. Looks like we are in a stalemate!")
    elif (s == "rock" and c == "paper"):
        print(f"You chose {s} and I chose {c}. Looks I win!")
    elif (s == "rock" and c == "scissors"):
        print(f"You chose {s} and I chose {c}. Looks like you win.")
    elif (s == "paper" and c == "rock"):
        print(f"You chose {s} and I chose {c}. Looks like you win.")
    elif (s == "paper" and c =="scissors"):
        print(f"You chose {s} and I chose  {c}. Looks like I win")
    elif (s == "scissors" and c =="rock"):
        print(f"You chose {s} and I chose {c}. Looks like I win")
    elif (s == "scissors" and c =="paper"):
        print(f"You chose {s} and I chose {c}. Looks like you win")

    if(input('Would you like to play again? Y / N: ').lower() == "n"):
        print("Thanks for playing with me! Now exiting")
        break


