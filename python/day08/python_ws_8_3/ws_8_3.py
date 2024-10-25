# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0


class Dog(Animal):
    def __init__(self):
        Animal.num_of_animal += 1

    def bark(self):
        print('멍멍!')


class Cat(Animal):
    def __init__(self, sound):
        Animal.num_of_animal += 1
        self.sound = sound

    def meow(self):
        print(f'{self.sound} !')


class Pet(Dog, Cat):
    @classmethod
    def access_num_of_animal(cls):
        num = cls.num_of_animal
        return f'동물의 수는 {num}마리 입니다.'


cat1 = Cat("야옹")
cat1.meow()
