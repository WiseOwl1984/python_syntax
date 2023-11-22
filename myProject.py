# Программа с графическим пользовательским интерфейсом (GUI)

# *** Генератор паролей ***

# Криптостойкие пароли 
# импортирование модулей 
# стандартная библетека 

import hashlib 
from tkinter import Tk, Label, Entry, Button, StringVar

# основная функция 
def pwd_Generator(pwd_str: str) -> str:
    #  кодирование в байт строку 
    byte_str = pwd_str.encode()
    # хэширование 
    hash_str = hashlib.sha256(byte_str)
    # преобразование в обычную строку 
    hex_str = hash_str.hexdigest()[:10]
    # возврат в хещ - строку 
    return hex_str

# # тестироание функции 
# while True:
#     pwd = input("Введите пароль: ")
#     if pwd == "stop":
#         break
#     res = pwd_Generator(pwd)
#     print(res)

# обьект окна 
app = Tk()

# обьекты для хранение строк 
raw_pwd = StringVar()
result = StringVar()

# виджет текстовой метки 
Label(text="Пароль:").grid(row=0, column=0)

# виджет поля ввода пароля 
Entry(textvariable=raw_pwd).grid(row=0, column=1)

# виджет кнопки 
def btn_func():
    result.set(pwd_Generator(raw_pwd.get()))
Button(text="START", command=btn_func).grid(row=1, column=0)

# виджет поля вывода результата 
Entry(textvariable=result).grid(row=1, column=1)


# точка входа программы

app.mainloop()
