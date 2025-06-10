class NegativeError(Exception):
    pass


def area(len, bre):
    if len >= 0 and bre >= 0:
        return len * bre
    else:
        raise NegativeError("-ve dimensions not allowed!!")


try:
    print(area(2, 5))
except NegativeError as ne:
    print(ne)
