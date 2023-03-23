import win32gui

w=win32gui
w.GetWindowText(w.GetForegroundWindow())
# If the text is not the expected, close window or wait as 
# before