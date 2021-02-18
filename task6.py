import requests
from pprint import pprint

class Rate:
    def __init__(self, format_ = 'full'):
        self.format = format_
    
    def exchange_rates(self):
        self.r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return self.r.json()['Valute']

    def make_format(self, currency):
        response = self.exchange_rates()
        if currency in response:
            if self.format == 'full':
                return response[currency]
            elif self.format == 'value':
                return response[currency]['Value']
        return 'Error'

    def eur(self):
        return self.make_format('EUR')


    def get_name(self):
        dict_ = {}
        response =  self.exchange_rates()
        for key in response:
            dict_[response[key]['Name']] = response[key]['Value']/response[key]['Nominal']
            max_value = max(dict_.items(), key=lambda x: x[1])
        pprint(dict_)


if __name__=='__main__':
    a = Rate().get_name()