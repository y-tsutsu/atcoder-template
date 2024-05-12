from random import randint


def write_one(f, a): f.write(f'{a}\n')
def write_multi(f, *a): f.write(f'{" ".join([str(x) for x in a])}\n')
def write_list_spase(f, a): f.write(f'{" ".join([str(x) for x in a])}\n')
def write_list_nline(f, a): f.write(f'{"\n".join([str(x) for x in a])}\n')


def make_random_test_in():
    def inner():
        # TODO
        a, b = randint(1, 100), randint(1, 100)
        return a, b

    ret = {}
    for val in range(90, 100):
        a, b = inner()
        ret[val] = a, b  # TODO
        with open(f'in_{val}.txt', 'w') as f:
            write_one(f, a)
            write_one(f, b)
    return ret


def make_random_test_out(indata):
    def inner(t):
        # TODO
        a, b = t
        return a + b

    for val in range(90, 100):
        ret = inner(indata[val])
        with open(f'out_{val}.txt', 'w') as f:
            write_one(f, ret)


def main():
    indata = make_random_test_in()
    make_random_test_out(indata)


if __name__ == '__main__':
    main()
