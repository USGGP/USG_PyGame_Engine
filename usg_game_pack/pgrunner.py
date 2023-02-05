from abc import abstractmethod

from usg_game_pack.pgevent import CEvent, set_event, run_python_event
from usg_game_pack.pgsprite import PgSprite
from usg_game_pack.pgsprite import set_sprite
from usg_game_pack.pgtext import PgText
from usg_game_pack.pgtext import set_text
from usg_game_pack.pgfeature import *

import pygame as pg
import json
import pandas as pd

pd.options.mode.chained_assignment = None
from threading import Thread

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class PygameManager:
    """
    This class is the main structure for playing game
    """

    @abstractmethod
    def __init__(self, size: tuple, title: str = "USG GAME BY PYGAME") -> None:
        """
        This initiates the setting

        Args:
            size: The window size
            title: The window title
        Returns:
            None
        """
        pg.init()
        self._size = size
        self._screen = pg.display.set_mode(self._size)
        pg.display.set_caption(title)
        self._done = False
        self._tabular_object = None
        self._clock = pg.time.Clock()
        # Pre data structure
        self._object_feature_list = {}
        self._tabular_comp = None
        self._event_list = {
            EventList.MOUSE_EVENT: [],
            EventList.KEY_DOWN_EVENT: [],
            EventList.KEY_UP_EVENT: [],
            EventList.DISPLAY_EVENT: []
        }

    @abstractmethod
    def start_thread(self):
        Thread(target=self._loop).start()

    @abstractmethod
    def start(self):
        self._loop()

    @abstractmethod
    def load_obj_json(self, path: str):
        """
        Load the json file which has the feature of object list
        """
        print("load obj json")
        with open(path, "r") as json_file:
            self._object_feature_list = json.load(json_file)
        self._object_table_set()

    @abstractmethod
    def load_comp_json(self, path: str):
        """
        Load the json file which has the feature of object list
        """
        print("load comp json")
        self._tabular_comp = pd.read_json(path, orient='index', dtype=object)
        self._component_table_set()

    @abstractmethod
    def load_comp_csv(self, path: str):
        """
        Load the json file which has the feature of object list
        """
        print("load comp json")
        self._tabular_comp = pd.read_csv(path)
        self._component_table_set()

    @abstractmethod
    def save2json(self, path: str):
        """
        save table data in json format
        Args:
            path: The path of save folder
        """
        self._tabular_comp.to_json(path + "_comp.json", default_handler=str, orient='records', indent=2)
        self._tabular_object.to_json(path + "_object.json", default_handler=str, orient='records', indent=2)

    @abstractmethod
    def save2csv(self, path: str):
        """
        save table data in csv format
        Args:
            path: The path of save folder
        """
        self._tabular_comp.to_csv(path + "_comp.csv", index=True)
        self._tabular_object.to_csv(path + "_object.csv", index=True)

    def _object_table_set(self):
        for row, col in self._object_feature_list.items():
            col[COMMON_FEATURE.POS] = list(map(int, col[COMMON_FEATURE.POS])) if col[
                                                                                     COMMON_FEATURE.POS] is not None else None
            col[SPRITE_FEATURE.CROP_RECT] = list(map(int, col[SPRITE_FEATURE.CROP_RECT])) if col[
                                                                                                 SPRITE_FEATURE.CROP_RECT] is not None else None
            col[SPRITE_FEATURE.SLICE_RECT] = list(map(int, col[SPRITE_FEATURE.SLICE_RECT])) if col[
                                                                                                   SPRITE_FEATURE.SLICE_RECT] is not None else None
            col[SPRITE_FEATURE.TRAN_RECT] = list(map(int, col[SPRITE_FEATURE.TRAN_RECT])) if col[
                                                                                                 SPRITE_FEATURE.TRAN_RECT] is not None else None
            col[TEXT_FEATURE.COLOR] = list(map(int, col[TEXT_FEATURE.COLOR])) if col[
                                                                                     TEXT_FEATURE.COLOR] is not None else None
            df = {row: {
                COMMON_FEATURE.LAYER: int(col[COMMON_FEATURE.LAYER]),
                CompList.OBJECT: col[CompList.OBJECT],
                CompList.TYPE: col[CompList.TYPE],
                COMMON_FEATURE.KEY: col[COMMON_FEATURE.KEY],
                COMMON_FEATURE.PATH: col[COMMON_FEATURE.PATH],
                COMMON_FEATURE.POS: col[COMMON_FEATURE.POS],
                COMMON_FEATURE.ENABLE: bool(col[COMMON_FEATURE.ENABLE]),
                SPRITE_FEATURE.CROP_RECT: col[SPRITE_FEATURE.CROP_RECT],
                SPRITE_FEATURE.SLICE_RECT: col[SPRITE_FEATURE.SLICE_RECT],
                SPRITE_FEATURE.TRAN_RECT: col[SPRITE_FEATURE.TRAN_RECT],
                TEXT_FEATURE.TEXT: col[TEXT_FEATURE.TEXT],
                TEXT_FEATURE.FONT_SZ: int(col[TEXT_FEATURE.FONT_SZ]),
                TEXT_FEATURE.COLOR: col[TEXT_FEATURE.COLOR],
                TEXT_FEATURE.ANTI: bool(col[TEXT_FEATURE.ANTI]),
                EVENT_FEATURE.EVENT_TRIGGER: col[EVENT_FEATURE.EVENT_TRIGGER]
            }}
            self._tabular_object = pd.concat([self._tabular_object, pd.DataFrame(data=df).transpose()])
        self._tabular_object = self._tabular_object.sort_values(by=[COMMON_FEATURE.LAYER], ascending=True)
        print(self._tabular_object.to_string())

    def _component_table_set(self):
        print(self._tabular_comp)

    def _run_table(self):
        for index, row in self._tabular_object.iterrows():
            if not row[COMMON_FEATURE.ENABLE]:
                continue
            if row[CompList.TYPE] == CompList.SPRITE:
                temp = PgSprite()
                sprite_feature = {
                    COMMON_FEATURE.PATH: row[COMMON_FEATURE.PATH],
                    COMMON_FEATURE.KEY: row[COMMON_FEATURE.KEY],
                    COMMON_FEATURE.POS: row[COMMON_FEATURE.POS],
                    SPRITE_FEATURE.CROP_RECT: row[SPRITE_FEATURE.CROP_RECT],
                    SPRITE_FEATURE.SLICE_RECT: row[SPRITE_FEATURE.SLICE_RECT],
                    SPRITE_FEATURE.TRAN_RECT: row[SPRITE_FEATURE.TRAN_RECT]
                }
                set_sprite(temp, **sprite_feature)
                self._screen.blit(temp.surface, temp.pos)
            elif row[CompList.TYPE] == CompList.TEXT:
                temp = PgText()
                text_feature = {
                    COMMON_FEATURE.PATH: row[COMMON_FEATURE.PATH],
                    COMMON_FEATURE.KEY: row[COMMON_FEATURE.KEY],
                    COMMON_FEATURE.POS: row[COMMON_FEATURE.POS],
                    TEXT_FEATURE.TEXT: row[TEXT_FEATURE.TEXT],
                    TEXT_FEATURE.FONT_SZ: row[TEXT_FEATURE.FONT_SZ],
                    TEXT_FEATURE.COLOR: row[TEXT_FEATURE.COLOR],
                    TEXT_FEATURE.ANTI: row[TEXT_FEATURE.FONT_SZ]
                }
                set_text(temp, **text_feature)
                self._screen.blit(temp.surface, temp.pos)
            elif row[CompList.TYPE] == CompList.EVENT:
                temp = CEvent()
                event_feature = {
                    COMMON_FEATURE.PATH: row[COMMON_FEATURE.PATH],
                    EVENT_FEATURE.EVENT_TRIGGER: row[EVENT_FEATURE.EVENT_TRIGGER],
                }
                set_event(temp, **event_feature)
                trg_comp_list = self._tabular_comp[self._tabular_comp[CompList.OBJECT] == row[CompList.OBJECT]
                                                   & self._tabular_comp[COMMON_FEATURE.ENABLE] is True].transpose().to_dict()
                for key, trg_comp in trg_comp_list.items():
                    run_python_event(temp, trg_comp)
                    self._tabular_comp.loc[key] = pd.Series(trg_comp)
            print(self._tabular_comp)

    @abstractmethod
    def _game_loop(self):
        pass

    def _loop(self):
        """
        Actual game loop
        """
        while not self._done:
            self._clock.tick(10)
            # exit check
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self._done = True
            self._screen.fill(WHITE)
            self._run_table()
            pg.display.flip()
