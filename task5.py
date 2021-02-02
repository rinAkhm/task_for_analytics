from datetime import datetime
from datetime import timedelta



'''The Moscow Times - Wednesday, October 2, 2002
The Guardian - Friday, 11.10.13
Daily News - Thursday, 18 August 1977'''

format1 ='Wednesday, October 2, 2002'
day1 = datetime.strptime(format1, "%A, %B %d, %Y")
print(day1,type(day1))

format2 ='Friday, 11.10.13'
day2 = datetime.strptime(format2, "%A, %y.%m.%d")
print(day2,type(day2))

format3 ='Thursday, 18 August 1977'
day3 = datetime.strptime(format3, "%A, %d %B %Y")
print(day3, type(day3))



def check_dates(stream):
    '''Напишите функцию, которая проверяет эти даты на корректность. Т. е. для каждой 
    даты возвращает True (дата корректна) или False (некорректная дата).'''
    for date in stream:
        try:
            datetime.strptime(date, "%Y-%m-%d")
            print(f'this date {date} is True')
        except ValueError as e:
            print(f'this date {date} is False')


def date_range(date_start:str, date_end:str):
    '''
    Напишите функцию date_range, которая возвращает список дат за период от start_date до end_date. 
    Даты должны вводиться в формате YYYY-MM-DD. 
    В случае неверного формата или при start_date > end_date должен возвращаться пустой список.'''
    list_date = []
    if date_start is None or date_end is None or date_end<date_start:
        # list_date = None
        print(list_date) 
    else:
        try:
            start = datetime.strptime(date_start, "%Y-%m-%d")
            end = datetime.strptime(date_end, "%Y-%m-%d")
            while start != end:
                start += timedelta(days=1)
                print(start.strftime("%Y-%m-%d"))

        except ValueError as e:
            print(e)
            list_date = []
            print(list_date)


if __name__ == "__main__":
    stream = ["2018-04-02", "2018-02-29", "2018-19-02"]
    check_dates(stream)
    date_range('2018-03-10','2018-04-10')
    