import pytest
from learn_pytest.src.py_testing import School
# general purpose fuxture for your whole project
# without having to import


@pytest.fixture(scope="session")
def school():
    s1 = School("school1")
    return s1
