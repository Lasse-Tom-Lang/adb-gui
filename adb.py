"""
  Module for communicating with adb
"""


import subprocess

def getConnectedDevice():
    return subprocess.getoutput("adb devices").split("\n")[1]


def getPackages():
    packages = subprocess.getoutput("adb shell pm list packages").replace("\n", "").split("package:")
    packages.pop(0)
    return packages


def reboot():
    subprocess.getoutput("adb shell reboot")


def getDeviceInfo():
    brand = subprocess.getoutput("adb shell getprop ro.product.brand")
    manufacturer = subprocess.getoutput("adb shell getprop ro.product.manufacturer")
    serialno = subprocess.getoutput("adb shell getprop ro.boot.serialno")
    return {"brand": brand, "manufacturer": manufacturer, "serialno": serialno}

def getBatteryInformation():
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


getBatteryInformation()