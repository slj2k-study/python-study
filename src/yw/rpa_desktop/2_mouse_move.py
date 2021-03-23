import pyautogui

#pyautogui.moveTo(200,100) # 지정 위치로 마우스 이동
#pyautogui.moveTo(100,200,duration=5) # 5초동안 이동

#pyautogui.moveTo(100,100)
#pyautogui.moveTo(200,200)
#pyautogui.moveTo(300,300)

pyautogui.move(-100,-100) #상대좌표, 현재 커서가 있는 위치로 부터 이동
print(pyautogui.position())
pyautogui.move(-100,-100, duration=5)
print(pyautogui.position())
