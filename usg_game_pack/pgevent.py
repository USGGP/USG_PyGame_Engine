import os.path
from dataclasses import dataclass
from ctypes import cdll
import sys


@dataclass
class CEvent:
    path: str = None  # code path
    trigger: str = None  # type of event trigger
    val: str = None  # input variable name
    ans: str = None  # return(output) variable name
    recv: object = None  # exact return variable


def set_event(
        event: CEvent,
        path: str,
        event_trigger: str,
        event_val: str,
        event_ans: str
) -> None:
    """
    This function run warping lib file
    Args:
        event: The event data class
        event_trigger: The type of event
        event_val: The name of input value
        event_ans: The name of output value
        path: the path of *.pyx
    """
    event.path = path
    event.trigger = event_trigger
    event.val = event_val
    event.ans = event_ans


def run_lib_event(
        event: CEvent,
) -> None:
    file_extension = os.path.splitext(event.path)[1]
    assert (file_extension == '.lib' or file_extension == '.so'), 'The given file extension is not a lib file!'
    lib = cdll.LoadLibrary(event.path)
    lib.python(event.val)


def run_python_event(
        event: CEvent,
) -> None:
    ans = {}
    exec(open(event.path, mode='r').read(), {event.val: 100}, ans)
    event.recv = ans[event.ans]
