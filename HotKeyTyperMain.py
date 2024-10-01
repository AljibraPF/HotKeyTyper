import pyautogui
import keyboard

def type_text():
    pyautogui.write("Hello!")

keyboard.add_hotkey('q', type_text, suppress=True)  

keyboard.wait('esc')  
