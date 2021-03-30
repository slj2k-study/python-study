import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0] #메모장 하나 띄워서 가져옴

w.activate()

