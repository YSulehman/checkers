import argparse
from src.checkers_game import Checkers

def main():
    # make an instance of checkers
    checkers = Checkers(640, 640)

    # launch game
    checkers.play_game()

if __name__=="__main__":
    main()