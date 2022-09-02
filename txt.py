'''
'r' -> Usado somente ler algo
'w' -> Usado somente para escrever algo
'r+'-> Usado para ler e escrever algo
'a' -> Usado para acrescentar algo
'''
#Deixar o user digitar os valores
#programa que lê e escreve e envia o arquivo via e-mail
#Deixar ele escolher o txt
#Criar menu

import os

def menu():
    print("Opcao '1': Inserir um valor.")
    print("Opcao 's': Para sair.")

def abrir_arquivo(file, mode):
    try:
        arquivo = open(file=file, mode=mode, encoding='utf-8')
    except:
        arquivo = False
        print("Ocorreu um erro ao abrir o arquivo!")
    
    return arquivo

def ler_arquivo():
    arquivo = abrir_arquivo('valores_celular.txt', 'r')

    if arquivo == False:
        print("Ocorreu um erro ao ler o arquivo.")
    else:
        for valor in arquivo:
            print(valor)
        #Confirmação de fechada de arquivo
        arquivo.close()

def sobrescrever_arquivo():
    arquivo = abrir_arquivo('valores_celular.txt', 'w')

    if arquivo == False:
        print("FALHA AO ABRIR ARQUIVO - VERIFIQUE!")
    else:
        menu()
        opcao = ''
        while opcao != 's':
            opcao = input("Digite uma opção: ").lower()
            match opcao:
                case '1':
                    valor = input("Adicione o valor ao arquivo: ")
                    arquivo.write(str(valor) + '\n')
                    os.system('cls')
                    menu()

                case 's':
                    os.system('cls')
                    return print("Saindo!")

                case _:
                    os.system('cls')
                    print("Opcao inválida")
                    print("Digite uma das seguintes opções")
                    menu()
    arquivo.close()

def zerar_arquivo_arquivo():
    arquivo = abrir_arquivo('valores_celular.txt', 'w')
    arquivo.write(str(''))
    print(f"Arquivo {arquivo.name} zerado com sucesso!")

def ler_escrever_arquivo() :
    arquivo = abrir_arquivo('valores_celular.txt', 'r+')

    if arquivo == False:
        print("Ocorreu um erro ao ler o arquivo.")
    else:
        os.system('cls')
        print("- VALORES ATUAIS -")
        for valor in arquivo:
            print(valor)
        
    resposta = ''
    while resposta != '2':    
        print(f"Deseja adicionar valores ao arquivo {arquivo.name} ?")
        resposta = input(""" Digite 1 para SIM\n Digite 2 para NÃO\n""").lower()

        os.system('cls')
        if resposta == '1':
            texto_novo = input("Digite o valor que você quer adicionar ao arquivo: ")
            arquivo.write(str(texto_novo) + '\n')

        elif resposta == '2':
            print("Saindo!")
        else:
            print("Opção inválida!")
    
    arquivo.close()
    
def acrescentar_arquivo():
    arquivo = abrir_arquivo('valores_celular.txt', 'a')

    if arquivo == False:
        print("Ocorreu um erro ao ler o arquivo.")
    
    resposta = '1'
    while resposta != '2':    
        resposta = input("""Deseja acrescentar valores ?\nDigite 1 para SIM e 2 para NÃO: """).lower()

        os.system('cls')
        if resposta == '1':
            texto_novo = input("Digite o valor que você quer acrescentar ao arquivo: ")
            arquivo.write(str(texto_novo) + '\n')

        elif resposta == '2':
            print("Ok, Saindo!")

        else:
            print("Opção inválida!")
    arquivo.close()

acrescentar_arquivo()
    


        