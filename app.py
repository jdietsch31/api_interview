import random
from site import addusersitepackages
import sqlite3
from flask import Flask, render_template, request, jsonify, redirect, session
from flask import abort
from flask_cors import CORS, cross_origin
from flask import make_response, url_for
import json
from time import gmtime, strftime

app = Flask (__name__, template_folder='template')

#@app.route('/')
# def hello():
# return 'Hello, World!';

@app.route("/api/v1/info")
def home_index():
    conn = sqlite3.connect('windb.db')
    print ("opened database successfully");
    api_list=[]
    cursor = conn.execute("SELECT buildtime, version, methods, links from apirelease")
    for row in cursor:
      api = {}
      api['version'] = row[0]
      api['buildtime'] = row[1]
      api['methods'] = row[2]
      api['links'] = row[3]
      api_list.append(api)
    conn.close()
    return jsonify({'api version': api_list}), 200

@app.route("/api/v1/users", methods=['GET'])
def get_users():
        return list_users()
def list_users():
        conn = sqlite3.connect ('windb.db')
        print("opened database sucessfully");
        api_list=[]
        cursor = conn.execute("SELECT username, full_name, email, password, id from users")
        for row in cursor:
                a_dict ={}
                a_dict['username'] = row[0]
                a_dict['name'] =row[1]
                a_dict['email'] =row[2]
                a_dict['password'] =row[3]
                a_dict['id'] =row[4]
                api_list.append(a_dict)
        conn.close()
        return jsonify ({'user list': api_list}), 200

@app.route('/api/v1/users', methods=['POST'])
def create_user():
    if not request.json or not 'username' in request.json or not 'email' in request.json or not 'password' in request.json:
        abort(400)
    user = {
        'username': request.json['username'],
        'email': request.json['email'],
        'name': request.json.get('name',""),
        'password': request.json['password']
    }
    return jsonify({'status': add_user(user)}), 201



@app.errorhandler(400)
def invalid_request(error):
        return make_response(jsonify({'error': 'Bad Request'}), 400)

def add_user(new_user):
    conn = sqlite3.connect('windb.db')
    print ("Opened database successfully");
    api_list=[]
    cursor=conn.cursor()
    cursor.execute("SELECT * from users where username=? or email=?",(new_user['username'],new_user['email']))
    data = cursor.fetchall()
    if len(data) != 0:
        abort(409)
    else:
       cursor.execute("insert into users (username, email, password, full_name) values(?,?,?,?)",(new_user['username'],new_user['email'], new_user['password'], new_user['name']))
       conn.commit()
       return "Success"
    conn.close()
    return jsonify(a_dict)

@app.route('/adduser')
def adduser():
        return render_template('adduser.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)
  
