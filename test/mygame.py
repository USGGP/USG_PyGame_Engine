import os

from usg_game_pack.pgrunner import PygameManager
from usg_game_pack.pgrunner import EventList


def test():
    print("test")
    return 1 + 2


def main():
    pg_manager = PygameManager((400, 400))
    pg_manager.load_json("temp.json")
    pg_manager.start()


if __name__ == "__main__":
    main()
