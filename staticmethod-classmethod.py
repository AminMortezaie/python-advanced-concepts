class car:
    def __init__(self) -> None:
        pass

    def do_something(self):
        print("do something!")

    @staticmethod
    def do_something_static():
        print("i'm doing staticly.")
    
    @classmethod
    def do_something_classical(cls):
        print("I'm doing classical!")


class other(car):
    def __init__(self) -> None:
        pass

o = other()
o.do_something()