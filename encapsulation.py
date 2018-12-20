class Hello:
    def __init__(self):
        self.__a = 10

    def get_a(self):
        print("get value:",self.__a)

    def set_a(self,b):
        self.__a = b
        print("set value:",self.__a)




obj = Hello()
(obj.get_a())
obj.set_a(20)
(obj.get_a())