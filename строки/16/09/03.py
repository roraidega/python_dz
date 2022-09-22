price1 = int(input('Цена первого товара:'))
price2 = int(input('Цена второго товара:'))
price3 = int(input('Цена третьего товара:'))
price=price1+price2+price3
if price1<price2<price3:
    print('Акция') or print(price//2)
elif price1>price2>price3:
    print('Акция!') or print(price//3)
else:
    print(price)
