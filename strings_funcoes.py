
#Para buscar caracter dentro de um banco de dados(texto) : .find()
#EX
#print(email_cliente.find("@"))
#Quando não for encontrado o solicitado dentro do find, ele retorna com o "-1"

#Para buscar o tamanho do texto(a quantidade de caracteres dentro da string ou informação)
#Ex:

print(len(email_cliente))
print(len(nome_cliente))

#Pegar um caracter - solicita dentro das chaves "[]"
print(email_cliente[15])
print(nome_cliente[10])
print(nome_cliente[-1])#solicitar caracter do final para o início
print(nome_cliente[:4])#solicitar informações a partir de um ponto até o outro solicitado
nome_cliente = 'Joao Pedro Carvalho'
email_cliente = 'EMAILCLIENTE@GMAIL.COM'

novo_email = email_cliente.replace("gmail.com", "hotmail.com")#troca informações dentro da string, uma pela outra: ".replace()"
print(novo_email)
novo_nome = nome_cliente.replace("Carvalho", "Felisberto")
print(novo_nome)

#Maíscula e minúscula
nome = 'carlos josé'

print(nome.capitalize())#coloca a primeira letra da string inteira para Maiúscula
print(nome.title())#Coloca a primeira letra de cada nome em maiúscula

#Transformando em letra maiúscula e minúscula:
email_cliente = email_cliente.upper() #Transforma a string em letras maiúscula
print(email_cliente)
email_cliente = email_cliente.lower() #Transforma a string em letras minúscula
print(email_cliente)


#Extrair informações de variáveis diferentes
#Pegar servidor do e-mail
posicao_arroba = email_cliente.find("@") +1
servidor = email_cliente[posicao_arroba:]

print(servidor)

#Captar o primeiro nome e sobrenome
posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco]
sobrenome = nome[posicao_espaco +1 :]
print(primeiro_nome) #Captar o primeiro nome
print(sobrenome) #Pegar sobrenome


