# Checkers game 
An implementation of checkers using the [pygame](https://github.com/pygame/pygame) library. In progress...

## Installation
In a new conda environment, run the following command: ```pip install -r requirements.txt```.

## Instructions for use.
To launch a game run the following command: ```python main.py```. The main game logic is handled in ```src/checkers_game.py```.

## TO DO CHECKLIST

Progress on multiple-jump take moves by utilising mouse tracking... Next:

1. angle tracking for valid moves; what range should it fall within for each team?
2. Updating position of moving piece for multiple-jump move?
3. add in make piece a king plus king functionalities.
4. display short messages for inavlid moves, game progress, etc.?
5. what unit tests to perform? 
6. add in logging to track different game instances.