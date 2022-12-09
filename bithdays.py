from datetime import datetime, timedelta


def get_birthdays_per_week(users):  # дні народження наступного тижня

    bithdays_next_week = {0: ['Monday', []], 1: ['Tuesday', []], 2: ['Wednesday', []],
                          3: ['Thursday', []], 4: ['Friday',  []]}
    current_datetime = datetime.now()

    current_date = current_datetime.date()

    # залишилось до настунної суботи(int)
    to_saturday = 5 - current_datetime.weekday()

    this_saturday = current_datetime + timedelta(days=to_saturday)

    next_saturday = this_saturday + timedelta(days=7)
    for di in users:
        bd = di['bithday']
        bithday_this_year = datetime(current_datetime.year, bd.month, bd.day)
        if this_saturday.date() <= bithday_this_year.date() < next_saturday.date():
            if bithday_this_year.weekday() > 4:
                bithdays_next_week[0][1].append(di['name'])
            else:
                bithdays_next_week[bithday_this_year.weekday()][1].append(
                    di['name'])
    for value in bithdays_next_week.values():
        if value[1]:
            print(value[0].ljust(10) + ':', end=' ')
            for i in range(len(value[1]) - 1):
                print(value[1][i], end=', ')
            print(value[1][len(value[1]) - 1])


users = [{'name': 'Ol', 'bithday': datetime(1965, 12, 10)},
         {'name': 'Ole', 'bithday': datetime(1965, 12, 11)},
         {'name': 'Oleg', 'bithday': datetime(1976, 12, 12)},
         {'name': 'Olegg', 'bithday': datetime(1965, 12, 15)},
         {'name': 'Olegv', 'bithday': datetime(1986, 12, 14)},
         {'name': 'Olegp', 'bithday': datetime(1965, 12, 15)},
         {'name': 'Olegvp', 'bithday': datetime(2005, 12, 15)}
         ]

get_birthdays_per_week(users)
