from pynput import mouse, keyboard
from time import time
import json
import os

OUTPUT_FILENAME = 'actions_test_01'
#declare mouse_listener gloabally so that keyboard on_release can stop it.
mouse_listener = None
#declare our start time globally so that our callback functions can reference it.
start_time = None
#keep track of unreleased keys to prevent over-reporting.
unreleased_keys = []
#storing all input events
input_events = []


class EventType():
    KEYDOWN = 'keyDown'
    KEYUP = 'keyUp'
    CLICK = 'click'

def main():
    runlisteners()
    print('Recording duration: {} seconds'.format(elapsed_time()))
    global input_events
    print(json.dumps(input_events))

    script_dir = os.path.dirname(__file__)
    filepath = os.path.join(
        script_dir, 
        'recordings', 
        '{}.json'.format(OUTPUT_FILENAME)
    )
    with open(filepath, 'w') as outfile:
        json.dump(input_events, outfile, indent=4)


def elapsed_time():
    global start_time
    return time() - start_time


def record_event(event_type, event_time, button, pos=None):
    global input_events
    input_events.append({
        'time': event_time,
        'type': event_type,
        'button': str(button), 
        'pos': pos
    })

    if event_type == EventType.CLICK:
        print('{} on {} pos {} at {}'.format(event_type, button, pos, event_time))
    else:
        print('{} on {} at {}'.format(event_type, button, event_time))




def on_press(key):
    #we only want to record the first keypress event until that key has been released.
    global unreleased_keys
    if key in unreleased_keys:
        return
    else:
        unreleased_keys.append(key)

    try:
        record_event(EventType.KEYDOWN, elapsed_time(), key.char)
        print('alphanumeric key {} pressed at {}'.format(key.char, elapsed_time()))
    except AttributeError:
        print(EventType.KEYDOWN, elapsed_time(), key)

def on_release(key):
    #mark key as no longer pressed.
    global unreleased_keys
    try: 
        unreleased_keys.remove(key)
    except ValueError:
        print('ERROR: {} not in unreleased_keys'.format(key))


    try:
        record_event(EventType.KEYUP, elapsed_time(), key.char)
        print('alphanumeric key {} pressed at {}'.format(key.char, elapsed_time()))
    except AttributeError:
        print(EventType.KEYUP, elapsed_time(), key)

    if key == keyboard.Key.esc:
        # Stop mouse listener
        global mouse_listener
        mouse_listener.stop()
        # Stop KB listener
        raise keyboard.Listener.StopException

def on_click(x, y, button, pressed):
    if not pressed:
        record_event(EventType.CLICK, elapsed_time(), button, (x, y))

def runlisteners():

    #collect mouse input events.
    global mouse_listener
    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()
    mouse_listener.wait() #wait for the listener to become ready.

    #collect keyboard inputs until released.
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        global start_time
        start_time = time()
        listener.join()
        


if __name__ == "__main__":
    main()