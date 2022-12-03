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
                "content" : Q
    }
  },
  "size": 100
        }
        body1 = {"suggest": {
    "my-suggestion" : {
      "text" : Q,
      "term" : {
        "field" : "content",
        "suggest_mode" : "missing"
        
      }
    }
  }
   }
        res = es.search(index="wikisearch1", body=body)
        res1 = es.search(index = "wikisearch1", body = body1)
    else:
        print("error occured while making request")
	
    #res1= [{'link':result['link'],'title':result['title']} for result in res['hits']['hits'][0]['_source']]

    return render_template('result.html',result = res['hits']['hits'],suggest = res1['suggest']['my-suggestion'] )

app.run(port=5000, debug=True)
