
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("汪汪汪！！！")

class Cat(Animal):
    def make_sound(self):
        print("喵喵喵！！！")

class Bird(Animal):
    def make_sound(self):
        print("啾啾啾！！！")

if __name__ == '__main__':
    # 创建动物对象及调用动物的方法
    dog = Dog("小黑", 5)
    dog.make_sound()

    cat = Cat("小美", 4)
    cat.make_sound()

    bird = Bird("鹦鹉八乖", 2)
    bird.make_sound()
