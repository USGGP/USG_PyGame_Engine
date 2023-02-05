import os

from usg_game_pack.pgrunner import PygameManager
from usg_game_pack.pgrunner import EventList

os.chdir(os.getcwd())

def main():
    pg_manager = PygameManager((400, 400))
    pg_manager.load_obj_json("temp.json")
    pg_manager.load_comp_json("data.json")
    pg_manager.save2json(os.getcwd())
    pg_manager.start()


if __name__ == "__main__":
    main()
