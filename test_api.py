from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch,MagicMock
import random
test=TestClient(app)

account_no=str(random.randint(100,9999999999))
@patch("bank.cx_Oracle.connect")
def test_create_account(mock_connect):
    mock_conn=MagicMock()
    mock_cursor=MagicMock()
    mock_cursor.fetchone.side_effect=[None]
    mock_conn.cursor.return_value=mock_cursor
    mock_connect.return_value=mock_conn
    res=test.post("/create_account",json={
        "name":"tharun",
        "age":22,
        "branch":"hyd",
        "account_no":account_no,
        "balance":1000
    })
    assert res.json()["message"]=="Account created successfully"
@patch("bank.cx_Oracle.connect")
def test_get_account(mock_connect):
    mock_conn=MagicMock()
    mock_cursor=MagicMock()
    mock_cursor.fetchone.return_value=("tharun",22,"hyd",account_no,1000.0)
    mock_conn.cursor.return_value=mock_cursor
    mock_connect.return_value=mock_conn
    res=test.get(f"/account/{account_no}")
    assert res.json()["account_no"] == account_no
    assert res.json()["balance"] == 1000.0
@patch("bank.cx_Oracle.connect")
def test_deposit(mock_connect):
     mock_conn = MagicMock()
     mock_cursor = MagicMock()
     mock_cursor.fetchone.return_value=("tharun",22,"hyd",account_no,1000.0)
     mock_conn.cursor.return_value=mock_cursor
     mock_connect.return_value=mock_conn
     res=test.post("/deposit",json={
        "account_no":account_no,
        "amount":500

    })
     assert res.json()["new_balance"]==1500
@patch("bank.cx_Oracle.connect")
def test_withdraw(mock_connect):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value=("tharun",22,"hyd",account_no,1000.0)
    mock_conn.cursor.return_value=mock_cursor
    mock_connect.return_value=mock_conn
    res=test.post("/withdraw",json={
        "account_no":account_no,
        "amount":300
    })
    assert res.json()["new_balance"]==700