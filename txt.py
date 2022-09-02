'''
'r' -> Usado somente ler algo
'w' -> Usado somente para escrever algo
'r+'-> Usado para ler e escrever algo
'a' -> Usado para acrescentar algo
'''
#programa que lê e escreve e envia o arquivo via e-mail
#Criar um find no texto
import os

def menu():
    print("Opcao '1': Inserir um valor.")
    print("Opcao 's': Para sair.")

def criar_arquivo_txt(nome):
    arquivo = abrir_arquivo(f'{nome}', 'x')
    return arquivo

def abrir_arquivo(caminho, modo = 'r', nome = ''):
    nome = caminho
    try:
        arquivo = open(file=caminho, mode=modo, encoding='utf-8')
    except:
        print(f"O arquivo {nome} não existe, deseja criar?")
        print("S para SIM, n para NÃO\n")
        resposta = input()
        if resposta == 's':
            arquivo = criar_arquivo_txt(nome)
        elif resposta == 'n':
            arquivo = False
            print("Ok, saindo!")
        else:
            print("Opção inválida")
            abrir_arquivo(caminho, modo)
    
    return arquivo

def ler_arquivo():
    os.system('cls')
    arquivo = abrir_arquivo('teste3.txt', 'r')

    if arquivo == False:
        print("Ocorreu um erro ao ler o arquivo.")
    else:
        linha = 1
        print("-------------------------------------------------------------")
        print('LINHA\t\tCONTEUDO')
        for valor in arquivo:
            print('[{}]\t\t{}'.format(linha, valor))
            linha = linha + 1
        
        print('\n\n' + f'O tamanho do arquivo é [{arquivo.tell()}] BYTES')
        print(f"O arquivo tem {linha} linhas")
        print("-------------------------------------------------------------")

def sobrescrever_criar_arquivo():
    arquivo = abrir_arquivo('valores_notebook.txt', 'w')

    if arquivo == False:
        print("FALHA AO ABRIR ARQUIVO - VERIFIQUE!")
    else:
        os.system('cls')
        valor = ''
        print("Digite um valor para adicionar ao arquivo ou digite s para sair: ")
        while valor != 's':
            valor = input().lower()
            match valor:
                case 's':
                    os.system('cls')
                    return print("Saindo!")

                case _:
                    arquivo.write(str(valor) + '\n')
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
        ler_arquivo()

    print(f"Deseja adicionar valores ao arquivo {arquivo.name} ?")
    print("""Digite s para SIM ou Digite n para NAO""")
    opcao = input("Resposta: ").lower()
    if opcao == 's':
        os.system('cls')
        print("Digite os valores ou digite S para SAIR")
        valor = ''

        while valor != 's': 
            valor = input().lower()
            match valor:
                case 's':
                    os.system('cls')
                    print("Saindo!")   
                case _: 
                    arquivo.write(str(valor) + '\n')

    elif opcao == 'n':
        print("Ok, Saindo!")
    else:
        print("Opção inválida")
        ler_escrever_arquivo()
        arquivo.close()
    
def acrescentar_arquivo():
    arquivo = abrir_arquivo('teste3.txt', 'a')

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

abrir_arquivo("teste3.txt")
acrescentar_arquivo()
ler_arquivo()


        