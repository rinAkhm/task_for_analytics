from datetime import datetime
def len_string(phrase_1:str, phrase_2:str)->str:
    if phrase_1>phrase_2:
        return print(f'phrase_1 больше и его длина {phrase_1}')
    elif phrase_1==phrase_2:
        return print(f'phrase_1 и phrase_2 одинаковые и их длина {phrase_1}')
    else:
        return print(f'phrase_2 больше и его длина {phrase_2}')

def leap_year(year:int)->str:
    if year%4!=0 or (year%100 == 0 and year%400 != 0):
        return print (f'обычный')
    else:
        return print(f'Високосный')

def horoscope():
    day = int(input('Введите день: '))
    if 1<day<31:
        month = input('Введите месяц: ').lower()
        if (day >= 21 and month == "март") or (day <= 20 and month == "апрель"):
            print ('Ваш знак зодиака: Овен')
        elif (day >= 21 and month == "апрель") or (day <= 21 and month == "май"):
            print ('Ваш знак зодиака: Телец')
        elif (day >= 22 and month == "май") or (day <= 21 and month == "июнь"):
            print ('Ваш знак зодиака: Близнецы')
        elif (day >= 22 and month == "июнь") or (day <= 22 and month == "июль"):
            print ('Ваш знак зодиака: Рак')
        elif (day >= 23 and month == "июль") or (day <= 23 and month == "август"):
            print ('Ваш знак зодиака: Лев')
        elif (day >= 24 and month == "август") or (day <= 22 and month == "сентябрь"):
            print ('Ваш знак зодиака: Дева')
        elif (day >= 23 and month == "сентябрь") or (day <= 23 and month == "октябрь"):
            print ('Ваш знак зодиака: Весы')
        elif (day >= 24 and month == "октябрь") or (day <= 22 and month == "ноябрь"):
            print ('Ваш знак зодиака: Скорпион')
        elif (day >= 23 and month == "ноябрь") or (day <= 22 and month == "декабрь"):
            print ('Ваш знак зодиака: Стрелец')
        elif (day >= 23 and month == "декабрь") or (day <= 20 and month == "январь"):
            print ('Ваш знак зодиака: Козерог')
        elif (day >= 21 and month == "январь") or (day <= 19 and month == "февраль"):
            print ('Ваш знак зодиака: Водолей')
        elif (day >= 20 and month == "февраль") or (day <= 20 and month == "март"):
            print ('Ваш знак зодиака: Рыбы')
        else:
            print ('Вы ввели некорректные значения')
    else:
        print('нужно писать числа от 1 до 31')
        

if __name__ == "__main__":    
    phrase_1 = len('Насколько проще было бы писать программы, если бы не заказчики')
    phrase_2 = len('640Кб должно хватить для любых задач. авылл Гейтс (по легенде)')
    len_string(phrase_1,phrase_2)
    
    leap_year(400)
    
    a = horoscope()
