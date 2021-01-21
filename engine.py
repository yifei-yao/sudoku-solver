# sudoku solver using brute-force (backtracking) algorithm
import copy


# brute-force the result using recursion
def solve(qz):
    next_one = get_next(qz)
    if next_one:
        options1 = options(qz, next_one)
        while len(options1) > 0:
            qzc = copy.deepcopy(qz)
            qzc[next_one[0]][next_one[1]] = options1.pop()
            returned = solve(qzc)
            if returned:
                return returned
        return False
    else:
        return qz


# find the position of the next empty cell
def get_next(qz):
    for i in range(9):
        for j in range(9):
            if qz[i][j] == 0:
                return i, j
    return None


# return a set of possible numbers (1-9) for a cell
def options(qz, tp):
    set1 = set()
    x = tp[0]
    y = tp[1]
    # check horizontally
    for i in qz[x]:
        set1.add(i)
    # check vertically
    for i in range(9):
        set1.add(qz[i][y])
    # check numbers in the 3x3 group
    for i in range(x // 3 * 3, x // 3 * 3 + 3):
        for j in range(y // 3 * 3, y // 3 * 3 + 3):
            set1.add((qz[i][j]))
    return {i for i in range(1, 10) if i not in set1}
