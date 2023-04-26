def z1():
    import json

    with open('файл.json',encoding='utf-8') as f:
        s = json.load(f)

    for product in s['products']:
        print('Название:', (product['name']))
        print('Цена:', product['price'])
        print('Вес:', product['weight'])
        if product['available']:
            print('В наличии')
        else:
            print('Нет в наличии!')
        print()

def z2():
    import json
    with open('файл.json',encoding='utf-8') as f:
        s = json.load(f)

    name = input('Введите название продукта: ')
    price = input('Введите цену продукта: ')
    weight = input('Введите вес продукта: ')
    available = input('Есть ли продукт в наличии? (да/нет): ').lower() == 'да'

    new = {'name': name, 'price': price, 'weight': weight, 'available': available}
    s['products'].append(new)

    for product in s['products']:
        print('Название:', (product['name']))
        print('Цена:', product['price'])
        print('Вес:', product['weight'])
        if product['available']:
            print('В наличии')
        else:
            print('Нет в наличии')
        print()


def z3():
    with open('en-ru.txt', 'r', encoding='utf8') as f:
        enrudict = {}
        for line in f:
            enword, ruwords = line.strip().split(' - ')
            if ruwords in enrudict:
                enrudict[ruwords].append(enword)
            else:
                enrudict[ruwords] = enword

    with open('ru-en.txt', 'w',encoding='utf8') as f:
        for ruword in sorted(enrudict.keys()):
            f.write(ruword + ' - ' + ''.join(enrudict[ruword]) + '\n')

z2()