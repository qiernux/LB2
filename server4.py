import requests
from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# Функція для отримання курсу валюти з API НБУ
def fetch_currency_rate(date):
    # Формуємо URL для запиту (исправлен разрыв строки)
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date={date}&json"

    # Надсилаємо GET-запит до API НБУ
    response = requests.get(url)

    # Перевіряємо статус відповіді
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['rate']  # Повертаємо курс
    return None  # Якщо немає відповіді або вона некоректна

@app.route('/currency', methods=['GET'])
def get_currency_rate():
    # Отримуємо параметр 'param' із URL
    param = request.args.get('param')

    if param == 'today':
        # Формуємо поточну дату у форматі YYYYMMDD
        date = datetime.now().strftime('%Y%m%d')
    elif param == 'yesterday':
        # Формуємо дату попереднього дня
        date = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')
    else:
        # Неправильний параметр
        return jsonify({"error": "Invalid parameter. Use 'today' or 'yesterday'."}), 400

    # Отримуємо курс валюти
    rate = fetch_currency_rate(date)

    if rate:
        # Повертаємо курс у форматі JSON
        return jsonify({"USD": rate, "date": date})
    else:
        # Якщо не вдалося отримати курс
        return jsonify({"error": "Unable to fetch currency rate from NBU."}), 500

if __name__ == '__main__':
    # Запускаємо сервер
    app.run(host='127.0.0.1', port=8000, debug=True)