# from flask import Flask, redirect, request
# import json
# import os
# import datetime
# import hashlib
# import pymysql.cursors
# import jwt
# import time
# time.sleep(1)
# password=open('/run/secrets/db-password')
# connection = pymysql.connect(
#     host="db",
#     user="root",
#     password="changeme",
#     database='USERS',
#     cursorclass=pymysql.cursors.DictCursor
# )
# mycursor = connection.cursor()
# service = Flask(__name__)
# @service.route('/validate',methods = ['POST'])
# def validate():
#     if(request.method == 'POST'):
#         content=request.json
#         print(content)
#         email= content['Email']
#         password=content['Password']
#         passwordHash=hashlib.md5(password.encode())
#         if (email!=None and password!=None):
#             query="SELECT * FROM user_data WHERE userEmail=%s"
#             email=(email,)
#             mycursor.execute(query,email)
#             myresult=mycursor.fetchone()
#             if(passwordHash.hexdigest()==myresult[2]):
#                 token=encode_auth_token(myresult[0])
#                 resp= redirect("http://63.35.237.119/catalogue", code=302)
#                 resp.set_cookie('authToken',token)
#                 return resp
#     return redirect("http://63.35.237.119/login", code=302)
# @service.route('/test')
# def test_():
#     return redirect("http://63.35.237.119/login", code=302)
# def encode_auth_token( user_id):
#     secret=os.getenv("SECRET_KEY")
#     payload={'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),'iat': datetime.datetime.utcnow(),'sub': user_id}
#     encoded_jwt = jwt.encode(payload, secret, algorithm="HS256")
#     return encoded_jwt

# if __name__ =='__main__':
#     service.run()