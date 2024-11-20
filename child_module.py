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
