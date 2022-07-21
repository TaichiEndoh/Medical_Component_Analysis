import itertools

def make_department_list(check_masuta,department_name):
    check_m = check_masuta[department_name]
    count=0
    department_list = []
    for k, g in itertools.groupby(check_m):
        count +=1
        department_list.append(k)
    return department_list