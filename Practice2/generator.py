from Practice1.employee import Employee
from Practice2.util import generate_birthday
import names
import random


class Generator:
    positions = {'Розробник': 60000,
                 'Інженер з тестування': 75000,
                 'Системний адміністратор': 90000,
                 'Архітектор': 110000,
                 'Менеджер проекту': 120000,
                 'Аналітик даних': 80000,
                 'Інженер з безпеки': 100000,
                 'UX/UI дизайнер': 95000,
                 'Технічний письменник': 70000,
                 'DevOps інженер': 105000}

    def generate_single(self) -> Employee:
        """Generates an instance of the Employee class with random or selected values of each class property

        :return: (Employee) single Employee instance
        """
        name = names.get_first_name()
        surname = names.get_last_name()
        birthday = generate_birthday(1950, 2000)
        position = random.choice(list(self.positions.keys()))
        salary = self.positions.get(position)
        experience = random.randint(0, 6)

        return Employee(name=name, surname=surname, birthday=birthday,
                        position=position, salary=salary, experience=experience)

    def generate_1000(self) -> list:
        """Generates 1000 instances of the Employee class

        :return: (list) list of 1000 instances of the Employee class
        """
        return [self.generate_single() for _ in range(1000)]

    def generate_10_000(self) -> list:
        """Generates 10.000 instances of the Employee class

        :return: (list) list of 10.000 instances of the Employee class
        """
        return [self.generate_single() for _ in range(10000)]


# if __name__ == "__main__":
#     employee = Generator()
#     for _ in range(5):
#         print(employee.generate_single())
#
#     list_1000 = employee.generate_1000()
#     print(len(list_1000))
#     print(list_1000[999])
#
#     list_10_000 = employee.generate_10_000()
#     print(len(list_10_000))
#     print(list_10_000[9999])
