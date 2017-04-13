from commons import coroutine


ASCII_ALPHA_START = 65


@coroutine
def calculate_score():
    score = None
    while True:
        name, pos = yield (score)
        vals = [(ord(c) - ASCII_ALPHA_START + 1)for c in name]
        score = reduce(lambda x, y: x + y, vals, 0) * pos


def read_file_split(path):
    f = open(path)
    content = f.read()
    return [n.replace('"', '') for n in content.split(',')]


def main():
    names = read_file_split('022-names-scores-input')
    names.sort()
    c = calculate_score()
    total_sum = 0
    for i, name in enumerate(names, 1):
        total_sum += c.send((name, i))
    print 'Total sum %s' % total_sum


if __name__ == "__main__":
    main()
