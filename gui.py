"""
  Module for creating windows
"""


import PySimpleGUI as sg


backgroundColor = "#303030"
highlightColor = "#404040"
textColor = "white"


def mainWindow() -> sg.Window:
    return sg.Window(
        "ADB",
        [
            [
                sg.Text(
                    "No device connected",
                    text_color=textColor,
                    background_color=backgroundColor,
                    key="-DEVICECONNECTED-",
                    font="Arial 16"
                )
            ],
            [
                sg.Button(
                    "Update package list",
                    key="-UPDATEPACKAGELIST-",
                    expand_x=True,
                    button_color=(textColor, backgroundColor)
                )
            ],
            [
                sg.Listbox(
                    [],
                    key="-PACKAGELIST-",
                    expand_x=True,
                    expand_y=True,
                    background_color=backgroundColor,
                    text_color=textColor,
                    sbar_trough_color=backgroundColor,
                    sbar_arrow_color=textColor,
                    sbar_background_color=highlightColor
                )
            ]
        ],
        background_color=backgroundColor,
        resizable=True
    )
