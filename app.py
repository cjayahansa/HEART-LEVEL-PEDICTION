from flask import Flask, render_template, request
import joblib
import numpy as np



model = joblib.load("myheart_risk_prediction_regression_model.sav")


app = Flask(__name__)
#emty app created

@app.route('/cheak')#web site eke url eke hama url ekata yatin aniwa funtion ekk thiyenne one
def hello_world():  # put application's code here
    return 'Hello World chamindu!' #function ekak thiyenne eka return karanne
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/')
def form():
    return render_template('form1.html')

@app.route('/submit', methods=['POST'])
def form_submit():
    name = request.form['name']
    email = request.form['email']

    return render_template('thankyou.html', name=name, email=email)

@app.route('/submit1', methods=['POST'])
def form_submit1():
    name = request.form['name']
    Gender = float(request.form['Gender'])
    age = float(request.form['age'])
    TC = float(request.form['TC'])
    HDL = float(request.form['HDL'])

    Smoke = float(request.form['Smoke'])
    BPM = float(request.form['BPM'])
    Diabetes = float(request.form['Diabetes'])

    # Corrected array creation
    test_data = np.array([Gender, age, TC, HDL, Smoke, BPM, Diabetes]).reshape(1, -1)

    # Make prediction
    prediction = model.predict(test_data)

    risk= prediction[0, 0]
    if risk < 20:
        risk_label = "Low Risk"
    elif risk < 50:
        risk_label = "Moderate Risk"
    else:
        risk_label = "High Risk"


    # Create result dictionary
    risk_level = {
        "name": name,
        "Gender": Gender,
        "age": age,
        "TC": TC,
        "HDL": HDL,
        "Smoke": Smoke,
        "BPM": BPM,
        "Diabetes": Diabetes,
        "risk": round(prediction[0,0], 2),
        "risk_label": risk_label
    }

    return render_template('Details.html', result=risk_level)


    #return render_template('Details.html', name=name, Gender=Gender, age=age, TC=TC, HDL=HDL, SBP=SBP, Smoke=Smoke, BPM=BPM, Diabetes=Diabetes)

#run the app
app.run(debug=True)#meken karanne funtion eka run karana eka
