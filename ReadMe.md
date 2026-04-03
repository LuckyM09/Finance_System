# 💰 Finance Tracking Backend System

## 📌 Overview

A Python-based backend system built using FastAPI to manage financial transactions such as income and expenses. The system provides CRUD operations, filtering, analytics, and role-based access control.

---

## 🚀 Features

### 🔹 Financial Records Management

* Create, Read, Update, Delete transactions
* Fields: amount, type (income/expense), category, date, notes
* Filter transactions by:

  * Type
  * Category
  * Date range

### 📊 Analytics

* Total income
* Total expenses
* Current balance
* Category-wise breakdown
* Monthly summaries

### 👤 User Roles

* **Admin**: Full access (create, update, delete)
* **Viewer**: Read-only access
* **Analyst**: Can view and filter data

### 🔐 Authentication (Simplified)

* Header-based user identification (`username`)
* Role-based access control

---

## 🛠 Tech Stack

* FastAPI
* SQLite
* SQLAlchemy
* Pydantic

---

## 📂 Project Structure

app/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── routes/
│   ├── transactions.py
│   ├── users.py
│   └── analytics.py

---

## ⚙️ Setup Instructions

### 1. Clone Repository

git clone https://github.com/LuckyM09/Finance_System.git
cd Finance_System

### 2. Create Virtual Environment

python -m venv venv
source venv/Scripts/activate  (Windows Git Bash)

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run Server

uvicorn app.main:app --reload

---

## 📘 API Documentation

Open in browser:
http://127.0.0.1:8000/docs

---

## 🧪 Example Usage

### Create User

POST /users
{
"username": "admin1",
"role": "admin"
}

### Create Transaction

Header:
username: admin1

Body:
{
"amount": 1000,
"type": "income",
"category": "salary",
"date": "2025-04-01",
"note": "salary"
}

---

## ⚠️ Assumptions

* Simple header-based authentication used
* No password system implemented
* Single-user environment for testing

---

## 📈 Future Improvements

* JWT Authentication
* Pagination
* CSV Export
* Frontend Dashboard Integration

---

## 👨‍💻 Author

Lucky Meena
