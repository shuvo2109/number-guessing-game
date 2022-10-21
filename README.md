# number-guessing-game
A small python game where the computer picks a number and you have to guess it.

## Required Python Version
This program requires `Python 3.X` or above. It was originally written using `Python 3.10`.

## How to use
Open `game.py`. The game will ask you to select an upper bound for its guessing. The upper bound has to be between 10 and 6900. For example, if you enter 1234 for the upper bound, the computer will pick a random number between 1 and 1234. If you enter 7 for the upper bound, it will be discarded since 7 is less than 10 and the game will ask you to enter another value for the upper bound. A similar scenario will happen if you try to enter something like 7000.

The game will ask you to enter your guesses and give a feedback whether the number you entered is correct, lower than the number or higher than the number. At the end of the round, the game will show you the number of tries you needed to guess the number, your points scored and will ask if you want to play another around. You have to enter another upper bound for the new round.

## Required Libraries and Modules
This program uses the `random` module.

## Contact Information
For any queries or confusion, contact: rahman.fahimur21@gmail.com
