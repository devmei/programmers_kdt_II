from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id": 1, "name": "Espresso", "price": 3800},
    {"id": 2, "name": "Americano", "price": 4100},
    {"id": 3, "name": "CafeLatte", "price": 4600},
]


@app.route('/')
def hello_flask():
    return "Hello World!"


@app.route('/menus')
# GET /menus   |  자료를 가지고 온다.
def get_menus():
    return jsonify({"menus": menus})


@app.route('/menus', methods=['POST'])
# POST /menus  |  자료를 자원에 추가한다.
def create_menus():
    # 전달받은 자료를 menus 자원에 추가
    # request가 JSON이라고 가정
    request_data = request.get_json()  # {"name": ..., "price": ...}
    new_menu = {
        "id": 4,
        "name": request_data['name'],
        "price": request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)


if __name__ == '__main__':
    app.run()