from Practice5.priorityqueue import PriorityQueue
from Practice1.employee import Employee
import pytest


class TestPriorityQueue:

    @pytest.fixture
    def empty_priorityqueue(self):
        return PriorityQueue()

    @pytest.fixture
    def sample_priorityqueue(self):
        priorityqueue = PriorityQueue()

        priorityqueue.enqueue(Employee("Name", "Surname2", "01.01.2001", 0, "-", 0))
        priorityqueue.enqueue(Employee("Name", "Surname1", "01.01.2001", 0, "-", 0))
        priorityqueue.enqueue(Employee("Name", "Surname5", "01.01.2001", 0, "-", 0))
        priorityqueue.enqueue(Employee("Name", "Surname4", "01.01.2001", 0, "-", 0))
        priorityqueue.enqueue(Employee("Name", "Surname3", "01.01.2001", 0, "-", 0))

        return priorityqueue

    def test_empty_priorityqueue_len(self, empty_priorityqueue):
        assert len(empty_priorityqueue) == 0

    def test_sample_priorityqueue_len(self, sample_priorityqueue):
        assert len(sample_priorityqueue) == 5

    def test_empty_priorityqueue_repr(self, empty_priorityqueue):
        assert empty_priorityqueue.__repr__() == '[]'

    def test_sample_priorityqueue_repr(self, sample_priorityqueue):
        assert sample_priorityqueue.__repr__() == ("[Employee(Name, Surname1, 01.01.2001, 0, -, 0), Employee(Name, "
                                                   "Surname2, 01.01.2001, 0, -, 0), Employee(Name, Surname3, "
                                                   "01.01.2001, 0, -, 0), Employee(Name, Surname4, 01.01.2001, 0, -, "
                                                   "0), Employee(Name, Surname5, 01.01.2001, 0, -, 0)]")

    def test_empty_priorityqueue_enqueue(self, empty_priorityqueue):
        empty_priorityqueue.enqueue(Employee("Name", "Surname1", "01.01.2001", 0, "-", 0))
        assert len(empty_priorityqueue) == 1

    def test_sample_priorityqueue_enqueue(self, sample_priorityqueue):
        sample_priorityqueue.enqueue(Employee("Name", "Surname6", "01.01.2001", 0, "-", 0))
        assert len(sample_priorityqueue) == 6

    def test_empty_priorityqueue_dequeue(self, empty_priorityqueue):
        with pytest.raises(IndexError):
            empty_priorityqueue.dequeue()

    def test_sample_priorityqueue_dequeue(self, sample_priorityqueue):
        e = sample_priorityqueue.dequeue()
        assert e == Employee("Name", "Surname1", "01.01.2001", 0, "-", 0) and len(sample_priorityqueue) == 4

    def test_empty_priorityqueue_top(self, empty_priorityqueue):
        with pytest.raises(IndexError):
            empty_priorityqueue.top()

    def test_sample_priorityqueue_top(self, sample_priorityqueue):
        e = sample_priorityqueue.top()
        assert e == Employee("Name", "Surname1", "01.01.2001", 0, "-", 0) and len(sample_priorityqueue) == 5
