from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', prediction=None, color=None)

@app.route('/', methods=['POST'])
def predict():
    # Extract form data
    p1 = float(request.form['input_1'])
    p2 = float(request.form['input_2'])
    p3 = float(request.form['input_3'])
    p4 = float(request.form['input_4'])
    p5 = float(request.form['input_5'])
    p6 = float(request.form['input_6'])
    p7 = float(request.form['input_7'])
    p8 = float(request.form['input_8'])

    # Load the model
    model = joblib.load('model_joblib_diabetes')

    # Make prediction
    result = model.predict([[p1, p2, p3, p4, p5, p6, p7, p8]])

    # Set prediction result and color
    if result == 0:
        prediction = 'Non-Diabetic'
        color = 'green'
    else:
        prediction = 'Diabetic'
        color = 'red'

    return render_template('index.html', prediction=prediction, color=color)

if __name__ == '__main__':
    app.run(debug=True)
