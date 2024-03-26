import pytest
from Practice1.employee import Employee


class TestEmployeeClass:
    """Перевірка базових дій класу Student
    """

    @pytest.fixture
    def init_employee(self):
        """Підготовка до тестів
        """
        return Employee("Name", "Surname", "12.10.2004", 3)

    def test_data_type(self, init_employee):
        """Перевірка відповідності класу"""
        assert isinstance(init_employee, Employee)

    def test_check_init(self, init_employee):
        """Перевірка ініціації й внесення даних
        """
        e = init_employee
        assert e.name == "Name"
        assert e.surname == "Surname"
        assert e.birthday == "12.10.2004"
        assert e.experience == 3

    def test_check_default(self, init_employee):
        """Перевірка значень за замовчуванням
        """
        assert init_employee.position == "-"
        assert init_employee.salary == 0

    def test_get_info(self, init_employee):
        """Перевірка методу get_info()
        """
        assert init_employee.get_info() == ("Employee: Name Surname\n"
                                            "Birthday: 12.10.2004 (19 y.o.)\n"
                                            "Experience: 3 y.\n"
                                            "Position: -\n"
                                            "Salary: 0")

    values_to_try = [(Employee("Name", "Surname1", "01.01.1956", 5),
                      "Ментор з підготовки молодих спеціалістів", 195000),
                     (Employee("Name", "Surname2", "12.04.1986", 6),
                      "Team Lead", 200000),
                     (Employee("Name", "Surname3", "18.10.1996", 5),
                      "Senior Python Developer", 190000),
                     (Employee("Name", "Surname4", "22.04.2002", 3),
                      "Middle Python Developer", 120000),
                     (Employee("Name", "Surname5", "06.05.2004", 0),
                      "Junior Python Developer", 45000),
                     (Employee("Name", "Surname6", "05.01.2012", 0), "-", 0)]

    @pytest.mark.parametrize('employee, position, salary', values_to_try)
    def test_get_message(self, employee, position, salary):
        """Перевірка get_message() на коректних значеннях
        """
        employee.get_message()
        assert employee.position == position and employee.salary == salary


class TestEmployeeErrors:

    @pytest.fixture
    def employee(self):
        return Employee("Name", "Surname", "12.10.2004", 3)

    @pytest.mark.xfail
    def test_wrong_name_type(self, employee):
        employee.name = 1234
        assert not isinstance(employee.name, str)

    @pytest.mark.xfail
    def test_wrong_birthday_type(self, employee):
        employee.birthday = True
        assert not isinstance(employee.birthday, str)

    @pytest.mark.xfail
    def test_experience_type_error(self):
        with pytest.raises(TypeError):
            Employee("Name", "Surname", "12.10.2004", "3")

    values_to_try = [("Name", "Surname1", "01.01.2004", -10),
                     ("Name", "Surname2", "01.01.2004", 20),
                     ("Name", "Surname3", "01.01.2004", 21)]

    @pytest.mark.xfail
    @pytest.mark.parametrize('name, surname, birthday, experience', values_to_try)
    def test_experience_value_error(self, name, surname, birthday, experience):
        with pytest.raises(ValueError):
            Employee(name, surname, birthday, experience)
