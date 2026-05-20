pokedex = {}
historicoP = []

#FUNCAO ADICIONAR VERIFICA SE O POKEMON JÁ EXISTE, SE NÃO PEDE O NOME, TIPO E NIVEL E GUARDA NO DICIONARIO POKEDEX
def adicionar():
    pokemon = input("Qual o nome do Pokemon ?: ")
    if pokemon in pokedex:
        print("\nPokemon já está em sua Pokedex\n")
        return
    else:
        tipo = input("Qual o tipo do Pokemon ?: ")
        nivel = int(input("Qual o nível do Pokemon?: "))
        if nivel > 100:
              print("\nO nível máximo é 100!\n")
        else:
            pokedex[pokemon] = {"Tipo": tipo, "Nivel": nivel}
            print(f"\nPokemon {pokemon} adicionado com sucesso na Pokedex\n")

#VERIFICA SE A POKEDEX ESTÁ VAZIA, SE SIM RETORNA UMA STRING DIZENDO QUE ESTA VAZIA, SE NÃO LISTA EM ORDEM ALFABETICA OS POKEMONS REGISTRADOS
def listar():
    if not pokedex:
          print("Pokedex vazia...\n")
          return
    print("\n-------POKEDEX-------\n")
    for pokemon in sorted(pokedex.keys()):
          info = pokedex[pokemon]
          print(f"\nPokemon: {pokemon}, Tipo: {info['Tipo']}, Nivel: {info['Nivel']}\n")

#VERIFICA SE O POKEMON EXISTE, SE SIM REMOVE ELE DO DICIONARIO, SE NÃO EXIBE MENSAGEM DE POKEMON NAO ENCONTRADO
def remover():
    pokemon = input("Qual o nome do Pokemon que você deseja remover ?: ")
    if pokemon not in pokedex:
          print("\nEsse Pokemon não está na sua Pokedex\n")
    else:
          del pokedex[pokemon]
    print(f"\nPokemon {pokemon} removido com sucesso\n")

#SE NAO HOUVER NENHUM HISTORICO DE CAPTURA RETORNA UMA STRING COM UMA MENSAGEM, SE HOUVER ELE MOSTRA O NOME DO POKEMON E QUANTIDADE DE VEZES CAPTURADO
def historico():
    if not historicoP:
          print("\nNenhum registro de captura...\n")
          return
    print("\n-------HISTORICO DE CAPTURAS-------\n")
    for info in historicoP:
          print(f"\nPokemon: {info['Pokemon']}, Capturas: {info['Capturas']}\n")

#VERIFICA SE O POKEMON EXISTE, SE SIM PEDE A QUANTIDADE DE VEZES CAPTURADO E GUARDA NA LISTA HISTORICO
def registrar():
    pokemon = input("Qual o nome do Pokemon que você deseja registrar as capturas?: ")
    if pokemon not in pokedex:
          print("\nErro, esse Pokemon nãoe está na sua Pokedex\n")
          return
    else:
          capturas = int(input(f"Quantas vezes {pokemon} foi capturado?: "))
          historicoP.append({"Pokemon": pokemon, "Capturas": capturas})
          print(f"\nPokemon {pokemon} foi capturado {capturas}x\n")

#VERIFICA SE O POKEMON EXISTE, SE SIM PEDE UM NOVO NIVEL E ATUALIZA NO DICIONARIO
def atualizar():
      pokemon = input("Qual o nome do Pokemon que deseja atualizar o nível ?: ")
      if pokemon not in pokedex:
            print("\nPokemon não encontrado na sua Pokedex\n")
            return
      else:
            novonivel = int (input(f"Qual o novo nível do {pokemon} ?: "))
            pokedex[pokemon]["Nivel"] = novonivel
            print(f"\nNível de {pokemon} atualizado para {novonivel}\n")

while True:  
    opcao = input (
        "qual opção você quer escolher ?:\n"
        "1 - Adicionar Pokemon\n"
        "2 - Listar Pokemons na Pokedex\n"
        "3 - Remover Pokemon da Pokedex\n"
        "4 - Registrar Captura de Pokemon\n"
        "5 - Historico de Pokemons Capturados\n"
        "6 - Atualizar nível do Pokemon\n"
        "7 - Sair\n"
        )
    if opcao == '1':
            adicionar()
    elif opcao == '2':
            listar()
    elif opcao == '3':
            remover()
    elif opcao == '4':
            registrar()
    elif opcao == '5':
            historico()
    elif opcao == '6':
          atualizar()
    elif opcao == '7':
            print("Saindo.......")
            break
    else:
            print("Erro, opção invalida")