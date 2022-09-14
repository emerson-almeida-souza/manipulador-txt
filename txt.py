'''
'r' -> Usado somente ler algo
'w' -> Usado somente para escrever algo
'r+'-> Usado para ler e escrever algo
'a' -> Usado para acrescentar algo

tell() -> Retorna posição atual do arquivo em bytes
'''
#programa que lê e escreve e envia o arquivo via e-mail
#Criar um find no texto
#Fazer gerar dentro de uma pasta
import os, shutil

def menu():
    print("Opcao '1': Inserir um valor.")
    print("Opcao 's': Para sair.")

def abrir_arquivo(nomeArquivo, modo):
    os.system('cls')
    nomeArquivo = nomeArquivo + '.txt'
    try:
        arquivo = open(file=nomeArquivo, mode=modo, encoding='utf-8')
    except:
        print(f"O arquivo {nomeArquivo} não existe, deseja criar?")
        print("S para SIM, n para NÃO")
        resposta = input().lower()
        if resposta == 's':
            arquivo = open(file = nomeArquivo, mode='x')
        elif resposta == 'n':
            arquivo = False
            print("Ok, saindo!")
        else:
            print("Opção inválida")
            abrir_arquivo(nomeArquivo, modo)
            
    return arquivo

def ler_arquivo(nomeArquivo):
    os.system('cls')
    arquivo = abrir_arquivo(f'{nomeArquivo}', 'r')

    if arquivo == False:
        print(f"Ocorreu um erro ao ler o {nomeArquivo}.")
    else:
        linha = 0
        print("-------------------------------------------------------------")
        print('LINHA\t\tCONTEUDO')
        for valor in arquivo:
            print('[{}]\t\t{}'.format(linha, valor))
            linha = linha + 1
        
        print('\n\n' + f'O tamanho do arquivo é [{arquivo.tell()}] BYTES')
        print(f"O arquivo tem {linha} linhas")
        print("-------------------------------------------------------------")

def sobrescrever_criar_arquivo(nomeArquivo):
    os.system('cls')
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
    os.system('cls')
    arquivo = abrir_arquivo(f'{nomeArquivo}', 'w')
    arquivo.write(str(''))
    print(f"Arquivo {nomeArquivo} zerado com sucesso!")

def ler_escrever_arquivo(nomeArquivo):
    os.system('cls')
    arquivo = abrir_arquivo(f'{nomeArquivo}', 'r+')

    if arquivo == False:
        print(f"Ocorreu um erro ao ler o {nomeArquivo}.")
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
    os.system('cls')
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

def exibir_primeira_linha(nomeArquivo):
    os.system('cls')
    arquivo = abrir_arquivo(nomeArquivo, 'r')

    tamanho_arquivo = arquivo.readlines()
    if  len(tamanho_arquivo)== 0:
        ler_arquivo(nomeArquivo)
    else:
       print(arquivo.readline())

def retorna_string(nomeArquivo):
    arquivo = abrir_arquivo(nomeArquivo, 'r+')
    string_arquivo = arquivo.read()

    return string_arquivo

def retorna_list(nomeArquivo):
    arquivo = abrir_arquivo(nomeArquivo, 'r+')
    # list_arquivo = arquivo.readlines() ADICIONA UM \n no final de cada linha
    # com o list obtemos o mesmo resultado
    list_arquivo = list(arquivo)

    return list_arquivo


def copiar_conteudo_arquivos():
    origem = 'src.txt'
    destino = 'dst.txt'

    #abre um em modo de leitura e o que vai modificar em modo de escrita
    arquivo1 = open(origem, 'r')
    arquivo2 = open(destino, 'w')

    shutil.copyfileobj(arquivo1, arquivo2)

def criarCopiaArquivo():
    #Personalizar nome do arquivo
    origem = './origem/src'
    destino = './backup/src(copia2).txt'
    #shutil.copyfile OU shutil.copy
    dest = shutil.copyfile(origem, destino)
    print("Cópia criado no caminho", dest)

def copiarArvoreDiretorios():
    #PERSONALIZAR NOME DA PASTA
    origem = r'G:\Meu Drive\PY\Arquivos\backup'
    destino = 'G:\Meu Drive\PY\Arquivos\copia'

    shutil.copytree(origem, destino)

def removeArvoreDiretorios():
    path = 'G:\Meu Drive\PY\Arquivos\copia'
    shutil.rmtree(path)

#Cria o diretoório se não já existir, e move o diretório caso já exista
#copytree(source, destination, ignore=ignore_patterns('*.pyc', 'tmp*')): copia tudo menos arquivos *.pyc e 
#começam com tmp. * é o coringa
def moverDiretorio():
    origem = r'G:\Meu Drive\PY\Arquivos\backup'
    destino =     destino = 'G:\Meu Drive\PY\Arquivos\movidosCriado'
    shutil.move(origem, destino)

#espaço total, usado e livre
def visualizarEspaço(path = 'G:\Meu Drive'):
    #implantar pra GB tb
    uso_disco = shutil.disk_usage(path)
    mb = uso_disco.used / 1024**2
    print(f'Você já usou: {round(mb, 2)} MB')

def ziparDiretorio(nomePastaZipada = "backupZip"):
    nomeMeuZip = f'G:\Meu Drive\PY\Arquivos\{nomePastaZipada}'
    diretorioBase =r'G:\Meu Drive\PY\Arquivos\backup'

    shutil.make_archive(nomeMeuZip, "zip" ,diretorioBase)

def descompactarZip():
    shutil.unpack_archive(r'G:\Meu Drive\PY\Arquivos\backupZip.zip', 'G:\Meu Drive\PY\Arquivos', 'zip')
