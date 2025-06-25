from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# ✅ Load trained pipeline model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = {
            'Age': float(request.form['Age']),
            'TypeofContact': request.form['TypeofContact'],
            'CityTier': int(request.form['CityTier']),
            'DurationOfPitch': float(request.form['DurationOfPitch']),
            'Occupation': request.form['Occupation'],
            'Gender': request.form['Gender'],
            'NumberOfFollowups': float(request.form['NumberOfFollowups']),
            'ProductPitched': request.form['ProductPitched'],
            'PreferredPropertyStar': float(request.form['PreferredPropertyStar']),
            'MaritalStatus': request.form['MaritalStatus'],
            'NumberOfTrips': float(request.form['NumberOfTrips']),
            'Passport': int(request.form['Passport']),
            'PitchSatisfactionScore': int(request.form['PitchSatisfactionScore']),
            'OwnCar': int(request.form['OwnCar']),
            'Designation': request.form['Designation'],
            'MonthlyIncome': float(request.form['MonthlyIncome']),
            'TotalVisits': float(request.form['TotalVisits']),
        }

        input_df = pd.DataFrame([input_data])
        prediction = model.predict(input_df)[0]
        output = "Yes" if prediction == 1 else "No"

        return render_template("result.html", prediction=output)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)


