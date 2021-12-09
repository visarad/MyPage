import redis
import pandas as pd
import sys

r = redis.StrictRedis('localhost',6379,decode_responses=True)

header = ['firstName','lastName','fullName','address']

def get_values(key):
    
    key = str(key)
    try:
        value = r.get(key)
    except:
        sys.exit("Error in Execution")
    return value

def set_values(key,value):
    key = str(key)
    try:
        r.set(key,value)
    except:
        sys.exit("Error in Execution")

set_values('child','pararthi')
print(get_values('child'))

