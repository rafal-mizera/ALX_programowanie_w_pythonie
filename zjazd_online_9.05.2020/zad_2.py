class Employee:
    pass






def test_init():
    employee = Employee("Jan", "Nowak", 100.0)
    assert employee
    assert employee.imie == "Jan"
    assert employee.nazwisko == "Nowak"
    assert employee.stawka == 100.0

def test_pay_salary1():
    employee = Employee("Jan", "Nowak", 100.0)
    assert employee.pay_salary() == 0
def test_pay_salary2():
    employee = Employee("Jan", "Nowak", 100.0)
    employee.register_time  = 5
    assert employee.pay_salary() == 500
def test_pay_salary2():
    employee = Employee("Jan", "Nowak", 100.0)
    employee.register_time = 10
    assert employee.pay_salary() == 1200

