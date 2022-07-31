import re


def match_number(num: str):
    pattern = r"([АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2})(\d{2,3})$"
    match = re.match(pattern, num)
    if match:
        return f"Номер {match.group(1)} валиден. Регион: {match.group(2)}"
    return "Номер не валиден"


# num = "А111АА88"
# print(match_number(num))

def deduplicator(text: str):
    print(re.sub(r"(\w+)(\s+\1)+", r"\1", text))


some_string = 'Напишите Напишите функцию функцию, которая будет будет будет будет удалять все все все все последовательные ' \
              'повторы слов из из из из заданной строки строки при помощи регулярных выражений.'
deduplicator(some_string)
