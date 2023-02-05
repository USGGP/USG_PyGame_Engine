
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
    LAYER = "layer"     # layer hirechy
    KEY = "key"         # key id
    PATH = "path"       # file path
    POS = "pos"         # position
    ENABLE = "enable"   # visibility on off


class EVENT_FEATURE:
    EVENT_TRIGGER = "event_trigger"


class SPRITE_FEATURE:
    CROP_RECT = "crop_rect"
    SLICE_RECT = "slice_rect"
    TRAN_RECT = "tran_rect"


class TEXT_FEATURE:
    TEXT = "text"
    FONT_SZ = "font_sz"
    COLOR = "color"
    ANTI = "anti"