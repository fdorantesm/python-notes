class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age
        
    def __repr__(self) -> str:
        return f'Human(name={self.__name}, age={self.__age})'
        
john = Human('John', 30)

print(john.get_age())