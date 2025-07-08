from fastapi.testclient import TestClient
from main import app
import random
test=TestClient(app)

account_no=str(random.randint(100,9999999999))
def test_create_account():
    res=test.post("/create_account",json={
        "name":"tharun",
        "age":22,
        "branch":"hyd",
        "account_no":account_no,
        "balance":1000
    })
    assert res.json()["message"]=="Account created successfully"

def test_get_account():
    res=test.get(f"/account/{account_no}")
    assert res.json()["account_no"] == account_no
def test_deposit():
    res=test.post("/deposit",json={
        "account_no":account_no,
        "amount":500

    })
    assert res.json()["new_balance"]==1500
def test_withdraw():
    res=test.post("/withdraw",json={
        "account_no":account_no,
        "amount":300
    })
    assert res.json()["new_balance"]==1200