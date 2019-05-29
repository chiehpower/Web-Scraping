import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
# If you already installed the pyspark, you can use the line 6 & 7 and line 47-50. 
# from pyspark import SparkContext
# sc = SparkContext()

# We mainly scrape the video of eyny and we will analyize the view, time, title, and link of each video.
# But in here I didnt deal with the day very well, becasue I didnt translate the unit of day such as one month which is equal to 30 days.
# We still can easily see which video is very popular.
# If you want to watch other categories, just change the url. 


def video(url): 
    url = requests.get(url)
    soup = BeautifulSoup(url.text,"html.parser")
    a = []
    for x in range(0,len(soup.select('p')),3):
        if x + 2 < len(soup.select('p')):
                s = soup.select('p')[x+2]
                title = re.findall('title=".+"', str(soup.select('p')[x])) 
                title = re.findall('".+"', str(title))
                
                href = re.findall('href="/.+" s', str(soup.select('p')[x])) 
                href = re.findall('/[a-zA-Z0-9-?=_]+', str(href))
                href = ['http://video.eyny.com/']+href
                href = ''.join(href)

                
                view = re.findall('[0-9]+  view', str(s))
                view = re.findall('[0-9]+', str(view))
                view = list(map(int, view))

                day = re.findall('[0-9]+ .[時天月年]前', str(s))
                day = re.findall('[0-9]+', str(day))
                day = list(map(int, day))

                title =''.join(title)
                a.append([title,view,day,href])
    return a
a = video('http://video.eyny.com/en/channel/UCYrHXcc_kb')


# After we scrape the data, we need to process those by pyspark. Combine those, and sortBy them.

# data = sc.parallelize(a)
# data_1 = data.map(lambda s: s[0]+s[1]+s[2]+[s[3]])\
#             .sortBy(lambda s: s[1],ascending = False)\
#             .collect()

a = sorted(a,key=lambda s: s[1], reverse=True)

# Here you should choose, if you use the spark to process, you should close the sorted, 
# and change the Data variable name in Next line. (like > d = pd.DataFrame(data_1))
d = pd.DataFrame(a)
d.columns = ['Title','view','day','href']

file_path = r'./Eyny_video.xlsx'
writer = pd.ExcelWriter(file_path)
d.to_excel(writer, index=False,encoding='utf-8',sheet_name='Sheet')
writer.save()
# Check the file, and name is video.xlsx. 



# PS 
# In here I didnt filter the duplicate cases.
# You can use the unique() or distinct() of pyspark to filter them.