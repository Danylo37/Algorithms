from Practice1.employee import Employee
from Practice5.deque import Deque
import pytest


class TestDeque:

    @pytest.fixture
    def empty_deque(self):
        return Deque()

    @pytest.fixture
    def sample_deque(self):
        deque = Deque()

        deque.push_last(Employee("Name", "Surname1", "01.01.2001", 0, "-", 0))
        deque.push_last(Employee("Name", "Surname2", "01.01.2001", 0, "-", 0))
        deque.push_last(Employee("Name", "Surname3", "01.01.2001", 0, "-", 0))
        deque.push_last(Employee("Name", "Surname4", "01.01.2001", 0, "-", 0))
        deque.push_last(Employee("Name", "Surname5", "01.01.2001", 0, "-", 0))

        return deque

    def test_empty_deque_len(self, empty_deque):
        assert len(empty_deque) == 0

    def test_sample_deque_len(self, sample_deque):
        assert len(sample_deque) == 5

    def test_empty_deque_repr(self, empty_deque):
        assert empty_deque.__repr__() == '[]'

    def test_sample_deque_repr(self, sample_deque):
        assert sample_deque.__repr__() == ("[Employee(Name, Surname1, 01.01.2001, 0, -, 0), Employee(Name, "
                                           "Surname2, 01.01.2001, 0, -, 0), Employee(Name, Surname3, "
                                           "01.01.2001, 0, -, 0), Employee(Name, Surname4, 01.01.2001, 0, -, "
                                           "0), Employee(Name, Surname5, 01.01.2001, 0, -, 0)]")

    def test_empty_deque_push_first(self, empty_deque):
        e = Employee("Name", "Surname1", "01.01.2001", 0, "-", 0)
        empty_deque.push_first(e)
        assert empty_deque.top_first() == e and len(empty_deque) == 1

    def test_sample_deque_push_first(self, sample_deque):
        e = Employee("Name", "Surname0", "01.01.2001", 0, "-", 0)
        sample_deque.push_first(e)
        assert sample_deque.top_first() == e and len(sample_deque) == 6

    def test_empty_deque_push_last(self, empty_deque):
        e = Employee("Name", "Surname1", "01.01.2001", 0, "-", 0)
        empty_deque.push_last(e)
        assert empty_deque.top_last() == e and len(empty_deque) == 1

    def test_sample_deque_push_last(self, sample_deque):
        e = Employee("Name", "Surname6", "01.01.2001", 0, "-", 0)
        sample_deque.push_last(e)
        assert sample_deque.top_last() == e and len(sample_deque) == 6

    def test_empty_deque_pop_first(self, empty_deque):
        with pytest.raises(IndexError):
            empty_deque.pop_first()

    def test_sample_deque_pop_first(self, sample_deque):
        e = sample_deque.pop_first()
        assert e == Employee("Name", "Surname1", "01.01.2001", 0, "-", 0) and len(sample_deque) == 4

    def test_empty_deque_pop_last(self, empty_deque):
        with pytest.raises(IndexError):
            empty_deque.pop_last()

    def test_sample_deque_pop_last(self, sample_deque):
        e = sample_deque.pop_last()
        assert e == Employee("Name", "Surname5", "01.01.2001", 0, "-", 0) and len(sample_deque) == 4

    def test_empty_deque_top_first(self, empty_deque):
        with pytest.raises(IndexError):
            empty_deque.top_first()

    def test_sample_deque_top_first(self, sample_deque):
        e = sample_deque.top_first()
        assert e == Employee("Name", "Surname1", "01.01.2001", 0, "-", 0) and len(sample_deque) == 5

    def test_empty_deque_top_last(self, empty_deque):
        with pytest.raises(IndexError):
            empty_deque.top_last()

    def test_sample_deque_top_last(self, sample_deque):
        e = sample_deque.top_last()
        assert e == Employee("Name", "Surname5", "01.01.2001", 0, "-", 0) and len(sample_deque) == 5

