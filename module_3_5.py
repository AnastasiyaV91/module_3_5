def get_multiplied_digits(number):                                 # Создаем функцию get_multiplied_digits и
                                                                   # параметр number в ней.
    str_number = str(number)                                       # Создаем переменную str_number и запишем
    first = int(str_number[0])                                     # в виде str числа number в неё.
    if len(str_number) > 1:                                        # Длинна строки str_number должна быть больше 1
        return first * get_multiplied_digits(int(str_number[1:]))  # Возвращаем
                                                                   # first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first                                               # Если длинна строки str_number не больше 1, то
                                                                   # возвращаем first


result = get_multiplied_digits(40203)
print(result)