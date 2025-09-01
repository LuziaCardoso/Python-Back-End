import os
#import datetime
#import pyautogui


#pyautogui.press("win") #estou pedindo para ele apertar o botão Windowns
#pyautogui.write("vscode") #estou pedindo para digitar vscode

#print(os.listdir("arquivos"))
#print(datetime.date.today())
lista_arquivos = os.listdir("arquivos")

for arquivo in lista_arquivos:
    if ".txt" in arquivo:
        if "22" in arquivo:
            os.rename(f"arquivos/{arquivo}", f"arquivos/22/{arquivo}")
        elif "23" in arquivo:
            os.rename(f"arquivos/{arquivo}", f"arquivos/23/{arquivo}")