import PySimpleGUI as sg
import gui, adb, eventManager


def main():
    deviceConnected = False
    mainWindow = gui.mainWindow()
    while True:
        event, values = mainWindow.read(timeout=2000)
        if event == sg.WIN_CLOSED:
            break
        device = adb.getConnectedDevice()
        if device != "" and not deviceConnected:
            deviceInfo = adb.getDeviceInfo()
            packageList = adb.getPackages()
            batteryData = adb.getBatteryInformation()
            eventManager.updateDeviceInfo(mainWindow, device, deviceInfo, packageList, batteryData)
            deviceConnected = True
        elif device == "":
            eventManager.removeDeviceInfo(mainWindow)
            deviceConnected = False
        if event == "-UPDATEPACKAGELIST-" and device != "":
            mainWindow["-PACKAGELIST-"].update(adb.getPackages())
        if event == "-REBOOT-" and device != "":
            rebootOutput = gui.rebootCheck()
            if rebootOutput == "OK":
                adb.reboot()
        if event == "-PACKAGELIST-" and len(values["-PACKAGELIST-"]) != 0:
            mainWindow["-PACKAGENAME-"].update(values["-PACKAGELIST-"][0])
        if event == "-REMOVEPACKAGE-" and len(values["-PACKAGELIST-"]) != 0:
            removeOutput = gui.removePackageCheck(values["-PACKAGELIST-"][0])
            if removeOutput == "OK":
                removeOutput = adb.removePackage(values["-PACKAGELIST-"][0])
                if removeOutput == "Success":
                    gui.packageRemoved(values["-PACKAGELIST-"][0])
                else:
                    removeOutput = gui.removePackageUserZero(values["-PACKAGELIST-"][0])
                    if removeOutput == "OK":
                      removeOutput = adb.removePackage(values["-PACKAGELIST-"][0], "0")
                      if removeOutput == "Success":
                          gui.packageRemoved(values["-PACKAGELIST-"][0])
                      else:
                          gui.packageRemoveFailed(values["-PACKAGELIST-"][0])
                packageList = adb.getPackages()
                mainWindow["-PACKAGELIST-"].update(packageList)
                mainWindow["-PACKAGENAME-"].update("No package selected")

    mainWindow.close()


if __name__ == "__main__":
    main()
