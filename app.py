from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Sample API',
    description='Design API Document',
)

@api.route('/my-resource/<id>')
@api.route('/product/<productName>')
@api.doc(params={'id': 'An ID'})
class MyResource(Resource):
    def get(self, id):
        return {}

    @api.response(403, 'Not Authorized')
    def post(self, id):
        api.abort(403)
    
    def post(self, productName):
        api.abort(403)


if __name__ == '__main__':
    app.run(debug=True)