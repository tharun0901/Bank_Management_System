from bank import Bank
import pytest

@pytest.fixture
def bank():
    return Bank("tharun", 22, "hyderabad", "123456", 1000.0)
def test_getter(bank):
    b = bank.getter()
    assert b["name"] == "tharun"
    assert b["age"] == 22
    assert b["branch"]=="hyderabad"
    assert b["account_no"] == "123456"
    assert b["balance"] == 1000.0
@pytest.mark.parametrize("initial,deposit_amount,expected_balance",[
   (1000,500,1500),
   (1000,1000,2000),
   (1000,5000,6000)
])
def test_deposit(initial,deposit_amount,expected_balance):
    b=Bank("tharun",22,"hyd","123",initial)
    b.deposit(deposit_amount)
    assert b.getter()["balance"] == expected_balance
@pytest.mark.parametrize("initial,withdraw_amount,expected_balance",[ 
    (1000,300,700),
    (700,200,500)
])
def test_withdraw(initial,withdraw_amount,expected_balance):
    b=Bank("tharun",22,"hyd","123",initial)
    b.withdraw(withdraw_amount)
    assert b.getter()["balance"] == expected_balance
def test_insufficient(bank):
     bank.withdraw(2000.0)
     assert bank.getter()["balance"] == 1000.0
def test_invaliddeposit(bank):
   bank.deposit(-1)
   assert bank.getter()["balance"] == 1000.0