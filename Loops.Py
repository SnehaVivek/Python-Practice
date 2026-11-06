# Fibonacci Sequence Generator
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Enter the number of terms: "))
print("Fibonacci Sequence:")
for i in range(num):
    print(fibonacci(i), end=" ")


# Rock, Paper, Scissors Game
import random
choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
for i in range(3):
    user = input("Choose rock, paper or scissors: ").lower()
    computer = random.choice(choices)
    print("Computer chose:", computer)
    if user not in choices:
        print("Invalid choice! Try again.")
        continue
    if user == computer:
        print("It's a tie!")