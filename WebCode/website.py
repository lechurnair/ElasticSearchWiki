from datetime import datetime
from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch
from flask import render_template

es = Elasticsearch()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
  

@app.route('/submit', methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        Q = request.form['query']

        body = {
            "query" : {
                "match" : {
                "content" : "science"
    }
  },
  "size": 100
        }
        res = es.search(index="wikisearch1", body=body)
    else:
        print("error occured while making request")

    #res1= [{'link':result['link'],'title':result['title']} for result in res['hits']['hits'][0]['_source']]

    return render_template('result.html',result = res['hits']['hits'])

app.run(port=5000, debug=True)
