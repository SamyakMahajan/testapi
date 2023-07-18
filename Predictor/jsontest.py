import json
req_body = {1:2,3:4,5:6}
req_body=json.dumps(req_body)
print("dumps converts dict to Json string :",(req_body),"type =", type(req_body))
####print(req_data)
req_d=json.loads(req_body)
print("loads converts Json string to dict:",(req_d),"type =", type(req_d))
##req_data = json.dumps(req_d)
##print(req_d[2])
name = req_d["1"]
print(name)

"""
Output:
    dumps converts dict to Json string : {"1": 2, "3": 4, "5": 6} type = <class 'str'>
    loads converts Json string to dict: {'1': 2, '3': 4, '5': 6} type = <class 'dict'>
    2
"""

"""
json keys need to be enclosed in double quotes!!!
"""