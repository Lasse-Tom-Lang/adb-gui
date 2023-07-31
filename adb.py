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
