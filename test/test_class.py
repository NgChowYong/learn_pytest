import pytest
from learn_pytest.src.py_testing import School

# pytest will execute all the files with format test_* or *_test
# in the current directory and subdirectories.


class TestClassDemo:
    # test fixture in class
    @pytest.fixture
    def fixture(self) -> int:
        return 1

    def test1(self, fixture):
        assert 1 == fixture

    def test2(self):
        assert 1 == 1
