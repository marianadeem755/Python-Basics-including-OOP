class Math:
    def __init__(self, num):
        self.num=num
    def show(self, n):
        self.num=self.num+n
        print(f"The show method shows that it has value {self.num}")
    @staticmethod
    def add(a,b):
        return a+b
a=Math(52)
print(a.num)
a.show(34)
print(Math.add(45,89))
        