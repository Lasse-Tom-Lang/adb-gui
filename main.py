import PySimpleGUI as sg
import gui, adb


def main():
    mainWindow = gui.mainWindow()
    while True:
        event, values = mainWindow.read(timeout=1000)
        if event == sg.WIN_CLOSED:
            break
        device = adb.getConnectedDevice()
        if device != "":
            mainWindow["-DEVICECONNECTED-"].update(f"Connected: {device}")
        else:
            mainWindow["-DEVICECONNECTED-"].update("No device connected")
            mainWindow["-PACKAGELIST-"].update([])
        if event == "-UPDATEPACKAGELIST-" and device != "":
            mainWindow["-PACKAGELIST-"].update(adb.getPackages())
        if event == "-REBOOT-" and device != "":
            rebootOutput = gui.rebootCheck()
            if rebootOutput == "OK":
              adb.reboot()
            
    mainWindow.close()


if __name__ == "__main__":
    main()