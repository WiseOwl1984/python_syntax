# тема урока "Цикл "

# оператор while 

# бесконечный цикл 
# while True:
#     print("Demis")

# цикл с условием 
val_1 = 0

# while val_1 <= 10:
#     print(f"значение: {val_1}")
#     # икремент - увеличение 
#     #val_1 = val_1 + 1
#     val_1 += 1 

# прерывание цикла по дополнительному условию 

# while True:
#     val = input("введите имя: ")
#     val = input("сколько вам лет: ")
#     if val == "stop":
#         print("Bye - Bye!")
#         break
#     print(f"Привет, {val}!")

# пропуск части кода тела цикла 

# val_1 = 0 
# while val_1 < 20:
#     # 1 кусок кода 
#     print(val_1)
#     val_1 += 1

#     if val_1 < 10:
#         continue

#     # 2 кусок кода
#     print("Demis")

# оператор  for

# 1. считывает какие то значения "чтение значения из обьекта с последовательностью по порядку"
# 2. считаное значение присваивает с вобственную переменную
# 3.выполняет код тела 

lst_0 = [10, 50, 30, 100, 777, 999]

# for v in lst_0:
#     v *= 100
#     print(v)

dict_0 = dict(a=100, b=200, c=300)

# print(dict_0)

# for k, v in dict_0.items():
#     print(k, v)

# val_1, val_2 = (100, 200, 300)
# print(val_1, val_2,)

# for k in dict_0.values():
#     print(k)

# класс range()

r = range(-10, 10, 2)
# print(r)

tuple_0 = tuple(r)
# print(tuple_0)

# for v in r:
#     print(v)

# for v in range(5):
#     v += 10
#     print(v)

for _ in range(5):
    print("Demis")

#  генератор списка (кортежа)
# генератор словаря 
#