from flask import Flask, redirect, request
import json
import os
import datetime
import hashlib
import mysql.connector
import jwt
import time
time.sleep(1)
password=open('/run/secrets/db-password')
mydb = mysql.connector.connect(
    host="db",
    user="root",
    password=password.read(),
    database='USERS',
    auth_plugin='mysql_native_password'
)
mycursor = mydb.cursor()
service = Flask(__name__)
@service.route('/validate',methods = ['POST'])
def validate():
    if(request.method == 'POST'):
        email= request.form['Email']
        password=request.form['Password']
        passwordHash=hashlib.md5(password.encode())
        if (email!=None and password!=None):
            query="SELECT * FROM user_data WHERE userEmail=%s"
            string=(email, )
            mycursor.execute(query,string)
            myresult=mycursor.fetchone()
            if(passwordHash.hexdigest()==myresult[2]):
                token=encode_auth_token(myresult[0])
                # resp= redirect("http://54.194.36.85//catalogue", code=302)
                # resp.set_cookie('authToken',token)
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully registered.',
                    'auth_token': token.decode()
                }
                return make_response(jsonify(responseObject)), 201
            else:
                responseObject = {
                    'status': 'Failed',
                    'message': 'password incorrect.'
            }
            return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                    'status': 'Failed',
                    'message': 'No UserName or password.'
            }
            return make_response(jsonify(responseObject)), 401
    #return redirect("http://54.194.36.85/login", code=302)
    responseObject = {
                'status': 'Failed',
                'message': 'incorrect method'
    }
    return make_response(jsonify(responseObject)), 400
@service.route('/test')
def test_():
    return redirect("http://54.194.36.85/login", code=302)
@service.route('/Authorise',methods = ['POST'])
def authorise():
    token=encode_auth_token('jack@example.com')
    
    responseObject = {
        'status': 'success',
        'message': 'Successfully registered.',
        'auth_token': jwt.decode(token,os.getenv("SECRET_KEY"))
    }
    return make_response(jsonify(responseObject)), 201

def encode_auth_token( user_id):
    secret=os.getenv("SECRET_KEY")
    payload={'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),'iat': datetime.datetime.utcnow(),'sub': user_id}
    encoded_jwt = jwt.encode(payload, secret, algorithm="HS256")
    return encoded_jwt

if __name__ =='__main__':
    service.run()