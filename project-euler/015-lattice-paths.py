GRID_SIZE = 20
grid_paths = (GRID_SIZE + 1) * [None]

for i in range(0, GRID_SIZE + 1):
    grid_paths[i] = (GRID_SIZE + 1) * [None]


def init_path_nums():
    for i in range(0, GRID_SIZE):
        grid_paths[i][GRID_SIZE] = 1
        grid_paths[GRID_SIZE][i] = 1


def calc_path_nums():
    for i in range(19, -1, -1):
        for j in range(GRID_SIZE - 1, -1, -1):
            grid_paths[i][j] = grid_paths[i + 1][j] + grid_paths[i][j + 1]


def main():
    init_path_nums()
    calc_path_nums()
    print 'Number of paths at start is %s' % grid_paths[0][0]


if __name__ == '__main__':
    main()
