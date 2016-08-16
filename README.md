

## Description
  - Built an app crawling "http://app.xiaomi.com" with Scapy and search system that finds interesting information based on MongoDB and ElasticSearch. 
  - Save data into MongoDB and connected MongoDB to ElasticSearch 
  - Integrated an interactive search system by NodeJs, Express and React 

## Demo
  - ScreenShot
    ![](./screenshots/intial page.png =250x250)
    ![](./screenshots/search.png = 100x20)
    ![](./screenshots/search result.png =100x20)
  - GIF
  - Link
  - ...

## Usage
- Install lastest verison of Node.JS, ElasticSearch, MongoDB  
- npm install  
- Run elasticsearch and MongoDB
- Come to the root directory
  - node server
  - npm run dev
- Open a browser and input http://localhost:8080/webpack-dev-server/ .

## Components/Structure

### Crawler

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

  - xiaomi_spider.py defines how to crawl the webpage "http://app.xiaomi.com" by Scrapy.  
  - items.py defines the data fields which stored in MongoDB, ElasticSearch and Solr, even though in the project only the code    about MongoDB is used.  
  - pipelines.py defines the store process in MongoDB, ElasticSearch and Solr, even though in the project only the code about     MongoDB is used.  

  Run scrapy crawl xiaomi.


### Acknowledgement
### License
### Project Information
  - Category: full stack
  - Stack: React, Node.js, MongoDB, ElasticSearch, Python

### Template
#### ReadMe Template
- [Github-Ranking-FrontEnd](https://github.com/hackjustu/Github-Ranking-FrontEnd)
- [Web-Crawle-rApp](https://github.com/nirvanastar/webcrawlerapp)

## Other Resource
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#headers)
- [Resource Summary](./Resource.md)

## Reference (continue adding)
- [LeoAJ/react-iTunes-search](https://github.com/LeoAJ/react-iTunes-search)
