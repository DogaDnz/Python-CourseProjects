import random

# Rock
Rock = ("""
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
Paper = ("""
Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
Scissors = ("""
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

user =input("Which move do you want to choose? (paper,rock or scissors)").lower()

computer = random.randint(0,2)
if computer == 0:
    computermove ="paper"
elif computer == 1:
    computermove = "rock"
elif computer == 2:
    computermove = "scissors"


if user == "paper" and computermove == "paper":
    print(f"Your move is {Paper}")
    print(f"Computer's move is {Paper} ")
    print("It is draw.")
elif user == "rock" and computermove == "rock":
    print(f"Your move is {Rock}")
    print(f"Computer's move is {Rock} ")
    print("It is draw.")
elif user == "scissors" and computermove == "scissors":
    print(f"Your move is {Scissors}")
    print(f"Computer's move is {Scissors} ")
    print("It is draw.")
elif user == "paper" and computermove == "rock":
    print(f"Your move is {Paper}")
    print(f"Computer's move is {Rock} ")
    print("You Won.")
elif user == "paper" and computermove == "scissors":
    print(f"Your move is {Paper}")
    print(f"Computer's move is {Scissors} ")
    print("You Lost.")
elif user == "rock" and computermove == "paper":
    print(f"Your move is {Rock}")
    print(f"Computer's move is {Paper} ")
    print("You lost.")
elif user == "rock" and computermove == "scissors":
    print(f"Your move is {Rock}")
    print(f"Computer's move is {Scissors} ")
    print("You Won.")
elif user == "scissors" and computermove == "paper":
    print(f"Your move is {Scissors}")
    print(f"Computer's move is {Paper} ")
    print("You Won.")
elif user == "scissors" and computermove == "rock":
    print(f"Your move is {Scissors}")
    print(f"Computer's move is {Rock} ")
    print("You Lost.")
else :
    print("Please write only paper rock or scissors!! ")



