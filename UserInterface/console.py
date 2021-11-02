from Domain.Vanzare import get_string, creeaza_carte, get_title, get_genre, get_price, get_sale
from Logic.ascending_sort_1 import asc_sort
from Logic.general_logic import create, update, delete, read
from Logic.modify_genre import modify_g
from Logic.modify_prices import modify_prices


def show_menu():
    print('1. CRUD')
    print('2. Reducere pret pentru clientii cu silver si gold')
    print('3. Modificarea genului pentru un titlu dat')
    print('5. Ordonarea vanzarilor crescator dupa pret')
    print('x. Exit')


def handle_add(vanzari):
    try:
        id_vanzare = int(input("Dati id-ul vanzarii: "))
    except ValueError as ve:
        print('Eroare, id-ul introdus nu este un numar valid! Detalii: ', ve)
        return vanzari

    nume = input("Dati numele cartii ce urmeaza a fi pusa in vanzare: ")
    gen = input("Introduceti genul cartii: ")
    try:
        pret = float(input("Dati pretul cartii: "))
    except ValueError as ve:
        print('Eroare, nu ati introdus un pret valid! Detalii: ', ve)
        #pret = float(input("Dati pretul cartii: "))
        return vanzari
    reducere = input("Introduceti tipul cardului de fidelitate: ")
    return create(vanzari,id_vanzare, nume, gen, pret, reducere)


def handle_show_all(vanzari):
    for vanzare in vanzari:
        print(get_string(vanzare))


def handle_update(vanzari):
    try:
        id_vanzare = int(input("Dati id-ul vanzarii care se actualizeaza: "))
        nume = input("Dati noul nume al cartii ce urmeaza a fi pusa in vanzare: ")
        gen = input("Introduceti noul gen al cartii: ")
        pret = float(input("Dati noul pret al cartii: "))
        reducere = input("Introduceti tipul cardului de fidelitate: ")
        return update(vanzari, creeaza_carte(id_vanzare, nume, gen, pret, reducere))
    except ValueError as ve:
        print('Eroare:', ve)

    return vanzari


def handle_delete(vanzari):
    try:
        id_vanzare = int(input("Dati id-ul vanzarii care se va sterge: "))
        vanzari = delete(vanzari, id_vanzare)
    except ValueError as ve:
        print('Eroare, ', ve)
    return vanzari


def handle_show_details(vanzari):
    id_vanzare = int(input("Dati id-ul vanzarii pentru care doriti detalii: "))
    vanzare = read(vanzari, id_vanzare)
    print(f'Titlul cartii: {get_title(vanzare)}')
    print(f'Genul cartii: {get_genre(vanzare)}')
    print(f'Pretul cartii: : {get_price(vanzare)}')
    print(f'Tipul reducerii: {get_sale(vanzare)}')


def handle_crud(vanzari):
    while True:
        try:
            print('1. Adaugare')
            print('2. Modificare')
            print('3. Stergere')
            print('a. Afisare')
            print('d. Detalii vanzare')
            print('b. Revenire')

            optiune = input('Optiunea aleasa: ')
            if optiune == '1':
                vanzari = handle_add(vanzari)
            elif optiune == '2':
                vanzari = handle_update(vanzari)
            elif optiune == '3':
                vanzari = handle_delete(vanzari)
            elif optiune == 'a':
                handle_show_all(vanzari)
            elif optiune == 'd':
                handle_show_details(vanzari)
            elif optiune == 'b':
                break
            else:
                print('Optiune invalida.')
        except Exception as ex:
            print('Eroare: ', ex)
    return vanzari


def handle_modify_genre(vanzari):
    try:
        to_modify = input("Dati tilul cartii a carui gen se doreste modificarea: ")
        genre_to_be_replaced_with = input("Introduceti noul gen al cartii")
        vanzari = modify_g(vanzari, to_modify, genre_to_be_replaced_with)
    except ValueError as ve:
        print('Eroare:', ve)
        return vanzari

def handle_ascending_sort(vanzari):
    handle_show_all(asc_sort(vanzari))

def run_ui(vanzari):

    while True:
        try:
            show_menu()
            optiune = input('Optiunea aleasa: ')
            if optiune == '1':
                vanzari = handle_crud(vanzari)
            elif optiune == '2':
                vanzari = modify_prices(vanzari)
            elif optiune == '3':
                vanzari = handle_modify_genre(vanzari)
            elif optiune == '5':
                handle_ascending_sort(vanzari)
            elif optiune == 'x':
                break
            else:
                print('Optiune invalida.')
        except Exception as ex:
            print('Eroare: ', ex)

    return vanzari

