import mysql.connector


def iniciardb(host='127.0.0.1', user='root', passwd='', database='loja'):
    global db
    s = False
    for n in range(0, 2):
        try:
            db = mysql.connector.connect(
                host=f'{host}',
                user=f'{user}',
                passwd=f'{passwd}',
                database=f'{database}'
            )
        except:
            db = mysql.connector.connect(
                host=f'{host}',
                user=f'{user}',
                passwd=f'{passwd}'
            )
            s = True
        if s:
            cursor = db.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS `roupas` (
  `codigo` int(11) NOT NULL,
  `tamanho` varchar(2) DEFAULT NULL,
  `descrição` varchar(100) DEFAULT 'sem descrição',
  `preço entrada` decimal(5,2) DEFAULT '00.00',
  `preço saida` decimal(5,2) DEFAULT '00.00',
  `dia entrada` date DEFAULT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;""")


def adicionar(codigo='DEFAULT', tamanho='', descricao='sem descrição', preco_entrada='R$00,00', preco_saida='R$00,00', dia_entrada=0):
    from datetime import date
    from funções import dados
    if dia_entrada == 0:
        dia_entrada = date.today()
    cursor = db.cursor()
    preco_entrada = dados.dinheiro(f'{preco_entrada}')
    preco_saida = dados.dinheiro(f'{preco_saida}')
    cursor.execute("INSERT INTO roupas"
                    "(`codigo`, `tamanho`, `descrição`, `preço entrada`, `preço saida`, `dia entrada`)"
                    "VALUES"
                    f"('{codigo}', '{tamanho}', '{descricao}', '{preco_entrada}', '{preco_saida}', '{dia_entrada}')"
                   )
    db.commit()

