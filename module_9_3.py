first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(first_) - len(second_) for first_, second_ in zip(first, second) if len(first_) != len(second_))
second_result = (len(first[j]) == len(second[j]) for j in range(len(second)))




print(list(first_result))
print(list(second_result))