import pyautogui
import keyboard
import pyperclip  

# Will paste '[🐍]': "" and insert the cursor between "" for easy access
# Why did i make this? I Like to be fancy in roleplaying So i can instantly press one single key and it'll print it all out
# example of use: '[🐍]': "Testing", '[🐍]': "My Name Is Slythery."
def type_text():
    pyperclip.copy("'[🐍]': \"\"") #To Write
    pyautogui.hotkey('ctrl', 'v')   
    pyautogui.press('left')  


#Choose HotKey        ↓
keyboard.add_hotkey('f1', type_text, suppress=True)  

keyboard.wait('esc')  
