import pygame as pg
from dataclasses import dataclass


@dataclass
class PgText:
    surface: object = None
    key: str = None
    font: object = None
    text: str = None
    pos: tuple = None
    color: tuple = None
    anti: bool = True


def set_text(
        pgtext: PgText,
        path: str,
        key: str,
        pos: tuple,
        text: str,
        font_sz: int,
        color: tuple = (0, 0, 0),
        anti: bool = True
) -> None:
    """
    Set text
    if text is none, creating text dataclass

    Args:
        pgtext: The structure for text dataclass
        key: The id
        text: The text for displaying
        path: The text source path
        pos: pos for text
        font_sz: The size of font
        color: The color for font
        anti: The antialiasing for text
    """
    pgtext = PgText() if pgtext is None else pgtext
    pgtext.key = key
    pgtext.front = pg.font.Font(path, font_sz)
    pgtext.text = text
    pgtext.color = color
    pgtext.pos = pos
    pgtext.anti = anti
    pgtext.surface = pgtext.front.render(pgtext.text, anti, color)
