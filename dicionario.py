#programa de hoje

'''

O exercício de hoje é 
Escrever um programa que faça uma agenda básica 

com as seguintes funções 
Inserir na agenda
remover da agenda
editar agenda 
Contar elementos da agenda
Interface modo texto
'''

# Isso é um dicionário
agenda = {}

#def -> definição de função

def insere():
    pass #-> deixa vazio enquanto não sabe o que fazer

def remove():
    pass

def edita():
    pass

def contabiliza():
    pass

# Loop da agenda 
#aqui vcs vão coletar elementos da agenda e os comandos que eu quero fazer

comando = ""

while (comando != "FIM"):
    print("Bem vindo à agenda de LP")
    comando = input("Digitie o comando que vc deseja: Inserir, Remover, Editar ou Contar")
    if comando == "Inserir":
        insere()
    elif comando == "Remover":
        remove()
    elif comando == "Editar":
        edita()
    elif comando == "Contar":
        contabiliza()
    else:
        comando = "FIM"
        print("Saindo do programa")
