#Automatiza os navegadores(Webdriver)
#Instalação: py -m pip install selenium

import selenium

from selenium import webdriver
import time

#Abrir o navegador
navegador = webdriver.Chrome()
#Esse é o tempo que o navegador ficará aberto!
#time.sleep(10) 

#Colocar o navegador em tela cheia
navegador.maximize_window()

#Acessar um site
navegador.get("https://www.python.org/")

#Seleciona um elemento no site
#donate_button = navegador.find_element("class name", "donate-button")

#Agora se tiver mais de um botão na mesma classe
lista_botoes = navegador.find_elements("class name", "button")

for botao in lista_botoes:
    if "Become a Member" in botao.text:
        botao.click()
        break

#Clicar no elemento
#donate_button.click()
#Esperar antes de fechar o navegador
time.sleep(5)
