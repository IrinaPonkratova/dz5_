# Напишите функцию, которая принимает на вход строку -
# абсолютный путь до файла. Функция возвращает кортеж
# из трёх элементов: путь, имя файла, расширение файла.


def func(data:str):

    parts = data.split('/')
    data_name = data.split('.')
    path = "/".join(parts[:-1])

    name_and_exp = "/".join(parts[-1:]).split('.')
    name = "/".join(name_and_exp[:1])

    exp = "/".join(data_name[1:])

    my_tuple = (path, name, exp)
    return my_tuple


print(func('/home/user/documents/report.docx'))