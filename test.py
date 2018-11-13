# import itertools
# day_in_mounth = 30
# schengen_constraint = 180
# shengen_time = list()
# visities = list()
# temp_list = list()
# visits = list()
# arr = list()
#
#
# with open('time_in_shengen.txt') as doc:
#     for visit in doc:
#         temp_list += visit.split()
# for i, item in enumerate(temp_list):
#     temp_list[i] = int(item)
# def f(lst):
#     return [lst[i:i + 2] for i in range(0, len(lst), 2)]
#
# print(visities)
# def count_day_in_shengen(visits, day_in_mounth, shengen_constraint):
#     visits = f(temp_list)
#     count = 0
#     for vis in visits:
#         date_arrival = vis[0]
#         date_leave = vis[1]
#         if date_arrival < date_leave:
#             for day in range(date_arrival, date_leave):
#                 count += 1
#         elif date_arrival > date_leave:
#             for day in range(date_arrival, day_in_mounth):
#                 count += 1
#             for day in range(0, date_leave):
#                 count += 1
#     print('Ви перебуваєте в шенгені: ', count, 'днів')
#     stay_day = shengen_constraint - count
#     if count < shengen_constraint:
#         print('Ліміт перебування в шенгені 180 днів, у вас залишилось: ', stay_day)
#     else:
#         print('Ви прострочили ліміт перебування в шенгені: ', stay_day)
#
# count_day_in_shengen(temp_list, day_in_mounth, 180)


def add_visits():
    a = int(input('Введіть початок поїздки: '))
    b = int(input('Введіть кінець поїздки: '))
    print(a+b)


def tralal():
    print('Hello world')


func_table = {
    'a': add_visits,
    'b': tralal
}

while True:
    user_input = input()
    func = func_table.get(user_input)
    if func is None:
        continue
    else:
        func()

