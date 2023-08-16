"""
  Handels GUI events
"""


import PySimpleGUI as sg
import gui
import adb


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
    noPackageSelected(mainWindow)


def noPackageSelected(mainWindow: sg.Window):
    mainWindow["-PACKAGENAME-"].update("No package selected")
    mainWindow["-PACKAGELOCATION-"].update("No package selected")


def installPackage(uploadPackageLocation: str):
    installOutput = gui.installPackage(uploadPackageLocation)
    if installOutput != "OK":
        return
    installOutput = adb.installPackage(uploadPackageLocation)
    if installOutput.split("\n")[-1] == "Success":
        gui.installPackageSuccess()
    else:
        gui.installPackageFailed()


def removePackage(packageToRemove: str):
    removeOutput = gui.removePackageCheck(packageToRemove)
    if removeOutput != "OK":
        return False
    removeOutput = adb.removePackage(packageToRemove)
    if removeOutput == "Success":
        gui.packageRemoved(packageToRemove)
        return True
    removeOutput = gui.removePackageUserZero(packageToRemove)
    if removeOutput == "OK":
      removeOutput = adb.removePackage(packageToRemove, "0")
      if removeOutput == "Success":
          gui.packageRemoved(packageToRemove)
      else:
          gui.packageRemoveFailed(packageToRemove)
    return True