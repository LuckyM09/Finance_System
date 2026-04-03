# Finance Tracking Backend System

## Overview
A Python-based backend system to manage financial transactions with role-based access and analytics.

## Tech Stack
- FastAPI
- SQLite
- SQLAlchemy

## Features
- CRUD operations on transactions
- Filtering by type, category, and date
- Financial analytics (income, expense, balance)
- User roles (Admin, Viewer, Analyst)

## API Endpoints
- /transactions
- /transactions/filter
- /analytics/summary
- /users

## How to Run
pip install -r requirements.txt
uvicorn app.main:app --reload

## API Docs
http://127.0.0.1:8000/docs

## Assumptions
- Basic header-based authentication used
- Single environment setup