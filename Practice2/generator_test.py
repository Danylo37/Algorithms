from Practice1.employee import Employee
from generator import Generator
import pytest


class TestGenerator:
    @pytest.fixture
    def init_employee(self):
        return Employee("Name", "Surname", "12.10.2004", 3)

    def test_gen_single_types(self):
        g = Generator()
        e = g.generate_single()
        assert isinstance(e, Employee)
        assert isinstance(e.name, str)
        assert isinstance(e.surname, str)
        assert isinstance(e.birthday, str)
        assert isinstance(e.position, str)
        assert isinstance(e.salary, int)
        assert isinstance(e.experience, int)

    def test_gen_1000_type(self):
        g = Generator()
        elist = g.generate_1000()
        assert isinstance(elist, list)
        assert isinstance(elist[0], Employee)
        assert len(elist) == 1000

    def test_gen_10_000_type(self):
        g = Generator()
        elist = g.generate_10_000()
        assert isinstance(elist, list)
        assert isinstance(elist[0], Employee)
        assert len(elist) == 10000
