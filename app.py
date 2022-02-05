from flask import Flask, request, jsonify
from flask import abort
from flask import make_response, url_for
import json
from time import gmtime, strftime
import sqlite3
app =Flask (__name__)


@app.route("/api/v1/info")
def home_index():
    conn = sqlite3.connect('mydb.db')
    print ("opened database successfully");
    api_list=[]
    cursor = conn.execute("Select buildtime, version, methods, links from apirelease ")
    for row in cursor:
        api ={}
        api['version'] = row[0]
        api['buildtime'] = row[1]
        api['methods'] = row[2]
        api['links'] = row[3]
        api_list.append(api)
    conn.close()
    return jsonify ({'api_version': api_list}),200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)

