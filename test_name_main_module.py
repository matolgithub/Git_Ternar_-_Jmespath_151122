x = 10


def sum_func(a=[2, 3]) -> int:
    print(sum(a))
    return sum(a)


def glob_func() -> dict:
    glob_var = globals()
    print(glob_var)


def main():
    sum_func()
    glob_func()


main()
