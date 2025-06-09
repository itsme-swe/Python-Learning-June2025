def Outer():

    def Inner():
        print("Inner Func")

    print("Outer Func")
    Inner()


Outer()

"""
Outer Func
Inner Func

"""
