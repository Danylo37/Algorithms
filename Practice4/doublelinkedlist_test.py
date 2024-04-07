import pytest
from Practice1.employee import Employee
from Practice4.doublelinkedlist import DoubleLinkedList


class TestDoubleLinkedList:

    @pytest.fixture
    def empty_doublelinkedlist(self):
        return DoubleLinkedList()

    @pytest.fixture
    def sample_doublelinkedlist(self):
        employees = [Employee("Name", "Surname1", "01.01.1956", 5, "Ментор з підготовки молодих спеціалістів", 195000),
                     Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000),
                     Employee("Name", "Surname3", "18.10.1996", 5, "Senior Python Developer", 190000),
                     Employee("Name", "Surname4", "22.04.2002", 3, "Middle Python Developer", 120000),
                     Employee("Name", "Surname5", "06.05.2004", 0, "Junior Python Developer", 45000),
                     Employee("Name", "Surname6", "05.01.2012", 0, "-", 0)]
        return DoubleLinkedList(*employees)

    def test_empty_doublelinkedlist_length(self, empty_doublelinkedlist):
        assert len(empty_doublelinkedlist) == 0

    def test_sample_doublelinkedlist_length(self, sample_doublelinkedlist):
        assert len(sample_doublelinkedlist) == 6

    def test_sample_doublelinkedlist_repr(self, sample_doublelinkedlist):
        assert (repr(sample_doublelinkedlist) == (
            "[Employee(Name, Surname1, 01.01.1956, 5, "
            "Ментор з підготовки молодих спеціалістів, 195000), "
            "Employee(Name, Surname2, 12.04.1986, 6, Team Lead, 200000), "
            "Employee(Name, Surname3, 18.10.1996, 5, Senior Python Developer, 190000), "
            "Employee(Name, Surname4, 22.04.2002, 3, Middle Python Developer, 120000), "
            "Employee(Name, Surname5, 06.05.2004, 0, Junior Python Developer, 45000), "
            "Employee(Name, Surname6, 05.01.2012, 0, -, 0)]"
        ))

    def test_empty_doublelinkedlist_repr(self, empty_doublelinkedlist):
        assert repr(empty_doublelinkedlist) == "[]"

    def test_sample_doublelinkedlist_getitem(self, sample_doublelinkedlist):
        assert sample_doublelinkedlist[1] == Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000)
        assert sample_doublelinkedlist[-1] == Employee("Name", "Surname6", "05.01.2012", 0, "-", 0)

    def test_sample_doublelinkedlist_slice(self, sample_doublelinkedlist):
        dll_slice = sample_doublelinkedlist[1:3]

        assert isinstance(dll_slice, type(sample_doublelinkedlist))
        assert dll_slice[0] == Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000)
        assert dll_slice[1] == Employee("Name", "Surname3", "18.10.1996", 5, "Senior Python Developer", 190000)

    def test_sample_doublelinkedlist_setitem(self, sample_doublelinkedlist):
        sample_doublelinkedlist[0] = Employee("Name", "Surname7", "01.05.2004", 0, "-", 0)
        sample_doublelinkedlist[-1] = Employee("Name", "Surname8", "03.02.1995", 0, "-", 0)
        assert sample_doublelinkedlist[0] == Employee("Name", "Surname7", "01.05.2004", 0, "-", 0)
        assert sample_doublelinkedlist[-1] == Employee("Name", "Surname8", "03.02.1995", 0, "-", 0)

    def test_sample_doublelinkedlist_setitem_duplicate(self, sample_doublelinkedlist):
        sample_doublelinkedlist[0] = sample_doublelinkedlist[1]
        assert sample_doublelinkedlist[0] != sample_doublelinkedlist[1]

    def test_sample_doublelinkedlist_append(self, sample_doublelinkedlist):
        e = Employee("Name", "Surname7", "01.05.2004", 0, "-", 0)
        sample_doublelinkedlist.append(e)
        assert sample_doublelinkedlist[6] == Employee("Name", "Surname7", "01.05.2004", 0, "-", 0)
        assert len(sample_doublelinkedlist) == 7

    def test_sample_doublelinkedlist_append_duplicate(self, sample_doublelinkedlist):
        e = sample_doublelinkedlist[2]
        sample_doublelinkedlist.append(e)
        assert sample_doublelinkedlist[5] == Employee("Name", "Surname6", "05.01.2012", 0, "-", 0)
        assert len(sample_doublelinkedlist) == 6

    def test_sample_doublelinkedlist_contains(self, sample_doublelinkedlist):
        e = Employee("Name", "Surname7", "01.05.2004", 0, "-", 0)
        assert sample_doublelinkedlist[0] in sample_doublelinkedlist
        assert e not in sample_doublelinkedlist

    def test_sample_doublelinkedlist_insert_in_head(self, sample_doublelinkedlist):
        e = Employee("Name", "Surname7", "01.05.2004", 0, "-", 0)
        sample_doublelinkedlist.insert(0, e)
        assert sample_doublelinkedlist[0] == e

    def test_sample_doublelinkedlist_insert(self, sample_doublelinkedlist):
        e = Employee("Name", "Surname8", "03.02.1995", 0, "-", 0)
        sample_doublelinkedlist.insert(1, e)
        assert sample_doublelinkedlist[1] == e

    def test_sample_doublelinkedlist_insert_in_tail(self, sample_doublelinkedlist):
        e = Employee("Name", "Surname9", "12.09.1992", 0, "-", 0)
        sample_doublelinkedlist.insert(len(sample_doublelinkedlist)-1, e)
        assert sample_doublelinkedlist[len(sample_doublelinkedlist)-1] == e

    def test_sample_doublelinkedlist_insert_duplicate(self, sample_doublelinkedlist):
        e = Employee("Name", "Surname5", "06.05.2004", 0, "Junior Python Developer", 45000)
        sample_doublelinkedlist.insert(1, e)
        assert sample_doublelinkedlist[1] != Employee("Name", "Surname5", "06.05.2004", 0, "Junior Python Developer",
                                                      45000)
        assert len(sample_doublelinkedlist) == 6

    def test_sample_doublelinkedlist_index(self, sample_doublelinkedlist):
        assert sample_doublelinkedlist.index(Employee("Name", "Surname6", "05.01.2012", 0, "-", 0)) == 5

    def test_sample_doublelinkedlist_index_with_start_and_stop(self, sample_doublelinkedlist):
        assert sample_doublelinkedlist.index(Employee("Name", "Surname6", "05.01.2012", 0, "-", 0), 2, 6) == 5

    def test_sample_doublelinkedlist_remove_head(self, sample_doublelinkedlist):
        sample_doublelinkedlist.remove(Employee("Name", "Surname1", "01.01.1956", 5,
                                                "Ментор з підготовки молодих спеціалістів", 195000))
        assert sample_doublelinkedlist[0] == Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000)

    def test_sample_doublelinkedlist_remove(self, sample_doublelinkedlist):
        sample_doublelinkedlist.remove(Employee("Name", "Surname4", "22.04.2002", 3, "Middle Python Developer", 120000))
        assert sample_doublelinkedlist[3] == Employee("Name", "Surname5", "06.05.2004", 0, "Junior Python Developer",
                                                      45000)

    def test_sample_doublelinkedlist_remove_tail(self, sample_doublelinkedlist):
        sample_doublelinkedlist.remove(Employee("Name", "Surname6", "05.01.2012", 0, "-", 0))
        assert len(sample_doublelinkedlist) == 5

    def test_sample_doublelinkedlist_clear(self, sample_doublelinkedlist):
        sample_doublelinkedlist.clear()
        assert len(sample_doublelinkedlist) == 0

    def test_sample_doublelinkedlist_copy(self, sample_doublelinkedlist):
        copied_array = sample_doublelinkedlist.copy()
        assert len(copied_array) == 6
        assert id(copied_array[0]) == id(sample_doublelinkedlist[0])

    def test_sample_doublelinkedlist_extend(self, sample_doublelinkedlist):
        sample_doublelinkedlist.extend(
            [Employee("Name", "Surname7", "15.03.2000", 7, "Middle Python Developer", 120000),
             Employee("Name", "Surname8", "03.03.1995", 3, "Senior Python Developer", 190000)])
        assert len(sample_doublelinkedlist) == 8

    def test_sample_doublelinkedlist_del(self, sample_doublelinkedlist):
        del sample_doublelinkedlist[2]
        del sample_doublelinkedlist[-2]
        assert len(sample_doublelinkedlist) == 4
        assert sample_doublelinkedlist[2] == Employee("Name", "Surname4", "22.04.2002", 3, "Middle Python Developer",
                                                      120000)
        assert sample_doublelinkedlist[-2] == Employee("Name", "Surname4", "22.04.2002", 3, "Middle Python Developer",
                                                       120000)

    def test_sample_doublelinkedlist_pop(self, sample_doublelinkedlist):
        popped_item1 = sample_doublelinkedlist.pop(1)
        popped_item2 = sample_doublelinkedlist.pop(-2)
        assert popped_item1.surname == "Surname2"
        assert popped_item2.surname == "Surname5"
        assert len(sample_doublelinkedlist) == 4

    def test_sample_doublelinkedlist_reverse(self, sample_doublelinkedlist):
        sample_doublelinkedlist.reverse()
        assert sample_doublelinkedlist[0].surname == "Surname6" and sample_doublelinkedlist[5].surname == "Surname1"
        assert sample_doublelinkedlist[1].surname == "Surname5" and sample_doublelinkedlist[4].surname == "Surname2"
        assert sample_doublelinkedlist[2].surname == "Surname4" and sample_doublelinkedlist[3].surname == "Surname3"

    def test_reverse_with_empty_doublelinkedlist(self, empty_doublelinkedlist):
        empty_doublelinkedlist.reverse()
        assert len(empty_doublelinkedlist) == 0

    def test_sample_doublelinkedlist_count(self, sample_doublelinkedlist):
        assert sample_doublelinkedlist.count(Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000)) == 1
        sample_doublelinkedlist.append(Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000))
        assert sample_doublelinkedlist.count(Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000)) == 1
        assert sample_doublelinkedlist.count(Employee("Name", "Surname", "12.04.1986", 6, "Team Lead", 200000)) == 0

    def test_sample_doublelinkedlist_deepcopy(self, sample_doublelinkedlist):
        copied_array = sample_doublelinkedlist.deepcopy()
        assert len(copied_array) == 6
        assert id(copied_array[0]) != id(sample_doublelinkedlist[0])

    def test_deepcopy_with_empty_doublelinkedlist(self, empty_doublelinkedlist):
        copied_list = empty_doublelinkedlist.deepcopy()
        assert len(copied_list) == 0

    def test_sample_doublelinkedlist_min(self, sample_doublelinkedlist):
        assert sample_doublelinkedlist.min().surname == "Surname1"

    def test_sample_doublelinkedlist_max(self, sample_doublelinkedlist):
        assert sample_doublelinkedlist.max().surname == "Surname6"

    def test_empty_doublelinkedlist_min(self, empty_doublelinkedlist):
        assert empty_doublelinkedlist.min() is None

    def test_empty_doublelinkedlist_max(self, empty_doublelinkedlist):
        assert empty_doublelinkedlist.max() is None

    def test_sample_doublelinkedlist_add(self, sample_doublelinkedlist):
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

        doublelinkedlist_to_add = DoubleLinkedList(*args_to_add)
        result_array = DoubleLinkedList(*result_args)
        test_array = sample_doublelinkedlist + doublelinkedlist_to_add
        assert test_array[7] == result_array[7]


