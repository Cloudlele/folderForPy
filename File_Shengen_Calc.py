day_in_mounth = 30
schengen_constraint = 180
shengen_time = list()
visits = list()
temp_list = list()


#Перероблено
def add_visits():
    a = int(input('Введіть початок поїздки: '))
    b = int(input('Введіть кінець поїздки: '))
    with open('time_in_shengen.txt', 'a') as doc:
        doc.write(str(a))
        doc.write(' ')
        doc.write(str(b))
        doc.write('\n')

def f(lst):
    return [lst[i:i + 2] for i in range(0, len(lst), 2)]

#Перероблено
def print_all_visits():
    with open('time_in_shengen.txt') as doc:
        for visit in doc:
            shengen_time.append(visit.split())
    print('Дати ваших поїздкок в шенгені: ')
    i = 1
    for vis in shengen_time:
        print(i, ': ', vis)
        i += 1


def loops_in_test(temp_list):
    with open('time_in_shengen.txt') as doc:
        for visit in doc:
            temp_list += visit.split()
    for i, item in enumerate(temp_list):
        temp_list[i] = int(item)
    return temp_list


def read_visits(visits):
    with open('time_in_shengen.txt') as doc:
        for visit in doc:
            visits.append(visit.split())
#перероблено
def count_day_in_shengen(visits, day_in_mounth, shengen_constraint):
    visits = f(temp_list)
    count = 0
    for vis in visits:
        date_arrival = vis[0]
        date_leave = vis[1]
        if date_arrival < date_leave:
            for day in range(date_arrival, date_leave):
                count += 1
        elif date_arrival > date_leave:
            for day in range(date_arrival, day_in_mounth):
                count += 1
            for day in range(0, date_leave):
                count += 1
    print('Ви перебуваєте в шенгені: ', count, 'днів')
    stay_day = shengen_constraint - count
    if count < shengen_constraint:
        print('Ліміт перебування в шенгені 180 днів, у вас залишилось: ', stay_day)
    else:
        print('Ви прострочили ліміт перебування в шенгені: ', stay_day)

loops_in_test(temp_list)

while True:
    print('Виберіть дію: ')
    print('a) Вивести всі візити;\n'
          'b) Порахувати кількість днів в шенгені;\n'
          'с) Додати новий візит\n')
    choiсe = input()
    if choiсe == 'a':
        print_all_visits()
    elif choiсe == 'b':
        count_day_in_shengen(visits, day_in_mounth, schengen_constraint)
    elif choiсe == 'c':
        add_visits()

