import pyautogui
pyautogui.FAILSAFE = False
pyautogui.moveTo(0,0,duration=1)
pyautogui.moveTo(100,200,duration=1)
#pyautogui.typewrite("Pilin", interval=0.25)
#pyautogui.move(200,200,duration=1)
imagen=pyautogui.locateOnScreen(r'C:\Proyectos_Python\Pyautogui\SAP.png',confidence=0.8)

if imagen is None:
    print('Image not found on the screen!')
else:
    pyautogui.doubleClick(imagen)


