from flask import Flask, request

app = Flask(__name__)


@app.route('/currency', methods=['GET'])
def get_currency():
    # Отримуємо параметри з URL
    today = request.args.get('today')
    key = request.args.get('key')

    # Статичний курс валют
    currency_rate = "USD - 41.5"

    return f"Курс валют: {currency_rate}"


if __name__ == '__main__':
    app.run(debug=True)
