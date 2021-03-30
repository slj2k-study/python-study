import  pyautogui
#premium = pyautogui.locateOnScreen("Premium.png") #이미지 파일 찾기
#print(premium.left, premium.top)
#pyautogui.moveTo(premium.left, premium.top) #해상도 및 이미지 바뀔 시 fail

#for i in pyautogui.locateAllOnScreen("Premium.png"):
#    print(i)
#    pyautogui.moveTo(i,duration=1 )
#화면내에서 모든 정보 가져오기, 여러개도 다 가져옴

#속도개선, 흑백비교
#trash_icon = pyautogui.locateOnScreen("trash.png", grayscale = True)
#pyautogui.moveTo(trash_icon)

#범위 지정
#trash_icon = pyautogui.locateOnScreen(
#    "trash.png", grayscale = True, region=(1360,1052,1662-1360,1317-1052))
#pyautogui.moveTo(trash_icon)

#정확도 조정
#run_btn = pyautogui.locateOnScreen("trash.png", confidence=0.7)
#pyautogui.moveTo(run_btn)

#자동화 대상이 바로 보여지지 않는 경우
'''
trash = pyautogui.locateOnScreen("trash.png", confidence=0.7)
if trash:
    pyautogui.moveTo(trash)
else:
    print('No data Found')

trash = pyautogui.locateOnScreen("trash.png")
'''

'''
trash = pyautogui.locateOnScreen("trash.png")
while trash is None:
    trash = pyautogui.locateOnScreen("trash.png")
    print("Fail")
pyautogui.moveTo(trash)
'''

#2 일정시간 기다리기
import time
import sys

'''
timeout = 2 #10초 대기
start = time.time() #시작 시간 설정

trash = None
while trash is None:
    trash = pyautogui.locateOnScreen("trash.png")
    end = time.time() #종료시간 설정
    if end - start > timeout: #지정한 10초를 초과시
        print("시간 종료")
        sys.exit()

pyautogui.click(trash)
'''
def find_target(img_file, timeout= 30):
        start = time.time()
        target = None
        while target is None:
            target = pyautogui.locateOnScreen(img_file)
            end = time.time()
            if end - start > timeout:
                break
        return target


def my_click(img_file, timeout=30):
    target = find_target(img_file,timeout)
    if target:
        pyautogui.click(target)
    else:
        print("f[Timeout {timeout}s]")
        sys.exit()

my_click("trash.png",20)


