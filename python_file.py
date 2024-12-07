from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)


model = joblib.load('student_weight_predictor.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.json

        heights = input_data.get('heights', 0)

        if not heights:

            return jsonify({'error': 'No heights provided'}), 400
        
        predictions = model.predict([[h] for h in heights])

        return jsonify({'predictions': predictions.tolist()})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
