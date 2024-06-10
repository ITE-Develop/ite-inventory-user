from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import Products, db, User, Rooms
from flasgger import Swagger

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:itedb001@localhost/postgres'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

swagger = Swagger(app)
db.init_app(app)


@app.route('/')
def hello_world():
    return 'Welcome to the ITE-Inventory Project API backend'

#   add products 
@app.route('/product', methods=['POST'])
def create_product():
    data = request.get_json()
    required_keys = ['name', 'code','image', 'description',
                     'expiry_date', 'purchase_date', 'location', 'users']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Missing required fields'}), 400

    new_product = Products(
        name=data['name'],
        code=data['code'],
        image=data['image'],
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

 # view all products 
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
 
    # Update Products 
@app.route('/product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = Products.query.get(product_id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404

    required_keys = ['name', 'code', 'image', 'description',
                     'expiry_date', 'purchase_date', 'location', 'users']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Missing required fields'}), 400

    product.name = data['name']
    product.code = data['code']
    product.image = data['image']
    product.description = data['description']
    product.expiry_date = data['expiry_date']
    product.purchase_date = data['purchase_date']
    product.location = data['location']
    product.users = data['users']
    product.category = data.get('category', product.category)
    product.availability = data.get('availability', product.availability)

    db.session.commit()
    return jsonify({'message': 'Product updated successfully'}), 200

    #deleted Products 
@app.route('/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Products.query.get(product_id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404

    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 200

 # View Products by id 
@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Products.query.get(product_id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404

    product_data = {
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
    return jsonify(product_data)

 

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    required_keys = ['username', 'image','age', 'group',
                     'phone_number', 'department', 'generation']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Missing required fields'}), 400

    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User added successfully'}), 201


# View user by id
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    user_data = {
        'id': user.id,
        'username': user.username,
        'image': user.image,
        'age': user.age,
        'group': user.group,
        'phone_number': user.phone_number,
        'department': user.department,
        'generation': user.generation
    }
    return jsonify(user_data)


# Views All users 
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [
        {
            'id': user.id,
            'username': user.username,
            'image':user.image,
            'age': user.age,
            'group': user.group,
            'phone_number': user.phone_number,
            'department': user.department,
            'generation': user.generation
        }
        for user in users
    ]
    return jsonify(users_list)
#Deleted user 
@app.route('/user/<int:users_id>', methods=['DELETE'])
def  delete_user():
    user = users.query.get(users_id)
    if user is None:
        return jsonify({'error':'User Not Found'}), 404

        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User Deleted successfully '}), 200

#update users 
@app.route('/user/<int:users_id>', methods=['PUT'])
def update_user():
    user = users.query.get(users_id)
    if user is None:
        return jsonify({'error': 'User not Found'}), 404

    required_keys =['username', 'image', 'age', 'group','phone_number','department','generation']
    if not all(key in data for key in required_keys):
        return jsonify({'error':'Missing required fields'}), 404 

        user.username= data['username']
        user.image = data['image']
        user.age = data['age']
        user.group = data['group']
        user.phone_number = data['phone_number']
        user.department = data['department']
        user.generation = data['generation']

        db.session.commit()
        return jsonify({'message':'user updated'}),200


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
