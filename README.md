
# Log Analysis Project

This project in Udacity Full Stack Nanodegree to build reporting tools to analyze the logs . in this project i used PostgreSQL database .
There are three tables in this database authors , articles and logs 

articles table contain author , title , slug, lead , body , time , id 
authors table contain name , bio , id 
log tabel contain path , ip , method , status , time , id

The questions that have been answered in this report are:
1- What are the most popular three articles of all time? 
2- Who are the most popular article authors of all time?
3- On which days did more than 1% of requests lead to errors?

## Installing
*  [Vagrant](https://www.vagrantup.com/downloads.html)
* [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
* [Udacity FSND virtual machine](https://github.com/udacity/fullstack-nanodegree-vm)
* [SQL script](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
* python 3


## How to run the project 
* cd vagrant
* vagrant up  
* vagrant ssh  
* cd /vagrant  
* mkdir log-analysis-project 
* cd log-analysis-project
*  load the data from the “newsdata.sql” using **psql -d news -f newsdata.sql**
* dowonload logAnalysis.py
* connect to database using  **psql -d news**
* Copy the create view statements from **create views** Section below into the psql console .
* Once the views have been created, exit the psql console by typing \q.
* Run the python script by typing python logAnalysis.py.

## create views 

``` SQL
CREATE VIEW views AS 
SELECT count (log.id) AS Number_of_viewer , articles.title 
FROM articles , log 
WHERE  log.path =concat('/article/', articles.slug)
GROUP BY log.path , articles.title 
ORDER BY Number_of_viewer DESC;
``` 

``` SQL
CREATE view  author_views AS 
SELECT views.title , views.number_of_viewer,
articles.author , authors.name  
FROM views INNER JOIN articles 
ON articles.title=views.title 
INNER JOIN authors 
ON authors.id= articles.author; 
``` 
``` SQL
CREATE VIEW TotalRequist AS 
SELECT DATE(log.time), COUNT(log.status) 
FROM log WHERE status='200 OK'
GROUP BY DATE(log.time);
``` 
``` SQL
CREATE VIEW BadRequist AS 
SELECT DATE(log.time), COUNT(log.status) 
FROM log WHERE NOT status='200 OK' 
GROUP BY DATE(log.time);
``` 
``` SQL
CREATE VIEW percent AS
SELECT TotalRequist.date , 
ROUND((BadRequist.count*1.0 /TotalRequist.count )*100 ,2) 
As percent FROM TotalRequist, BadRequist
WHERE TotalRequist.date=BadRequist.date ;
``` 
