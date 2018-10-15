import sys
from collections import Counter

input_file = sys.argv[1]


def get_first_common_element(x, y):
    for w in x:
        if w in y:
            return w
    return None

days_list = []
match_list = []
players_list = []
home = []
away = []
lista1 = []
lista2 = []

with open(input_file, 'r') as i:
    lines_list = i.readlines()

for i in lines_list:
    for k in i:
        if k != ' ' and k != '\n':
            players_list.append(k)

days_of_tournament = Counter(players_list).values()
days_of_tournament = int(max(days_of_tournament)) + 2

home = players_list[::2]
away = players_list[1::2]

players_list = sorted(list(set(players_list)))

for i in range(0, len(players_list)):
    new = []
    for j in range(0, days_of_tournament):
        new.append(j)
    days_list.append(new + [i])

for i in home:
    for j in players_list:
        if j == i:
            k = j
    id1 = players_list.index(k)
    lista1.append(id1)

for i in away:
    for j in players_list:
        if j == i:
            k = j
    id1 = players_list.index(k)
    lista2.append(id1)

for f, b in zip(lista1, lista2):
    day_var = get_first_common_element(days_list[f], days_list[b])
    match_list.append(((home[lista1.index(f)], away[lista2.index(b)]), day_var))
    for i in days_list:
        for j in i:
            if (days_list.index(i) == f or days_list.index(i) == b) and j == day_var:
                i.remove(j)

for i in match_list:
    print i
