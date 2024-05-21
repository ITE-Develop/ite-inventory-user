from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import Products, db, User, Rooms


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:itedb001@localhost/postgres'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)


@app.route('/')
def hello_world():
    return 'Welcome to the ITE-Inventory Project API backend'


@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    required_keys = ['name', 'code', 'description',
                     'expiry_date', 'purchase_date', 'location', 'users']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Missing required fields'}), 400

    new_product = Products(
        name=data['name'],
        code=data['code'],
        description=data['description'],
        expiry_date=data['expiry_date'],
        purchase_date=data['purchase_date'],
        location=data['location'],
        users=data['users'],
        category=data['category'],
        availability=data['availability']

    )
    new_product = Products(**data)
    db.session.add(new_product)
    db.session.commit()

    return jsonify({'message': 'Product added successfully'}), 201


@app.route('/products', methods=['GET'])
def get_products():
    products = Products.query.all()
    products_list = [
        {
            'id': product.id,
            'name': product.name,
            'code': product.code,
            'description': product.description,
            'expiry_date': product.expiry_date,
            'purchase_date': product.purchase_date,
            'location': product.location,
            'users': product.users,
            'category': product.category,
            'availability': product.availability


        }
        for product in products
    ]
    return jsonify(products_list)


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    required_keys = ['username', 'age', 'group',
                     'phone_number', 'department', 'generation']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Missing required fields'}), 400

    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User added successfully'}), 201


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [
        {
            'id': user.id,
            'username': user.username,
            'age': user.age,
            'group': user.group,
            'phone_number': user.phone_number,
            'department': user.department,
            'generation': user.generation
        }
        for user in users
    ]
    return jsonify(users_list)


@app.route('/rooms', methods=['POST'])
def add_room():
    data = request.get_json()
    required_keys = ['building', 'chairs', 'num_tables',
                     'board', 'number']

    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Missing required fields'}), 400

    new_room = Rooms(**data)
    db.session.add(new_room)
    db.session.commit()

    return jsonify({'message': 'Room has been added'}), 201


@app.route('/rooms', methods=['GET'])
def get_rooms():
    rooms = Rooms.query.all()
    rooms_list = [
        {
            'id': room.id,
            'building': room.building,
            'chairs': room.chairs,
            'num_tables': room.num_tables,
            'board': room.board,
            'number': room.number
        }
        for room in rooms
    ]

    return jsonify(rooms_list)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
