import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : "https://smartclass-a14a0-default-rtdb.asia-southeast1.firebasedatabase.app/"
})


ref = db.reference('Students')

data = {
"20E31A6600":
    {
        "name":"Musk Mama" ,
        "Branch": "C.S.M",
        "Batch": "2020-2024",
        "Total_Attendance":18,
        "Last_Attendance_time":"2023-12-04 08:45:55"
    },

"20E31A6601":
    {
        "name":"ACHYUTHUNI KOUNDINYA" ,
        "Branch": "C.S.M",
        "Batch": "2020-2024",
        "Total_Attendance":30,
        "Last_Attendance_time":"2023-12-04 08:45:45"
    },

"20E31A6604":
    {
        "name":"E SAI MAHESH RAJ" ,
        "Branch": "C.S.M",
        "Batch": "2020-2024",
        "Total_Attendance":12,
        "Last_Attendance_time":"2023-12-04 10:45:45"
    },

"20E31A6610":
    {
        "name":"LANKA HARICHARAN" ,
        "Branch": "C.S.M",
        "Batch": "2020-2024",
        "Total_Attendance":20,
        "Last_Attendance_time":"2023-12-04 09:10:45"
    },

"20E31A6616":
    {
        "name":"MOHAMMED ASLAM" ,
        "Branch": "C.S.M",
        "Batch": "2020-2024",
        "Total_Attendance":21,
        "Last_Attendance_time":"2023-12-04 09:40:45"
    },

"20E31A6617":
    {
        "name":"MOHAMMAD FAHAD" ,
        "Branch": "C.S.M",
        "Batch": "2020-2024",
        "Total_Attendance":21,
        "Last_Attendance_time":"2023-12-04 09:40:45"
    },

"20E31A6619":
    {
        "name":"MOSALI LALITH KRISHNA REDDY" ,
        "Branch": "C.S.M",
        "Batch": "2020-2024",
        "Total_Attendance":27,
        "Last_Attendance_time":"2023-12-04 09:13:45"
    },

"20E31A6621":
    {
        "name":"NEELAM YASHWANTH" ,
        "Branch": "C.S.M",
        "Batch": "2020-2024",
        "Total_Attendance":23,
        "Last_Attendance_time":"2023-12-04 09:16:45"
    },

"20E31A6624":
    {
        "name":"PILLI RAHUL MAHENDRA" ,
        "Branch": "C.S.M",
        "Batch": "2020-2024",
        "Total_Attendance":20,
        "Last_Attendance_time":"2023-12-04 09:22:45"
    },

"20E31A6626":
    {
        "name":"RAMIDI JITHENDER REDDY" ,
        "Branch": "C.S.M",
        "Batch": "2020-2024",
        "Total_Attendance":19,
        "Last_Attendance_time":"2023-12-04 09:20:45"
    },

"20E31A6627":
    {
        "name":"LAXMIKANTH " ,
        "Branch": "C.S.M",
        "Batch": "2020-2024",
        "Total_Attendance":19,
        "Last_Attendance_time":"2023-12-04 09:11:45"
    },

"20E31A6630":
    {
        "name":"HIMAWANT SOMAROWTHU" ,
        "Branch": "C.S.M",
        "Batch": "2020-2024",
        "Total_Attendance":8,
        "Last_Attendance_time":"2023-12-04 10:45:55"
    },

"20E31A6631":
    {
        "name":"THUMUKUNTA GANDLA AAKASH" ,
        "Branch": "C.S.M",
        "Batch": "2020-2024",
        "Total_Attendance":12,
        "Last_Attendance_time":"2023-12-04 09:45:55"
    },

"20E31A6635":
    {
        "name":"GADAGOTTU CHANDRASEKHAR" ,
        "Branch": "C.S.M",
        "Batch": "2020-2024",
        "Total_Attendance":20,
        "Last_Attendance_time":"2023-12-04 09:10:55"
    },

"21E35A6602":
    {
        "name":"CHIKKUDU RAMTEJA" ,
        "Branch": "C.S.M",
        "Batch": "2020-2024",
        "Total_Attendance":18,
        "Last_Attendance_time":"2023-12-04 09:17:55"
    },

"21E35A6605":
    {
        "name":"SARAGUNDLA JYOTHI SWAROOP" ,
        "Branch": "C.S.M",
        "Batch": "2020-2024",
        "Total_Attendance":24,
        "Last_Attendance_time":"2023-12-04 09:15:55"
    },

"20E31A6611":
    {
        "name":"MADDUR AMEER SOHAIL" ,
        "Branch": "C.S.M",
        "Batch": "2020-2024",
        "Total_Attendance":24,
        "Last_Attendance_time":"2023-12-04 09:37:25"
    },
}


for key, value in data.items():
    ref.child(key).set(value)