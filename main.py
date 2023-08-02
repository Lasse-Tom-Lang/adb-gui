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
            eventManager.updateDeviceInfo(mainWindow, device, deviceInfo, packageList)
            deviceConnected = True
        elif device == "":
            eventManager.removeDeviceInfo()
            deviceConnected = False
        if event == "-UPDATEPACKAGELIST-" and device != "":
            mainWindow["-PACKAGELIST-"].update(adb.getPackages())
        if event == "-REBOOT-" and device != "":
            rebootOutput = gui.rebootCheck()
            if rebootOutput == "OK":
              adb.reboot()
            
    mainWindow.close()


if __name__ == "__main__":
    main()