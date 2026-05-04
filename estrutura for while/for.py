print("-------------------------------------")
print("\nBem vindo!\n")
print("-------------------------------------")

sair = 0
n_tentativas = 2
rodada = 1
saldo = 1000
versaldo = 3

for n_tentativas in range(1, n_tentativas):
    print ("Para Prosseguir 1, para sair 0")
    entrada = int(input("digite um número: "))
    saida = entrada == sair
    chutemaior = entrada == rodada


    print(f"Você digitou o número: {entrada}")

    if(saida):
        print("Volte Sempre!")
        break
    else:
        if(chutemaior):
            print ("Para ver seu saldo digite número 3")
            contaSaldo = int(input("digite um número: "))
            ver = contaSaldo == versaldo
    if(ver):
        print(f"O saldo da sua conta é de {saldo} reais")
