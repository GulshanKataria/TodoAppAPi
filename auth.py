from flask import request
#!flask/bin/python
from flask import Flask
from flask_restful import Resource,Api,reqparse,abort
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'gulshan':
        return 'gulshanpassword'
    return None

@app.route('/todos', methods=['GET'])
@auth.login_required
@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

def get(self,todo_id):
        return todos[todo_id]
if __name__ == '__main__':
    app.run(debug=True)