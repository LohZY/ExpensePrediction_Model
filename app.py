#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, Float, String, Date
from sqlalchemy.orm import sessionmaker, declarative_base
import pymysql
import pickle

app = Flask(__name__)

model = pickle.load(open('Models/model_transport.pkl', 'rb'))
# add all other models in
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:Amazonloh!2828@expensedb.cnsuso6sw07n.ap-southeast-1.rds.amazonaws.com:3306/flaskaws'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Create the table and its columns
class FoodExpense(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(50), nullable=False)
    merchant_name = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)

class TransportExpense(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(50), nullable=False)
    merchant_name = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)

class UtilityExpense(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(50), nullable=False)
    merchant_name = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)

class EntertainmentExpense(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(50), nullable=False)
    merchant_name = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

#Each expense category is its own end point
@app.route('/addFood', methods=['POST'])
def create_food_expense():
    data = request.get_json()
    new_expense = FoodExpense(
        category=data['category'],
        merchant_name=data['merchant_name'],
        date=data['date'],
        amount=data['amount']
    )
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({"message": "Food expense added successfully!"}), 201

#endroute to add Transport expense
@app.route('/addTransport', methods=['POST'])
def create_transport_expense():
    data = request.get_json()
    new_expense = TransportExpense(
        category=data['category'],
        merchant_name=data['merchant_name'],
        date=data['date'],
        amount=data['amount']
    )
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({"message": "Transport expense added successfully!"}), 201

#endroute to add Entertainment expense
@app.route('/addEntertainment', methods=['POST'])
def create_entertainment_expense():
    data = request.get_json()
    new_expense = EntertainmentExpense(
        category=data['category'],
        merchant_name=data['merchant_name'],
        date=data['date'],
        amount=data['amount']
    )
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({"message": "Entertainment expense added successfully!"}), 201

#endroute to add Utility expense
@app.route('/addUtility', methods=['POST'])
def create_utility_expense():
    data = request.get_json()
    new_expense = UtilityExpense(
        category=data['category'],
        merchant_name=data['merchant_name'],
        date=data['date'],
        amount=data['amount']
    )
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({"message": "Utility expense added successfully!"}), 201

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    weeks = data['month']

    if isinstance(weeks, list) and len(weeks) >= 4:
        print("take last four")
        weeks = weeks[-4:]
    elif isinstance(weeks, list) and len(weeks) < 4:
        print("dun take last four")
      
        
    prediction = model.forecast(weeks)
    total_sum = sum(prediction)
    output = round(total_sum, 2)
    response={
        "prediction": output
    }
    return jsonify(response)

@app.route('/getAllExpenses', methods=['GET'])
def getAllExpenses():
    food_expenses = FoodExpense.query.all()
    transport_expenses = TransportExpense.query.all()
    utility_expenses = UtilityExpense.query.all()
    entertainment_expenses = EntertainmentExpense.query.all()

    # Combine all expenses into a single list
    all_expenses = []

    for expense in food_expenses:
        all_expenses.append({
            "id": expense.id,
            "category": expense.category,
            "merchant_name": expense.merchant_name,
            "date": str(expense.date),
            "amount": expense.amount
        })

    for expense in transport_expenses:
        all_expenses.append({
            "id": expense.id,
            "category": expense.category,
            "merchant_name": expense.merchant_name,
            "date": str(expense.date),
            "amount": expense.amount
        })

    for expense in utility_expenses:
        all_expenses.append({
            "id": expense.id,
            "category": expense.category,
            "merchant_name": expense.merchant_name,
            "date": str(expense.date),
            "amount": expense.amount
        })

    for expense in entertainment_expenses:
        all_expenses.append({
            "id": expense.id,
            "category": expense.category,
            "merchant_name": expense.merchant_name,
            "date": str(expense.date),
            "amount": expense.amount 
        })

    # Sort the combined list by date
    all_expenses.sort(reverse=True, key=lambda x: x['date'])
    return jsonify(all_expenses)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')


# In[ ]:




