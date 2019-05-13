from flask import Flask , request , jsonify
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config['MySQL_HOST']="localhost"
app.config['MySQL_USER']="root"
app.config['MySQL_PASSWORD']="realmadrid@1902"
app.config['MySQL_DB']="learn1"
mysql=MySQL(app)
import json
class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o:o.__dict__, sort_keys=True, indent=4)
@app.route("/")
def hello():
    return "Hello World!"

#cur=None

@app.route("/learn1",methods=["POST"])
def add_learn():
    request.get_json(force=True)   #force=True because we dont want a request body
    #global cur
    username = request.json['username']
    email = request.json['email']
    cur=mysql.connection.cursor()
    query="insert into t1 values (null,%s,%s)"  #null is only used when we have auto increament with primary key
    data=[username,email]
    cur.execute(query,data)
    cur.connection.commit()
    cur.close()

    me= Object()
    me.name= username
    me.email=email
    return jsonify(me.toJSON())

if __name__=="__main__":
    app.run(debug=True)
