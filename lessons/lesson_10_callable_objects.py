class A:
    def __init__(self, parameter):
        self.parameter = parameter

    def __call__(self, number):
        return number ** self.parameter


a = A(10)
a(5)

b = A(5)
b(10)