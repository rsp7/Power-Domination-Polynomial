import Polynomial


def is_unimodal(order, polynomial):
    falling = False
    for i in range(order - 1):
        if polynomial[i] < polynomial[i + 1] and falling:
            return False
        elif polynomial[i] > polynomial[i + 1]:
            falling = True
    return True


def main():
    num_graphs = [1, 2, 4, 11, 34, 156, 1044, 12346, 274668]
    for order in range(1, len(num_graphs) + 1):
        with open('order' + str(order) + 'AM.txt') as f:
            for i in range(num_graphs[order - 1]):
                next(f)
                next(f)
                graph = []
                for j in range(order):
                    graph.append([int(x) for x in list(next(f))[:-1]])
                if not is_unimodal(order, Polynomial.calc_polynomial(order, graph)):
                    print('Conjecture failed for graph ' + str(i) + 'of order ' + str(order))
                    return
        print('Conjecture holds for all graphs on ' + str(order) + ' vertices')


main()
