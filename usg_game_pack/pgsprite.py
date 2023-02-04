import os

import pygame as pg
from dataclasses import dataclass


@dataclass
class PgSprite:
    surface: object = None  # The source image
    pos: tuple = None  # The position of image
    rect: tuple = None  # The rect of image
    src_rect: tuple = None  # The rect of source image
    tran_rect: tuple = None  # The transform rect of image
    key: str = None

def set_sprite(sprite: PgSprite,
               path: str,
               key: str,
               pos: tuple,
               crop_rect: tuple = None,
               slice_rect: tuple = None,
               tran_rect: tuple = None
) -> None:
    """
    Set sprite
    if sprite is none, creating sprite dataclass

    Args:
        sprite: The structure of sprite
        key: The id
        path: The image source
        pos: The position of image in surface
        crop_rect: The cropping rect (directly edit the image)
        slice_rect: It slice the image (# width, # height, pos of row, pos of col)
        tran_rect: The size of resizing the image

    Returns:
        None
    """
    sprite = PgSprite() if sprite is None else sprite
    sprite.surface = pg.image.load(path).convert_alpha()
    sprite.src_rect = sprite.surface.get_rect()
    sprite.pos = pos
    sprite.key = key
    if crop_rect is not None and all(x >= 0 for x in crop_rect):
        sprite.surface = sprite.surface.subsurface(sprite.rect)
    if slice_rect is not None and all(x >= 0 for x in slice_rect):
        sprite_w = sprite.src_rect[0] / slice_rect[0]
        sprite_h = sprite.src_rect[1] / slice_rect[1]
        sprite.rect = (sprite_w,
                       sprite_h,
                       sprite.src_rect[2] * sprite_w,
                       sprite.src_rect[3] * sprite_h)
        sprite.surface = sprite.surface.subsurface(sprite.rect)
    if tran_rect is not None and all(x >= 0 for x in tran_rect):
        sprite.tran_rect = tran_rect
        sprite.surface = pg.transform.scale(sprite.surface, sprite.tran_rect)
