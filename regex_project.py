import re
with open('./regex_test.txt') as f:
    data = f.readlines()
    # print(data)

pattern = re.compile('^[A-Z][a-zA-Z]{4,}(?: [A-Z][a-zA-Z]+)?(?: [A-Z][a-zA-Z]+)?$')

for person in data:
    find_names = pattern.findall(person)
    if find_names:
        print(f'{find_names}')
    else:
        print('none')