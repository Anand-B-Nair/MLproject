from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                background-image: url('bg.jpg');
                background-size: cover;
                background-repeat: no-repeat;
                /* Your additional CSS styling goes here */
            }
            
            form {
                margin-top: 20px;
            }

            label {
                display: block;
                margin-bottom: 5px;
            }

            input {
                margin-bottom: 10px;
            }

            button {
                padding: 10px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }

            h2 {
                font-size: 20px;
                font-weight: bold;
                margin-top: 20px;
            }
        </style>
        <title>Diabetes Prediction</title>
    </head>
    <body>
        <!-- Your HTML content goes here -->

        <form method="post" action="/">
            <label>Pregnancies:</label>
            <input type="text" name="input_1" required><br>

            <label>Glucose:</label>
            <input type="text" name="input_2" required><br>

            <label>Enter Value of BloodPressure:</label>
            <input type="text" name="input_3" required><br>

            <label>Enter Value of SkinThickness:</label>
            <input type="text" name="input_4" required><br>

            <label>Enter Value of Insulin:</label>
            <input type="text" name="input_5" required><br>

            <label>Enter Value of BMI:</label>
            <input type="text" name="input_6" required><br>

            <label>Enter Value of DiabetesPedigreeFunction:</label>
            <input type="text" name="input_7" required><br>

            <label>Enter Value of Age:</label>
            <input type="text" name="input_8" required><br>

            <button type="submit">Predict</button>
        </form>

        {% if prediction %}
            <h2 style="color: {{ color }}; font-weight: bold;">{{ prediction }}</h2>
        {% endif %}
    </body>
    </html>
    """

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
