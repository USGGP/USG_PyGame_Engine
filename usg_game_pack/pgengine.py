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


def create_obj_window(obj_list: dict, obj_feature: dict = None) -> None:
    ############################
    #       Data format        #
    ############################
    if obj_feature is None:
        obj_feature = {}
    try:
        obj_feature[CompList.OBJECT]
    except LookupError:
        obj_feature[CompList.OBJECT] = None
    try:
        obj_feature[COMMON_FEATURE.PATH]
    except LookupError:
        obj_feature[COMMON_FEATURE.PATH] = os.getcwd()
    try:
        obj_feature[CompList.TYPE]
    except LookupError:
        obj_feature[CompList.TYPE] = CompList.SPRITE
    try:
        obj_feature[COMMON_FEATURE.LAYER]
    except LookupError:
        obj_feature[COMMON_FEATURE.LAYER] = 0
    try:
        obj_feature[COMMON_FEATURE.KEY]
    except LookupError:
        obj_feature[COMMON_FEATURE.KEY] = None
    try:
        obj_feature[COMMON_FEATURE.POS]
    except LookupError:
        obj_feature[COMMON_FEATURE.POS] = [0, 0]
    try:
        obj_feature[SPRITE_FEATURE.TRAN_RECT]
    except LookupError:
        obj_feature[SPRITE_FEATURE.TRAN_RECT] = [None, None]
    try:
        obj_feature[SPRITE_FEATURE.CROP_RECT]
    except LookupError:
        obj_feature[SPRITE_FEATURE.CROP_RECT] = [None, None, None, None]
    try:
        obj_feature[SPRITE_FEATURE.SLICE_RECT]
    except LookupError:
        obj_feature[SPRITE_FEATURE.SLICE_RECT] = [None, None, None, None]
    try:
        obj_feature[TEXT_FEATURE.TEXT]
    except LookupError:
        obj_feature[TEXT_FEATURE.TEXT] = None
    try:
        obj_feature[TEXT_FEATURE.FONT_SZ]
    except LookupError:
        obj_feature[TEXT_FEATURE.FONT_SZ] = 15
    try:
        obj_feature[TEXT_FEATURE.COLOR]
    except LookupError:
        obj_feature[TEXT_FEATURE.COLOR] = [0, 0, 0]
    try:
        obj_feature[TEXT_FEATURE.ANTI]
    except LookupError:
        obj_feature[TEXT_FEATURE.ANTI] = False
    try:
        obj_feature[EVENT_FEATURE.EVENT_TRIGGER]
    except LookupError:
        obj_feature[EVENT_FEATURE.EVENT_TRIGGER] = 'main'
    try:
        obj_feature[COMMON_FEATURE.ENABLE]
    except LookupError:
        obj_feature[COMMON_FEATURE.ENABLE] = True
    # set list of feature
    obj_feature[SPRITE_FEATURE.CROP_RECT] = [None, None, None, None] \
        if obj_feature[SPRITE_FEATURE.CROP_RECT] is None else obj_feature[SPRITE_FEATURE.CROP_RECT]
    obj_feature[SPRITE_FEATURE.SLICE_RECT] = [None, None, None, None] \
        if obj_feature[SPRITE_FEATURE.SLICE_RECT] is None else obj_feature[SPRITE_FEATURE.SLICE_RECT]
    obj_feature[SPRITE_FEATURE.TRAN_RECT] = [None, None, None, None] \
        if obj_feature[SPRITE_FEATURE.TRAN_RECT] is None else obj_feature[SPRITE_FEATURE.TRAN_RECT]
    #####################################
    #       Sprite layout format        #
    #####################################
    sprite_layout = \
        [[sg.Text(SPRITE_FEATURE.CROP_RECT, size=(10, 1)),
          sg.InputText(obj_feature[SPRITE_FEATURE.CROP_RECT][0], key=SPRITE_FEATURE.CROP_RECT + 'x', size=(4, 1)),
          sg.InputText(obj_feature[SPRITE_FEATURE.CROP_RECT][1], key=SPRITE_FEATURE.CROP_RECT + 'y', size=(4, 1)),
          sg.InputText(obj_feature[SPRITE_FEATURE.CROP_RECT][2], key=SPRITE_FEATURE.CROP_RECT + 'w', size=(4, 1)),
          sg.InputText(obj_feature[SPRITE_FEATURE.CROP_RECT][3], key=SPRITE_FEATURE.CROP_RECT + 'h', size=(4, 1))],
         [sg.Text(SPRITE_FEATURE.SLICE_RECT, size=(10, 1)),
          sg.InputText(obj_feature[SPRITE_FEATURE.SLICE_RECT][0], key=SPRITE_FEATURE.SLICE_RECT + 'x', size=(4, 1)),
          sg.InputText(obj_feature[SPRITE_FEATURE.SLICE_RECT][1], key=SPRITE_FEATURE.SLICE_RECT + 'y', size=(4, 1)),
          sg.InputText(obj_feature[SPRITE_FEATURE.SLICE_RECT][2], key=SPRITE_FEATURE.SLICE_RECT + 'w', size=(4, 1)),
          sg.InputText(obj_feature[SPRITE_FEATURE.SLICE_RECT][3], key=SPRITE_FEATURE.SLICE_RECT + 'h', size=(4, 1))],
         [sg.Text(SPRITE_FEATURE.TRAN_RECT, size=(10, 1)),
          sg.InputText(obj_feature[SPRITE_FEATURE.TRAN_RECT][0], key=SPRITE_FEATURE.TRAN_RECT + 'w', size=(4, 1)),
          sg.InputText(obj_feature[SPRITE_FEATURE.TRAN_RECT][1], key=SPRITE_FEATURE.TRAN_RECT + 'h', size=(4, 1))]]
    ###################################
    #       Text layout format        #
    ###################################
    text_layout = \
        [[sg.Text(TEXT_FEATURE.TEXT, size=(10, 1)),
          sg.InputText(obj_feature[TEXT_FEATURE.TEXT], key=TEXT_FEATURE.TEXT, size=(20, 1))],
         [sg.Text(TEXT_FEATURE.FONT_SZ, size=(10, 1)),
          sg.InputText(obj_feature[TEXT_FEATURE.FONT_SZ], key=TEXT_FEATURE.FONT_SZ, size=(20, 1))],
         [sg.Text(TEXT_FEATURE.ANTI, size=(10, 1)),
          sg.InputText(obj_feature[TEXT_FEATURE.ANTI], key=TEXT_FEATURE.ANTI, size=(20, 1))],
         [sg.Text(TEXT_FEATURE.COLOR, size=(10, 1)),
          sg.InputText(obj_feature[TEXT_FEATURE.COLOR][0], key=TEXT_FEATURE.COLOR + 'r', size=(5, 1)),
          sg.InputText(obj_feature[TEXT_FEATURE.COLOR][1], key=TEXT_FEATURE.COLOR + 'g', size=(5, 1)),
          sg.InputText(obj_feature[TEXT_FEATURE.COLOR][2], key=TEXT_FEATURE.COLOR + 'b', size=(5, 1))]]
    ###################################
    #       event layout format       #
    ###################################
    event_layout = \
        [[sg.Text(EVENT_FEATURE.EVENT_TRIGGER, size=(10, 1)),
          sg.InputText(obj_feature[EVENT_FEATURE.EVENT_TRIGGER], key=EVENT_FEATURE.EVENT_TRIGGER, size=(20, 1))],
         ]
    # TAB layout
    tab_layout = [sg.Tab('Sprite', sprite_layout, key=CompList.SPRITE),
                  sg.Tab('Text', text_layout, key=CompList.TEXT),
                  sg.Tab('Func', event_layout, key=CompList.EVENT)]
    ###################################
    #       main layout format        #
    ###################################
    layout = [
        [sg.InputText(obj_feature[COMMON_FEATURE.PATH], key='-USER FOLDER-', size=(21, 1), readonly=True),
         sg.FileBrowse(initial_folder=obj_feature[COMMON_FEATURE.PATH], target='-USER FOLDER-',
                       file_types=[("png files", "*.png")], size=(9, 1))],
        [sg.Text('OBJECT NAME', size=(10, 1)),
         sg.InputText(obj_feature[CompList.OBJECT], key=CompList.OBJECT, size=(20, 1))],
        [sg.Text('COMP TYPE', size=(10, 1)),
         sg.InputText(CompList.SPRITE, readonly=True, key=CompList.TYPE, size=(20, 1))],
        [sg.Text(COMMON_FEATURE.LAYER, size=(5, 1)),
         sg.InputText(obj_feature[COMMON_FEATURE.LAYER], key=COMMON_FEATURE.LAYER, size=(9, 1)),
         sg.Text(COMMON_FEATURE.KEY, size=(3, 1)),
         sg.InputText(obj_feature[COMMON_FEATURE.KEY], key=COMMON_FEATURE.KEY, size=(9, 1))],
        [sg.Text(COMMON_FEATURE.POS, size=(5, 1)),
         sg.InputText(obj_feature[COMMON_FEATURE.POS][0], key=COMMON_FEATURE.POS + 'x', size=(10, 1)),
         sg.InputText(obj_feature[COMMON_FEATURE.POS][1], key=COMMON_FEATURE.POS + 'y', size=(10, 1))],
        [sg.Text('ENABLE', size=(6, 1)),
         sg.Button('ON', key=COMMON_FEATURE.ENABLE, size=(20, 1))],
        [sg.TabGroup([tab_layout], enable_events=True, key='-Tab-')],
        [sg.Multiline(size=(40, 18), key='textbox', auto_refresh=True)],
        [sg.Button("Save")]
    ]
    window = sg.Window("sprite window", layout, modal=True).Finalize()
    # Tab Selection
    if obj_feature[CompList.TYPE] == CompList.TEXT:
        window[CompList.TEXT].select()
    elif obj_feature[CompList.TYPE] == CompList.EVENT:
        window[CompList.EVENT].select()
    else:
        window[CompList.SPRITE].select()

    window[COMMON_FEATURE.ENABLE].Update(('Disable', 'Enable')[obj_feature[COMMON_FEATURE.ENABLE]],
                                         button_color=(
                                             ('black', ('red', 'green')[obj_feature[COMMON_FEATURE.ENABLE]])))
    # loop
    while True:
        event, values = window.read(timeout=500)
        ###############################
        #   Update format displayer   #
        ###############################
        # Toggle button selection
        try:
            pos_rect = [values[COMMON_FEATURE.POS + 'x'],
                        values[COMMON_FEATURE.POS + 'y']]
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
            rgb_rect = [values[TEXT_FEATURE.COLOR + 'r'],
                        values[TEXT_FEATURE.COLOR + 'g'],
                        values[TEXT_FEATURE.COLOR + 'b']]
        except:
            pass
        if values is not None:
            text_format = "\n".join([
                values[CompList.OBJECT]
                , ":{"
                , '\t\"' + CompList.OBJECT + "\":" + values[CompList.OBJECT] + ","
                , '\t\"' + CompList.TYPE + "\":" + values[CompList.TYPE] + ","
                , '\t\"' + COMMON_FEATURE.LAYER + "\":" + values[COMMON_FEATURE.LAYER] + ","
                , '\t\"' + COMMON_FEATURE.PATH + "\":" + values['-USER FOLDER-'] + ","
                , '\t\"' + COMMON_FEATURE.KEY + "\":" + values[COMMON_FEATURE.KEY] + ","
                , '\t\"' + COMMON_FEATURE.POS + "\":" + '[' + ','.join(pos_rect) + ']' + ","
                , '\t\"' + SPRITE_FEATURE.CROP_RECT + "\":" + '[' + ','.join(crop_rect) + ']' + ","
                , '\t\"' + SPRITE_FEATURE.SLICE_RECT + "\":" + '[' + ','.join(slice_rect) + ']' + ","
                , '\t\"' + SPRITE_FEATURE.TRAN_RECT + "\":" + '[' + ','.join(trans_rect) + ']' + ","
                , '\t\"' + TEXT_FEATURE.TEXT + "\":" + values[TEXT_FEATURE.TEXT] + ","
                , '\t\"' + TEXT_FEATURE.FONT_SZ + "\":" + values[TEXT_FEATURE.FONT_SZ] + ","
                , '\t\"' + TEXT_FEATURE.COLOR + "\":" + '[' + ','.join(rgb_rect) + ']' + ","
                , '\t\"' + TEXT_FEATURE.ANTI + "\":" + values[TEXT_FEATURE.ANTI] + ","
                , '\t\"' + EVENT_FEATURE.EVENT_TRIGGER + "\":" + values[EVENT_FEATURE.EVENT_TRIGGER] + ","
                , '\t\"' + COMMON_FEATURE.ENABLE + "\":" + ('true' if obj_feature[COMMON_FEATURE.ENABLE] else 'false')
                , "}"])
            window['textbox'].Update(value=text_format)

        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == COMMON_FEATURE.ENABLE:
            obj_feature[COMMON_FEATURE.ENABLE] = not obj_feature[COMMON_FEATURE.ENABLE]
            window[COMMON_FEATURE.ENABLE] \
                .Update(('Disable', 'Enable')[obj_feature[COMMON_FEATURE.ENABLE]],
                        button_color=(('black', ('red', 'green')[obj_feature[COMMON_FEATURE.ENABLE]])))
        elif event == '-Tab-':
            window[CompList.TYPE].update(values['-Tab-'])
        ############################
        #   Save feature in dict   #
        ############################
        elif event == "Save":
            print(values)
            # set common feature
            feature = {CompList.OBJECT: values[CompList.OBJECT],
                       CompList.TYPE: values[CompList.TYPE],
                       COMMON_FEATURE.LAYER: values[COMMON_FEATURE.LAYER],
                       COMMON_FEATURE.PATH: values['-USER FOLDER-'],
                       COMMON_FEATURE.KEY: values[COMMON_FEATURE.KEY],
                       COMMON_FEATURE.POS: list(map(int, pos_rect)),
                       SPRITE_FEATURE.CROP_RECT: list(map(int, crop_rect)),
                       SPRITE_FEATURE.SLICE_RECT: list(map(int, slice_rect)),
                       SPRITE_FEATURE.TRAN_RECT: list(map(int, trans_rect)),
                       TEXT_FEATURE.TEXT: values[TEXT_FEATURE.TEXT],
                       TEXT_FEATURE.FONT_SZ: values[TEXT_FEATURE.FONT_SZ],
                       TEXT_FEATURE.COLOR: list(map(int, rgb_rect)),
                       TEXT_FEATURE.ANTI: bool(values[TEXT_FEATURE.ANTI]),
                       EVENT_FEATURE.EVENT_TRIGGER: values[EVENT_FEATURE.EVENT_TRIGGER],
                       COMMON_FEATURE.ENABLE: obj_feature[COMMON_FEATURE.ENABLE]}
            obj_list[values[CompList.OBJECT]] = feature
            print('save object', values[CompList.TYPE])
    window.close()


