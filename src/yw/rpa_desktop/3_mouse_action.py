import pyautogui

pyautogui.sleep(1)  # 3초대기
print(pyautogui.position())

# pyautogui.moveto(1352,23)
# pyautogui.click(1352,23,duration=1) #1초동안 좌표로 이동 후 마우스 클릭
# pyautogui.click()

# pyautogui.mouseDown()
# pyautogui.mouseUp()

# pyautogui.doubleClick()
# pyautogui.click(clicks=2) #같다

# 그림판 연 후 진행, 줄 그임
# pyautogui.moveTo(300,300)
# pyautogui.mouseDown()
# pyautogui.moveTo(400,400)
# pyautogui.mouseUp()

# pyautogui.rightClick() #우클릭
# pyautogui.middleClick() #중앙클릭

# pyautogui.drag(100,100) #현재 위치 기준으로 x 100만큼, y 0 만큼 드래그, 이건 너무 빨라서 안됨
#pyautogui.drag(100, 100, duration=0.5)  # 현재 위치 기준으로 x 100만큼, y 0 만큼 드래그
#pyautogui.dragTo(500,500) #절대좌표 위치로 드래그

pyautogui.scroll(300) #위 방향으로 300만큼 스크롤, -300 은 아래로 양수 위, 음수 아래
