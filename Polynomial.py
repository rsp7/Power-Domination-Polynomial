def gen_sets(order):
    ret = []
    num = 2 ** order
    for i in range(num):
        ret.append([])
        power = num
        rem = i
        for j in range(order):
            power /= 2
            ret[i].append(rem / power)
            rem %= power
    return ret


def is_pds(order, graph, v_set):
    for i in range(order):
        graph[i][-1] = v_set[i]
    for i in range(order):
        if v_set[i] == 1:
            for j in range(order):
                if graph[i][j] == 1:
                    graph[j][-1] = 1
    while True:
        stop = True
        for i in range(order):
            if graph[i][-1] == 1:
                target = -1
                for j in range(order):
                    if graph[i][j] == 1 and graph[j][-1] == 0:
                        if target >= 0:
                            target = -1
                            break
                        target = j
                if target >= 0:
                    stop = False
                    graph[target][-1] = 1
        if stop:
            break
    for i in range(order):
        if graph[i][-1] == 0:
            return False
    return True


def calc_polynomial(order, graph):
    ret = []
    for i in range(order):
        graph[i].append(0)
        ret.append(0)
    for v_set in gen_sets(order):
        size = 0
        for i in range(order):
            size += v_set[i]
        if is_pds(order, graph, v_set):
            ret[size - 1] += 1
    for i in range(order):
        graph[i].pop()
    return ret



