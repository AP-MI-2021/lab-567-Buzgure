from Domain.Vanzare import get_price


def asc_sort(vanzari):
    return sorted(vanzari, key=get_price)
