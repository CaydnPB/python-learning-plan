class Animal:
    def __init__(self, name, sound):
        self._name = name
        self._sound = sound

    def make_sound(self):
        pass

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_sound(self):
        return self._sound

    def set_sound(self, sound):
        self._sound = sound


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")

    def make_sound(self):
        return f"{self.get_name()} says {self.get_sound()}"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

    def make_sound(self):
        return f"{self.get_name()} says {self.get_sound()}"


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name, "Tweet")

    def make_sound(self):
        return f"{self.get_name()} sings {self.get_sound()}"

def animal_sounds(animal):
    print(animal.make_sound())

def check_animal_type(animal):
    if isinstance(animal, Animal):
        print(f"{animal.get_name()} is an instance of Animal")
    elif isinstance(animal, Dog):
        print(f"{animal.get_name()} is an instance of Dog")
    elif isinstance(animal, Cat):
        print(f"{animal.get_name()} is an instance of Cat")
    elif isinstance(animal, Bird):
        print(f"{animal.get_name()} is an instance of Bird")
    else:
        print("Unknown animal type")

dog = Dog("Clifford")
cat = Cat("Garfield")
bird = Bird("Twitter")

animal_sounds(dog)
animal_sounds(cat)
animal_sounds(bird)

check_animal_type(dog)
check_animal_type(cat)
check_animal_type(bird)

print(f"Before Setting: {dog.get_name()} says {dog.get_sound()}")
dog.set_name("Dogbert")
dog.set_sound("Bark")
print(f"After Setting: {dog.get_name()} says {dog.get_sound()}")