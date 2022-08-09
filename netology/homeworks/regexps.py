import re


"2"
def remove_repeats(string):
   return re.sub(r'(\w+)(\s\1)+', r'\1', string)


text = "очень очень очень, много много пробелов"
print(remove_repeats(text))

"3"

some_string = 'Напишите функцию функцию, которая будет будет будет будет удалять все все все все последовательные повторы слов из из из из заданной строки строки при помощи регулярных выражений '


# res = re.findall(r'(\w+)(\s+\1)+', some_string)
# c = 1

# (asdasfasdfas )

# some_words = 'Информационные технологии'
#
# re.sub(r'(\w+)', r'\1'[0].upper(), some_words)

res = re.findall(r'[бвгджзклмнпрстфхцчшщ]{1}\w+', some_string)
print(res)