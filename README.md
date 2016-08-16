
### How
- Description
  - Built an app crawling "http://app.xiaomi.com" with Scapy and search system that finds interesting information based on MongoDB and ElasticSearch. 
  - Save data into MongoDB and connected MongoDB to ElasticSearch 
  - Integrated an interactive search system by NodeJs, Express and React 

- Demo
  - Screenshot
    ![](./screenshots/intial page.png =100x20)
    ![](./screenshots/search.png =100x20)
    ![](./screenshots/search result.png =100x20)
  - GIF
  - Link
  - ...
- Usage
- Components/Structure
  - ## Crawler

```
  xiaomiapp
  |__ xiaomiapp
         |__ spiders
               |__ init__.py
               |__ xiaomi_spider.py
         |__ init__.py
         |__ items.py
         |__ pipelines.py
         |__ settings.py
```

xiaomi_spider.py defines how to crawl the webpage "http://app.xiaomi.com" by Scrapy.  
items.py defines the data fields which stored in MongoDB, ElasticSearch and Solr, even though in the project only the code about MongoDB is used.  
pipelines.py defines the store process in MongoDB, ElasticSearch and Solr, even though in the project only the code about MongoDB is used.  

Run scrapy crawl xiaomi.


- Acknowledgement
- License
- Project Information
 - Category: full stack
 - Stack: React, Node.js, MongoDB, ElasticSearch, Python

### Template
- [readme_template](https://github.com/hackjustu/Github-Ranking-FrontEnd)
- [readme_template](https://github.com/nirvanastar)

## 3. Other Resource
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#headers)
- [Resource Summary](./Resource.md)

## 4. Reference (continue adding)
- [LeoAJ/react-iTunes-search](https://github.com/LeoAJ/react-iTunes-search)
