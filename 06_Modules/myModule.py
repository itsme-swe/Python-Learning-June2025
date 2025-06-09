data = 500


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


# 💥 Use to restrict the data of one module

if __name__ == "__main__":

    print(f"Sum is: {add(20 ,20)}")

    print(f"Diff is: {sub(50, 20)}")

    print("Name:", __name__)  # Name: __main__
