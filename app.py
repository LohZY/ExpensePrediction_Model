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
    


@app.route('/predict', methods=['POST'])
def predict():
    prediction = model.forecast(1)
    output = round(prediction[0], 2)
    response={
        "prediction": output
    }
    return jsonify(response)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')


# In[ ]:




