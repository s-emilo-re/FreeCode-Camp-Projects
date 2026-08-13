def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    states = [f"{rods[0]} {rods[1]} {rods[2]}"]

    def move(src, dst):
        rods[dst].append(rods[src].pop())
        states.append(f"{rods[0]} {rods[1]} {rods[2]}")

    def hanoi(n, src, dst, aux):
        if n == 0:
            return
        hanoi(n - 1, src, aux, dst)
        move(src, dst)
        hanoi(n - 1, aux, dst, src)

    hanoi(n, 0, 2, 1)
    return "\n".join(states)