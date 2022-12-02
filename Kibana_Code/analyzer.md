# Analyzer modification

Default analyzer for the elastic search table, wikisearch is changed.

```
POST /wikisearch/_close
GET wikisearch/_analyze 
{
  "analyzer": "my_custom_analyzer", 
  "text":     "Is this déjà vu?[edit]"
}


PUT /wikisearch/_settings
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_custom_analyzer": { 
          "type": "custom",
          "char_filter": [
            "square_remove"
          ],
          "tokenizer": "punctuation",
          "filter": [
            "lowercase",
            "english_stop"
          ]
        }
      },
      "tokenizer": {
        "punctuation": { 
          "type": "pattern",
          "pattern": "[ .,!?]"
        }
      },
      "char_filter": {
        "square_remove": { 
          "type": "pattern_replace",
          "pattern": "\\[[a-z]*[0-9]*\\]"
        }
      },
      "filter": {
        "english_stop": { 
          "type": "stop",
          "stopwords": "_english_"
        }
      }
    }
  }
}

POST /wikisearch/_open
```

# Results 
Unless overridden with the search_analyzer mapping parameter, this analyzer is used for both index and search analysis. The settings of the index after making the above change.

```
settings
{
  "wikisearch" : {
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
        "provided_name" : "wikisearch",
        "creation_date" : "1669634434638",
        "analysis" : {
          "filter" : {
            "english_stop" : {
              "type" : "stop",
              "stopwords" : "_english_"
            }
          },
          "char_filter" : {
            "square_remove" : {
              "pattern" : """\[[a-z]*[0-9]*\]""",
              "type" : "pattern_replace",
              "replacement" : ""
            }
          },
          "analyzer" : {
            "my_custom_analyzer" : {
              "filter" : [
                "lowercase",
                "english_stop"
              ],
              "char_filter" : [
                "square_remove"
              ],
              "type" : "custom",
              "tokenizer" : "punctuation"
            }
          },
          "tokenizer" : {
            "punctuation" : {
              "pattern" : "[ .,!?]",
              "type" : "pattern"
            }
          }
        },
        "number_of_replicas" : "1",
        "uuid" : "d-vrZ4hRQ8e1MUsu2pxihg",
        "version" : {
          "created" : "7100199"
        }
      }
    }
  }
}
```
