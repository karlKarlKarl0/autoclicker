from pynput import keyboard
from pynput.mouse import Button, Controller
import threading
import time

toggleKey = 'n'
clicking = False 
pressing = False
mouse = Controller()
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


def toggle_click(key):
    try:
        #print(f'Key {key.char} pressed')
        if key.char == toggleKey:  #checks if toggle key is pressed
            print("toggle key pressed")
            global clicking 
            clicking = not clicking
        
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



def main():
    print("hello") 
    #below is the event listener for toggle
    listener = keyboard.Listener(on_release=toggle_click)
    listener.start()
    
    clickingLoop()



if __name__ == "__main__":
    main()