def create_comp_window(comp_list: dict, comp_feature: dict = None) -> None:
    ############################
    #       Data format        #
    ############################
    if comp_feature is None:
        comp_feature = {}
    try:
        comp_feature[COMMON_FEATURE.KEY]
    except LookupError:
        comp_feature[COMMON_FEATURE.KEY] = None
    try:
        comp_feature[CompList.OBJECT]
    except LookupError:
        comp_feature[CompList.OBJECT] = None
    try:
        comp_feature[COMMON_FEATURE.ENABLE]
    except LookupError:
        comp_feature[COMMON_FEATURE.ENABLE] = True
    layout = [[sg.Multiline(size=(40, 5), key='textbox', auto_refresh=True)],
              [sg.Button("Save")]]
    window = sg.Window("sprite window", layout, modal=True).Finalize()
    window['textbox'].Update(value=comp_feature)
    # loop
    while True:
        event, values = window.read(timeout=500)
        ###############################
        #   Update format displayer   #
        ###############################
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        ############################
        #   Save feature in dict   #
        ############################
        elif event == "Save":
            try:
                comp_feature = json.loads(values['textbox'].replace("\'", "\"").replace("None", "null").replace("True",'true').replace("False","false"))
                comp_list[comp_feature[COMMON_FEATURE.KEY]] = comp_feature
                print('save component', comp_feature)
            except:
                print('save error', comp_feature)
    window.close()


