from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Загрузка модели из файла
model = joblib.load('/Users/shklyarmike/xgb_gs.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)  # Получаем данные из POST запроса
    prediction = model.predict(data)  # Делаем предсказание
    return jsonify(prediction.tolist())  # Возвращаем предсказания в JSON формате

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Запуск сервера на всех доступных IP адресах