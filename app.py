from flask import Flask,request,jsonify
from bank import Bank
app=Flask(__name__)
@app.route('/')
def home():  
    return jsonify({
        "message":"      Welcome to Bank services     ",
        "routes":{
            "Create account":"/create-account",
            "Fetch account":"/acount/<account_no",
            "Deposit":"/deposit/<account_no>",
            "withdraw":"/withdraw/<account_no>"
        }
    })
@app.route('/create-account',methods=['post'])
def create_account():
    data=request.get_json()
    name=data.get('name')
    age=data.get('age')
    branch=data.get('branch')
    account_no=data.get('account_no')
    balance=data.get('balance',0.0)
    account=Bank(name,int(age),branch,account_no,float(balance))
    account.file_write()
    account.database()
    return jsonify({
        "message":"Acccount created succussfully",
        "account_details":account.getter()
    })
@app.route('/account/<account_no>',methods=['GET'])
def fetch_account(account_no):
    account=Bank.fetch_details(account_no)
    if account:
        return jsonify({
            "Account detaiils":account.getter()
        })
    else:
        return jsonify({
            "message":"Account not found"
        })
@app.route('/deposit/<account_no>',methods=['PUT'])
def deposit(account_no):
    data=request.get_json()
    amount=data.get('amount')
    if amount <=0:
        return jsonify({
            "message":"Invalid amount"
        })
    account =Bank.fetch_details(account_no)
    if account:
        account.deposit(float(amount))
        account.file_write()
        account.update_balance()
        return jsonify({
            "message":f"{amount} deposited successfully",
            "new_balance":account.getter()['balance']
        })
    else:
        return jsonify({"message":"account not found"})
@app.route('/withdraw/<account_no>',methods=['PUT'])
def withdraw(account_no):
    data=request.get_json()
    amount=data.get('amount')
    if amount <=0:
        return jsonify({"messsage":"Inavalid withdraw"})
    account=Bank.fetch_details(account_no)
    if account:
        if amount> account.getter()['balance']:
            return jsonify({"message":"Insufficient balance"})
        account.withdraw(float(amount))
        account.file_write()
        account.update_balance()
        return jsonify({
            "message":f"{amount} withdraw successfull",
            "new_balance":account.getter()['balance']
        })
    else:
        return jsonify({"message":"account  not found"})
if __name__ == '__main__':
   app.run(debug=True)