a = int(input())
# Обозначим переменной 'b' счетчик длинны монотонного фрагмента:
b = 0
# Обозначим переменной 'c' число, которое стоит перед числом 'a':
c = 0
# Создаем цикл: пока переменная 'a' больше 0, цикл выполняется:
while a > 0: 
   # Создаем условие: если переменная 'a' больше переменной 'c', то выполняем алгоритм:
    if a > c: 
        c = a
        b += 1
        a = int(input())
    # Создаем условие: если переменная 'a' равна переменной 'c', то выполняем алгоритм:
    elif a == c:
        c = a
        b += 0
        a = int(input())
    # Создаем условие: если переменная 'a' меньше переменной 'c', то выполняем алгоритм:
    elif a < c:
        c = a
        b = 1
        a = int(input()) 
# После завершения цикла выводим переменную 'b' в результат:
print(b)