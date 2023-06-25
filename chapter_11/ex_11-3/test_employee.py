import pytest

from employee import Employee

@pytest.fixture
def martin():
    """Create employee instance"""
    employee_martin = Employee('martin', 'luciana', 30000)
    return employee_martin


def test_give_default_raise(martin):
    """Testing the default raise of 5000"""
    martin.give_raise()
    assert martin.salary == 35000

def test_give_custom_raise(martin):
    """Testing the default raise of 8000"""
    martin.give_raise(10000)
    assert martin.salary == 40000

#def test_give_default_raise():
#    """Testing the default raise of 5000"""
#    employee_martin = Employee('martin', 'luciana', 30000)
#    employee_martin.give_raise()
#    assert employee_martin.salary == 35000
#
#def test_give_custom_raise():
#    """Testing the default raise of 8000"""
#    employee_martin = Employee('martin', 'luciana', 30000)
#    employee_martin.give_raise(10000)
#    assert employee_martin.salary == 40000
