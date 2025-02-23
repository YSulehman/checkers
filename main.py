import argparse
from src.checkers_game import Checkers

def main():
    # make an instance of checkers
    checkers = Checkers(400, 400)

    # launch game
    checkers.play_game()

if __name__=="__main__":
    main()