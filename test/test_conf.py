import pytest
from learn_pytest.src.py_testing import School

# pytest will execute all the files with format test_* or *_test
# in the current directory and subdirectories.


def setup_function():
    # setup and teardown functions for each test
    pass


def teardown_function():
    # setup and teardown functions for each test
    pass


def test_read_conf(school):
    result = [["s1", "test_a"], ["s2", "test_b"]]
    conf = school.readConf("test_conf.txt")
    assert result == conf


def test_read_conf(school):
    result = [["s1", "test_a"], ["s2", "test_b"]]
    school.createStudent(result)
    students = school.getStudents()
    assert "s1" in students
    assert "s2" in students


@pytest.mark.number
def test_student_number_1(school):
    result = [["s1", "test_a"], ["s2", "test_b"]]
    school.createStudent(result)
    assert school.getNumberOfStudents() == 2


@pytest.mark.number
def test_student_number_2(school):
    result = [["s1", "test_a"]]
    school.clearStudents()  # note that fixture will be called once, variable is not cleared
    school.createStudent(result)
    assert school.getNumberOfStudents() == 1


@pytest.mark.number
@pytest.mark.parametrize("id, name", [("id1", "name1"), ("id2", "name2")])
def test_student_number_3(school, id, name):
    result = [[id, name]]
    school.clearStudents()
    school.createStudent(result)
    assert school.getNumberOfStudents() == 1


@pytest.mark.xfail
def test_student_number_not_fail(school):
    result = [["s1", "test_a"]]
    school.createStudent(result)
    assert school.getNumberOfStudents() == 2


@pytest.mark.skip
def test_student_number_skip(school):
    result = [["s1", "test_a"]]
    school.createStudent(result)
    assert school.getNumberOfStudents() == 3
