import json

#Retrieve all resources
def getAll():
    with open('mockDB.json') as f:
        data = json.load(f)

    return data

# Retrieve resource by ID
def getById(id):
    full = getAll()

    # Create an empty list for our data
    data = []

    # Loop through the data and match data that fit the requested ID.
    # IDs are unique, but other fields might return many data
    for row in full:
        if row['id'] == id:
            data.append(row)

    return data

# Averages the inputs for each action
def getAverages():
    data = getAll()

    # Create an empty list for our data
    # averages = {"run" : 0, "jump": 0}
    averages = {"jump": {"total": 0}, "run": {"total": 0} }
    jumpAverage = 0;
    runAverage = 0;
    results = []

    # Loop through the data and match data that fit the requested ID.
    # IDs are unique, but other fields might return many data
    for action in data["actions"]:
        for row in data["actions"][action]:
            averages[action]["total"] += int(row["time"])

    for action in averages:
        rowCount = len(data["actions"][action])

        if rowCount > 0:
            averages[action]["avg"] = averages[action]["total"]/rowCount
        else:
            averages[action]["avg"] = "n/a"

    return averages

# Insert or Create a new action
def upsert(input):
    # Create an empty list for our data
    data = getAll()

    results = []

    # Loop through the data and match data that fit the requested ID.
    # IDs are unique, but other fields might return mixed
    for action in data["actions"]:
        if action == input["action"]:
            results = data
            newRecord = {"time": input["time"]}
            results["actions"][action].append(newRecord)
            updateDB(results)

    return data

#Here we would lock the file or row if we weren't rewriting the full file
#in this example
def updateDB(data):
    with open('mockDB.json', 'w') as file:
        json.dump(data, file)