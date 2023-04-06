import sys
sys.setrecursionlimit(10000)

f = open(r"C:\Users\Halim\OneDrive\Рабочий стол\Олимпиадки\Тесты к задачам и мои заметки\Компания ХХХ\input_s1_11.txt")
iter = 0
line = ""

workers = {}
relationships = {}

list_rez = []
list_temp = []


def recursion(list_temp):
    list_temp = list_temp[:]
    i, j = 0, 0

    for i in range(len(list_temp)):
        list_temp = list_temp[:]
        list_rez.append(list_temp[i])
        if list_temp[i] in relationships.keys():
            for j in range(len(relationships[list_temp[i]])):
                list_temp.append(relationships[list_temp[i]][j])

    list_temp = list_temp[i+1:]
    if list_temp != []:
        return recursion(list_temp)
    else:
        return list_rez


def workers_add():
    if len(line) == 4 and id not in workers.keys():
        workers[id] = "Unknown Name"
    elif len(line) > 4:
        workers[id] = line[5:]


def relationships_add():
    if iter % 2 == 1 and id_boss not in relationships.keys():  # руководитель
        relationships[id_boss] = []
    elif iter % 2 == 0:  # подчинённый, если подчинённый явл чьим-то руководителем, то из его списка добавить подчинённых ещё и к руководителю, тогда не надо будет рекурсию делать
        relationships[id_boss].append(id_worker)


while True:
    iter += 1
    line = f.readline()
    line = line[:len(line) - 1]  # убрал \n
    line = line.rstrip()
    if line == "END":
        break

    if iter % 2 == 1:
        id_boss = line[:4]
    elif iter % 2 == 0:
        id_worker = line[:4]
    id = line[:4]

    workers_add()
    relationships_add()


string = f.readline()
if string in workers.values():
    id = list(workers.keys())[list(workers.values()).index(string)]
else:
    id = string
if id in relationships.keys():
    recursion(relationships[id])


if list_rez:
    list_rez.sort()
    for i in range(len(list_rez)):
        print(list_rez[i], workers[list_rez[i]])
else:
    print("NO")