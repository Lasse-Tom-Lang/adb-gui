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