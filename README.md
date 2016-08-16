

## Description
  - Built an app crawling "http://app.xiaomi.com" with Scapy and search system that finds interesting information based on MongoDB and ElasticSearch. 
  - Save data into MongoDB and connected MongoDB to ElasticSearch 
  - Integrated an interactive search system by NodeJs, Express and React 

## Demo
  - ScreenShot
    ![](./screenshots/intial page.png )
    ![](./screenshots/search.png )
    ![](./screenshots/search result.png )
  - GIF
  - Link
  - ...

## Usage
- Install lastest verison of Node.JS, ElasticSearch, MongoDB and mongo-connector
- npm install  
- Run elasticsearch and MongoDB
- Come to the root directory
  - node server
  - npm run dev
- Open a browser and input http://localhost:8080/webpack-dev-server/

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
  
### Search System
Built a website to implement searching. Node.JS for back-end and React.JS for front-end, while Express.Js is used as a standard server framework for Node.js.

#### Back-End

```
services
 |__ basicService.js
 |__ esService.js

```

#### Server Framework

```
routes
 |__ route.js
server.js

```

#### Front-End

```
scripts
 |__ components
         |__ App.jsx
         |__ Container.js
         |__ Header.js
         |__ Items.js
         |__ Map.js
 |__ vendor
     |__ dropdown.js
     |__ transition.js
 |__ emitter.js
 |__ index.jsx
index.html
webpack-server.js
webpack.config.js

```



### Acknowledgement
### License
### Project Information
  - Category: full stack
  - Stack: ReactJs, Node.js, Express.js, MongoDB, ElasticSearch, Python

### Template
#### ReadMe Template
- [Github-Ranking-FrontEnd](https://github.com/hackjustu/Github-Ranking-FrontEnd)
- [Web-Crawle-rApp](https://github.com/nirvanastar/webcrawlerapp)

## Other Resource
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#headers)
- [Resource Summary](./Resource.md)

## Reference (continue adding)
- [LeoAJ/react-iTunes-search](https://github.com/LeoAJ/react-iTunes-search)
