import pyautogui as pyautogui

def mousePosition():
    print("Current Mouse Position:", pyautogui.position())

if __name__ == '__main__':
    mousePosition()