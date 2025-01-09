from Metrics import Auth, Basement
import util, datetime as dt, sqlite3
from app import logger

def HandleMetric (data, conn):
    ## route the metric to the proper function for handling based on EventName
    if data.get('EventName') is not None :
        eventName = data.get('EventName')
        if eventName in MetricHandler.keys():
            ingestData = MetricHandler[eventName](data)
            logger.debug(util.format_dt(dt.datetime.now()) + " - Ingest into %s." % (eventName))
            IngestMetric(ingestData, eventName, conn)
            return "POST Success" 
        else:
            ingestData = MetricHandler['Basement'](data)
            logger.debug(util.format_dt(dt.datetime.now()) + " - Ingest into Basement: EventName - %s not found." % (eventName))
            IngestMetric(ingestData, 'Basement', conn)
            return  "Off to the Basement - Unschematized Event"
    else:
        ingestData = MetricHandler['Basement'](data)
        logger.debug(util.format_dt(dt.datetime.now()) + " - Ingest into Basement: EventName is NULL.")
        IngestMetric(ingestData, 'Basement', conn)
        return "Off to the Basement - Unknown Event"
    
def IngestMetric(data, EventName, conn):
    ## Create the insert statement then try running it
    sql = "INSERT INTO " + EventName + " (" + ", ".join([col for col in data]) + ") VALUES (" + ", ".join(["?"]*len(data)) + ")"
    values = [data[col] for col in data]
    try:
        c = conn.cursor()
        c.execute(sql, values)
        conn.commit()
    except sqlite3.Error as e:
        logger.error(util.format_dt(dt.datetime.now()) + " - Failed to ingest data into %s using command %s with the following data: \n%s\nError: %s" % (EventName, sql, values, e))
    return None

## Maps EventNames to proper function for handling
MetricHandler = {
    'Auth': Auth.Auth
    ,'Basement': Basement.Basement
    ## list of other future metrics
}
