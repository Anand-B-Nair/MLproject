from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    inputs = [float(request.form[f'input_{i+1}']) for i in range(8)]

    model = joblib.load('model_joblib_diabetes')
    result = model.predict([inputs])

    if result == 0:
        prediction = 'Non-Diabetic'
        color = 'green'
    else:
        prediction = 'Diabetic'
        color = 'red'

    return render_template('index.html', prediction=prediction, color=color)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
