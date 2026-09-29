import pytest
from app2.calculations import add, BankAcc

@pytest.fixture
def zero_bank_acc():
    return BankAcc()

@pytest.fixture
def bank_acc():
    return BankAcc(45)
@pytest.mark.parametrize("num1, num2, expected", [(4,5,9),(1,2,3)])

def test_add(num1,num2,expected):
    assert add(num1, num2) == expected

def test_bank():
    bankacc = BankAcc(50)
    assert bankacc.balance == 50

def test_bank0(zero_bank_acc):
    # bankacc = BankAcc()
    assert zero_bank_acc.balance == 0

def test_bankdep():
    bankacc = BankAcc(50)
    bankacc.deposit(20)
    assert bankacc.balance == 70


def test_bankwit():
    bankacc = BankAcc(50)
    bankacc.withdrow(20)
    assert bankacc.balance == 30

