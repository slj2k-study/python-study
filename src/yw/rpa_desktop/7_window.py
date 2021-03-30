import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창
#
# print(fw.title) #활성화 창의 제목 정보
# print(fw.size) # 창의 크기 정보 (width, height)
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표정보
#
# pyautogui.click(fw.left + 200 , fw.top + 500)



# for w in pyautogui.getAllWindows():
#     print(w) #모든 윈도우 띄우기


w = pyautogui.getWindowsWithTitle("yw – 7_window.py")
print(w)

if w[0].isActive == False:
    w[0].activate()

if w[0].isMaximized == False:
    w[0].maximize()

pyautogui.sleep(2)
w[0].restore()

w[0].close()


