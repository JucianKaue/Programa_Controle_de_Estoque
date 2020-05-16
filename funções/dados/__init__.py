def dinheiro(n):
    n = str(n).strip()
    n = n.replace(',', '.')
    num = []
    for e in n:
        if e in '1234567890.':
           num.append(e)
    money = ''.join(num)
    return money


def data_hoje(padrao=1):
    from datetime import date
    if padrao != 1:
        d = date.today().day
        m = date.today().month
        y = date.today().year
        return [y, m, d]
    else:
       return date.today()


def data(data):
    e = data.replace('/', ' ').split()
    return f'{e[2]}-{e[1]}-{e[0]}'


print(data('15/05/2020'))
