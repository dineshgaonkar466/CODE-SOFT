import random

print("🎮 Welcome to Rock–Paper–Scissors Game 🎮")
print("Press Ctrl + C anytime to stop the game.\n")

user_points = 0
cpu_points = 0
choices = ["rock", "paper", "scissors"]

while True:
    player = input("Your move (rock/paper/scissors): ").lower()

    if player not in choices:
        print("❌ Invalid choice! Try again.\n")
        continue

    computer = random.choice(choices)
    print(f"You chose → {player}")
    print(f"Computer chose → {computer}")

    if player == computer:
        print("It's a tie 🤝")
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        print("🎉 You win this round!")
        user_points += 1
    else:
        print("💻 Computer wins this round!")
        cpu_points += 1

    print(f"Current Score → You: {user_points} | Computer: {cpu_points}\n")