class EngineWindow:
    def __init__(self):
        ##################
        #   Set layout   #
        ##################
        sg.theme("Default1")
        command = ['Create', 'Remove']
        obj_list_box = sg.Listbox(enable_events=True, size=(20, 20), values=[],
                                  key="-obj_List_Box-", right_click_menu=['&Right', command])

        comp_list_box = sg.Listbox(enable_events=True, size=(20, 20), values=[],
                                   key="-comp_List_Box-", right_click_menu=['&Right', command])

        list_tab_layer = [sg.Tab("Object", [[obj_list_box]]), sg.Tab("Component", [[comp_list_box]])]

        create_btn = sg.Button("Object Create", size=(10, 2))
        remove_btn = sg.Button("Object Remove", size=(10, 2))
        edited_btn = sg.Button("Object Edit", size=(10, 2))
        object_btn_layer = sg.Frame("Object option", [[create_btn], [remove_btn], [edited_btn]])

        comp_create_btn = sg.Button("Component Create", size=(10, 2))
        comp_remove_btn = sg.Button("Component Remove", size=(10, 2))
        comp_edited_btn = sg.Button("Component Edit", size=(10, 2))
        comp_btn_layer = sg.Frame("Component option", [[comp_create_btn], [comp_remove_btn], [comp_edited_btn]])

        btn_layer = [[object_btn_layer, comp_btn_layer]]

        graphic_layer = sg.Graph(key='-Canvas-',
                                 canvas_size=(400, 400),
                                 graph_bottom_left=(0, 0),
                                 graph_top_right=(400, 400),
                                 background_color='gray')
        path_file = sg.InputText(os.path.join(os.getcwd(), "../test/temp.json"), key="-FILE PATH-", size=(20, 1))
        file_io_layer = [sg.Text("Path"), path_file, sg.FileBrowse("Find"), sg.Button("Save"), sg.Button("Load")]
        self.obj_list: dict = {}
        self.comp_list: dict = {}
        self.window = None
        self.values = None
        self.event = None
        self.select_obj = None
        self.select_comp = None
        self.layout = \
            [[graphic_layer, sg.TabGroup([list_tab_layer], enable_events=True)],
             [file_io_layer],
             [sg.Column(btn_layer)]]

    def _comp_listbox_event(self):
        if self.event == '-comp_List_Box-':
            try:
                self.select_comp = self.values['-comp_List_Box-'][0]
                print('comp selection: ', self.comp_list[self.select_comp])
            except LookupError:
                self.select_comp = None
        elif self.event == 'Component Create':
            print('open create component window')
            create_comp_window(self.comp_list, None)
            self._comp_list_update()
        elif self.event == 'Component Remove' and self.select_comp is not None:
            print('remove: ', self.comp_list[self.select_comp])
            del self.comp_list[self.select_comp]
            self._comp_list_update()
            self.select_comp = None
        elif self.event == 'Component Edit' and self.select_comp is not None:
            print('edit: ', self.comp_list[self.select_comp])
            create_comp_window(self.comp_list, self.comp_list[self.select_comp])
            self._comp_list_update()

    def _obj_listbox_event(self):
        if self.event == '-obj_List_Box-':
            try:
                self.select_obj = self.values['-obj_List_Box-'][0]
                print('object selection: ', self.obj_list[self.select_obj])
            except LookupError:
                self.select_obj = None
        elif self.event == 'Object Create':
            print('open create object window')
            create_obj_window(self.obj_list, None)
            self._object_list_update()
        elif self.event == 'Object Remove' and self.select_obj is not None:
            print('remove: ', self.obj_list[self.select_obj])
            del self.obj_list[self.select_obj]
            self._object_list_update()
            self.select_obj = None
        elif self.event == 'Object Edit' and self.select_obj is not None:
            print('edit: ', self.obj_list[self.select_obj])
            create_obj_window(self.obj_list, self.obj_list[self.select_obj])
            self._object_list_update()

    def draw(self):
        self.window['-Canvas-'].erase()
        for obj in self.obj_list.values():
            if obj[CompList.TYPE] == CompList.SPRITE:
                self.window['-Canvas-'].DrawImage(filename=obj[COMMON_FEATURE.PATH], location=obj[COMMON_FEATURE.POS])

    def _object_list_update(self):
        print('object update:', self.obj_list)
        self.window["-obj_List_Box-"].update(self.obj_list)

    def _comp_list_update(self):
        print('comp update:', self.comp_list)
        self.window["-comp_List_Box-"].update(self.comp_list)

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
                self._obj_listbox_event()
                self._comp_listbox_event()
            self.draw()
        self.window.close()


def main():
    usg_engine = EngineWindow()
    usg_engine.start()


if __name__ == "__main__":
    main()
