g = 20.5

print("Global: ", g)


def fun():
    global g
    a = 10
    g = 200

    print("local: ", a)
    print("local: ", g)


fun()

print("Modified global variable:", g)

"""
Global:  20.5
local:  10
local:  200
Modified global variable: 200

"""

# 💥 To modify the global varibale inside function scope we need to use ref. "global" inside function
