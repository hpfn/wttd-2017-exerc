# coding=utf-8
def tower_builder(n_floors):
    # this first part: does not need all this
    # (n_floors * 2) - 1
    list_odd = list()
    count = 1
    while len(list_odd) < n_floors:
        if count % 2 != 0:
            list_odd.append(count)
        count += 1

    tam_str = list_odd[-1]
    final = [' ' * i +
             '*' * (tam_str - (i*2)) +
             ' ' * i
             for i in range(n_floors)]

    final.reverse()
    return final
