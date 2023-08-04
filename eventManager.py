"""
  Handels GUI events
"""


import PySimpleGUI as sg


def updateDeviceInfo(mainWindow: sg.Window, device: str, deviceInfo: dict, packageList: list[str], batteryData: dict) -> None:
    """
      Function for updating the device information displayed in the GUI.
    """
    mainWindow["-DEVICECONNECTED-"].update(f"Connected: {device}")
    mainWindow["-BRAND-"].update(f"Brand: {deviceInfo['brand']}")
    mainWindow["-MANIFACTURER-"].update(f"Manufacturer: {deviceInfo['manufacturer']}")
    mainWindow["-SERIALNO-"].update(f"Serialno: {deviceInfo['serialno']}")
    mainWindow["-PACKAGELIST-"].update(packageList)
    mainWindow["-ACPOWERED-"].update(f"AC powered: {batteryData['AC powered']}")
    mainWindow["-USBPOWERED-"].update(f"USB powered: {batteryData['USB powered']}")
    mainWindow["-WIRELESSPOWERED-"].update(f"Wireless powered: {batteryData['Wireless powered']}")
    mainWindow["-BATTERYLEVEL-"].update(f"Battery percent: {batteryData['level']}%")
    mainWindow["-BATTERYTEMPERATURE-"].update(f"Temperature: {batteryData['temperature']}K  / {round(int(batteryData['temperature']) - 273.15, 1)}°C")


def removeDeviceInfo(mainWindow: sg.Window) -> None:
    """
      Function for removing all device information displayed in the GUI.
    """
    mainWindow["-DEVICECONNECTED-"].update("No device connected")
    mainWindow["-PACKAGELIST-"].update([])
    mainWindow["-BRAND-"].update("Brand:")
    mainWindow["-MANIFACTURER-"].update("Manufacturer:")
    mainWindow["-SERIALNO-"].update("Serialno:")
    mainWindow["-ACPOWERED-"].update("AC powered:")
    mainWindow["-USBPOWERED-"].update("USB powered:")
    mainWindow["-WIRELESSPOWERED-"].update("Wireless powered:")
    mainWindow["-BATTERYLEVEL-"].update("Battery percent:")
    mainWindow["-BATTERYTEMPERATURE-"].update("Temperature:")
    mainWindow["-PACKAGENAME-"].update("No package selected")