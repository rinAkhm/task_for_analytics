
def count_queris(queries:list)->int:
    '''Вам необходимо написать программу, которая выведет на экран распределение количества слов в запросах в требуемом виде.'''
    word_dict = {}
    count = 0
    for word in queries:
        if len(word.split()) not in word_dict:
            word_dict.setdefault(len(word.split()),1)
        else:
            word_dict[len(word.split())] += 1
    for key, value in word_dict.items():
        print(f'Поисковых запросов, содержащих {key} слов(a): {value/len(queries)*100:.2f}%')


queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    ]
# count_queris(queries)

def calculation_roi(results:dict)->dict:
    ''' Необходимо дополнить исходную структуру показателем ROI, который рассчитаем по формуле: (revenue / cost - 1) * 100'''
    for company in results:
        results[company]['roi'] = float('{:.2f}'.format((results[company]['revenue'] 
        - results[company]['cost'])/results[company]['cost']*100))
        results[company] = dict(sorted(results[company].items(), reverse=True))     
    print(dict(sorted(results.items())))

results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
    }

calculation_roi(results)

advertising_sales = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}


def max_statistic_from_chanal(stats:dict)-> str:
    ''' Напишите программу, которая возвращает название канала с максимальным объемом продаж.'''
    max_stats = [(value, key) for key, value in stats.items()]
    print(f'Максимальный объем продаж на рекламном канале: {max(max_stats)[1]}')


stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}
max_statistic_from_chanal(stats)


def unique_nums(ids:dict)->set:
    '''Вам необходимо написать программу, которая выведет на экран множество уникальных 
    гео-меток всех пользователей.'''
    nums = set()
    for i in ids:
        for j in ids[i]:
            nums.add(j)
    print (nums)

ids = {'user1': [213, 213, 213, 15, 213],
    'user2': [54, 54, 119, 119, 119],
    'user3': [213, 98, 98, 35]}
# unique_nums(ids)