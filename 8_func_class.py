# *** Функции***

#  создание функции 
# не обладает параметрами и ниего не возвращает 
def func_1():
    print("Demis from func_1")

# обладает параметрами и ничего не возвращает 
def func_2(par_0, par_1, par_2=5):
    res = par_0 + par_1 + par_2
    print(res)

# обладает параметрами и возвращает что- то 
def func_3(par_1):
    res = par_1 ** 2
    return res

# вызов функций 
# func_2(999, 777, 666)


# ***классы***

# создание класса 
class Cat:
    # метод - конструктор ( сохдавать атрибуты )
    def __init__(self, name, a):
        # атрибуты 
        self.name = name
        self.age = a

    # свои методы Экземпляр обычные методы  - ФУНКЦИЯ ОБЬЕКТА ДАННОГО КЛАССА 
    def myau(self):
        res = f"Myau-Myau! My name is {self.name}! Age = {self.age}."
        print(res)

# создание экземпляров (обьектов) класса Cat
c_0 = Cat("FU-FA", 3)
c_1 = Cat("Dori", 2)
c_2 = Cat("Murka", 1)

# вызов методов 
c_0.myau()
c_1.myau()

# работа с атрибутами 

#c_2.name = "Dori"

#print(c_2.name)

c_2.myau()

# Функции более подробна 
# обьектно - ориентированное программирование 



