import os, json


def loadConfigFile(file: str) -> str:
    f = open(f"config/{file}")
    return f.read()
    
def saveConfigFile(file, content: str) -> None:
    f = open(f"config/{file}", "w")
    f.write(content)


def LoadPermissions():
    global permissions
    rawPermissions = loadConfigFile("permissions.json")
    permissions = json.loads(rawPermissions)

def getModerationPermission(permission: str) -> str:
    moderation = permissions["moderation"]
    if not moderation[permission]:
        return moderation["default"]
    else:
        return moderation[permission]

def LoadLogging():
    global logging
    rawLogging = loadConfigFile("logging.json")
    logging = json.loads(rawLogging)

def getLogging(value: str) -> str:
    print(logging)
    print(value)
    print(logging[value])
    return logging[value]

def LoadCounting():
    global counting
    rawCounting = loadConfigFile("counting.json")
    counting = json.loads(rawCounting)

def getCounting(value: str) -> str:
    return counting[value]

def saveCounting(count: int, lastCountUser: int) -> None:
    counting["count"] = count
    counting["lastCountUser"] = lastCountUser
    saveConfigFile("counting.json", json.dumps(counting))