#!/usr/bin/env python3
from brain_games.common_logic import logic
from brain_games.games import calc_game


def main():
    logic.execute_brain_games(calc_game)


if __name__ == '__main__':
    main()
