import requests, random as r, base64

authJSON = {
    "EventName": "Auth"
    ,"UserID": r.randint(1,1000) ## unique integer accountID, not public
    ,"UserName": "DefinitelyPII"
    ,"Platform": "PC" ## could be mobile in the future
    ,"SessionID": base64.b64encode(r.randbytes(16)).decode('utf-8') ## Unique identifier for the session
    ## some other data??
    ,"EventData": {} ## Auth is a basic metric. It won't contain any event data but this would matter for more complex metrics
}

FlawedJSON = {
    "EventName": None
    ,"UserID": r.randint(1,1000) ## unique integer accountID, not public
    ,"UserName": "DefinitelyPII"
    ,"Platform": "PC" ## could be mobile in the future
    ,"SessionID": base64.b64encode(r.randbytes(16)).decode('utf-8') ## Unique identifier for the session
    ## some other data??
    ,"EventData": {} ## It's Auth with EventName missing. Auth is a basic metric. It won't contain any event data but this would matter for more complex metrics
}

UnschematizedJSON = {
    "EventName": "Fight"
    ,"EventData": {
        "MatchGUID": base64.b64encode(r.randbytes(16)).decode('utf-8') ## Match indentifier
        ,"Day": 1
        ,"Players": [{
            "UserID": r.randint(1,1000) ## unique integer accountID, not public
            ,"UserName": "DefinitelyPII"
            ,"SessionID": base64.b64encode(r.randbytes(16)).decode('utf-8')
            ,"Character": "Vanessa"
            ,"Level": 1
            ,"Skills": {}
            ,"Items": [{
                "Item": "Cutlass"
                ,"Tier": 2 ## Silver
                ,"Cooldown": 5
                ,"Damage": 12
                ## additional fields could include heal, shield, burn, poison, etc...
            },
            {
                "Item": "Silencer"
                ,"Tier": 1
            }]
        },
        {
            "UserID": None
            ,"Character": "Banannabal"
        }]
    }
}

r = requests.post('http://127.0.0.1:5000/jsonAPI', json=authJSON)
r = requests.post('http://127.0.0.1:5000/jsonAPI', json=UnschematizedJSON)
r = requests.post('http://127.0.0.1:5000/jsonAPI', json=FlawedJSON)