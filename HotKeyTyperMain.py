import pyautogui
import keyboard

def type_text():
    #Choose what to type
    pyautogui.write("Hello!")


#Choose HotKey        ↓
keyboard.add_hotkey('f1', type_text, suppress=True)  

keyboard.wait('esc')  
