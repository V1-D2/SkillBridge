import json as JSON


def intArr2Json(arr):
    str = JSON.dumps(arr)
    print(str)
    return str


def json2IntArr(json):
    arr = JSON.loads(json)
    print(arr)
    return arr
