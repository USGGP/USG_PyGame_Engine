from abc import abstractmethod

import pandas

from usg_game_pack.pgevent import CEvent, set_event, run_python_event
from usg_game_pack.pgsprite import PgSprite
from usg_game_pack.pgsprite import set_sprite
from usg_game_pack.pgtext import PgText
from usg_game_pack.pgtext import set_text

import pygame as pg
import json
import pandas as pd
from threading import Thread

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class CompList:
    OBJECT = 'object'
    TYPE = 'type'
    SPRITE = 'sprite_comp'
    TEXT = 'text_comp'
    EVENT = 'event_comp'


class EventList:
    MOUSE_EVENT = "mouse"
    KEY_DOWN_EVENT = 'key-down'
    KEY_UP_EVENT = 'key-up'
    DISPLAY_EVENT = 'display'


class COMMON_FEATURE:
    LAYER = "layer"
    KEY = "key"
    PATH = "path"
    POS = "pos"


class EVENT_FEATURE:
    EVENT_TRIGGER = "event_trigger"
    EVENT_VAL = "event_val"
    EVENT_ANS = "event_ans"
    EVENT_RECV = "event_recv"

class SPRITE_FEATURE:
    CROP_RECT = "crop_rect"
    SLICE_RECT = "slice_rect"
    TRAN_RECT = "tran_rect"


class TEXT_FEATURE:
    TEXT = "text"
    FONT_SZ = "font_sz"
    COLOR = "color"
    ANTI = "anti"


class PygameManager:
    @abstractmethod
    def __init__(self, size: tuple):
        """
        This initiates the setting

        Args:
            size: The window size
        """
        pg.init()
        self._size = size
        self._screen = pg.display.set_mode(self._size)
        pg.display.set_caption("Useop Game")
        self._done = False
        self.tabular = None
        self._clock = pg.time.Clock()
        # Pre data structure
        self.feature_list = {}
        self._comp_list = {}
        self._event_list = {
            EventList.MOUSE_EVENT: [],
            EventList.KEY_DOWN_EVENT: [],
            EventList.KEY_UP_EVENT: [],
            EventList.DISPLAY_EVENT: []
        }

    @abstractmethod
    def load_json(self, path: str):
        """
        Load the json file which has feature list
        """
        print("load json")
        with open(path, "r") as json_file:
            self.feature_list = json.load(json_file)
        self.table_set()

    @abstractmethod
    def table_set(self):
        for row, col in self.feature_list.items():
            col[COMMON_FEATURE.POS] = [col[COMMON_FEATURE.POS][0], col[COMMON_FEATURE.POS][1]]
            col[SPRITE_FEATURE.CROP_RECT] = [-1, -1, -1, -1] if col[SPRITE_FEATURE.CROP_RECT] is None else col[
                SPRITE_FEATURE.CROP_RECT]
            col[SPRITE_FEATURE.SLICE_RECT] = [-1, -1, -1, -1] if col[SPRITE_FEATURE.SLICE_RECT] is None else col[
                SPRITE_FEATURE.SLICE_RECT]
            col[SPRITE_FEATURE.TRAN_RECT] = [-1, -1] if col[SPRITE_FEATURE.TRAN_RECT] is None else [
                col[SPRITE_FEATURE.TRAN_RECT][0], col[SPRITE_FEATURE.TRAN_RECT][1], -1, -1]
            col[TEXT_FEATURE.COLOR] = [col[TEXT_FEATURE.COLOR][0], col[TEXT_FEATURE.COLOR][1],
                                       col[TEXT_FEATURE.COLOR][2]]
            df = {row: {
                COMMON_FEATURE.LAYER: pd.to_numeric(col[COMMON_FEATURE.LAYER]).astype(int),
                CompList.OBJECT: col[CompList.OBJECT],
                CompList.TYPE: col[CompList.TYPE],
                COMMON_FEATURE.KEY: col[COMMON_FEATURE.KEY],
                COMMON_FEATURE.PATH: col[COMMON_FEATURE.PATH],
                COMMON_FEATURE.POS: pd.array(col[COMMON_FEATURE.POS], dtype='int32'),
                SPRITE_FEATURE.CROP_RECT: pd.array(col[SPRITE_FEATURE.CROP_RECT], dtype='int32'),
                SPRITE_FEATURE.SLICE_RECT: pd.array(col[SPRITE_FEATURE.SLICE_RECT], dtype='int32'),
                SPRITE_FEATURE.TRAN_RECT: pd.array(col[SPRITE_FEATURE.TRAN_RECT], dtype='int32'),
                TEXT_FEATURE.TEXT: col[TEXT_FEATURE.TEXT],
                TEXT_FEATURE.FONT_SZ: pd.to_numeric(col[TEXT_FEATURE.FONT_SZ]).astype(int),
                TEXT_FEATURE.COLOR: pd.array(col[TEXT_FEATURE.COLOR], dtype='int32'),
                TEXT_FEATURE.ANTI: True if col[TEXT_FEATURE.ANTI].lower() == "true" else False,
                EVENT_FEATURE.EVENT_TRIGGER: col[EVENT_FEATURE.EVENT_TRIGGER],
                EVENT_FEATURE.EVENT_VAL: col[EVENT_FEATURE.EVENT_VAL],
                EVENT_FEATURE.EVENT_ANS: col[EVENT_FEATURE.EVENT_ANS]
            }}
            self.tabular = pd.concat([self.tabular, pd.DataFrame(data=df).transpose()])
        self.tabular = self.tabular.sort_values(by=[COMMON_FEATURE.LAYER], ascending=True)
        print(self.tabular.to_string())

    @abstractmethod
    def table2obj(self):
        for index, row in self.tabular.iterrows():
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
            elif row[CompList.TYPE] == CompList.EVENT:
                temp = CEvent()
                event_feature = {
                    COMMON_FEATURE.PATH: row[COMMON_FEATURE.PATH],
                    EVENT_FEATURE.EVENT_TRIGGER: row[EVENT_FEATURE.EVENT_TRIGGER],
                    EVENT_FEATURE.EVENT_VAL: row[EVENT_FEATURE.EVENT_VAL],
                    EVENT_FEATURE.EVENT_ANS: row[EVENT_FEATURE.EVENT_ANS]
                }
                set_event(temp, **event_feature)
                run_python_event(temp)

    @abstractmethod
    def start_thread(self):
        Thread(target=self._loop).start()

    @abstractmethod
    def start(self):
        self._loop()

    @abstractmethod
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
            self.table2obj()
            pg.display.flip()
