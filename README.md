# 🧩 Maze Solver - Data Structures Course Project

This project is an **interactive maze-solving visualizer**, developed using **Python** and the **Pygame** library. It was created as part of the **Data Structures** course during the **3rd semester of university**.

The core algorithm used for pathfinding in this project is **Depth-First Search (DFS)**.

---

## 📘 About the Project

In this project, the user can interactively build a maze by:
- Selecting a **start point** (red)
- Selecting an **end point** (green)
- Placing **walls** (black)

Once the setup is complete, pressing any keyboard key triggers the pathfinding process. The algorithm finds a path (if one exists) and displays it using **yellow** tiles.

---

## ⚙️ How It Works

- The maze is implemented as a **2D grid** using `pygame.Rect` objects.
- The DFS algorithm explores the maze recursively (with a stack) to find a valid path.
- Walls are treated as blocked cells and are skipped during traversal.
- The path is shown with a short delay (`time.sleep(0.1)`) for step-by-step visualization.

---

## 🔍 Algorithm: Depth-First Search (DFS)

The DFS approach is used for solving the maze:
- A stack keeps track of the current path.
- Each visited cell is marked to prevent cycles.
- When the end point is reached, the path is returned and visualized.

Although DFS is not guaranteed to find the shortest path in all cases, it is simple and efficient for solving mazes with a limited size.

---

## 📦 Requirements

- Python 3.x
- [Pygame](https://www.pygame.org/)

Install dependencies:
```bash
pip install pygame
