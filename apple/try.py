class Person:

    count = 0

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self, food):
        print('%d岁的%s正在吃%s！' % (self.age, self.name, food))

    def play(self, something):
        print('%d岁的%s正在玩%s这个东西！' % (self.age, self.name, something))

    def by(self, traffic):
        print('%d岁的%s正在乘坐%s玩耍！' % (self.age, self.name, traffic))

    def where(self, place):
        print('%d岁的%s正在%s旅游！' % (self.age, self.name, place))


p1 = Person('张恒', 26, '男')


