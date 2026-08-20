# Asteroids

A classic **Asteroids-style arcade game** built with Python and Pygame as part of the [Boot.dev](https://www.boot.dev/) learning project.

The project focuses on learning and applying Python programming concepts through the development of a small 2D game, including object-oriented programming, game loops, sprite groups, collision detection, movement, shooting, and asteroid spawning.

## 🎮 Features

* Control a spaceship in a 2D space environment
* Rotate and move the player ship
* Shoot projectiles at asteroids
* Asteroids spawn continuously around the game area
* Destroyed asteroids split into smaller asteroids
* Collision detection between:

  * Player and asteroids
  * Shots and asteroids
* Game-over condition when the player collides with an asteroid
* Game loop running at 60 FPS
* Basic event and state logging

## 🛠️ Tech Stack

* **Python 3.13+**
* **Pygame 2.6.1**
* **uv** for Python project and dependency management

The project's `pyproject.toml` specifies Python 3.13+ and Pygame 2.6.1 as the main dependency.

## 📁 Project Structure

```text
Asteroids/
├── asteroid.py          # Asteroid game object and behavior
├── asteroidfield.py     # Asteroid spawning and field management
├── circleshape.py       # Base circular game-object implementation
├── constants.py         # Game configuration and constants
├── logger.py            # Game state and event logging
├── main.py              # Main game loop and initialization
├── player.py            # Player spaceship and controls
├── shot.py              # Projectile implementation
├── pyproject.toml       # Project configuration and dependencies
├── uv.lock              # Locked dependency versions
├── .python-version      # Python version configuration
└── README.md
```

## 🚀 Getting Started

### Prerequisites

Make sure you have:

* Python **3.13 or later**
* [uv](https://docs.astral.sh/uv/) installed

You can verify your Python version with:

```bash
python --version
```

And verify `uv`:

```bash
uv --version
```

### Clone the Repository

```bash
git clone https://github.com/quikrish/Asteroids.git
cd Asteroids
```

### Install Dependencies

Using `uv`:

```bash
uv sync
```

This creates the project's environment and installs the dependencies defined in `pyproject.toml`.

### Run the Game

```bash
uv run main.py
```

Alternatively, if the dependencies have already been installed in your active environment:

```bash
python main.py
```

## 🎮 Controls

| Key     | Action       |
| ------- | ------------ |
| `W`     | Move forward |
| `A`     | Rotate left  |
| `D`     | Rotate right |
| `Space` | Shoot        |

## 🧩 How the Game Works

The game is built around a continuous game loop.

At startup, the game:

1. Initializes Pygame.
2. Creates the game window.
3. Creates sprite groups for objects that need to be updated and/or drawn.
4. Creates the player.
5. Creates the asteroid field.
6. Continuously processes input and game events.
7. Updates game objects.
8. Checks for collisions.
9. Draws the objects to the screen.
10. Updates the display.

The game loop is limited to approximately **60 frames per second**.

### Player

The `Player` class represents the spaceship. It handles:

* Position
* Rotation
* Movement
* Shooting
* Shooting cooldown
* Rendering the spaceship

### Asteroids

Asteroids are represented by the `Asteroid` class.

When a projectile hits an asteroid, the asteroid is destroyed and can split into smaller asteroids.

### Shots

The `Shot` class represents projectiles fired by the player.

When a shot collides with an asteroid:

```text
Shot
  │
  ▼
Asteroid collision
  │
  ├── Asteroid destroyed
  ├── Smaller asteroids created
  └── Shot removed
```

### Collision Detection

The game checks collisions between the player and asteroids as well as between shots and asteroids.

A player collision results in:

```text
Game Over!
```

## 📚 Learning Objectives

This project was developed as a practical way to learn Python and game development concepts.

Some of the concepts covered include:

* Python classes and inheritance
* Object-oriented programming
* Class attributes
* Methods and constructors
* `pygame.sprite.Group`
* Game loops
* Event handling
* Vector-based movement
* Rotation
* Collision detection
* Object spawning
* Object destruction
* Timers and cooldowns
* Modular Python code organization
* Dependency management with `uv`

## 🔧 Development

The project uses a `pyproject.toml` configuration and a `uv.lock` file to keep dependencies reproducible.

After making changes, run the game with:

```bash
uv run main.py
```

## 📝 Project Status

This project is primarily a **learning project** based on the Boot.dev Asteroids course.

Additional gameplay features such as scoring, lives, levels, sound effects, menus, and other enhancements can be added as future exercises.

## 📖 Credits

Built as part of the **Boot.dev Asteroids Game Project**.

* Boot.dev: https://www.boot.dev/
* Pygame: https://www.pygame.org/

## 📄 License

This project is intended primarily for educational and learning purposes.
