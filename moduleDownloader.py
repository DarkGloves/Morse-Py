# Made by DarkGloves
# This module gets an specified module from pypi in case it's not found
# You can find more information on https://github.com/DarkGloves/moduleDownloader-py
import os


def getmodules(*modules, pipver=int):
    for module in modules:
        try:
            if module == 'pillow':
                import PIL
            else:
                __import__(module)
        except ModuleNotFoundError:
            os.system(f'pip{pipver} install {module}')
