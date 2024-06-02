from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Loading our model from file
model = joblib.load('/Users/shklyarmike/xgb_gs.joblib')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        data = request.form.to_dict()
        data = {k: [float(v)] for k, v in data.items()}  # Transforming values to float
        data_frame = pd.DataFrame(data)
        # Prediction of the model
        prediction = model.predict(data_frame)
        result = 'Fraud' if prediction[0] == 1 else 'Not Fraud'
        # Turn the result back on the new page
        return render_template('result.html', prediction=result)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')