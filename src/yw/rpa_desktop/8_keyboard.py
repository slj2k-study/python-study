import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0] #메모장 하나 띄워서 가져옴
w.activate()


# pyautogui.write("1234")
# pyautogui.write("Nao", interval=0.3)
# #한글 안됨
#
# pyautogui.write(["t","e","s","t","left","enter"],interval=0.3)
#https://automatetheboringstuff.com/2e/chapter20/
#Table 20-1: PyKeyboard Attributes

#특수문자

# pyautogui.keyDown("shift")
# pyautogui.press("4")
# pyautogui.keyUp("shift")

#조합키
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

#간편한 조합키
# pyautogui.hotkey("ctrl","alt","shift","a")
# down ctrl -> alt -> shift -> a 후에 up a -> shift->alt->ctrl
#pyautogui.hotkey("ctrl","a")

import pyperclip
pyperclip.copy("나도 코딩") # 클립보드에 저장
pyautogui.hotkey("ctrl","a")
pyautogui.hotkey("ctrl","v")

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

# win : ctrl + alt + del 자동화 끝남
