from flask import Flask, request
from Metrics import metricHandler as m
import logging
import sqlite3

logging.basicConfig(filename="metricLog.txt", level=logging.DEBUG)
logger = logging.getLogger('flask_log') 

# Connect to DB
conn = sqlite3.connect("bazaar.db", check_same_thread=False)
cursor = conn.cursor()

## db schema creation -- This is only done for the sake of making this project code function. In any production level code, we would connect to a pre-existing db
sql = 'create table if not exists Auth (Timestamp TEXT, UserID INTEGER, Platform TEXT, SessionID TEXT)'
cursor.execute(sql)
sql = 'create table if not exists Basement (Timestamp TEXT, EventName TEXT, UserID INTEGER, Platform TEXT, SessionID TEXT, EventData TEXT)'
cursor.execute(sql)
conn.commit()

app = Flask(__name__)

@app.route('/')

@app.route('/jsonAPI', methods = ['POST']) 
def jsonAPI():
    if request.method == 'POST':
        data = request.get_json()        
        return m.HandleMetric(data, conn)
    else:
        return "Waiting for data"

if __name__=='__main__': 
    app.run(debug=True)

