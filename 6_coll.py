# *** коллекции ***

# Кортеж (tuple)

 # упорядоченная неизменяемая (мутабельная ) коллекция 

#  создание предворительного заполненного кортежа 
tuple_1 = (2010, 3010, 50, 5, 8)
tuple_1 = tuple([10, 100, 3.14, "python"])
tuple_1 = tuple("HELLO,tuple")

# чтение значений 
val_1 = tuple_1[8]

# срез кортежа 
slice_1 =tuple_1[2:8]
slice_1 =tuple_1[::-1]

# print(slice_1)

# словарь (dict, dictionari)

# Неупорядочная изменяемая коллекция 

# элемент словаря - пара " ключ значение"

# создание пустого словаря 
dict_1 = {}
dict_1 = dict()

#  создание предворительно заполненного словаря 
# хеш таблицы 

dict_2 = {7:7000, 0:3.14, 'A':20, "DEMIS":"python", "кортеж":(2010)}

lst_1 = [(13, 26), ("D", "S"), (5, dict_2)]

dict_3 = dict(lst_1)

dict_3 = dict(a=200, b=300)

# чтение значения 
val_1 = dict_2["кортеж"]

# добавление целой пары 
dict_2["B"] = 999
dict_2["D"] = "HELLO"

# замена значения 
dict_2["D"] = "Bye"

# удаление пары 
del dict_2["B"]

# методы 

print(dict_2)

items_0 = list(dict_2.items())
values_0 = list(dict_2.values())
keys_0 = list(dict_2.keys())

val_2 = dict_2.pop("D")

print(val_2)
print(dict_2)

# просмотреть остальные методы словарей
# методы кортежа 
# множества (set)




