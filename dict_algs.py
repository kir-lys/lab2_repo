#
# Реализуйте в нём следующий алгоритм: 
# i. есть несколько сотрудников, описанных в виде массива словарей
#  emps (данные приведены ниже в конце этого раздела) 
# ii. выведите имена тех сотрудников, у которых есть дети старше 18  лет 
#

ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 12,
    }, {
        "name": "petja",
        "age": 10,
    }],
}
darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    }, {
        "name": "pavel",
        "age": 15,
    }],
}
emps = [ivan, darja]

# ii. выведите имена тех сотрудников, у которых есть дети старше 18  лет 
for e in emps:
    if e.get("children") == None:
        continue
    else:
        for ch in e.get("children"):
            if ch == None:
                continue
            elif ch["age"] >= 18:
                print(e["name"])
                break
