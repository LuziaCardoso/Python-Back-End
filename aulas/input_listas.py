#inputs e listas de informações
#inputs
email = input("Dighite o seu e-mail: ")
nome = input("Digite o seu primeiro nome: ")
print(nome, email)
print(f'{nome}, verifique se o e-mail: {email} está correto!')

faturamento = float(input("Digite o faturamento da empresa: "))
imposto = faturamento * 0.1
print(imposto)

#Listas
vendas = [100, 50, 15, 20, 30, 500]
print(vendas)

#soma de elementos da lista
total_vendas = sum(vendas)
print(total_vendas)

#Tamanho da lista
quantidade_vendas = len(vendas)
print(quantidade_vendas)

#máximo e mínimo
print(max(vendas))
print(min(vendas))

#Pegar uma posição da lista
print(vendas[0]) #se colocar "-1", ele começa de trás para frente'''

#Verificar um elemento da lista
lista_produtos = ["iphone", "airpod", "ipad", "macbook"]
#print(lista_produtos)
print("apple watch" in lista_produtos)#Entra com um retorno Booleana, Se não tiver o item na lista retorna "False"
print("iphone" in lista_produtos) #Se tiver, o retorno será "True"

produto_procurado = input("Digite o nome do produto: ")
print(produto_procurado in lista_produtos)

#Adicionar um item na lista
lista_produtos.append("apple watch")
print(lista_produtos)

#Remover item da lista
lista_produtos.remove("apple watch") #remove o item inteiro
lista_produtos.pop(0)#remove o item de acordo com a posição na lista

#editar um item da lista
precos_produtos = [1000, 500, 2500, 1500]
precos_produtos[0] = 6000 #com o item mantendo o padrão da posição dentro da lista, ele altera a informação
print(precos_produtos)
precos_produtos[0] = precos_produtos[0] * 1.5 #essa opção faz a alteração do preço do produto (percentual de aumento ou redução)
print(precos_produtos)

#contar quantas vezes um item aparece ma lista
lista_produtos = ["iphone", "airpod", "ipad", "iphone", "ipad"]
print(lista_produtos.count("ipad")) #nesse caso aparece o ipad 2 vezes

#ordenar uma lista
lista_produtos.sort() #organiza os produtos em ordem alfabética
lista_produtos.reverse() #ordem alfabética inversa
print(lista_produtos)

precos_produtos.sort() #ordem crescente
precos_produtos.reverse() #ordem decrescente
print(precos_produtos)
