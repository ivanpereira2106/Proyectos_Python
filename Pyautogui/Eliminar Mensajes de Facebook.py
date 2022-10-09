import pyautogui
for i in range(200):
    pyautogui.FAILSAFE = True
    pyautogui.moveTo(0,100)
    pyautogui.click() 
    #Posicion Sobre el Globo de Opciones (...)
    pyautogui.moveTo(290,500)
    pyautogui.click() 
    #Posicion Sobre el Boton de Eliminar
    pyautogui.moveTo(290,850)
    pyautogui.click() 
    #Posicion Sobre el Mensaje de Eliminar
    pyautogui.moveTo(900,570)
    pyautogui.click() 

    #pyautogui.write("Pilin", interval=0.25)
    #pyautogui.move(200,200,duration=1)
    #imagen=pyautogui.locateOnScreen(r'C:\Users\ivan.pereira\Documents\Python_Proyects\SAP.png',confidence=0.8)

    #if imagen is None:
    #    print('Image not found on the screen!')
    #else:
    #    pyautogui.doubleClick(imagen)


