'''
Created on 25-Mar-2018

@author: Titan
'''

from firebase import firebase
import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore

#from google.cloud import firestore

'''
fb = firebase.FirebaseApplication('https://******************.firebaseio.com/', None)
result = fb.get('users', None)
print(result)

'''
cred = credentials.Certificate("./serviceAccountKey.json")
app = firebase_admin.initialize_app(cred)

db = firestore.client(app)
users_ref = db.collection(u'users')
docs = users_ref.get()
print(docs)
