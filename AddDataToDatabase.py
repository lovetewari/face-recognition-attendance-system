import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-1e629-default-rtdb.firebaseio.com/"
})

ref = db.reference('Doctors')

data = {
    "321654":
        {
            "name": "Shaurya Mehrotra",
            "specialization": "ENT",
            "starting_year": 2017,
            "total_attendance": 7,
            "slots": 27,
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Love Tewari",
            "specialization": "Cardiologist",
            "starting_year": 2021,
            "total_attendance": 12,
            "slots": 30,
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Kumkum Bagha",
            "specialization": "Neurologist",
            "starting_year": 2020,
            "total_attendance": 7,
            "slots": 10,
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)