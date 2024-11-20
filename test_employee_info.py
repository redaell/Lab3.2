import employee_info as ei
from employee_info import employee_data as ed

def test_get_employees_by_age_range():
    upper = 33
    lower = 29
    expected = [ed[0], ed[4]]
    result = ei.get_employees_by_age_range(lower,upper)
    assert(expected==result)

def test_calculate_average_salary():
    expected= 60166.67
    result=ei.calculate_average_salary()
    assert(expected==result)

def test_get_employees_by_dept():
    dept = "Sales"
    expected=[ed[0],ed[5]]
    result=ei.get_employees_by_dept(dept)
    assert(result==expected)