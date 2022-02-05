import sqlite3
from flask import Flask, request, jsonify
from flask import abort
from flask import make_response, url_for
import json
from time import gmtime, strftime

app = Flask (__name__)

#@app.route('/')
#def hello():
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)
  
