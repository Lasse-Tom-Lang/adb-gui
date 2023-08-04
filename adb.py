"""
  Module for communicating with Android Debugger Bridge (ADB)
"""


import subprocess

def getConnectedDevice() -> str:
    """
      Function that checks if a device is connected to adb.
      Returns emthy string when no device is found.
    """
    return subprocess.getoutput("adb devices").split("\n")[1]


def getPackages() -> list[str]:
    """
      Returns a list with all packages installed on the connected device.
    """
    packages = subprocess.getoutput("adb shell pm list packages").replace("\n", "").split("package:")
    packages.pop(0)
    return packages


def reboot() -> None:
    """
      Reboots the connected device.
    """
    subprocess.getoutput("adb shell reboot")


def getDeviceInfo() -> dict:
    brand = subprocess.getoutput("adb shell getprop ro.product.brand")
    manufacturer = subprocess.getoutput("adb shell getprop ro.product.manufacturer")
    serialno = subprocess.getoutput("adb shell getprop ro.boot.serialno")
    return {"brand": brand, "manufacturer": manufacturer, "serialno": serialno}

def getBatteryInformation() -> dict:
    rawData = subprocess.getoutput("adb shell dumpsys battery").split(":")
    dataList = list()
    for dataLine in rawData:
        split = dataLine.split("\n")
        dataList.append(split[0][1:])
        if len(split) == 2:     
            dataList.append(split[1][2:])
    dataList.pop(0)
    dataList.pop(0)
    dataDict = dict()
    i = 0
    while i < len(dataList):
        dataDict[dataList[i]] = dataList[i + 1]
        i += 2
    return dataDict