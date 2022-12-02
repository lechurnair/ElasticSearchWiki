#intially doing all imports
try:
    import os
    import sys
    import elasticsearch
    from elasticsearch import Elasticsearch 
    import pandas as pd
    from elasticsearch import helpers

    print("All Modules Loaded ! ")
except Exception as e:
    print("Some Modules are Missing {}".format(e))

def connect_elasticsearch():
    es = None
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if es.ping():
        print('Connection established')
    else:
        print('Sed life, no connection')
    return es
es = connect_elasticsearch()

df = pd.read_json("sample.json")
#convert json to appropriate format


#covert it into appropriate format for uploading to elastic search
df1 = df.to_dict('records')

#function to generate IDs
global c
c = 0
def func(x):
    global c
    c = c+1
    return c

#Create an ID
df["ID"] = df["link"].apply(func)

df2 = df.to_dict('records')
#print(df2[0])
#generator that takes in data frame

def generator(df):
    for c, line in enumerate(df):
        yield{
    '_index': 'wikisearch1',
    '_type': 'dataset',
    '_id': line.get('ID'),
    '_source': {
        'link' : line.get("link", ["No Data"]),
        'title' : line.get("title", ["No Data"]),
        'subheadings' : line.get("subheadings", ["No Data"]),
        'content' : line.get("content", ["No Data"])
    }
        }

#gen = generator(df2)
#print(gen)
try:
    res = helpers.bulk(es,generator(df2))
    print("working")
except Exception as e:
    print(e)
#print("Working")
