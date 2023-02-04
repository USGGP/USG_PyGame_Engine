import json

from usg_game_pack.pgrunner import SPRITE_FEATURE, EventList, COMMON_FEATURE
from usg_game_pack.pgrunner import TEXT_FEATURE
from usg_game_pack.pgrunner import EVENT_FEATURE
from usg_game_pack.pgrunner import CompList
import PySimpleGUI as sg
import os

"""
This is create the feature which is used for the pgmanager 
"""


def create_obj_window(obj_list: dict, pre_data: dict = None) -> None:
    ############################
    #       Data format        #
    ############################
    if pre_data is None:
        pre_data = {
            CompList.OBJECT: 'none',
            COMMON_FEATURE.PATH: os.getcwd(),
            CompList.TYPE: CompList.SPRITE,
            COMMON_FEATURE.LAYER: 0,
            COMMON_FEATURE.KEY: 'none key',
            COMMON_FEATURE.POS: [0, 0],
            SPRITE_FEATURE.CROP_RECT: [None, None, None, None],
            SPRITE_FEATURE.SLICE_RECT: [None, None, None, None],
            SPRITE_FEATURE.TRAN_RECT: [None, None],
            TEXT_FEATURE.TEXT: None,
            TEXT_FEATURE.FONT_SZ: 15,
            TEXT_FEATURE.COLOR: [0, 0, 0],
            TEXT_FEATURE.ANTI: False,
            EVENT_FEATURE.EVENT_TRIGGER: None,
            EVENT_FEATURE.EVENT_VAL: 'x',
            EVENT_FEATURE.EVENT_ANS: 'ans'
        }
    # set list of feature
    pre_data[SPRITE_FEATURE.CROP_RECT] = [None, None, None, None] \
        if pre_data[SPRITE_FEATURE.CROP_RECT] is None else pre_data[SPRITE_FEATURE.CROP_RECT]
    pre_data[SPRITE_FEATURE.SLICE_RECT] = [None, None, None, None] \
        if pre_data[SPRITE_FEATURE.SLICE_RECT] is None else pre_data[SPRITE_FEATURE.SLICE_RECT]
    pre_data[SPRITE_FEATURE.TRAN_RECT] = [None, None, None, None] \
        if pre_data[SPRITE_FEATURE.TRAN_RECT] is None else pre_data[SPRITE_FEATURE.TRAN_RECT]
    #####################################
    #       Sprite layout format        #
    #####################################
    sprite_layout = \
        [[sg.Text(SPRITE_FEATURE.CROP_RECT, size=(10, 1)),
          sg.InputText(pre_data[SPRITE_FEATURE.CROP_RECT][0], key=SPRITE_FEATURE.CROP_RECT + 'x', size=(4, 1)),
          sg.InputText(pre_data[SPRITE_FEATURE.CROP_RECT][1], key=SPRITE_FEATURE.CROP_RECT + 'y', size=(4, 1)),
          sg.InputText(pre_data[SPRITE_FEATURE.CROP_RECT][2], key=SPRITE_FEATURE.CROP_RECT + 'w', size=(4, 1)),
          sg.InputText(pre_data[SPRITE_FEATURE.CROP_RECT][3], key=SPRITE_FEATURE.CROP_RECT + 'h', size=(4, 1))],
         [sg.Text(SPRITE_FEATURE.SLICE_RECT, size=(10, 1)),
          sg.InputText(pre_data[SPRITE_FEATURE.SLICE_RECT][0], key=SPRITE_FEATURE.SLICE_RECT + 'x', size=(4, 1)),
          sg.InputText(pre_data[SPRITE_FEATURE.SLICE_RECT][1], key=SPRITE_FEATURE.SLICE_RECT + 'y', size=(4, 1)),
          sg.InputText(pre_data[SPRITE_FEATURE.SLICE_RECT][2], key=SPRITE_FEATURE.SLICE_RECT + 'w', size=(4, 1)),
          sg.InputText(pre_data[SPRITE_FEATURE.SLICE_RECT][3], key=SPRITE_FEATURE.SLICE_RECT + 'h', size=(4, 1))],
         [sg.Text(SPRITE_FEATURE.TRAN_RECT, size=(10, 1)),
          sg.InputText(pre_data[SPRITE_FEATURE.TRAN_RECT][0], key=SPRITE_FEATURE.TRAN_RECT + 'w', size=(4, 1)),
          sg.InputText(pre_data[SPRITE_FEATURE.TRAN_RECT][1], key=SPRITE_FEATURE.TRAN_RECT + 'h', size=(4, 1))]]
    ###################################
    #       Text layout format        #
    ###################################
    text_layout = \
        [[sg.Text(TEXT_FEATURE.TEXT, size=(10, 1)),
          sg.InputText(pre_data[TEXT_FEATURE.TEXT], key=TEXT_FEATURE.TEXT, size=(20, 1))],
         [sg.Text(TEXT_FEATURE.FONT_SZ, size=(10, 1)),
          sg.InputText(pre_data[TEXT_FEATURE.FONT_SZ], key=TEXT_FEATURE.FONT_SZ, size=(20, 1))],
         [sg.Text(TEXT_FEATURE.ANTI, size=(10, 1)),
          sg.InputText(pre_data[TEXT_FEATURE.ANTI], key=TEXT_FEATURE.ANTI, size=(20, 1))],
         [sg.Text(TEXT_FEATURE.COLOR, size=(10, 1)),
          sg.InputText(pre_data[TEXT_FEATURE.COLOR][0], key=TEXT_FEATURE.COLOR + 'r', size=(5, 1)),
          sg.InputText(pre_data[TEXT_FEATURE.COLOR][1], key=TEXT_FEATURE.COLOR + 'g', size=(5, 1)),
          sg.InputText(pre_data[TEXT_FEATURE.COLOR][2], key=TEXT_FEATURE.COLOR + 'b', size=(5, 1))]]
    ###################################
    #       event layout format       #
    ###################################
    event_layout = \
        [[sg.Text(EVENT_FEATURE.EVENT_TRIGGER, size=(10, 1)),
          sg.Combo([EventList.MOUSE_EVENT, EventList.KEY_UP_EVENT, EventList.DISPLAY_EVENT], readonly=True,
                   key=EVENT_FEATURE.EVENT_TRIGGER, size=(20, 1))],
         [sg.Text(EVENT_FEATURE.EVENT_VAL, size=(10, 1)),
          sg.InputText(pre_data[EVENT_FEATURE.EVENT_VAL], key=EVENT_FEATURE.EVENT_VAL, size=(20, 1))],
         [sg.Text(EVENT_FEATURE.EVENT_ANS, size=(10, 1)),
          sg.InputText(pre_data[EVENT_FEATURE.EVENT_ANS], key=EVENT_FEATURE.EVENT_ANS, size=(20, 1))]
         ]
    # TAB layout
    tab_layout = [sg.Tab('Sprite', sprite_layout, key=CompList.SPRITE),
                  sg.Tab('Text', text_layout, key=CompList.TEXT),
                  sg.Tab('Func', event_layout, key=CompList.EVENT)]
    ###################################
    #       main layout format        #
    ###################################
    layout = [
        [sg.InputText(pre_data[COMMON_FEATURE.PATH], key='-USER FOLDER-', size=(20, 1), readonly=True),
         sg.FileBrowse(initial_folder=pre_data[COMMON_FEATURE.PATH], target='-USER FOLDER-',
                       file_types=[("png files", "*.png")], size=(9, 1))],
        [sg.Text('OBJECT NAME', size=(12, 1)),
         sg.InputText(pre_data[CompList.OBJECT], key=CompList.OBJECT, size=(20, 1))],
        [sg.InputText(CompList.SPRITE, readonly=True, key=CompList.TYPE, size=(26, 1))],
        [sg.Text(COMMON_FEATURE.LAYER, size=(5, 1)),
         sg.InputText(pre_data[COMMON_FEATURE.LAYER], key=COMMON_FEATURE.LAYER, size=(9, 1)),
         sg.Text(COMMON_FEATURE.KEY, size=(5, 1)),
         sg.InputText(pre_data[COMMON_FEATURE.KEY], key=COMMON_FEATURE.KEY, size=(9, 1))],
        [sg.Text(COMMON_FEATURE.POS, size=(10, 1)),
         sg.InputText(pre_data[COMMON_FEATURE.POS][0], key=COMMON_FEATURE.POS + 'x', size=(4, 1)),
         sg.InputText(pre_data[COMMON_FEATURE.POS][1], key=COMMON_FEATURE.POS + 'y', size=(4, 1))],
        [sg.TabGroup([tab_layout], tab_location="right", enable_events=True, key='-Tab-')],
        [sg.Button("Save")]
    ]
    window = sg.Window("sprite window", layout, modal=True).Finalize()
    if pre_data[CompList.TYPE] == CompList.TEXT:
        window[CompList.TEXT].select()
    elif pre_data[CompList.TYPE] == CompList.EVENT:
        window[CompList.EVENT].select()
    else:
        window[CompList.SPRITE].select()
    while True:
        event, values = window.read(timeout=100)
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == '-Tab-':
            window[CompList.TYPE].update(values['-Tab-'])
        elif event == "Save":
            print(values)
            # set common feature
            feature = {
                CompList.OBJECT: values[CompList.OBJECT],
                CompList.TYPE: values[CompList.TYPE],
                COMMON_FEATURE.LAYER: values[COMMON_FEATURE.LAYER],
                COMMON_FEATURE.PATH: values['-USER FOLDER-'],
                COMMON_FEATURE.KEY: values[COMMON_FEATURE.KEY],
                COMMON_FEATURE.POS: None,
            }
            pos_rect = [values[COMMON_FEATURE.POS + 'x'],
                        values[COMMON_FEATURE.POS + 'y']]
            if all(bool(x.replace(" ", "")) for x in pos_rect):
                feature[COMMON_FEATURE.POS] = [int(x) for x in pos_rect]
            crop_rect = [values[SPRITE_FEATURE.CROP_RECT + 'x'],
                         values[SPRITE_FEATURE.CROP_RECT + 'y'],
                         values[SPRITE_FEATURE.CROP_RECT + 'w'],
                         values[SPRITE_FEATURE.CROP_RECT + 'h']]
            slice_rect = [values[SPRITE_FEATURE.SLICE_RECT + 'x'],
                          values[SPRITE_FEATURE.SLICE_RECT + 'y'],
                          values[SPRITE_FEATURE.SLICE_RECT + 'w'],
                          values[SPRITE_FEATURE.SLICE_RECT + 'h']]
            trans_rect = [values[SPRITE_FEATURE.TRAN_RECT + 'w'],
                          values[SPRITE_FEATURE.TRAN_RECT + 'h']]
            # get list of crop rect
            if all(bool(x.replace(" ", "")) for x in crop_rect):
                feature[SPRITE_FEATURE.CROP_RECT] = [int(x) for x in crop_rect]
            else:
                feature[SPRITE_FEATURE.CROP_RECT] = None
            # get list of slice rect
            if all(bool(x.replace(" ", "")) for x in slice_rect):
                feature[SPRITE_FEATURE.SLICE_RECT] = [int(x) for x in slice_rect]
            else:
                feature[SPRITE_FEATURE.SLICE_RECT] = None
            # get list of trans rect
            if all(bool(x.replace(" ", "")) for x in trans_rect):
                feature[SPRITE_FEATURE.TRAN_RECT] = [int(x) for x in trans_rect]
            else:
                feature[SPRITE_FEATURE.TRAN_RECT] = None
            feature[TEXT_FEATURE.TEXT] = values[TEXT_FEATURE.TEXT]
            feature[TEXT_FEATURE.FONT_SZ] = values[TEXT_FEATURE.FONT_SZ]
            feature[TEXT_FEATURE.COLOR] = [int(values[TEXT_FEATURE.COLOR + 'r']),
                                           int(values[TEXT_FEATURE.COLOR + 'g']),
                                           int(values[TEXT_FEATURE.COLOR + 'b'])]
            feature[TEXT_FEATURE.ANTI] = values[TEXT_FEATURE.ANTI]
            feature[EVENT_FEATURE.EVENT_TRIGGER] = values[EVENT_FEATURE.EVENT_TRIGGER]
            feature[EVENT_FEATURE.EVENT_VAL] = values[EVENT_FEATURE.EVENT_VAL]
            feature[EVENT_FEATURE.EVENT_ANS] = values[EVENT_FEATURE.EVENT_ANS]
            obj_list[values[CompList.OBJECT]] = feature
            print('save object', values[CompList.TYPE])
            break
    window.close()


