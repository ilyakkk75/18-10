import random

class car:
    def __init__(self, color, cost, owner):
        self.__number = random.randint(100, 999)
        self.color = color
        self.cost = cost
        self.owner = owner

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        if value < 0:
            raise ValueError("стоимость машины не может быть отрицательной")
        self._cost = value

    def change_owner(self, new_owner):
        self.owner = new_owner

    def change_color(self, new_color):
        self.color = new_color

    def get_info(self):
        return (
            f"номер: {self.__number}"
            f"цвет: {self.color}\n"
            f"стоимость: {self.cost}"
            f"владелец: {self.owner}"
        )

car1 = car("красный", 1500000, "иван")
car2 = car("синий", 800000, "мария")
car3 = car("белый", 50000, "петр")

car1.change_color("зеленый")
car1.cost = 1200000
car1.change_owner("алексей")

try:
    car2.cost = -100
except ValueError as e:
    print(f"попытка установить отрицательную цену для второй машины: {e}")

print("информация о машинах:")
print(f' машина 1: {car1.get_info()}')
print(f'машина 2: {car2.get_info()}')
print(f'машина 3: {car3.get_info()}')