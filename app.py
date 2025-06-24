from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ml/predict')
def predict():
    return jsonify({'result': 'Prediction from Python ML service'})

if __name__ == '__main__':
    app.run(port=6000)
