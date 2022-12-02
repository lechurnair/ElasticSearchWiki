# Similarity changing
Changing scoring mechanism to TF-IDF from default one.
```
POST /wikisearch1/_close
PUT /wikisearch1/_settings
{
  "settings": {
    "similarity": {
      "scripted_tfidf": {
        "type": "scripted",
        "weight_script": {
          "source": "double idf = Math.log((field.docCount+1.0)/(term.docFreq+1.0)) + 1.0; return query.boost * idf;"
        },
        "script": {
          "source": "double tf = Math.sqrt(doc.freq); double norm = 1/Math.sqrt(doc.length); return weight * tf * norm;"
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "field": {
        "type": "text",
        "similarity": "scripted_tfidf"
      }
    }
  }
}



POST /wikisearch1/_open
```
## Change in settings
```
{
  "wikisearch1" : {
    "settings" : {
      "index" : {
        "routing" : {
          "allocation" : {
            "include" : {
              "_tier_preference" : "data_content"
            }
          }
        },
        "number_of_shards" : "1",
        "provided_name" : "wikisearch1",
        "similarity" : {
          "scripted_tfidf" : {
            "type" : "scripted",
            "weight_script" : {
              "source" : "double idf = Math.log((field.docCount+1.0)/(term.docFreq+1.0)) + 1.0; return query.boost * idf;"
            },
            "script" : {
              "source" : "double tf = Math.sqrt(doc.freq); double norm = 1/Math.sqrt(doc.length); return weight * tf * norm;"
            }
          }
        },
        "creation_date" : "1669813155444",
        "number_of_replicas" : "1",
        "uuid" : "3BqVUzmXRSm0uUH6ldkchg",
        "version" : {
          "created" : "7100199"
        }
      }
    }
  }
}
```
