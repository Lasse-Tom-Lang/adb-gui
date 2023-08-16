import PySimpleGUI as sg
import gui, adb, eventManager


def main():
    deviceConnected = False
    packageList = list()
    packageData = {}
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
            packageData = {}
            deviceConnected = False
        if event == "-UPDATEPACKAGELIST-" and device != "":
            mainWindow["-PACKAGELIST-"].update(adb.getPackages())
            eventManager.noPackageSelected(mainWindow)
            packageData = {}
        if event == "-REBOOT-" and device != "":
            rebootOutput = gui.rebootCheck()
            if rebootOutput == "OK":
                adb.reboot()
        if event == "-PACKAGELIST-" and len(values["-PACKAGELIST-"]) != 0:
            packageData = adb.getPackageData(values["-PACKAGELIST-"][0])
            mainWindow["-PACKAGENAME-"].update(values["-PACKAGELIST-"][0])
            mainWindow["-PACKAGELOCATION-"].update(f"Location: {packageData['location']}")
        if event == "-REMOVEPACKAGE-" and len(values["-PACKAGELIST-"]) != 0:
            output = eventManager.removePackage(values["-PACKAGELIST-"][0])
            if output:
              packageList = adb.getPackages()
              mainWindow["-PACKAGELIST-"].update(packageList)
              eventManager.noPackageSelected(mainWindow)
              packageData = {}
        if event == "-PACKAGESEARCH-":
            searchList = list()
            for package in packageList:
                if values["-PACKAGESEARCH-"] in package:
                    searchList.append(package)
            mainWindow["-PACKAGELIST-"].update(searchList)
            eventManager.noPackageSelected(mainWindow)
            packageData = {}
        if event == "-INSTALLPACKAGE-" and values["-UPLOADPACKAGELOCATION-"] != "" and device != "":
            eventManager.installPackage(values["-UPLOADPACKAGELOCATION-"])
        if event == "-DOWNLOADPACKAGE-" and packageData != {} and values["-DOWNLOADPACKAGE-"] != "":
            adb.downloadPackage(packageData["location"], values["-DOWNLOADPACKAGE-"])

    mainWindow.close()


if __name__ == "__main__":
    main()
