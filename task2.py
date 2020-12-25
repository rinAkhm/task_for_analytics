def mid_letter(word:str)->'print_word':
    '''Выводит средний символ, если строка нечетная. Выводит пару символов, если строка четная'''
    x = int(len(word) / 2)
    if len(word)%2 != 0:
        print(word[x])
    else:
        print (word[x-1:x+1])

#mid_letter('word')



def count_num()->int:
    '''Подсчет веденных чисел, если вести число 0 пограмма выдаст сумму '''
    sum_num = 0
    while True:
        try:
            number = int(input('Введите число: '))
            sum_num += number
            if number==0:
                print(f'Результат:{a}\n')
                break
        except ValueError as er:
            print('Нужно вводить числа')

# count_num()



def match_pair(girls:list,boys:list)->'print_str':
    '''Составление сотрудников по парам'''
    if len(girls)==len(boys):
        girls.sort()
        boys.sort()
        girl = 0
        for boy in boys:
            print(f'{boy} : {girls[girl]}\n')
            girl+=1
    else:
        print('Внимание, кто-то может остаться без пары!\n')

boys = ['Peter', 'Alex', 'John', 'Artur', 'Rchard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
#match_pair(boys, girls)



def average_countries_temperature(countries_temperature:list)->str:
    ''' Подсчет среднего армитической температуры в стране'''
    for country in countries_temperature:
        result = sum(country[1])/len(country[1])
        print(f'{country[0]} : {(result):.1f} С \n') 

passcountries_temperature = [
['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
['Germany', [57.2, 55.4, 59, 59, 53.6]],
['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
#average_countries_temperature(passcountries_temperature)



def average_stream(streams:list)->'print_str':
    ''' Подсчет среднего количества просмотров по пользователям'''
    list_users = []
    count_stream = 0 
    for log in streams:
        count_stream += int(log.split(',')[2])
        if log.split(',')[1] not in list_users:
            list_users.append(log.split(',')[1])
        else:
            continue    
    print(f'Среднее количество просмотров на уникального пользователя: {count_stream/len(list_users)}')

streams = [
'2018-01-01,user1,3',
'2018-01-07,user1,4',
'2018-03-29,user1,1',
'2018-04-04,user1,13',
'2018-01-05,user2,7',
'2018-06-14,user3,4',
'2018-07-02,user3,10',
'2018-03-21,user4,19',
'2018-03-22,user4,4',
'2018-04-22,user4,8',
'2018-05-03,user4,9',
'2018-05-11,user4,11',
]
#average_stream(streams)


def duplicate_num():
    ''' Вывод веденных дубликатов'''
    temp_list = []
    numbers = input('Вводи числа через пробел:\n').split(' ')
    [temp_list.append(numbers[num]) for num in range(len(numbers))  if numbers[num] not in temp_list and numbers[num] in numbers[num+1:] ]      
    print(temp_list)

duplicate_num()