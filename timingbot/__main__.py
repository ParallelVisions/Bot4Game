import pyautogui
import time


DELAYBTWNCOMMANDS = 1.00

def main():

    initializePyAutoGUI()
    countdowntimer()

    #clickingstarchart
    openStarChart1()


    reportMousePos()

def initializePyAutoGUI():
    #initialized PyAutoGUI
    pyautogui.FAILSAFE = True


def countdowntimer():
    #Countdown timer to allow switching to game window.
    print("Starting", end="")
    for i in range(0, 10):
        print(".", end="")
        time.sleep(1)
    print("Bot executing.")


def reportMousePos(seconds=10):
    for i in range(0, seconds):
        print(pyautogui.position())
        time.sleep(1)

def openStarChart1():
    pyautogui.moveTo(128, 110, 0.5)
    time.sleep(DELAYBTWNCOMMANDS)
    pyautogui.click()

    #wait for star chart to open.
    time.sleep(2.0)
    #instead of calling pyautogui again we can just input the coords.
    #code below sets Edani as destination, preparing us for autopilot.
    pyautogui.click(449, 291, duration=0.25)
    time.sleep(1.0)
    pyautogui.click(819, 512, duration=0.25)
    time.sleep(1.0)
    pyautogui.click(524, 165, duration=0.25)
    time.sleep(1.0)
    pyautogui.click(794, 454, duration=0.25)
    





if __name__ == "__main__":
    main()