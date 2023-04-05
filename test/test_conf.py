import pytest
import sys
sys.path.insert(0, '../pytesting')
from src.py_testing import School


@pytest.fixture(scope="session")
def school():
    s1 = School("school1")
    return s1


def test_read_conf(school):
    result = [["s1", "test_a"], ["s2", "test_b"]]
    conf = school.readConf("test_conf.txt")
    assert result == conf


def test_read_conf(school):
    result = [["s1", "test_a"], ["s2", "test_b"]]
    school.createStudent(result)
    students = school.getStudents()
    assert students[0].id == "s1"
    assert students[1].id == "s2"
    assert students[0].name == "test_a"
    assert students[1].name == "test_b"
