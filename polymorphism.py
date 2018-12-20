class Parent:
    def one(self):
        print("one from parent")

    def two(self):
        print("two from parent")

class Child(Parent):
    def one(self):
        super(Child, self).one()
        print("one from child")

obj = Child()
print(obj.one())
print(obj.two())