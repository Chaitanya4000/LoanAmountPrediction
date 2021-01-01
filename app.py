import pickle
import os

from flask import Flask, request, jsonify

app = Flask(__name__)

try:
    modelpath = os.path.join(os.getcwd(),'Model/Regressor')
    with open(modelpath, 'rb') as f:
        model = pickle.load(f)
    print(modelpath,'This was success')
except Exception as e:
    print(str(e))

@app.route('/hello')
def hello():
    return 'hi'


@app.route('/LoanAmountPrediction', methods=['GET', 'POST'])
def SalaryPredict():
    Age = request.json['Age']
    AnnualIncome = request.json['AnnualIncome']
    ExisitingLoans = request.json['ExisitingLoans']
    AnnualIncomeOfCoApplicant = request.json['AnnualIncomeOfCoApplicant']
    exp_input = [Age,AnnualIncome,ExisitingLoans,AnnualIncomeOfCoApplicant]
    PredictedLoanAmount = model.predict([exp_input])
    return jsonify({'results': PredictedLoanAmount[0]})


if __name__ == "__main__":
    app.run()