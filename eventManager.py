"""
  Handels GUI events
"""


def updateDeviceInfo(mainWindow, device, deviceInfo, packageList):
    mainWindow["-DEVICECONNECTED-"].update(f"Connected: {device}")
    mainWindow["-BRAND-"].update(f"Brand: {deviceInfo['brand']}")
    mainWindow["-MANIFACTURER-"].update(f"Manufacturer: {deviceInfo['manufacturer']}")
    mainWindow["-SERIALNO-"].update(f"Serialno: {deviceInfo['serialno']}")
    mainWindow["-PACKAGELIST-"].update(packageList)


def removeDeviceInfo(mainWindow):
    mainWindow["-DEVICECONNECTED-"].update("No device connected")
    mainWindow["-PACKAGELIST-"].update([])
    mainWindow["-BRAND-"].update("Brand:")
    mainWindow["-MANIFACTURER-"].update("Manufacturer:")
    mainWindow["-SERIALNO-"].update("Serialno:")