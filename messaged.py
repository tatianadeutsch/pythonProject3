# Вызов сообщений

from flask import Flask

app = Flask(__name__)


@app.route('/message/')
def page_messages():
    return "Сообщения пользователя"


app.run(host='0.0.0.0', port=8000)