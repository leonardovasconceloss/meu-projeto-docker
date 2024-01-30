from flask import Flask, request, jsonify
from models import db, Item

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db/appflaskpydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return "Seja bem vindo! Parece que deu tudo certo ao acessar minha aplicação - Att: Leonardo :) "

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = Item(name=data['name'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Item criado com sucesso!"}), 201

@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name} for item in items])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
