'''
'r' -> Usado somente ler algo
'w' -> Usado somente para escrever algo
'r+'-> Usado para ler e escrever algo
'a' -> Usado para acrescentar algo
'''
#programa que lê e escreve e envia o arquivo via e-mail
#Criar um find no texto
#Fazer gerar dentro de uma pasta
import os

def menu():
    print("Opcao '1': Inserir um valor.")
    print("Opcao 's': Para sair.")

def criar_arquivo_txt(nomeArquivo):
    arquivo = open(f'{nomeArquivo}.txt', 'x')
    return arquivo

def abrir_arquivo(caminho, modo = 'r', nomeArquivo = ''):
    nomeArquivo = caminho
    caminho = caminho + '.txt'
    try:
        arquivo = open(file=caminho, mode=modo, encoding='utf-8')
    except:
        print(f"O arquivo {nomeArquivo} não existe, deseja criar?")
        print("S para SIM, n para NÃO")
        resposta = input().lower()
        if resposta == 's':
            arquivo = criar_arquivo_txt(nomeArquivo)
        elif resposta == 'n':
            arquivo = False
            print("Ok, saindo!")
        else:
            print("Opção inválida")
            abrir_arquivo(caminho, modo)

    return arquivo

def ler_arquivo(nomeArquivo):
    os.system('cls')
    arquivo = abrir_arquivo(f'{nomeArquivo}', 'r')

    if arquivo == False:
        print(f"Ocorreu um erro ao ler o {nomeArquivo}.")
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

def sobrescrever_criar_arquivo(nomeArquivo):
    arquivo = abrir_arquivo(f'{nomeArquivo}', 'w')

    if arquivo == False:
        print(f"FALHA AO ABRIR O {nomeArquivo} - VERIFIQUE!")
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

def zerar_arquivo_arquivo(nomeArquivo):
    arquivo = abrir_arquivo(f'{nomeArquivo}', 'w')
    arquivo.write(str(''))
    print(f"Arquivo {nomeArquivo} zerado com sucesso!")

def ler_escrever_arquivo(nomeArquivo) :
    arquivo = abrir_arquivo(f'{nomeArquivo}', 'r+')

    if arquivo == False:
        print("Ocorreu um erro ao ler o {nomeArquivo}.")
    else:
        os.system('cls')
        ler_arquivo()

    print(f"Deseja adicionar valores ao arquivo {nomeArquivo} ?")
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
    
def acrescentar_arquivo(nomeArquivo):
    arquivo = abrir_arquivo(f'{nomeArquivo}', 'a')

    if arquivo == False:
        print(f"Ocorreu um erro ao ler o {nomeArquivo}.")
    
    resposta = input("""Deseja acrescentar valores ?\nDigite S para SIM e N para NÃO: """).lower()
    while resposta != 'n':    

        if resposta == 's':
            texto_novo = input()
            arquivo.write(str(texto_novo) + '\n')

        elif resposta == 'n':
            print("Ok, Saindo!")

        else:
            print("Opção inválida!")
    arquivo.close()

ler_arquivo("valores_celular")


        