import sys
import os

_sys_executable_path = os.path.dirname(sys.executable)
_sys_executable_path = os.path.normpath(_sys_executable_path)
_sys_executable_path = _sys_executable_path.split(os.sep)

if "/".join(_sys_executable_path[-3:]) != 'read_new_words_collector/venv/Scripts':
    raise Exception("read_new_words_collector/venv/Scripts venv has to be activated")

base_dir = os.sep.join(_sys_executable_path[:-2])
