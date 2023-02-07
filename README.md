# USG_PyGame_Engine
This is pygame engine project\
You can easily create 2D game\
It uses kind of ECS system through pandas table

<img src=https://user-images.githubusercontent.com/47798805/217277074-659e8e5e-43fe-446f-a044-bf38d8e16188.png width="350" height="350"><img src=https://user-images.githubusercontent.com/47798805/217277164-347df1e5-526d-41cf-89d9-0ae46319141c.png width="350" height="350">

## How to use
1. run pgengine.py
2. create object through create object button
3. create component through create comp button
* The component must written as json format 
* It must include key: str, object: str and enable: bool
4. coding function
5. click the world start

## Guide for using GUI
<img src= https://user-images.githubusercontent.com/47798805/217285645-a6008c9b-b65c-4665-82d7-4d08100582a8.png width="250" height="200">

+ OBJECT NAME: The name of object that will be used for the game
+ COMP TYPE: There are three different type of object component 
  + [sprite_comp]: It is used for image object\
  + [text_comp]: It is used for text object\
  + [func_comp]: It is used for calling function (not function itself)
* layer: The order of drawing object
* key: to distinguish the object (object can have the same name but not the same key)
* pos: position of image (other component not use it)
* ENABLE: check it for using in game

+ Sprite 
<img src= https://user-images.githubusercontent.com/47798805/217285162-b28aa226-51e4-4c63-8414-faafe41e1534.png width="200" height="150">

* crop_rect: Rect of cropping for image
* slice_rect: Rect for slicing image by index [x,y, # slice w,  # slice h]
* tran_rect: Change the size of image

## other license
- USG_PyGame_Engine : GNU Affero License
- PyGame : LGPL License
- PySimpleGUI : LGPL License
- pandas: BSD 3
- numpy: https://numpy.org/doc/stable/license.html
