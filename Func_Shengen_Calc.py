day_in_mounth = 30
visits = [[1, 10], [22, 11], [14, 20], [28, 3]]
schengen_constraint = 180

def add_visits(visits):
    a = int(input('Введіть початок поїздки: '))
    b = int(input('Введіть кінець поїздки: '))
    visits.append([a, b])

def print_all_visits(visits):
    print('Дати ваших поїздкок в шенгені: ')
    i = 1
    for vis in visits:
        print(i, ': ', vis)
        i += 1


def count_day_in_shengen(visits, day_in_mounth, shengen_constraint):
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



while True:
    print('Виберіть дію: ')
    print('a) Вивести всі візити;\n'
          'b) Порахувати кількість днів в шенгені;\n'
          'с) Додати новий візит\n')
    choiсe = input()
    if choiсe == 'a':
        print_all_visits(visits)
    elif choiсe == 'b':
        count_day_in_shengen(visits, day_in_mounth, schengen_constraint)
    elif choiсe == 'c':
        add_visits(visits)

