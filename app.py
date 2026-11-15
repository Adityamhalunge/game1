import tkinter Oas tk
import random

# -----------------------------
# Game Functions
# -----------------------------

choices = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0


def play_game(player_choice):
    global player_score, computer_score

    computer_choice = random.choice(choices)

    player_label.config(text=f"You: {player_choice}")
    computer_label.config(text=f"Computer: {computer_choice}")

    if player_choice == computer_choice:
        result = "Draw! 🤝"

    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win! 🎉"
        player_score += 1

    else:
        result = "Computer Wins! 🤖"
        computer_score += 1

    result_label.config(text=result)

    score_label.config(
        text=f"Score    You: {player_score}   |   Computer: {computer_score}"
    )


def reset_game():
    global player_score, computer_score

    player_score = 0
    computer_score = 0

    player_label.config(text="You: -")
    computer_label.config(text="Computer: -")
    result_label.config(text="Choose your move!")
    score_label.config(text="Score    You: 0   |   Computer: 0")


# -----------------------------
# Frontend
# -----------------------------

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x600")
root.configure(bg="#151515")
root.resizable(False, False)

# Title
title = tk.Label(
    root,
    text="ROCK PAPER SCISSORS",
    font=("Arial", 24, "bold"),
    fg="white",
    bg="#151515"
)
title.pack(pady=30)

# Result
result_label = tk.Label(
    root,
    text="Choose your move!",
    font=("Arial", 20, "bold"),
    fg="#00ff99",
    bg="#151515"
)
result_label.pack(pady=20)

# Player and computer choices
player_label = tk.Label(
    root,
    text="You: -",
    font=("Arial", 15),
    fg="white",
    bg="#151515"
)
player_label.pack(pady=5)

computer_label = tk.Label(
    root,
    text="Computer: -",
    font=("Arial", 15),
    fg="white",
    bg="#151515"
)
computer_label.pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#151515")
button_frame.pack(pady=40)

rock_button = tk.Button(
    button_frame,
    text="🪨 Rock",
    font=("Arial", 14, "bold"),
    width=10,
    command=lambda: play_game("Rock")
)
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(
    button_frame,
    text="📄 Paper",
    font=("Arial", 14, "bold"),
    width=10,
    command=lambda: play_game("Paper")
)
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(
    button_frame,
    text="✂️ Scissors",
    font=("Arial", 14, "bold"),
    width=10,
    command=lambda: play_game("Scissors")
)
scissors_button.grid(row=0, column=2, padx=10)

# Score
score_label = tk.Label(
    root,
    text="Score    You: 0   |   Computer: 0",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#151515"
)
score_label.pack(pady=20)

# Reset button
reset_button = tk.Button(
    root,
    text="Reset Game",
    font=("Arial", 12, "bold"),
    command=reset_game
)
reset_button.pack(pady=10)

root.mainloop()
