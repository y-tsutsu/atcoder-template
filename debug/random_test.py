from random import randint


def write_one(f, a): print(a, file=f)
def write_multi(f, *a): print(f'{" ".join([str(x) for x in a])}', file=f)
def write_list_spase(f, a): print(f'{" ".join([str(x) for x in a])}', file=f)
def write_list_nline(f, a): print(f'{"\n".join([str(x) for x in a])}', file=f)
def print_one(a): print(a)
def print_multi(*a): print(f'{" ".join([str(x) for x in a])}')
def print_list_spase(a): print(f'{" ".join([str(x) for x in a])}')
def print_list_nline(a): print(f'{"\n".join([str(x) for x in a])}')


def make_random_test_in():
    # TODO
    a, b = randint(1, 100), randint(1, 100)
    return a, b


def make_random_test_in_file():
    ret = {}
    for val in range(90, 100):
        t = make_random_test_in()
        ret[val] = t
        with open(f'in_{val}.txt', 'w') as f:
            # TODO
            a, b = t
            write_one(f, a)
            write_one(f, b)
    return ret


def make_random_test_out(t):
    # TODO
    a, b = t
    return a + b


def make_random_test_out_file(indata):
    for val in range(90, 100):
        ret = make_random_test_out(indata[val])
        with open(f'out_{val}.txt', 'w') as f:
            # TODO
            write_one(f, ret)


def make_random_test_file():
    indata = make_random_test_in_file()
    make_random_test_out_file(indata)


def do_random_test_online(solve, count=1000):
    for _ in range(count):
        indata = make_random_test_in()
        outdata0 = make_random_test_out(indata)
        outdata1 = solve(*indata)
        if outdata0 != outdata1:
            # TODO
            print('random in:')
            print_list_nline(indata)
            print('random out:')
            print_one(outdata0)
            print('solve:')
            print_one(outdata1)
            print()


def main():
    make_random_test_file()


if __name__ == '__main__':
    main()
