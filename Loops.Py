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


# Rock, Paper, Scissors Game
import random
choices_answer = ["Rock","Paper","Scissors"]
player_score =0
computer_score =0
for i in range(5):
    player = input("Enter your choice ")
    computer = random.choice(choices_answer)
    print("Player value ",player, "Computer value ",computer)
    if player ==  computer:
        print("Tie")
    elif ((player == "Rock" and computer == "Scissors") or (player == "Paper" and computer == "Rock") or (player == "Scissors" and computer == "Paper")):
        player_score +=1
        print("Player wins")
    else:
        computer_score +=1
        print("Computer wins")
if player_score > computer_score:
    print("Player wins the game")
elif (player_score == computer_score):
    print("Tie")
else:
    print("Computer  wins the game")


# Check how many vowels are in a string = your name
n="Sneha Vivek"
count=0
for i in range(len(n)):
    if n[i] == "a" or n[i] == "e" or n[i] == "i" or n[i] == "o" or n[i] == "u":
        count+=1
    else:
        continue
print(count)


# Check if a string is palindrome ( ex - madam , reverse is same as original)
n="madam"
if n==n[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


# Create a list of 10 numbers and use a for loop to:
# Print every element.
# Print only even numbers.
# Print only odd numbers.
# Calculate the sum of all elements.