"""
  Module for creating windows with PySimpleGUI
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
                sg.TabGroup(
                    [
                        [
                            sg.Tab(
                                "Device info",
                                [
                                    
                                    [
                                        sg.Text(
                                            "Brand:",
                                            text_color=textColor,
                                            background_color=backgroundColor,
                                            key="-BRAND-",
                                            font="Arial 12"
                                        )
                                    ],
                                    [
                                        sg.Text(
                                            "Manufacturer:",
                                            text_color=textColor,
                                            background_color=backgroundColor,
                                            key="-MANIFACTURER-",
                                            font="Arial 12"
                                        )
                                    ],
                                    [
                                        sg.Text(
                                            "Serialno:",
                                            text_color=textColor,
                                            background_color=backgroundColor,
                                            key="-SERIALNO-",
                                            font="Arial 12"
                                        )
                                    ],
                                    [
                                        sg.Frame(
                                            "Battery",
                                            [
                                                [
                                                    sg.Text(
                                                        "AC powered:",
                                                        text_color=textColor,
                                                        background_color=backgroundColor,
                                                        key="-ACPOWERED-",
                                                        font="Arial 12"
                                                    )
                                                ],
                                                [
                                                    sg.Text(
                                                        "USB powered:",
                                                        text_color=textColor,
                                                        background_color=backgroundColor,
                                                        key="-USBPOWERED-",
                                                        font="Arial 12"
                                                    )
                                                ],
                                                [
                                                    sg.Text(
                                                        "Wireless powered:",
                                                        text_color=textColor,
                                                        background_color=backgroundColor,
                                                        key="-WIRELESSPOWERED-",
                                                        font="Arial 12"
                                                    )
                                                ],
                                                [
                                                    sg.Text(
                                                        "Battery percent:",
                                                        text_color=textColor,
                                                        background_color=backgroundColor,
                                                        key="-BATTERYLEVEL-",
                                                        font="Arial 12"
                                                    )
                                                ],
                                                [
                                                    sg.Text(
                                                        "Temperature:",
                                                        text_color=textColor,
                                                        background_color=backgroundColor,
                                                        key="-BATTERYTEMPERATURE-",
                                                        font="Arial 12"
                                                    )
                                                ]
                                            ],
                                            textColor,
                                            backgroundColor,
                                            expand_x=True,
                                            font="Arial 14"
                                        )
                                    ],
                                    [
                                        sg.Button(
                                            "Reboot",
                                            key="-REBOOT-",
                                            expand_x=True,
                                            button_color=(textColor, highlightColor),
                                            border_width=0,
                                            font="Arial 12"
                                        )
                                    ]
                                ],
                                background_color=backgroundColor
                            )
                        ],
                        [
                            sg.Tab(
                                "Package manager",
                                [
                                    [
                                        sg.Column(
                                            [
                                                [
                                                    sg.Button(
                                                        "Update package list",
                                                        key="-UPDATEPACKAGELIST-",
                                                        expand_x=True,
                                                        button_color=(textColor, highlightColor),
                                                        border_width=0,
                                                        font="Arial 12"
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
                                                        sbar_background_color=highlightColor,
                                                        font="Arial 14",
                                                        change_submits=True
                                                    )
                                                ]
                                            ],
                                            backgroundColor,
                                            expand_x=True,
                                            expand_y=True
                                        ),
                                        sg.VerticalSeparator(
                                            textColor
                                        ),
                                        sg.Column(
                                            [
                                                [
                                                    sg.Text(
                                                        "No package selected",
                                                        (100, 1),
                                                        font="Arial 14",
                                                        background_color=backgroundColor,
                                                        text_color=textColor,
                                                        key="-PACKAGENAME-",
                                                    )
                                                ]
                                            ],
                                            backgroundColor,
                                            expand_x=True,
                                            expand_y=True
                                        )
                                    ]
                                ],
                                background_color=backgroundColor
                            )
                        ]
                    ],
                    expand_x=True,
                    expand_y=True,
                    background_color=backgroundColor,
                    title_color=textColor,
                    tab_background_color=highlightColor,
                    font="Arial 14",
                    selected_background_color=highlightColor
                )
            ]
        ],
        background_color=backgroundColor,
        resizable=True,
        size=(700, 500),
        alpha_channel=1
    )


def rebootCheck():
    return sg.PopupOKCancel(
        "Do you want to reboot the connected device?",
        title="Reboot device",
        background_color=backgroundColor,
        button_color=(textColor, highlightColor),
        font="Arial 12"
    )