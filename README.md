# Checkers game 
An implementation of checkers using the [pygame](https://github.com/pygame/pygame) library. In progress...

## Installation
In a new conda environment, run the following command: ```pip install -r requirements.txt```.

## Instructions for use.
To launch a game run the following command: ```python main.py```. The main game logic is handled in ```src/checkers_game.py```.

## TO DO CHECKLIST

1. make dedicated conda environment and install pygame (DONE)
2. how to make/display board (DONE)
3. how to add in movable pieces? (pieces added; make this code block more efficient and add in movability); pieces moving, can make more efficient later
4. update board based on moves made (DONE)
5. how to check and only allow valid moves? Need to enforce that moves alternate. (DONE)
6. add in take opposing piece moves
7. add in make piece a king plus king functionalities.
8. display short messages for inavlid moves, game progress, etc.?
9. what unit tests to perform? 
10. add in logging to track different game instances.