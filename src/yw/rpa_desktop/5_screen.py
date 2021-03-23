import pyautogui

#img = pyautogui.screenshot()
#img.save("screenshot.png") #파일로 저장

#pyautogui.mouseInfo()
#135,156 255,0,0 #FF0000

pixel = pyautogui.pixel(135, 156)
print(pixel)

print(pyautogui.pixelMatchesColor(136,156, (255,0,0)))
print(pyautogui.pixelMatchesColor(136,156, pixel))

