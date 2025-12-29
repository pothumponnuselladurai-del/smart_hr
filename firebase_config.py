import firebase_admin
from firebase_admin import credentials, firestore

# Firebase service account key file
cred = credentials.Certificate("serviceAccountKey.json")

# Initialize Firebase app (only once)
firebase_admin.initialize_app(cred)

# Firestore database reference
db = firestore.client()
