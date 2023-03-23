import pyautogui

all_windows = pyautogui.getAllWindows()
for window in all_windows:
    print(window.title)
    # if title is the popup one, close the window
    #(window.close()), clicking on some element or waiting for
    # it to be gone