# ElasticSearchWiki
## Search Engine based on Elastic Search framework
In this project we have created a search engine that takes keyword queries as input and retrieves a
ranked list of relevant results as output. 

## Features present:

- Cleaning and preprocessing of data.
- Proper visualization of ranked the list of pages that hold the relevant answers.
- Support for BM25 scoring model and TF-IDF scoring model.
- Query Keyword suggestions, based on the Levenstein edit distance.
- A configuration window for users to choose any of the scoring models and no. of results to show on the result page.

## To Run
To scrape wikipages following few seed wikipedia pages

```
    python3 Scraping.py
```
To add the json file from scrapper to elasticsearch
```
    python3 Wiki_to_Indices.py
```
