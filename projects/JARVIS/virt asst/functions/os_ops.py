import os
import subprocess as sp

paths = {
    'notepad': "C:\\Windows\\WinSxS\\amd64_microsoft-windows-notepad_31bf3856ad364e35_10.0.19041.1865_none_e39f984125619fa1\\Notepad.lnk",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}


def open_notepad():
    os.startfile(paths['notepad'])


def open_cmd():
    os.system('start cmd')


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    sp.Popen(paths['calculator'])
