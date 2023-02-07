
<img src= https://user-images.githubusercontent.com/47798805/217285645-a6008c9b-b65c-4665-82d7-4d08100582a8.png width="250" height="200">

+ ```OBJECT NAME```: The name of object that will be used for the game
+ ```COMP TYPE```: There are three different type of object component 
  + [sprite_comp]: It is used for image object
  + [text_comp]: It is used for text object
  + [func_comp]: It is used for calling function (not function itself)
* ```layer```: The order of drawing object
* ```key```: object unique id (can not be duplicated)
* ```pos```: position of image (other component not use it)
* ```ENABLE```: check it for using in game
----
### Sprite Tab
<img src= https://user-images.githubusercontent.com/47798805/217285162-b28aa226-51e4-4c63-8414-faafe41e1534.png width="200" height="150">

* ```crop_rect([int][int][int][int])```: Rect of cropping for image
* ```slice_rect([int][int][int][int])```: Rect for slicing image by index [x,y, # slice w,  # slice h]
  * If it is used with crop_rect, the cropping is applied first then slice_rect is used
* ```tran_rect([int][int])```: Change the size of image
----
### Text Tab
<img src= https://user-images.githubusercontent.com/47798805/217287712-60d7742d-d0ed-4e91-8014-cdc5936c1a00.png >

* ```text(str)```: The in game text
* ```font_sz(int)```: The size of font
* ```anti(bool)```: Anti aliasing for text
* ```color([int,int,int])```: R,G,B color in int
----
### Event Tab
<img src= https://user-images.githubusercontent.com/47798805/217288691-df9f1cac-4b46-4aae-951e-bbb8fb081f85.png>

* event_trigger: The code for calling function 
----
### Component Window
<img src = https://user-images.githubusercontent.com/47798805/217289277-dbbba1d0-84c7-48d7-97cf-5896ad5e5e3b.png>

* It is json format
* Must inclulde key, object, enable 

Here is example

> object.json
```json
{
"target event object name":{
       "object": "test_func2",
        "type": "event_obj",
        "layer": "0",
        "path": "..//test//test.py",
        "key": "function1",
        "pos": [
            0,
            0
        ],
        "crop_rect": null,
        "slice_rect": null,
        "tran_rect": null,
        "text": "",
        "font_sz": "15",
        "color": [
            0,
            0,
            0
        ],
        "anti": "0",
        "event_trigger": "ans = sum(a, b)",
        "enable": true
  }
}
```
> code.py
```py
def sum(a,b):
  return a + b
```
> component.json
```json
{
"key": "test",
"object": "target event object name",
"a": 1,
"b": 2,
"ans": 0,
"enalbe": true
}
```
----
