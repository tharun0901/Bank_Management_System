from fastapi.testclient import TestClient
from main import app
test=TestClient(app)
def test_create_account():
    res=test.post("/create_account",json={
        "name":"tharun",
        "age":22,
        "branch":"hyd",
        "account_no":"123123",
        "balance":1000
    })
    assert res.json()["message"]=="Account created successfully"

def test_get_account():
    res=test.get("/account/123123")
    assert res.json()["account_no"] == "123123"
def test_deposit():
    res=test.post("/deposit",json={
        "account_no":"123123",
        "amount":500

    })
    assert res.json()["new_balance"]==1500
def test_withdraw():
    res=test.post("/withdraw",json={
        "account_no":"123123",
        "amount":300
    })
    assert res.json()["new_balance"]==1200