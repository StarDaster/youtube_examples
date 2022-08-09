from functools import reduce
data = ['2018-01-01', 'yandex', 'cpc', 100]
print(reduce(lambda val, key: {key: val}, reversed(data)))
