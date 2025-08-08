class Animal:
    def __init__(self, name: str,
                 appetite: int,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry
    #     self.__repr__()

    # def __repr__(self) -> None:
    #     return self.name

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry is True:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        else:
            return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, is_hungry)
        if is_hungry is True:
            self.appetite = 3
        else:
            self.appetite = 0

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, is_hungry)
        if is_hungry is True:
            self.appetite = 7
        else:
            self.appetite = 0

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    return sum(animal.feed() for animal in animals)
