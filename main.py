import firebase_admin
from firebase_admin import db
import json

cred_object = firebase_admin.credentials.Certificate('key.json')
firebase_admin.initialize_app(cred_object, {
	'databaseURL':'https://pythonconn-2578e-default-rtdb.asia-southeast1.firebasedatabase.app/'
	})

ref = db.reference("/")
# with open("sample.json", "r") as f:
# 	file_contents = json.load(f)
# ref.set(file_contents)

a = '{"name":"joemama", "age":2873498731}'
ref.set(json.loads(a))
