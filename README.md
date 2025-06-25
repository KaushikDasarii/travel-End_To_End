# Travel Product Prediction - Flask App

This is a simple Flask application that predicts whether a travel product will be taken by a customer based on input features.

## Features
- Uses a trained machine learning model (`cleaned_travel.pkl`)
- User-friendly input form with proper datatype handling
- Predicts `ProdTaken` as Yes/No

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/YOUR_USERNAME/travel-End_To_End.git
   cd travel-End_To_End
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the app:
   ```
   python app.py
   ```

4. Or deploy with Gunicorn (e.g. on Render or Heroku):
   ```
   gunicorn app:app
   ```

## File Structure

```
travel-flask-app/
├── app.py
├── cleaned_travel.pkl
├── requirements.txt
├── README.md
└── templates/
    ├── index.html
    └── result.html
```
