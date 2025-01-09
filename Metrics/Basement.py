import datetime as dt, util

def Basement(data):
    Timestamp = util.format_dt(dt.datetime.now())
    EventName = data.get('EventName')
    UserID = data.get('UserID')
    Platform = data.get('Platform')
    SessionID = data.get('SessionID')
    EventData = str(data.get('EventData')) ## conver JSON object to string to store in SQLite TEXT field
    
    return {
        "Timestamp": Timestamp
        ,"EventName": EventName
        ,"UserID": UserID
        ,"Platform": Platform
        ,"SessionID": SessionID
        ,"EventData": EventData
    }