from Practice1.abstract_object import Employee
from Practice1.util import calculate_age


class EmployeeBasic(Employee):
    name: str  # employee's name
    surname: str  # employee's surname
    birthday: str  # employee's date of birthday
    age: int  # employee's age
    position: str  # employee's position
    salary: int  # employee's salary
    experience: int  # employee's experience of work

    def __init__(self, name: str, surname: str, birthday: str,
                 experience: int, position: str = "-", salary: int = 0) -> None:
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.age = calculate_age(self.birthday)
        self.position = position
        self.salary = salary
        self.experience = experience

    def get_message(self) -> str:
        """Prints message by employee's age and experience

        :return: (str) string with message by employee's age and experience
        """
        if self.age >= 50 and self.experience >= 2:
            self.position = "Ментор з підготовки молодих спеціалістів"
            self.salary = 195000
            return f"{self.name} {self.surname}, у нас для Вас є вакансія Ментору з підготовки молодих спеціалістів"

        elif self.age >= 35 and self.experience >= 5:
            self.position = "Team Lead"
            self.salary = 200000
            return f"{self.name} {self.surname}, у нас для Вас є вакансія Team Lead з окладом 2000000 грн"

        elif self.age >= 18 and self.experience >= 5:
            self.position = "Senior Python Developer"
            self.salary = 190000
            return f"{self.name} {self.surname}, у нас для Вас є вакансія Senior Python Developer з окладом 190000 грн"

        elif self.age >= 18 and self.experience >= 2:
            self.position = "Middle Python Developer"
            self.salary = 120000
            return f"{self.name} {self.surname}, у нас для Вас є вакансія Middle Python Developer з окладом 190000 грн"

        elif self.age >= 18 and self.experience >= 0:
            self.position = "Junior Python Developer"
            self.salary = 45000
            return f"{self.name} {self.surname}, у нас для Вас є вакансія Junior Python Developer з окладом 190000 грн"

        else:
            return f"{self.name} {self.surname}, нажаль у нас не має для Вас пропозицій."

    def get_info(self) -> str:
        """Prints employee's info

        :return: (str) string with short info
        """
        return (f"Employee: {self.name} {self.surname}\n"
                f"Birthday: {self.birthday} ({self.age} y.o.)\n"
                f"Experience: {self.experience} y.\n"
                f"Position: {self.position}\n"
                f"Salary: {self.salary}")

    def __repr__(self) -> str:
        """Represents class Employee

        :return: (str) short string with the class arguments
        """
        return (f"Employee({self.name}, {self.surname}, "
                f"{self.birthday}, {self.experience}, {self.position}, {self.salary})")


class Employee(EmployeeBasic):
    __experience: int

    @property
    def experience(self):
        """Getter для атрибута experience"""
        return self.__experience

    @experience.setter
    def experience(self, value):
        """Setter для атрибута experience з забороною помилкових значень"""
        if type(value) is not int:
            raise TypeError("Experience must be type int")
        elif value < 0 or value >= self.age:
            raise ValueError("Experience must be 0 or more and less than employee's age")
        else:
            self.__experience = value

    def __eq__(self, other):
        """Метод порівняння в ПР3-6 двох об'єктів для пошуку збігу"""
        return (self.surname == other.surname and
                self.name == other.name and
                self.birthday == other.birthday and
                self.position == other.position and
                self.salary == other.salary and
                self.experience == other.experience)

    def __le__(self, other):
        """Метод визначення меншого в ПР3-6 з двох об'єктів для впорядкування"""
        return (self.surname, self.name, self.birthday, self.position, self.salary, self.experience) \
            <= (other.surname, other.name, other.birthday, other.position, other.salary, other.experience)

    def __ge__(self, other):
        """Метод визначення більшого в ПР3-6 з двох об'єктів для впорядкування"""
        return (self.surname, self.name, self.birthday, self.position, self.salary, self.experience) \
            >= (other.surname, other.name, other.birthday, other.position, other.salary, other.experience)
