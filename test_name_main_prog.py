from test_name_main_module import *


def prog_main():
    print(globals())
    print(__file__)


if __name__ == "__main__":
    prog_main()
