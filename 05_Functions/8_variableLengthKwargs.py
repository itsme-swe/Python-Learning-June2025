def myFun(**kwargs):
    for i, val in kwargs.items():
        print(f"{i} : {val}")


myFun(first="defender", second="land cruiser", third="rubicon")

"""
first : defender
second : land cruiser
third : rubicon

"""
