from inspect import _void

class Person:

    def __init__(self, name: str, age: int, height: float):
        self._name = name
        self._age = age
        self._height = height

    def __lt__ (self, other: object) -> bool:
        return (self._age < other._age and self._height < other._height)

    def __gt__ (self, other: object) -> bool:
        return (self._age > other._age and self._height > other._height)

    def __eq__ (self, other: object) -> bool:
        return (self._name == other._name and self._age == other._age and self._height == other._height)
    
    def __ne__ (self, other: object) -> bool:
        return (self._name != other._name or self._age != other._age or self._height != other._height)

    def __add__(self, other) -> object:
        return Person(self._name + ' '+ other._name, 
                      self._age + other._height, 
                      self._height + other._height)

    def __str__ (self) -> str:
        return self._name

    def show (self) -> _void:
        print(f'{self._name}\t{self._age}\t{self._height}')






