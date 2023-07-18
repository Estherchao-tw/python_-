import pyautogui
print(pyautogui.position())

# #用1.5秒移動x=100,y=100的距離
# pyautogui.move(100,100,duration=1.5)
# #用1.5秒移動到x=100,y=100的位置
# pyautogui.moveTo(100,100,duration=1.5)

# #用2秒移動x=100,y=100的距離後，點右鍵
# pyautogui.drag(100,100,duration=2,button='right')
# #用2秒移動到x=100,y=100的位置，點右鍵
# pyautogui.dragTo(220,150,duration=2,button='right')

# #點擊兩下，間隔0.5秒，按右鍵
# pyautogui.click(clicks=2,interval=0.5,button='left')

#模擬滑鼠滾輪
# pyautogui.scroll(500)## not working

##鍵盤控制

# pyautogui.press('enter')
# pyautogui.press('alt')
# pyautogui.press('f1')

pyautogui.keyDown('ctrl')
pyautogui.press('a')
pyautogui.keyUp('ctrl')

# 快捷鍵，按照先後順序按
#打開工作管理員
# pyautogui.hotkey('ctrl','shift','esc')

#截圖
pyautogui.screenshot('1.png')
