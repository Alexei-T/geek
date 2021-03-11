spisok = [7, 5, 3, 3, 2]
num = int(input("Введите целое число: "))
a = spisok.count(num)
for element in spisok:
    if a > 0:
        i = spisok.index(num)
        spisok.insert(i + a, num)
        break
    else:
        if num > element:
            b = spisok.index(element)
            spisok.insert(b, num)
            break
        elif num < spisok[len(spisok) - 1]:
            spisok.append(num)
print(spisok)