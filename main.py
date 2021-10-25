from Logic.general_logic import create
from Tests.test_crud import test_crud
from UserInterface.console import run_ui


def main():
    vanzari = []
    vanzari = create(vanzari, 1, 'Marvel Spider-Man', 'Fiction', 63.5, 'Silver')
    vanzari = run_ui(vanzari)


if __name__ == '__main__':
    test_crud()
    main()