class EngineWindow:
    def __init__(self):
        sg.theme("Default1")
        command = ['Create', 'Remove']
        list_box = sg.Listbox(enable_events=True, size=(20, 10), values=[],
                              key="-ListBox-", right_click_menu=['&Right', command])
        create_btn = sg.Button("Create", size=(10, 1))
        remove_btn = sg.Button("Remove", size=(10, 1))
        edited_btn = sg.Button("Edit", size=(10, 1))
        colum_layer = [[create_btn], [remove_btn], [edited_btn]]
        graphic_layer = sg.Graph(key='-Canvas-',
                                 canvas_size=(400, 400),
                                 graph_bottom_left=(0, 0),
                                 graph_top_right=(400, 400),
                                 background_color='gray')
        path_file = sg.InputText(os.path.join(os.getcwd(), "../test/temp.json"), key="-FILE PATH-", size=(20, 1))
        self.obj_list: dict = {}
        self.window = None
        self.values = None
        self.event = None
        self.select_obj = None
        self.layout = \
            [[graphic_layer,
              sg.Column([[list_box, sg.Column(colum_layer)],
                         [sg.Text("Path"), path_file, sg.Button("Save"), sg.Button("Load")]])]]

    def _listbox_event(self):
        if self.event == '-ListBox-':
            self.select_obj = self.values['-ListBox-'][0]
            print('selection: ', self.obj_list[self.select_obj])
        elif self.event == 'Create':
            print('open create feature window')
            create_obj_window(self.obj_list, None)
            self._object_list_update()
        elif self.event == 'Remove' and self.select_obj is not None:
            print('remove: ', self.obj_list[self.select_obj])
            del self.obj_list[self.select_obj]
            self._object_list_update()
            self.select_obj = None
        elif self.event == 'Edit' and self.select_obj is not None:
            print('edit: ', self.obj_list[self.select_obj])
            create_obj_window(self.obj_list, self.obj_list[self.select_obj])
            self._object_list_update()

    def draw(self):
        self.window['-Canvas-'].erase()
        for obj in self.obj_list.values():
            if obj[CompList.TYPE] == CompList.SPRITE:
                self.window['-Canvas-'].DrawImage(
                    filename=obj[COMMON_FEATURE.PATH], location=obj[COMMON_FEATURE.POS])

    def _object_list_update(self):
        print('object update:', self.obj_list)
        self.window["-ListBox-"].update(self.obj_list)

    def start(self):
        self.window = sg.Window('Simple Pygame Engine', self.layout, grab_anywhere=True)
        self.window.Finalize()
        while True:
            self.event, self.values = self.window.read()
            if self.event == "Exit" or self.event == sg.WIN_CLOSED:
                break
            elif self.event == 'Save':
                print('save json')
                with open(self.values["-FILE PATH-"], 'w') as json_file:
                    json.dump(self.obj_list, json_file, indent=4)
            elif self.event == 'Load':
                print('load json')
                with open(self.values["-FILE PATH-"], 'r') as json_file:
                    self.obj_list = json.load(json_file)
                    self._object_list_update()
            else:
                self._listbox_event()
            self.draw()
        self.window.close()


def main():
    usg_engine = EngineWindow()
    usg_engine.start()


if __name__ == "__main__":
    main()
