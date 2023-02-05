import os.path
from dataclasses import dataclass
from ctypes import cdll
import copy
import sys


@dataclass
class CEvent:
    path: str = None  # code path
    trigger: str = None  # type of event trigger


def set_event(
        event: CEvent,
        path: str,
        event_trigger: str
) -> None:
    """
    This function run warping lib file
    Args:
        path: the path of function
        event: The event data class
        event_trigger: The type of event
    """
    event.path = path
    event.trigger = event_trigger


def run_lib_event(event: CEvent) -> None:
    file_extension = os.path.splitext(event.path)[1]
    assert (file_extension == '.lib' or file_extension == '.so'), 'The given file extension is not a lib file!'
    lib = cdll.LoadLibrary(event.path)
    lib.python()


def run_python_event(event: CEvent, component: dict) -> None:
    code = open(event.path, mode='r').read()
    code += "\n" + event.trigger
    result = dict()
    input_component = copy.deepcopy(component)
    exec(code, input_component, result)
    for x in component.keys():
        try: component[x] = result[x]
        except LookupError: continue
