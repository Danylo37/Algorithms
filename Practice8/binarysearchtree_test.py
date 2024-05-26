from Practice1.employee import Employee
from Practice8.binarysearchtree import BinarySearchTree
import pytest


class TestBinarySearchTree:

    @pytest.fixture
    def sample_bst(self):
        employees = [Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000),
                     Employee("Name", "Surname6", "05.01.2012", 0, "-", 0),
                     Employee("Name", "Surname1", "01.01.1956", 5, "Ментор з підготовки молодих спеціалістів", 195000),
                     Employee("Name", "Surname3", "18.10.1996", 5, "Senior Python Developer", 190000),
                     Employee("Name", "Surname5", "06.05.2004", 0, "Junior Python Developer", 45000),
                     Employee("Name", "Surname4", "22.04.2002", 3, "Middle Python Developer", 120000)]
        return BinarySearchTree(*employees)

    @pytest.fixture
    def empty_binarytree(self):
        return BinarySearchTree()

    def test_sample_binarysearchtree_len(self, sample_bst):
        assert len(sample_bst) == 6

    def test_sample_binarysearchtree_repr(self, sample_bst):
        assert (repr(sample_bst) ==
                ('  l: Employee(Name, Surname1, 01.01.1956, 5, Ментор з підготовки молодих спеціалістів, 195000)\n'
                 'Employee(Name, Surname2, 12.04.1986, 6, Team Lead, 200000)\n'
                 '    l: Employee(Name, Surname3, 18.10.1996, 5, Senior Python Developer, 190000)\n'
                 '        l: Employee(Name, Surname4, 22.04.2002, 3, Middle Python Developer, 120000)\n'
                 '      r: Employee(Name, Surname5, 06.05.2004, 0, Junior Python Developer, 45000)\n'
                 '  r: Employee(Name, Surname6, 05.01.2012, 0, -, 0)\n'))

    def test_empty_binarysearchtree_repr(self, empty_binarytree):
        assert repr(empty_binarytree) == '[]'

    def test_sample_binarysearchtree_insert(self, sample_bst):
        e = Employee("Name", "Surname0", "05.01.2012", 0, "-", 0)
        sample_bst.insert(e)
        assert len(sample_bst) == 7 and sample_bst.find(e)

    def test_sample_binarysearchtree_find_true(self, sample_bst):
        assert sample_bst.find(Employee("Name", "Surname6", "05.01.2012", 0, "-", 0))

    def test_sample_binarysearchtree_find_false(self, sample_bst):
        assert not sample_bst.find(Employee("Name", "Surname0", "05.01.2012", 0, "-", 0))

    def test_sample_binarysearchtree_remove(self, sample_bst):
        sample_bst.remove(Employee("Name", "Surname6", "05.01.2012", 0, "-", 0))
        assert len(sample_bst) and not sample_bst.find(Employee("Name", "Surname6", "05.01.2012", 0, "-", 0))

    def test_binarysearchtree_remove_value_error(self, sample_bst):
        with pytest.raises(ValueError):
            sample_bst.remove(Employee("Name", "Surname0", "05.01.2012", 0, "-", 0))

    def test_sample_binarysearchtree_min(self, sample_bst):
        e = Employee("Name", "Surname1", "01.01.1956", 5, "Ментор з підготовки молодих спеціалістів", 195000)
        assert sample_bst.min() == e

    def test_sample_binarysearchtree_clear(self, sample_bst):
        sample_bst.clear()
        assert len(sample_bst) == 0

    def test_sample_binarysearchtree_replace(self, sample_bst):
        old = Employee("Name", "Surname6", "05.01.2012", 0, "-", 0)
        new = Employee("Name", "Surname0", "05.01.2012", 0, "-", 0)
        sample_bst.replace(old, new)
        assert not sample_bst.find(old)
        assert sample_bst.find(new)

    def test_sample_binarysearchtree_iter(self, sample_bst):
        employees = [Employee("Name", "Surname1", "01.01.1956", 5, "Ментор з підготовки молодих спеціалістів", 195000),
                     Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000),
                     Employee("Name", "Surname3", "18.10.1996", 5, "Senior Python Developer", 190000),
                     Employee("Name", "Surname4", "22.04.2002", 3, "Middle Python Developer", 120000),
                     Employee("Name", "Surname5", "06.05.2004", 0, "Junior Python Developer", 45000),
                     Employee("Name", "Surname6", "05.01.2012", 0, "-", 0)]
        for i, e in enumerate(sample_bst):
            assert e == employees[i]

    def test_sample_binarysearchtree_extend(self, sample_bst):
        employees = [Employee("Name", "Surname7", "01.01.1956", 5, "Ментор з підготовки молодих спеціалістів", 195000),
                     Employee("Name", "Surname8", "12.04.1986", 6, "Team Lead", 200000),
                     Employee("Name", "Surname9", "05.01.2012", 0, "-", 0)]
        sample_bst.extend(employees)
        assert sample_bst.find(employees[0])
        assert sample_bst.find(employees[1])
        assert sample_bst.find(employees[2])

    def test_sample_binarysearchtree_count(self, sample_bst):
        e = Employee("Name", "Surname6", "05.01.2012", 0, "-", 0)
        sample_bst.insert(e)
        assert sample_bst.count(e) == 2

    def test_sample_binarysearchtree_max(self, sample_bst):
        e = Employee("Name", "Surname6", "05.01.2012", 0, "-", 0)
        assert sample_bst.max() == e

    def test_sample_binarysearchtree_add(self, sample_bst):
        args_to_add = [
            Employee("Name", "Surname7", "15.03.2000", 7, "Middle Python Developer", 120000),
            Employee("Name", "Surname8", "03.03.1995", 3, "Senior Python Developer", 190000)]

        bst_to_add = BinarySearchTree(*args_to_add)
        test_bst = sample_bst + bst_to_add
        assert test_bst.find(args_to_add[0])
        assert test_bst.find(args_to_add[1])

    def test_sample_binarysearchtree_mul(self, sample_bst):
        test_bst = sample_bst * 2
        for e in test_bst:
            assert test_bst.count(e) == 2

    def test_sample_binarysearchtree_traversal(self, sample_bst):
        employees = [Employee("Name", "Surname1", "01.01.1956", 5, "Ментор з підготовки молодих спеціалістів", 195000),
                     Employee("Name", "Surname2", "12.04.1986", 6, "Team Lead", 200000),
                     Employee("Name", "Surname3", "18.10.1996", 5, "Senior Python Developer", 190000),
                     Employee("Name", "Surname4", "22.04.2002", 3, "Middle Python Developer", 120000),
                     Employee("Name", "Surname5", "06.05.2004", 0, "Junior Python Developer", 45000),
                     Employee("Name", "Surname6", "05.01.2012", 0, "-", 0)]
        sample_bst.traversal()
        for i, e in enumerate(sample_bst):
            assert e == employees[i]
