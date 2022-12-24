def decorator(func):
    def inner():
        print("I'm decorating")
        func()
        print("finished!")
    return inner

@decorator
def hello_world():
    print("hello world!")

hello_world()



def smart_devide(func):
    def inner(a,b):
        print("deviding")
        if b==0:
            print("Deviding is impossible.")
        else:
            func(a,b)
    return inner

@smart_devide
def devider(a,b):
    print(a/b)

devider(15,5)
devider(15,0)


def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner


@star
@percent
def printer(msg):
    print(msg)

printer("Hello")