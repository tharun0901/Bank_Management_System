from bank import Bank
from pydantic import BaseModel
from fastapi import FastAPI,HTTPException
import logging

app=FastAPI(title="Bank Management System API")
class createAccount(BaseModel):
   name:str
   age: int
   branch:str
   account_no:str
   balance:float=0.0
class Transaction(BaseModel):
   account_no:str
   amount:float

@app.post("/create_account")
def create_account(d:createAccount):
   try: 
      account=Bank(d.name, d.age ,d. branch, d.account_no, d.balance)
      account.file_write()
      account.database()
      return {"message":"Account created successfully"}
   except Exception as e:
      raise HTTPException(status_code=404,detail=str(e))
@app.get("/account/{account_no}")
def get_account(account_no:str):
   account=Bank.fetch_details(account_no)
   if account:
      return account.getter()
   raise HTTPException(status_code=404,detail="sorry, account not found")
@app.post("/deposit")
def deposit(d:Transaction):
   account=Bank.fetch_details(d.account_no)
   if not account:
     raise HTTPException(status_code=404,detail="aCCOUNT not found")
   account.deposit(d.amount)
   account.update_balance()
   account.file_write()
   return {
      "message":"Deposited",
      "new_balance":account.getter()["balance"]
   }
@app.post("/withdraw")
def withdraw(d: Transaction):
   account=Bank.fetch_details(d.account_no)
   if not account:
      raise HTTPException(status_code=404,detail="Account not found")
   account.withdraw(d.amount)
   account.update_balance()
   account.file_write()
   return {
      "message":"withdraw successfull",
      "new_balance":account.getter()["balance"]
   }