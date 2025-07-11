# Bank Management System using FastAPI and Oracle Database
This is a **Bank Management System** built using **FastAPI** and **Oracle Database**.It helps you perform operations like Create acoount,Fetching your details,deposit and withdraw
It also comes with **automated testing** and runs **unit test**" every time you push on githhub

## Features

-Creating a new bank account
 Create a new bank account
- View existing account details
- Deposit money into an account
- Withdraw money from an account
- Store account data in both a `.txt` file and Oracle DB
- Run automated tests using GitHub Actions
- Supports mock database testing

## Technologies used

-**FastAPI**-Web framework for API
-**cx_Oracle**- Oracle database driver for python
-**python-dotenv**- Manage environment variables
-**pytest**- unit testing and running test
-**unitest.mock**- for mocking DB connections
-**TestClient**- to simulate API requests
-**Docker** - to containerize the app and database
-**GitHub Actions**- for automated testing on push

## How to run
1.Clone the Repository
  ```bash
 command:git clone https://github.com/tharun0901/Bank_Management_System
 cd Bank_Management_System_Project
2.Make sure Docker open
3.Build and Start the Containers
 Command:docker-compose up --build -d
4.Open the FastApI Docs
  After the container Start,visit:
  http://localhost:8000/docs
5.Run Test cases
  docker exec -it bank-app pytest test_api.py



