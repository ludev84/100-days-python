import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if (player > 2 or player < 0): print("You typed an invalid number, you lose!")
else:
  computer = random.randint(0,2)
  
  print(options[player])
  
  print("Computer chose:")
  
  print(options[computer])
  
  if (player == computer): print("It's a draw")
  elif (player == 0 and computer == 2): print("You win")
  elif (player == 1 and computer == 0): print("You win")
  elif (player == 2 and computer == 1): print("You win")
  else: print("You lose")