class TestDoubleLinkedListErrors:

    @pytest.fixture
    def sample_doublelinkedlist(self):
        employees = [Employee("Name", "Surname1", "01.01.1956", 5, "Ментор з підготовки молодих спеціалістів", 195000),
                     Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000),
                     Employee("Name", "Surname3", "18.10.1996", 5, "Senior Python Developer", 190000),
                     Employee("Name", "Surname4", "22.04.2002", 3, "Middle Python Developer", 120000),
                     Employee("Name", "Surname5", "06.05.2004", 0, "Junior Python Developer", 45000),
                     Employee("Name", "Surname6", "05.01.2012", 0, "-", 0)]
        return DoubleLinkedList(*employees)

    def test_sample_doublelinkedlist_getitem_type_error(self, sample_doublelinkedlist):
        with pytest.raises(TypeError):
            assert sample_doublelinkedlist["a"]

    def test_sample_doublelinkedlist_getitem_index_error(self, sample_doublelinkedlist):
        with pytest.raises(IndexError):
            assert sample_doublelinkedlist[10]

    def test_sample_doublelinkedlist_setitem_type_error(self, sample_doublelinkedlist):
        with pytest.raises(TypeError):
            sample_doublelinkedlist["a"] = Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000)

    def test_sample_doublelinkedlist_setitem_index_error(self, sample_doublelinkedlist):
        with pytest.raises(IndexError):
            sample_doublelinkedlist[10] = Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000)

    def test_sample_doublelinkedlist_insert_index_error(self, sample_doublelinkedlist):
        with pytest.raises(IndexError):
            sample_doublelinkedlist.insert(10, Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000))

    def test_sample_doublelinkedlist_index_value_error(self, sample_doublelinkedlist):
        with pytest.raises(ValueError):
            sample_doublelinkedlist.index(Employee("Name", "Surname9", "12.04.1986", 6, "Team Lead", 200000))

    def test_sample_doublelinkedlist_del_index_error(self, sample_doublelinkedlist):
        with pytest.raises(IndexError):
            del sample_doublelinkedlist[11]

    def test_sample_doublelinkedlist_pop_index_error(self, sample_doublelinkedlist):
        with pytest.raises(IndexError):
            sample_doublelinkedlist.pop(11)

    def test_sample_doublelinkedlist_add_type_error(self, sample_doublelinkedlist):
        with pytest.raises(TypeError):
            assert sample_doublelinkedlist + list()

    def test_sample_doublelinkedlist_mul_not_implemented_error(self, sample_doublelinkedlist):
        with pytest.raises(NotImplementedError):
            sample_doublelinkedlist * 2
