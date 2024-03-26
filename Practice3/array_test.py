import pytest
from Practice1.employee import Employee
from Practice3.array import Array


class TestArray:

    @pytest.fixture
    def empty_array(self):
        return Array()

    @pytest.fixture
    def sample_array(self):
        employees = [Employee("Name", "Surname1", "01.01.1956", 5, "Ментор з підготовки молодих спеціалістів", 195000),
                     Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000),
                     Employee("Name", "Surname3", "18.10.1996", 5, "Senior Python Developer", 190000),
                     Employee("Name", "Surname4", "22.04.2002", 3, "Middle Python Developer", 120000),
                     Employee("Name", "Surname5", "06.05.2004", 0, "Junior Python Developer", 45000),
                     Employee("Name", "Surname6", "05.01.2012", 0, "-", 0)]
        return Array(*employees)

    def test_empty_array_length(self, empty_array):
        assert len(empty_array) == 0

    def test_sample_array_length(self, sample_array):
        assert len(sample_array) == 6

    def test_sample_array_getitem(self, sample_array):
        assert sample_array[1] == Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000)

    def test_sample_array_setitem(self, sample_array):
        sample_array[0] = sample_array[1]
        assert sample_array[0] == Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000)

    def test_sample_array_append(self, sample_array):
        e = Employee("Name", "Surname7", "01.05.2004", 0, "-", 0)
        sample_array.append(e)
        assert len(sample_array) == 7

    def test_sample_array_index(self, sample_array):
        assert sample_array.index(Employee("Name", "Surname6", "05.01.2012", 0, "-", 0)) == 5

    def test_sample_array_remove(self, sample_array):
        sample_array.remove(Employee("Name", "Surname6", "05.01.2012", 0, "-", 0))
        assert len(sample_array) == 5

    def test_sample_array_clear(self, sample_array):
        sample_array.clear()
        assert len(sample_array) == 0

    def test_sample_array_copy(self, sample_array):
        copied_array = sample_array.copy()
        assert len(copied_array) == 6
        assert id(copied_array[0]) == id(sample_array[0])

    def test_sample_array_extend(self, sample_array):
        sample_array.extend([Employee("Name", "Surname7", "15.03.2000", 7, "Middle Python Developer", 120000),
                             Employee("Name", "Surname8", "03.03.1995", 3, "Senior Python Developer", 190000)])
        assert len(sample_array) == 8

    def test_sample_array_pop_del(self, sample_array):
        del sample_array[2]
        assert len(sample_array) == 5
        assert sample_array[2] == Employee("Name", "Surname4", "22.04.2002", 3, "Middle Python Developer", 120000)

    def test_sample_array_pop(self, sample_array):
        popped_item = sample_array.pop(1)
        assert popped_item.surname == "Surname2"
        assert len(sample_array) == 5

    def test_sample_array_reverse(self, sample_array):
        sample_array.reverse()
        assert sample_array[0].surname == "Surname6" and sample_array[5].surname == "Surname1"
        assert sample_array[1].surname == "Surname5" and sample_array[4].surname == "Surname2"
        assert sample_array[2].surname == "Surname4" and sample_array[3].surname == "Surname3"

    def test_sample_array_count(self, sample_array):
        assert sample_array.count(Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000)) == 1
        sample_array.append(Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000))
        assert sample_array.count(Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000)) == 2

    def test_sample_array_deepcopy(self, sample_array):
        copied_array = sample_array.deepcopy()
        assert len(copied_array) == 6
        assert id(copied_array[0]) != id(sample_array[0])

    def test_sample_array_min(self, sample_array):
        assert sample_array.min().surname == "Surname1"

    def test_sample_array_max(self, sample_array):
        assert sample_array.max().surname == "Surname6"

    def test_sample_array_add(self, sample_array):
        args_to_add = [
            Employee("Name", "Surname7", "15.03.2000", 7, "Middle Python Developer", 120000),
            Employee("Name", "Surname8", "03.03.1995", 3, "Senior Python Developer", 190000)]
        result_args = [
            Employee("Name", "Surname1", "01.01.1956", 5, "Ментор з підготовки молодих спеціалістів", 195000),
            Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000),
            Employee("Name", "Surname3", "18.10.1996", 5, "Senior Python Developer", 190000),
            Employee("Name", "Surname4", "22.04.2002", 3, "Middle Python Developer", 120000),
            Employee("Name", "Surname5", "06.05.2004", 0, "Junior Python Developer", 45000),
            Employee("Name", "Surname6", "05.01.2012", 0, "-", 0),
            Employee("Name", "Surname7", "15.03.2000", 7, "Middle Python Developer", 120000),
            Employee("Name", "Surname8", "03.03.1995", 3, "Senior Python Developer", 190000)]

        array_to_add = Array(*args_to_add)
        result_array = Array(*result_args)
        test_array = sample_array + array_to_add
        assert test_array[6] == result_array[6]
        assert test_array[7] == result_array[7]

    def test_sample_array_mul(self, sample_array):
        result_args = [
            Employee("Name", "Surname1", "01.01.1956", 5, "Ментор з підготовки молодих спеціалістів", 195000),
            Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000),
            Employee("Name", "Surname3", "18.10.1996", 5, "Senior Python Developer", 190000),
            Employee("Name", "Surname4", "22.04.2002", 3, "Middle Python Developer", 120000),
            Employee("Name", "Surname5", "06.05.2004", 0, "Junior Python Developer", 45000),
            Employee("Name", "Surname6", "05.01.2012", 0, "-", 0),
            Employee("Name", "Surname1", "01.01.1956", 5, "Ментор з підготовки молодих спеціалістів", 195000),
            Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000),
            Employee("Name", "Surname3", "18.10.1996", 5, "Senior Python Developer", 190000),
            Employee("Name", "Surname4", "22.04.2002", 3, "Middle Python Developer", 120000),
            Employee("Name", "Surname5", "06.05.2004", 0, "Junior Python Developer", 45000),
            Employee("Name", "Surname6", "05.01.2012", 0, "-", 0)
        ]

        result_array = Array(*result_args)
        test_array = sample_array * 2
        assert test_array[6] == result_array[6]
        assert test_array[7] == result_array[7]
        assert test_array[10] == result_array[10]
        assert test_array[11] == result_array[11]
