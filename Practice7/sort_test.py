from Practice1.employee import Employee
from Practice7.sort import Sort
import pytest


class TestSort:

    @pytest.fixture
    def sample_sort(self):
        employees = [Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000),
                     Employee("Name", "Surname6", "05.01.2012", 0, "-", 0),
                     Employee("Name", "Surname1", "01.01.1956", 5, "Ментор з підготовки молодих спеціалістів", 195000),
                     Employee("Name", "Surname3", "18.10.1996", 5, "Senior Python Developer", 190000),
                     Employee("Name", "Surname5", "06.05.2004", 0, "Junior Python Developer", 45000),
                     Employee("Name", "Surname4", "22.04.2002", 3, "Middle Python Developer", 120000)]
        return Sort(*employees)

    def test_sample_sort_sort(self, sample_sort):
        sorted_example = [
            Employee("Name", "Surname1", "01.01.1956", 5, "Ментор з підготовки молодих спеціалістів", 195000),
            Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000),
            Employee("Name", "Surname3", "18.10.1996", 5, "Senior Python Developer", 190000),
            Employee("Name", "Surname4", "22.04.2002", 3, "Middle Python Developer", 120000),
            Employee("Name", "Surname5", "06.05.2004", 0, "Junior Python Developer", 45000),
            Employee("Name", "Surname6", "05.01.2012", 0, "-", 0)]

        sample_sort.sort()
        for i in range(6):
            assert sorted_example[i] == sample_sort[i]

    def test_sample_sort_sort_reverse(self, sample_sort):
        sorted_example = [
            Employee("Name", "Surname6", "05.01.2012", 0, "-", 0),
            Employee("Name", "Surname5", "06.05.2004", 0, "Junior Python Developer", 45000),
            Employee("Name", "Surname4", "22.04.2002", 3, "Middle Python Developer", 120000),
            Employee("Name", "Surname3", "18.10.1996", 5, "Senior Python Developer", 190000),
            Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000),
            Employee("Name", "Surname1", "01.01.1956", 5, "Ментор з підготовки молодих спеціалістів", 195000)]

        sample_sort.sort(True)
        for i in range(6):
            assert sorted_example[i] == sample_sort[i]

    def test_sample_sort_sort_by_attr(self, sample_sort):
        sorted_example = [
            Employee("Name", "Surname6", "05.01.2012", 0, "-", 0),
            Employee("Name", "Surname5", "06.05.2004", 0, "Junior Python Developer", 45000),
            Employee("Name", "Surname4", "22.04.2002", 3, "Middle Python Developer", 120000),
            Employee("Name", "Surname3", "18.10.1996", 5, "Senior Python Developer", 190000),
            Employee("Name", "Surname1", "01.01.1956", 5, "Ментор з підготовки молодих спеціалістів", 195000),
            Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000)]

        sample_sort.sort_by_attr("salary")
        for i in range(6):
            assert sorted_example[i] == sample_sort[i]

    def test_sample_sort_sort_by_attr_reverse(self, sample_sort):
        sorted_example = [
            Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000),
            Employee("Name", "Surname1", "01.01.1956", 5, "Ментор з підготовки молодих спеціалістів", 195000),
            Employee("Name", "Surname3", "18.10.1996", 5, "Senior Python Developer", 190000),
            Employee("Name", "Surname4", "22.04.2002", 3, "Middle Python Developer", 120000),
            Employee("Name", "Surname5", "06.05.2004", 0, "Junior Python Developer", 45000),
            Employee("Name", "Surname6", "05.01.2012", 0, "-", 0)]

        sample_sort.sort_by_attr("salary", True)
        for i in range(6):
            assert sorted_example[i] == sample_sort[i]

    def test_sample_sort_sort_by_lambda(self, sample_sort):
        sorted_example = [
            Employee("Name", "Surname6", "05.01.2012", 0, "-", 0),
            Employee("Name", "Surname5", "06.05.2004", 0, "Junior Python Developer", 45000),
            Employee("Name", "Surname4", "22.04.2002", 3, "Middle Python Developer", 120000),
            Employee("Name", "Surname3", "18.10.1996", 5, "Senior Python Developer", 190000),
            Employee("Name", "Surname1", "01.01.1956", 5, "Ментор з підготовки молодих спеціалістів", 195000),
            Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000)]

        sample_sort.sort_by_lambda(lambda x, y: x.salary > y.salary)
        for i in range(6):
            assert sorted_example[i] == sample_sort[i]
