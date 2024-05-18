from Practice1.employee import Employee
from Practice6.find import Find
import pytest


class TestFind:

    @pytest.fixture
    def sample_find(self):
        employees = [Employee("Name", "Surname1", "01.01.1956", 5, "Ментор з підготовки молодих спеціалістів", 195000),
                     Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000),
                     Employee("Name", "Surname3", "18.10.1996", 5, "Senior Python Developer", 190000),
                     Employee("Name", "Surname4", "22.04.2002", 3, "Middle Python Developer", 120000),
                     Employee("Name", "Surname5", "06.05.2004", 0, "Junior Python Developer", 45000),
                     Employee("Name", "Surname6", "05.01.2012", 0, "-", 0)]
        return Find(*employees)

    @pytest.fixture
    def non_existent_value(self):
        return Employee("Name", "Surname", "01.01.2000", 0, "", 0)

    def test_sample_find_append(self, sample_find):
        e1 = Employee("Name", "Surname", "01.01.1956", 5, "Ментор з підготовки молодих спеціалістів", 195000)
        e2 = Employee("Name", "Surname1.5", "01.01.1956", 5, "Ментор з підготовки молодих спеціалістів", 195000)
        e3 = Employee("Name", "Surname7", "01.01.1956", 5, "Ментор з підготовки молодих спеціалістів", 195000)

        sample_find.append(e1)
        sample_find.append(e2)
        sample_find.append(e3)

        assert sample_find[0] == e1
        assert sample_find[2] == e2
        assert sample_find[8] == e3
        assert len(sample_find) == 9

    def test_sample_find_find(self, sample_find):
        assert sample_find.find(sample_find[3]) == 3

    def test_sample_find_find_non_existent(self, sample_find, non_existent_value):
        assert sample_find.find(non_existent_value) == -1

    def test_sample_find_find_by_attr(self, sample_find):
        assert sample_find.find_by_attr("Surname4", "surname") == 3

    def test_sample_find_find_by_attr_non_existent(self, sample_find):
        assert sample_find.find_by_attr("Surname", "surname") == -1

    def test_sample_find_find_by_attrs(self, sample_find):
        assert sample_find.find_by_attrs(surname='Surname4', name='Name') == 3

    def test_sample_find_find_by_attrs_non_existent(self, sample_find):
        assert sample_find.find_by_attrs(surname='Surname', name='Name') == -1

    def test_sample_find_find_by_lambda(self, sample_find):
        assert sample_find.find_by_lambda(sample_find[3], lambda x, y: x.surname == y.surname) == 3

    def test_sample_find_find_by_lambda_non_existent(self, sample_find, non_existent_value):
        assert sample_find.find_by_lambda(non_existent_value, lambda x, y: x.surname == y.surname) == -1

    def test_sample_find_exponential_search_first(self, sample_find):
        assert sample_find.exponential_search(sample_find[0]) == 0

    def test_sample_find_exponential_search_last(self, sample_find):
        assert sample_find.exponential_search(sample_find[5]) == 5

    def test_sample_find_exponential_search_non_existent(self, sample_find, non_existent_value):
        assert sample_find.exponential_search(non_existent_value) == -1
