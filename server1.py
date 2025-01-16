from flask import Flask, request  # Импортируем Flask

app = Flask(__name__)  # Создаем приложение Flask

@app.route("/", methods=['GET'])  # Обрабатываем GET-запрос на главной странице
def hello_world():
    return "Hello World!"  # Возвращаем текст (отступ исправлен!)

if __name__ == '__main__':
    app.run(port=5000)  # Запускаем сервер на порту 5000