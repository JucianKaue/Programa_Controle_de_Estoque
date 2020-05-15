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


def tecla(key):
    import keyboard
    return keyboard.is_pressed(key)

