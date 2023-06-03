# Профиль

from flask import Flask

app = Flask(__name__)


@app.route("/profile/<uid>")
def page_profile(uid):
    return f"<h1>Профиль {uid}</h1>"

#Превращаем строковый тип в число

# @app.route('/users/<int:uid>')
# def profile(uid):
#     print(uid)
#     print(type(uid))
#     return ""

@app.route("/catalog/items/<itemid>")
def profile(itemid):
    return f'<h1>Страничка товара {itemid}</h1>'

app.run(host='0.0.0.0', port=8000)