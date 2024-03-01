global_var=20

def myfun():
    local=10
    print(local)
    print(global_var)

myfun()

xy=200
def cool():
    xy=100
    print(xy)
cool()

def A():
    global x
    x=150
    print(x)
A()
