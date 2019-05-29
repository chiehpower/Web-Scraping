# Web-Scraping
Here is my scraping file.
I used the popular library of scraping such as beautifulsoup, requests, and so on.
In particular, I also used the pyspark to process the data, becasue pyspark is very useful so I highly suggest that you can install the pyspark.
Of course, you do not necessarily need to use pyspark. Is is just because I am familiar with spark.

### Installation:
If you didnt install the library of scraping for beautifulsoup, type the command below.
`pip install beautifulsoup4` or `pip3 install beautifulsoup4`

If you want to use the `lxml` parser of beautifulsoup, type the command below.
`pip install lxml` or `pip3 install lxml`

### List:
- [Eyny_video.py](./Eyny_video.py)
    We practice scraping the anime page of Eyny forum. It will output the `['Title','view','day','href']`, so we can analyize each video which has how many views? and how long has it upload, and its link. But I should say that the day is not correct actually. (I already wrote in Eyny_video.py file.) 
- [Save_pictures.py](./Save_pictures.py)
    In this file, There are two purposes that one is how to requests the picture from web-page; another one is how to save the binary picture after you get the content. In addition, I also compared two kinds of different methods that first I used the content of requests to save the picture, and second I used the shutil.copyfileobj to save the pic.
    We can see the result of shutil which cannot get the picture from first web-page, but content can get successfully. But if our url has the name of jpg in the end, then both can get the picture successfully.
    So I would say that using content method is more flexible here.

*Adult Area*
- 🔞[Xvideo.py](./Xvideo.py) 
    We can use web-scrapy to list all the videos for each key in order from high to low views.

- 🔞[X_tages.py](./X_tages.py) 
    We can use web-scrapy to list all the tags in order from high to low views.


### Notice:
- For pyspark, `Distinct()` 
    - Cannot process this case： `[ [ ], [ ], ... ,[ ]]`
        example : dtry = `[['1'],['1'],['2'],['2'],['3'],['4'],['5'],['6'],['7']]`
    - Can process this case： `[ (),(),(),...() ]`
        example：dtry = `[('1'),('1'),('2'),('2'),('3'),('4'),('5'),('6'),('7')]`
    - If there is an integer which cannot be iteration in the list, it cannot use the `tuple()` or `list()`. However, we can directly use `()` or `[]` to replace it without using `tuple()`.
        - Correct example：`Data.append((title,view,time,href))`
        - Wrong example：`Data.append(tuple(title,view,time,href))`

