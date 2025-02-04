from flask import Flask, request
import pickle
import sklearn

model = open("classifier.pkl", "rb")
clf = pickle.load(model)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Ashish</p>"

@app.route("/ping", methods = ['GET'])
def pinger():
    return "<h1>Pinged the server</h1>"

@app.route("/predict", methods = ['POST'])
def prediction():
    # Pre-processing user input

    loan_req = request.get_json()
    print(loan_req)

    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1

    if loan_req['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1

    if loan_req['Credit_History'] == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount'] / 1000

    # Making predictions
    prediction = clf.predict(
        [[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred

