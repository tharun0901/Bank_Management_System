from fastapi.middleware.cors import CORSMiddleware
from bank import Bank
from pydantic import BaseModel
from fastapi import FastAPI,HTTPException,UploadFile,File
import logging
import base64
import uuid
import os

app=FastAPI(title="Bank Management System API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class ImageData(BaseModel):
   image:str

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
   if d.amount <= 0:
      raise HTTPException(status_code=400, detail="Invalid deposit amount")
    
   account=Bank.fetch_details(d.account_no)
   if not account:
     raise HTTPException(status_code=404,detail="aCCOUNT not found")
   account.deposit(d.amount)
   account.update_balance()
   account.file_write()
   return {
      "account_no":account.getter()["account_no"],
      "amount":d.amount,
      "message":"Deposited",
      "new_balance":account.getter()["balance"]
   }
@app.post("/withdraw")
def withdraw(d: Transaction):
   if d.amount <= 0:
      raise HTTPException(status_code=400, detail="Invalid withdrawal amount")
   account=Bank.fetch_details(d.account_no)
   if not account:
      raise HTTPException(status_code=404,detail="Account not found")
   if d.amount > account.getter()["balance"]:
      raise HTTPException(status_code=400, detail="Insufficient balance for withdrawal.")
   account.withdraw(d.amount)
   account.update_balance()
   account.file_write()
   return {
      "account_no":account.getter()["account_no"],
      "amount":d.amount,
      "message":"withdraw successfull",
      "new_balance":account.getter()["balance"]
   }
@app.post("/upload-video")
async def upload_video(file:UploadFile=File(...)):
   try:
      os.makedirs("videos",exist_ok=True)
      filename = f"recording_{uuid.uuid4().hex[:8]}.webm"
      save_path=os.path.join("videos",filename)
      with open(save_path,"wb") as f:
         f.write(await file.read())
         return {"message":"uploaded successfully","filename":filename}
   except Exception as e:
      raise HTTPException(status_code=500,detail=str(e))