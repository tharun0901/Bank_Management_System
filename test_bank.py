from bank import Bank
import pytest

def test_getter():
    bank = Bank("tharun",22,"hyderabad","123456",1000.0)
    b = bank.getter()
    assert b["name"] == "tharun"
    assert b["age"] == 22
    assert b["branch"]=="hyderabad"
    assert b["account_no"] == "123456"
    assert b["balance"] == 1000.0
def test_deposit():
    bank=Bank("tharun",22,"hyderabad","123456",1500.0)
    bank.deposit(500.0)
    assert bank.getter()["balance"] == 2000.0
def test_withdraw():
    bank=Bank("tharun",22,"hyderabad","123456",1000.0)
    bank.withdraw(500.0)
    assert bank.getter()["balance"] == 500.0
def test_insufficient():
    bank=Bank("tharun",22,"hyderabad","123456",1.0)
    bank.withdraw(100.0)
    assert bank.getter()["balance"] == 1.0
def test_invaliddeposit():
    bank=Bank("tharun",22,"hyderabad","123456",1000.0)
    bank.deposit(0)
    assert bank.getter()["balance"] == 1000.0