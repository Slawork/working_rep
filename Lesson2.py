x = -4
y = -5
if (x <0 and y >=0) or (x>=0 and y <0):
    print('Error')
else:
    print((x*y)**0.5)


#(x*y)**0.5

sheeps = ['овца', 'овца', 'овца', 'овца', 'овца', 'овца', 'овца', 'волк']


if 'волк' in sheeps:
    wolf_pos = sheeps.index('волк')
    if wolf_pos == 0:
        print(2)
    elif wolf_pos == len(sheeps)-1:
        print(wolf_pos)
    else:
        print(f'{wolf_pos} и {wolf_pos+2}')
else:
    print("Все овцы в безопасности")

#   Дан
#  список
#    чисел.Пока
#   в
    списке
    не
    останется
    одно
    число, необходимо: При
    первой, третьей, пятой
    и
    т.д.операциях
    складывать
    друг
    с
    другом
    соседние
    числа.[1, 2, 3, 4, 5, 6, 7, 8] = > [3, 7, 11, 15]

    При
    второй, четвёртой, шестой
    и
    т.д.операциях
    перемножать
    соседние
    числа.[3, 7, 11, 15] = > [21, 165]

    [21, 165] = > 186

    tyu = [1, 2, 3, 4, 5, 6, 7, 8]
    y = 0
    while len(tyu) > 1:
        y += 1
        you = []
        if y % 2 != 0:
            for i in range(0, len(tyu), 2):
                you.append(tyu[i] + tyu[i + 1])
        else:
            for i in range(0, len(tyu), 2):
                you.append(tyu[i] * tyu[i + 1])
        tyu = you[::]
        print(tyu)