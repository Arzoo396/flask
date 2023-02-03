from flask import Flask, request, make_response, jsonify
from flask_restful import Resource, Api
from functools import wraps
import pymysql
app = Flask(__name__)
api = Api(app)

# To connect MySQL database
@app.route('/sel', methods=['GET'])
def get():
    #return {"msg" : "get method"}
    conn = pymysql.connect(host='localhost', user='root', password = "", db='students')
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("select * from users LIMIT 10")
    output = cur.fetchall()

    #print(type(output)); #this will print tuple
    return jsonify(output);

    for rec in output:
        print(rec);


@app.route('/insert', methods=['POST'])
def post():
    user_name = request.args.get('user_name');
    user_age = request.args.get('user_age');
    user_city = request.args.get('user_city');
    conn = pymysql.connect(host='localhost', user='root', password = "", db='students')
    cur = conn.cursor()
    sql = f"INSERT INTO `users` (`id`, `name`, `age`, `city`, `added_at`, `updated_at`) VALUES (NULL, '{user_name}', '{user_age}', '{user_city}', NOW(), NOW() )";
    cur.execute(sql);
    conn.commit();

    return f"record inserted";

@app.route('/update' , methods =['PUT'])
def put():
    user_id = request.args.get('user_id');
    user_name = request.args.get('user_name');
    user_age = request.args.get('user_age');
    user_city = request.args.get('user_city');
    conn = pymysql.connect(host='localhost', user='root', password = "", db='students')
    cur = conn.cursor()
    sql = f"UPDATE `users` SET `name` = '{user_name}', `age` = '{user_age}', `city` = '{user_city}'  WHERE `ID` = '{user_id}' ";
    cur.execute(sql);
    conn.commit()
    return f"record updated";

@app.route('/del', methods=['DELETE'])
def delete():
    id=request.args.get('id');
    conn = pymysql.connect(host='localhost', user='root', password = "", db='students')
    cur = conn.cursor()

    sql = f"DELETE FROM `users` WHERE `ID` = {id}";
    cur.execute(sql);
    conn.commit()
    return f"record of {id} is deleted";
    


if __name__ == "__main__":
    app.run(debug=True)

