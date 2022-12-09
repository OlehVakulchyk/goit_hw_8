from datetime import datetime, timedelta
def get_birthdays_per_week(users):  # дні народження наступного тижня
    

    bithdays_next_week = {0:['Monday', []], 1:['Tuesday', []], 2:['Wednesday', []],
                          3:['Thursday', []], 4:['Friday',  []]}
    current_datetime = datetime.now()
#    print(f'current_datetime = {current_datetime}', type(current_datetime))
    current_date = current_datetime.date()
#    print(f'current_date = {current_date}')
    to_saturday = 5 - current_datetime.weekday()  # залишилось до настунної суботи(int)
#    print(f'to_saturday = {to_saturday}')
    this_saturday = current_datetime + timedelta(days=to_saturday)
#    print(f'this_saturday = {this_saturday.date()}')
    next_saturday = this_saturday + timedelta(days=7)
    for di in users:
        bd = di['bithday']
        bithday_this_year = datetime(current_datetime.year, bd.month, bd.day)
        if this_saturday.date() <= bithday_this_year.date() < next_saturday.date():
            if bithday_this_year.weekday() > 4:
                bithdays_next_week[0][1].append(di['name'])
            else:
                bithdays_next_week[bithday_this_year.weekday()][1].append(di['name'])
    for key in bithdays_next_week:
        if bithdays_next_week[key][1]:
            print(bithdays_next_week[key][0].ljust(10) + ':', end=' ')
            for i in range(len(bithdays_next_week[key][1]) - 1):
                print(bithdays_next_week[key][1][i], end=', ')
            print(bithdays_next_week[key][1][len(bithdays_next_week[key][1]) - 1])
        

users = [{'name': 'Ol', 'bithday': datetime(1965, 12, 10)},
         {'name': 'Ole', 'bithday': datetime(1965, 12, 11)},
         {'name': 'Oleg', 'bithday': datetime(1976, 12, 12)},
         {'name': 'Olegg', 'bithday': datetime(1965, 12, 15)},
         {'name': 'Olegv', 'bithday': datetime(1986, 12, 14)},
         {'name': 'Olegp', 'bithday': datetime(1965, 12, 15)},
         {'name': 'Olegvp', 'bithday': datetime(2005, 12, 15)}
        ]

get_birthdays_per_week(users)
