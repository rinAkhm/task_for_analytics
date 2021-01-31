import os
import json



'''
содержимое файла перенисите в файл purchase_log.csv'''

with open ('C://Users//r.akhmetzyanov//Downloads//purchase_log.txt', 'r', encoding='utf-8' ) as file:
    text = ''
    with open('purchase_log.csv', 'w', encoding='utf-8') as write_file:
        for i, line in enumerate(file):
            text  = file.readline().strip()
            text += "\n"
            write_file.write(text)
            print(text)
            if i > len(text):
                print('write was successful')
                break


'''
Переведите содержимое файла purchase_log.txt в словарь purchases вида: {‘1840e0b9d4’: ‘Продукты’, …}
Для каждого user_id в файле visit_log.csv определите третий столбец с категорией покупки 
(если покупка была, сам файл visit_log.csv изменять не надо). Запишите в файл funnel.csv визиты из файла visit_log.csv, 
в которых были покупки с указанием категории.
Пример:
['user_id,source,category \n',
 '1840e0b9d4,other,Продукты \n']
'''


dict_with_product  = {}
with open('C://Users//r.akhmetzyanov//Downloads//purchase_log.txt', encoding='utf-8') as read_file:
    for line in read_file:
        row = json.loads(line.strip())
        if row['user_id'] == 'user_id':
            continue
        else:
            dict_with_product[row['user_id']]=row['category'] 

with open('C://Users//r.akhmetzyanov//Downloads//visit_log.csv', encoding='utf-8') as read_file2:
    with open('funnel.csv', 'w', encoding='utf-8') as funnel:
        for line in read_file2: 
            text_from_logfile = line.strip().split(',')
            row =  line.strip()
            if text_from_logfile[0] == 'user_id':
                row += ',{}'.format('category')
                funnel.write(f'{row}\n')
            elif text_from_logfile[0] in dict_with_product:
                row += ',{}'.format(dict_with_product[text_from_logfile[0]])
                funnel.write(f'{row}\n')

