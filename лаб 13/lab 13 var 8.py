class CHILD:
    def __init__(self, surname_name, year):
        self.SN = surname_name
        self.Year = year
        self.Age = 0

    def SetAge(self, current_year):
        """Розрахунок віку дитини за поточним роком."""
        self.Age = current_year - self.Year

    def GetAge(self):
        """Повернення віку дитини."""
        return self.Age
from child_module import CHILD

class LAKE:
    def __init__(self, name, continent, area, depth):
        self.name = name
        self.continent = continent
        self.area = area
        self.depth = depth

    def change_area(self, new_area):
        """Зміна площі поверхні."""
        self.area = new_area

    def change_depth(self, new_depth):
        """Зміна глибини."""
        self.depth = new_depth

    def __del__(self):
        print(f"Озеро {self.name} видалено.")

# Основна програма
if __name__ == "__main__":
    # Створення списку озер
    lakes = [
        LAKE("Baikal", "Asia", 31500, 1642),
        LAKE("Superior", "North America", 82100, 406),
        LAKE("Victoria", "Africa", 69485, 84)
    ]

    # Виведення інформації про озера
    for lake in lakes:
        print(f"Озеро: {lake.name}, Континент: {lake.continent}, Площа: {lake.area} км², Глибина: {lake.depth} м")

    # Створення списку дітей
    children = [
        CHILD("Третьяков Євгеній", 2016),
        CHILD("Петренко Марія", 2019),
        CHILD("Іванов Олексій", 2017),
        CHILD("Сидоренко Ганна", 2020)
    ]

    current_year = 2024
    for child in children:
        child.SetAge(current_year)

    # Відбір дітей до першого класу (6-7 років) та дитячого садка (3 роки)
    first_grade = [child for child in children if 6 <= child.GetAge() <= 7]
    kindergarten = [child for child in children if child.GetAge() == 3]

    print("\nДіти до першого класу:")
    for child in first_grade:
        print(f"{child.SN}, Вік: {child.GetAge()}")

    print("\nДіти до дитячого садка:")
    for child in kindergarten:
        print(f"{child.SN}, Вік: {child.GetAge()}")
class CHILD:
    def __init__(self, surname_name, year):
        """Ініціалізує прізвище, ім'я та рік народження."""
        self.SN = surname_name
        self.Year = year
        self.Age = 0

    def SetAge(self, current_year):
        """Розраховує вік дитини на основі поточного року."""
        self.Age = current_year - self.Year

    def GetAge(self):
        """Повертає вік дитини."""
        return self.Age
