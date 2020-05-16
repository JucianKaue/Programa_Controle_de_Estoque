from funções import database, dados, gui


database.iniciardb()
try:
    gui.AddWindow()
except:
    roupas = open('C:/Users/jucia/PycharmProjects/Controle_de_Estoque/temp.txt', 'r')
    roupa = roupas.readlines()
    temp = []
    for e in roupa:
        valor = e.split('-')
        valor[3] = dados.dinheiro(valor[3])
        valor[4] = dados.dinheiro(valor[4])
        valor[5] = dados.data(valor[5])
        print(valor)
        for c in range(int(valor[6])):
            database.adicionar(
                codigo=valor[0],
                tamanho=valor[1],
                descricao=valor[2],
                preco_entrada=valor[3],
                preco_saida=valor[4],
                dia_entrada=valor[5]
            )