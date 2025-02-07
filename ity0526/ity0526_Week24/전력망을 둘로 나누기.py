def solution(n, wires):
    differ = n
    for i in range(len(wires)):
        pop_wires = wires.copy()
        pop_wires.pop(i)
        first_tree = DFS(wires[i][0], pop_wires)
        second_tree = DFS(wires[i][1], pop_wires)
        differ = min(differ, abs(first_tree - second_tree))

    return differ


def DFS(node, wires):
    count = 1

    for i in range(len(wires)):
        if wires[i][0] == node:
            pop_wires = wires.copy()
            pop_wires.pop(i)
            count += DFS(wires[i][1], pop_wires)

        if wires[i][1] == node:
            pop_wires = wires.copy()
            pop_wires.pop(i)
            count += DFS(wires[i][0], pop_wires)

    return count