# 🎮 Tetris Game (Python Edition)

[![Watch the demo on YouTube](https://your-youtube-link.com)](https://your-youtube-link.com)

## 🎬 Inspiration

The other day, I was watching the movie *Tetris* (2023), which tells the fascinating story behind the discovery of the game and the challenges of obtaining its licensing rights. After finishing the film, I felt the urge to play a classic Tetris game.

I started searching for a legal version online, but most of the ones I found were modern remakes. I really wanted to play the original, classic version. After some time browsing, I thought to myself, *"I'm a programmer, why not build my own Tetris?"* So I opened my laptop, launched Visual Studio Code, and started coding.

I chose **Python** for this project since it's the language I’m most comfortable with. Here's how it came together!

## ⚙️ Technologies Used

- **Python 3.12.6** – Main programming language.
- **Pygame 2.6.1** – For rendering graphics, handling events, and managing game loops.
- **PyInstaller** – To package the game into a standalone executable.
- **Blackhole (macOS)** – To record in-game audio during development.
- **VSCode** – The primary code editor.

## 🚧 Challenges Faced

- **Key Repeat Logic:** Implementing smooth and responsive key hold functionality for moving and dropping pieces took several iterations to perfect.
- **Scoring System:** Designing a balanced scoring mechanism that factors in both the number of cleared lines and the current level.
- **Instant Drop Feature:** Implementing a "hard drop" that allows the piece to instantly fall to the bottom and lock in place.
- **Game Packaging:** Creating a working `.exe` (and `.app` for macOS) using PyInstaller while ensuring all dependencies, like music and assets, were bundled correctly.

## 🕹️ How to Play

### 🎯 Objective

Clear as many lines as possible by completing horizontal rows without gaps. The game speeds up as you level up, increasing the challenge.

### 🎮 Controls

| Action             | Default Key |
|--------------------|-------------|
| Move Left          | Left Arrow  |
| Move Right         | Right Arrow |
| Soft Drop          | Down Arrow  |
| Hard Drop          | Spacebar    |
| Rotate Piece       | Up Arrow    |
| Pause Game         | Esc         |
| Configure Controls | C (in Menu) |
| Start Game         | Enter       |

*Note:* You can reconfigure movement keys in the menu.

### 🧮 Scoring

The scoring system is based on a combination of lines cleared, level multipliers, and bonus coefficients:

- **Base Formula:** `(10 × number of lines) × (line coefficient × level multiplier)`

- **Line Clear Coefficients:**
  - 1 line → ×1.0
  - 2 lines → ×1.2
  - 3 lines → ×1.6
  - 4 lines (Tetris) → ×2.0

- **Level Multipliers:**
  - Level 1 → ×1.0
  - Level 2 → ×1.1
  - Level 3 → ×1.2
  - … up to Level 10 → ×2.0

You need **300 points** to advance to the next level.

## 🛠️ How to Run

### ▶️ Run from Source

1. **Clone the repository:**
   ```bash
   git clone https://github.com/RaulEstevezA/tetrisInPython.git
   cd tetrisInPython
   ```

2. **Install Dependencies:**
   ```bash
   pip install pygame
   ```

3. **Run the Game:**
   ```bash
   python tetris.py
   ```

### 📦 Build Executable

If you want to create a standalone executable:

1. **Install PyInstaller:**
   ```bash
   pip install pyinstaller
   ```

2. **Build the game:**
   ```bash
   pyinstaller --onefile --windowed tetris.py
   ```

3. **Find the executable:**  
   The `.exe` or `.app` will be located in the `dist/` folder.

## 🎵 Audio & Music

- The game includes a background track inspired by classic Tetris tunes.
- Music playback is handled using Pygame's mixer.
- Volume is set to 60% by default but can be adjusted in the source.

## 📹 Demo Video

Check out the gameplay demo on [YouTube](https://your-youtube-link.com) to see it in action!

## 📋 License

This project is for educational and personal use.  
Inspired by the original **Tetris** game concept, but all code here is original.

## 🚀 Final Thoughts

This project was a fun dive into game development using Python. It helped me sharpen my skills with Pygame, understand game loop logic, and tackle challenges like input handling, scoring systems, and packaging for distribution.

If you enjoy it, feel free to leave feedback or suggest improvements. Happy stacking!

🎉 **Thanks for playing!** 🎉

