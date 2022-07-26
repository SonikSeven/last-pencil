# Last Pencil

This GitHub project features an implementation of the classic game Last Pencil. In this simple, interactive game, players take turns removing certain number of pencils until no pencils remain. The player to take the last pencil loses.

## Description

The Last Pencil game starts with a number of pencils laid out in a line. Two players, John and Jack, each take turns to remove either one, two, or three pencils from the line. The aim of the game is to avoid being the person to take the last pencil.

John is controlled by the user, while Jack is controlled by the bot, which can make random choices or, if possible, strategic choices based on the current state of the game.

## Rules of the Game

1. The game starts by specifying the total number of pencils.
2. Each player can take 1, 2, or 3 pencils on their turn.
3. The player to remove the last pencil loses the game.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/last-pencil.git
```

## How to Run

To run the program, follow these steps:

1. Open a terminal and navigate to the directory where the script is located.
2. Run the script using Python:

```
python main.py
```

## Usage Example

```
How many pencils would you like to use:
6
Who will be the first (John, Jack):
John
||||||
John's turn:
2
||||
Jack's turn:
1
||
John's turn:
```

## Gameplay

This is a turn-based game that starts by asking the user two questions:

- How many pencils would they like to use for the game.
- Who will make the first move.

If an invalid response is given, the game will prompt the user again with clear instructions.

To make the players' turns, John (the user) inputs a number between 1-3, and Jack (the bot) will play its turn following a set of strategic rules to enhance its chances of winning.

## License

This project is licensed under the [MIT License](LICENSE.txt).
