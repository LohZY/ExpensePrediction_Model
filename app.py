#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from flask import Flask, request, render_template, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open('Models/model_transport.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    prediction = model.forecast(1)
    output = round(prediction[0],2)
    return jsonify(output)

#build another route for updating

if __name__ == "__main__":
    #app.debug = True
    app.run(host='0.0.0.0')


# # Another Method with HTML

# In[ ]:


# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     prediction = model.forecast(1)
#     output = round(prediction[0],2)
#     return render_template('index.html', prediction_text='Predicted Expenses is {}'.format(output))


# In[ ]:




