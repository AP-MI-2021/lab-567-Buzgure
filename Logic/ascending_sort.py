from Domain.Vanzare import get_price, get_id, creeaza_carte
from Logic.general_logic import read, update


def list_prices(vanzari):
    list = []
    for vanzare in vanzari:
        price = get_price(vanzare)
        list.append(price)
    list.sort()
    return list


def list_id_ascending(vanzari):
    list_id = []
    index = 0
    list = list_prices(vanzari)
    while index < len(list):
        for vanzare in vanzari:
            if index < len(list) and get_price(vanzare) == list[index]:
                list_id.append(get_id(vanzare))
                index += 1
    return list_id

def get_data():
    return [
        creeaza_carte(1, 'b1','g1', 30.0, 'None'),
        creeaza_carte(2, 'b2', 'g2', 23.89, 'Silver'),
        creeaza_carte(3,'b3','g3',29,'None'),
        creeaza_carte(4,'b4','g4',30,'Gold'),
        creeaza_carte(5,'b5','g5',100.50,'Gold'),
        creeaza_carte(6,'b6','g6',10,'None'),



    ]

test_list = get_data()
print(list_id_ascending(test_list))
