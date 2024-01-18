from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle the form submission
        p1 = float(request.form['input_1'])
        p2 = float(request.form['input_2'])
        p3 = float(request.form['input_3'])
        p4 = float(request.form['input_4'])
        p5 = float(request.form['input_5'])
        p6 = float(request.form['input_6'])
        p7 = float(request.form['input_7'])
        p8 = float(request.form['input_8'])
        
        model = joblib.load('model_joblib_diabetes')
        result = model.predict([[p1, p2, p3, p4, p5, p6, p7, p8]])

        prediction = "Non-Diabetic" if result == 0 else "Diabetic"
        color = "green" if result == 0 else "red"
        return render_template('index.html', prediction=prediction, color=color)

    # Render the initial form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
