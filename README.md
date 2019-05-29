# Web-Scraping
Here is my scraping file.
I used the popular lib of scraping such as beautifulsoup, requests, and so on.
In particular, I also used the pyspark to process the data, becasue pyspark is very useful so I highly suggest that you can install the pyspark.
Of course, you do not necessarily need to use pyspark. Is is just because I am familiar with spark.

### Introduction:
- [Xvideo.py](./Xvideo.py) 
    We can use web-scrapy to list all the videos for each key in order from high to low views.
- [Eyny_video.py](./Eyny_video.py)
    We practice scraping the anime page of Eyny forum. It will output the `['Title','view','day','href']`, so we can analyize each video which has how many views? and how long has it upload, and its link. But I should say that the day is not correct actually. (I already wrote in Eyny_video.py file.) 
