'''
Created on 21-Mar-2018

@author: Titan
'''
import firebase
from firebase import firebase
from google.cloud import *
#from google.cloud import firestore_v1beta1
#from google.cloud import storage

from google.cloud.firestore_v1beta1 import *
from google.cloud.firestore_v1beta1.proto import *
from google.cloud.firestore_v1beta1.proto.admin import *
from google.cloud.firestore_v1beta1.gapic import *
#from google.cloud import firestore
#from google.cloud.firestore_v1beta1 import __version__
#from google.cloud.firestore_v1beta1._helpers import GeoPoint
from google.cloud.firestore_v1beta1.proto import *
#from rpc import *
#import grpc
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#from google.cloud import firestore


if __name__ == '__main__':
    fb = firebase.FirebaseApplication('https://***************.firebaseio.com/', None)
    result = fb.get('users', None)
    print(result)





'''
cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.Client()
users_ref = db.collection(u'users')
docs = users_ref.get()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))    

docref = db.collection(u'users').document(u'userdoc')

docref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})

'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





























































