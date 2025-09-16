#EXPLICAÇÃO: if/else
#if condição/comparação
    #tudo que acontece se a condição for verdadeira
    #outras condições
#else condição/comparação
    #tudo que acontece se a condição for falsa
    #outras condições
#elife 

#COMPARADORES
# > naior que
# < menor que
# >= maior ou igual que
# <= menor ou igual que
# == igual
# != diferente

#EXEMPLO 1:
#vendas = 1500
#meta = 1500

#if vendas >= meta:
#    print("vendedor ganha bônus.")
#    print("Bateu a meta de vendas!")
#    bonus =  0.1 * vendas
#    print("Bonus do vendedor: ", bonus)
#else:
#    print("Vendedor não ganha bonus.")
#    print("Não bateu a meta!")

#EXEMPLO 2:
#vendas = 1800
#meta1 = 1300 #ganha 10%
#meta2 = 2000 #ganha 13%

#if vendas >= 2000:
#    bonus = 0.13 * vendas
#else:
#    if vendas >= 1300:
#        bonus = 0.10 * vendas
#    else:
#        bonus = 0
#print("Bonus", bonus)

#EXEMPLO 3:
#vendas = 1300
#meta1 = 1300 #ganha 10%
#meta2 = 2000 #ganha 13%
#if vendas >= 2000:
#    bonus = 0.13 * vendas
#elif vendas >= 1300:
#    bonus = 0.1 *vendas
#else:
#    bonus = 0
#print("Bonus:", bonus)

#EXEMPLO 4: tem que ser da meta do maior valor para o menor, senão não funciona
#vendas = 2600
#meta1 = 1300 #ganha 10%
#meta2 = 2000 #ganha 13%
#meta3 = 2500 #ganha 15%
##if vendas >= meta3:
#    bonus = 0.15 * vendas
#elif vendas >= meta2:
#    bonus = 0.13 *vendas
#elif vendas >= meta1:
#    bonus = 0.10 *vendas
#else:
#    bonus = 0
#print("Bonus:", bonus)

#EXEMPLO 5:
#lista_produtos = ["arroz", "feijão", "macarrão", "farinha"]
#produto_procurado = input("Procure um produto: ")
#produto_procurado = produto_procurado.lower()

#if produto_procurado in lista_produtos:
#    print("Produto em estoque")
#else:
#    print("Não temos este produto")

#EXEMPLO 6: Só ganha o bônus se a empresa bater a meta geral, mesmo que o vendedor bata sua meta pessoal
#vendas = int (input("Digite o valor das vendas:")) #pede para inserir as vendas, mas tem que colocar int para transformar o string em nº
#vendas_empresa = 17000
#meta_empresa = 18000
#meta1 = 1300 #ganha 10%
#meta2 = 2000 #ganha 13%
#meta3 = 2500 #ganha 15%
#if vendas >= 2500 and vendas_empresa >= meta_empresa:
#    bonus = 0.15 * vendas
#elif vendas >= 2000 and vendas_empresa >= meta_empresa:
#    bonus = 0.13 * vendas
#elif vendas >= 1300 and vendas_empresa >= meta_empresa:
#    bonus = 0.1 * vendas
#else:
#    bonus = 0
#print("Bonus", bonus)


#EXPLICAÇÃO 2: for/loop
#for i in range(10):#sinaliza quantas vezes uma ação deve ser repetida
#    print("Loop do python")

#lista_vendas = [1000, 500, 800, 2000, 2300]
#meta = 1200
#percentual_bonus = 0.1

#for item in lista_vendas:#escreve todos os itens da lista (o nome item, da varivel, pode ser qualquer outro)
#    print(item)

#for venda in lista_vendas: #de acordo com a lista, verifica um por um e calcula o bonus dentro da condição
#    if venda >= meta:
#        bonus = percentual_bonus * venda
#    else:
#        bonus = 0
#    print("Bonus: ", bonus)

#EXPLICAÇÃO 3: dicionarios - assimilar uma lista com a outra
lista_produtos = ["arroz", "feijão", "macarrão", "farinha"]
precos = [20, 10, 5, 2]

#dic_produtos = {"chave": valor, "chave2": valor2}
dic_produtos = {"arroz": 20, "feijão": 10, "macarrão": 5, "farinha": 2}

#pegar um elemento dentro da lista do dicionário e mostra o valor correlacionado
#print(dic_produtos["arroz"])

#quantidade de itens da lista
#print(len(dic_produtos))

#editar elemento
#dic_produtos["feijão"] = dic_produtos["feijão"] * 1.3
#print(dic_produtos)

#retirar um item
#dic_produtos.pop("farinha")
#print(dic_produtos)

#adicionar um item
#dic_produtos["café"] = 40
#print(dic_produtos)

#verificar se um item existe no dicionário
#if "arroz" in dic_produtos:
#    print ("Existe o produto")
#else:
#    print("Não existe")

#verificar se um valor existe nos valores do dicionário
#if 50 in dic_produtos.values():
#    print("Existe")
#else:
#    print("Não existe")

nome_produto = input("Nome do Produto")
preco_produto = input("Preco do Produto")

#Cadastrar o novo produto (Se o produto não existir)
#Caso o produto exista, ele vai editar o produto
produto = "arroz"
nome_produto = nome_produto.lower()
preco_produto = float(preco_produto)

dic_produtos[nome_produto] = preco_produto
print(dic_produtos)

# Além disso, o programa tem que atualizar o preço de todos os produto#para novos 
#valores em 10% a mais do que o preço original

for produto in dic_produtos:
    novo_preco = dic_produtos[produto] * 1.1
    dic_produtos[produto] = novo_preco

    