from flask import Flask, request, jsonify
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    # Отримуємо значення заголовка "Content-Type"
    content_type = request.headers.get('Content-Type')

    # Статичні дані
    data = {"currency": "USD", "rate": 41.5}

    if content_type == 'application/json':
        return jsonify(data)  # Повертаємо JSON документ

    elif content_type == 'application/xml':
        # Створюємо XML з даних
        root = ET.Element("currency")
        ET.SubElement(root, "currency_name").text = data["currency"]
        ET.SubElement(root, "rate").text = str(data["rate"])
        xml_data = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
        return xml_data, 200, {'Content-Type': 'application/xml'}

    else:
        # Явно вказуємо UTF-8 для тексту (ИСПРАВЛЕННАЯ ОШИБКА)
        return "Курс валют: USD - 41.5", 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(debug=True)