#É um processo de automação robótica.
#Ele só roda na máquina com todas as informações instaladas! Então é "por máquina"
#Tem que ter o Python e a biblioteca na máquina instalados!
import pyautogui
import time #colocar o tempo de execução do click do mouse
#Pega a posição do mouse e informação da tela 
pyautogui.PAUSE = 1 #Ele dá um "deley" antes de executar qualquer ação do meu código abaixo! Sempre tem
#que colocar esse comando antes do código!

print(pyautogui.position())#Essa função dá a coordenada X e Y
print(pyautogui.size())#resolução da tela

#Funções do mouse
time.sleep(1)
#pyautogui.click(x=359, y=400, button="rigth")
#nesse caso, está especificando qual botão será pressionado na hora que ativar as coordenadas escolhidas
#(rigth, left ou meddle)
#pyautogui.click(x=449, y=899, clicks=2)#Ele seleciona doble click no mouse
pyautogui.moveTo(x=282, y=223, duration=0.3)
#Ele move o mouse pra onde gostaríamos(no caso em um site que tenha um menu que aparece opções 
#sem precisar clicar(por exemplo, Kabum))
#Esse comando duration ele dá um time com a seta movendo na tela
pyautogui.moveTo(x=288, y=377, duration=0.3)
pyautogui.click(x=288, y=377, duration=0.3)
pyautogui.moveTo(x=531, y=302, duration=0.3)
pyautogui.click(x=531, y=302, duration=0.3)
pyautogui.moveTo(x=767, y=349, duration=0.3)
pyautogui.click(x=767, y=3496, duration=0.3)
time.sleep(2)
pyautogui.scroll(-2800)
pyautogui.click(x=833, y=164, duration=1)

#Funções do Teclado
pyautogui.write("monitor gamer lg", interval=0.2)
pyautogui.click(clicks=3)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "c")#Serve para apertar duas teclas juntas
#pyautogui.press("enter")
time.sleep(0.5)
pyautogui.moveTo(x=633, y=20)
time.sleep(2)
pyautogui.click()
pyautogui.moveTo(x=358, y=52)
pyautogui.click(2)
pyautogui.hotkey("crtl", "v")
pyautogui.press("enter")