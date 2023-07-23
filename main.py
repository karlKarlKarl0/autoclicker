from pynput import keyboard
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller
from threading import Thread
import time

clickToggleKey = 'n'
pressToggleKey = 'm'
clicking = False 
pressing = False
pressingKey = 'a'
mouse = Controller()
kb = Controller()
click_time_int = .1 #time between clicks
press_time_int = .1
#maybe later implement a toggleHotKey

# def on_press(key):  this is on press
#     try:
#         print(f'Key {key.char} pressed')
#         return {key.char}
#     except AttributeError:
#         print(f'Special key {key} pressed')

def click_left():
    mouse.press(Button.left)
    mouse.release(Button.left)



def toggle_clickpress(key):
    try:
        #print(f'Key {key.char} pressed')
        if key.char == clickToggleKey:  #checks if toggle key is pressed
            print("click toggle key pressed")
            global clicking 
            clicking = not clicking
        elif key.char == pressToggleKey:

            global pressing
            pressing = not pressing
        
    except AttributeError:
        print(f'Special key {key} pressed')
    # if key == keyboard.Key.esc:
    #     # Stop the listener
    #     return False
    

def clickingLoop():
    while True:
        if clicking:
            click_left()
            time.sleep(click_time_int)

def pressingLoop():
    while True:
        if pressing:
            kb.press(pressingKey)
            time.sleep(press_time_int)



def main():
    print("hello") 
    #below is the event listener for toggle
    listener = keyboard.Listener(on_release=toggle_clickpress)
    listener.start()
    
    cThread = Thread(target = clickingLoop)
    pThread = Thread(target = pressingLoop)
    cThread.start()
    pThread.start()



if __name__ == "__main__":
    main()

