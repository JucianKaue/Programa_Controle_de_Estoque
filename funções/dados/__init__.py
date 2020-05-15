def dinheiro(n):
    n = str(n).strip()
    n = n.replace(',', '.')
    num = []
    for e in n:
        if e in '1234567890.':
           num.append(e)
    money = ''.join(num)
    return money