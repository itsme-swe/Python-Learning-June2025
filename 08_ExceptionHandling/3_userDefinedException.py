class NegativeError(Exception):

    def __init__(self):
        self.msg = "-ve dimensions not allowed!!"

    def __str__(self):
        return self.msg


def area(len, bre):
    if len >= 0 and bre >= 0:
        return len * bre
    else:
        raise NegativeError()


try:
    print(area(-5, 5))
except NegativeError as ne:
    print(ne)

# op:  -ve dimensions not allowed!!
