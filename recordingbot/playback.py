import pyautogui
from time import sleep
import os
import json

def main():

    initializePyAutoGUI()
    countdowntimer()

    playActions("actions_test_01.json")


def initializePyAutoGUI():
    #initialized PyAutoGUI, failsafe by moving mouse to upper-left corner to terminate.
    pyautogui.FAILSAFE = True

def countdowntimer():
    #Countdown timer to allow switching to game window.
    print("Starting", end="")
    for i in range(0, 10):
        print(".", end="")
        sleep(1)
    print("Bot executing.")

def playActions(filename):
    script_dir = os.path.dirname(__file__)
    filepath = os.path.join(
        script_dir, 
        'recordings', 
        filename
    )
    with open(filepath, 'r') as jsonfile:
        #parse the json first
        data = json.load(jsonfile)
        
        #loop over each action
        for index, action in enumerate(data):
            #look for escape input to exit
            if action['button'] == 'Key.esc':
                break

            #perform the action
            if action['type'] == 'keyDown':
                pyautogui.keyDown(action['button'])
            elif action['type'] == 'keyUp':
                pyautogui.keyUp(action['button'])
            elif action['type'] == 'click':
                pyautogui.click(action['pos'][0], action['pos'][1], duration=0.25)

            #then sleep until next action should occur
            try:
                next_action = data[index + 1]
            except IndexError:
                break
            elapsed_time = next_action['time'] - action['time']
            
            if elapsed_time >= 0:
                sleep(elapsed_time)

            else:
                raise Exception('Unexpected action ordering.')

if __name__ == "__main__":
    main()