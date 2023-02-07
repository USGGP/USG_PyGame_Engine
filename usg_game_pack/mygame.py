import os

from usg_game_pack.pgrunner import PygameManager
from usg_game_pack.pgrunner import EventList

os.chdir(os.getcwd() + "\../usg_game_pack")

def main():
    pg_manager = PygameManager((400, 400))
    pg_manager.load_obj_json("\\".join([os.getcwd(), "object.json"]))
    pg_manager.load_comp_json("\\".join([os.getcwd(), "comp.json"]))
    pg_manager.save2json(os.getcwd())
    pg_manager.start()


if __name__ == "__main__":
    main()
