# 🎮 Rock Paper Scissors

A simple **Rock Paper Scissors game built with Python and Tkinter**.

The player chooses Rock, Paper, or Scissors, and the computer randomly selects its choice. The game keeps track of the score and displays the result.

## 🚀 Features

- 🪨 Rock
- 📄 Paper
- ✂️ Scissors
- 🎲 Random computer choice
- 🏆 Score tracking
- 🔄 Reset game button
- 🖥️ Simple graphical user interface using Tkinter

## 🛠️ Technologies Used

- Python 3
- Tkinter
- Random module
- Git
- Docker

## 📁 Project Structure

```text
rock-paper-scissors/
├── game.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/rock-paper-scissors.git
```

### 2. Go to the project directory

```bash
cd rock-paper-scissors
```

### 3. Run the game

```bash
python game.py
```

> Tkinter is included with most standard Python installations, so no external Python packages are required.

## 🐳 Docker

### Build the Docker image

```bash
docker build -t rock-paper-scissors .
```

### Run the container

```bash
docker run --name rock-paper-scissors rock-paper-scissors
```

> **Note:** This application uses Tkinter for the graphical interface. Running a Tkinter GUI inside Docker requires additional display configuration. For a browser-based Docker application, Flask would be a better choice.

## 🎮 How to Play

1. Start the game.
2. Choose **Rock**, **Paper**, or **Scissors**.
3. The computer makes a random choice.
4. The winner is displayed.
5. Your score is updated automatically.
6. Click **Reset Game** to start again.

## 🏆 Game Rules

| Player | Computer | Result |
|---|---|---|
| Rock | Scissors | You Win |
| Paper | Rock | You Win |
| Scissors | Paper | You Win |
| Same choice | Same choice | Draw |

Otherwise, the computer wins.

## 📸 Screenshot

Add a screenshot of your game here:

```markdown
![Game Screenshot](screenshot.png)
```

## 📌 Future Improvements

- Add sound effects
- Add animations
- Add dark/light mode
- Add player names
- Add best-of-5 mode
- Create a web version using Flask
- Deploy the web version using Docker

## 👨‍💻 Author

**Aditya Mhalunge**

GitHub: `https://github.com/YOUR-USERNAME`

LinkedIn: `https://www.linkedin.com/in/aditya-mhalunge`
