try: 
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    numero3 = int(input("Digite o terceiro número: "))
    print(f"Os números digitados foram: \n{numero1} \n{numero2} \n{numero3}")
except ValueError:
    #Código que será executado se der erro
    print("Entrada inválida! Por favor, digite apenas números.")