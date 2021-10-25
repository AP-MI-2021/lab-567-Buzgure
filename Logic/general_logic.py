from Domain.Vanzare import creeaza_carte, get_id, get_sale, get_title, get_genre, get_price


def create(lst_vanzari,
           id_vanzare: int, titlu_carte: str, gen_carte: str, pret: float, reducere_client: str):
   """

   :param lst_vanzari: lista de vanzari.
   :param id_vanzare: id-ul vanzarii
   :param titlu_carte: titlul cartii din vanzarea curenta
   :param gen_carte: genul cartii
   :param pret: pretul cartii
   :param reducere_client: tipul reducerii
   :return: o lista formata din lst_vanzari si o noua vanzare adaugata
   """

   vanzare = creeaza_carte(id_vanzare, titlu_carte, gen_carte, pret, reducere_client)
   return lst_vanzari + [vanzare]


def read(lst_vanzari, id_vanzare):
   """
   Citeste o vanzare
   :param lst_vanzari:lista de vanzari
   :param id_vanzare: id-ul vanzarii
   :return: vanzarea cu id-ul id_vanzare sau lista cu vanzari daca id_vanzare = None
   """
   check_vanzare = None
   for vanzari in lst_vanzari:
      if get_id(vanzari) == id_vanzare:
         check_vanzare = vanzari

   if check_vanzare:
      return check_vanzare
   return lst_vanzari


def update(lst_vanzari, new_vanzare):
   """
   Actualizeaza o vanzare existenta
   :param lst_vanzari: lista de vanzari
   :param new_vanzare: vanzarea care se va actualiza, folosind id-ul
   :return: o lista ce contine vanzarea actualizata
   """
   new_list = []
   for vanzare in lst_vanzari:
      if get_id(vanzare) != get_id(new_vanzare):
         new_list.append(vanzare)
      else:
         new_list.append(new_vanzare)

   return new_list


def delete(lst_vanzari, id_vanzare):
   """
   Sterge o vanzare existenta din lista
   :param lst_vanzari: lista de vanzari
   :param id_vanzare: id-ul vanzarii care urmeaza a fi stearsa
   :return: lista cu vanzari fara vanzarea cu id-ul id_vanzare
   """
   new_list = []
   for vanzare in lst_vanzari:
      if get_id(vanzare) != id_vanzare:
         new_list.append(vanzare)
   return new_list

def apply_discount_silver(price):
   """
   Calculeaza pretul dupa o reducere de 5%
   :param price: pretul initial
   :return: pretul redus
   """
   discount = 5 * price / 100
   return price - discount

def apply_discount_gold(price):
   """
    Calculeaza pretul dupa o reducere de 10%
    :param price: pretul initial
    :return: pretul redus
    """
   discount = 10 * price / 100
   return price - discount


def modify_prices(lst_vanzari):
   """
   Modifica pretul vanzarilor in functie de tipul de reducere aplicat fiecareia
   :param lst_vanzari: lista de vanzari
   :return: lst_vanzari dupa aplicarea discount-urilor
   """

   for vanzare in lst_vanzari:
      reducere = get_sale(vanzare)
      id = get_id(vanzare)
      nume = get_title(vanzare)
      gen = get_genre(vanzare)
      price = get_price(vanzare)
      if reducere == 'Silver':
         lst_vanzari = update(lst_vanzari, creeaza_carte(id, nume, gen, apply_discount_silver(price), 'None'))
      elif reducere == 'Gold':
         lst_vanzari = update(lst_vanzari, creeaza_carte(id, nume, gen, apply_discount_gold(price), 'None'))
   return lst_vanzari