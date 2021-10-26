from Logic.general_logic import create
from Tests.test_crud import test_crud
from Tests.test_modify_prices import test_modify_prices
from UserInterface.console import run_ui


def main():
    vanzari = []
    vanzari = run_ui(vanzari)


if __name__ == '__main__':
    test_crud()
    test_modify_prices()
    main()