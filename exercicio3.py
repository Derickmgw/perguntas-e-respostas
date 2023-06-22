# exercicio - sistema de perguntas e respostas

perguntas = [
    {
        'pergunta': 'quanto é 2 + 2?',
        'opções': ['1', '3', '4', '5'],
        'resposta': '4',

    },
    {
        'pergunta': 'quanto é 5 * 5?',
        'opções': ['25', '55', '10', '51'],
        'resposta': '25',

    },
    {
        'pergunta': 'quanto é 10/2?',
        'opções': ['4', '5', '2', '1'],
        'resposta': '5',

    },
    {
        'pergunta': 'quanto é 500 * 4?',
        'opções': ['4000', '2000', '10000', '5000'],
        'resposta': '2000',

    },
    {
        'pergunta': 'quanto é 50/10?',
        'opções': ['10', '9', '5', '8'],
        'resposta': '5',

    },
]

acertos = 0
for pk in perguntas:
    print('pergunta:',pk["pergunta"])
    print()
    
    opcoes =  pk["opções"]
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('escolha uma opção: ')
    
    acertou = False
    escolha_int = None
    qt_opc = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qt_opc:
            if opcoes[escolha_int] == pk["resposta"]:
                acertos += 1
                print('Parabéns, você acertou!!!')
            else:
                print('que pena, você errou!')
              
    print()

print('você acertou', acertos, 'de',\
      len(perguntas), 'perguntas')
    
        
        
       
                

