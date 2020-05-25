# Scrapping-Restaurants-Data-From-Dineout-Using-Scrapy

To gather the Restaurant Name, Cuisines offered, Food Types available, Cost for 2 people, Facilities provided, Rating, No. of Votes, Reviews and it's Location.

## Installation Documentaion

    $ sudo apt install git

    $ git clone https://github.com/ShobhitBansal/Scrapping-Restaurants-Data-From-Dineout-Using-Scrapy.git
  
    $ cd Scrapping-Restaurants-Data-From-Dineout-Using-Scrapy
    
![](Screenshots/1.png)

    $ sudo apt-get install virtualenv
    
![](Screenshots/2.png)

    $ virtualenv env

    $ source env/bin/activate
    
    $ sudo apt-get install python3.7
    
    $ sudo apt-get install python3-pip
    
![](Screenshots/3.png)

    $ pip3 install -r requirements.txt
    
![](Screenshots/4.png)
    
    $ scrapy crawl restaurants -o <filename>.(csv/xml/json) -a city'"<cityname>"
    
![](Screenshots/5.png)
    
The restaurants data will get stored in the csv/xml/json file and Restaurants.db database file

![](Screenshots/6.png)

Open the csv file in LibreOffice

![](Screenshots/7.png)
    
To open the restaurants.db Database File 
    
    $ sudo apt-get install sqlite3
    
    $ sudo apt-get install sqlitebrowser
    
![](Screenshots/8.png)

Now open the restaurants.db file in the SQLite Browser

![](Screenshots/9.png)
