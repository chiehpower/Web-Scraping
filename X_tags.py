import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
# If you already installed the pyspark, you can use the line 6 & 7 and line 35-37. 
# from pyspark import SparkContext
# sc = SparkContext()

url = requests.get('https://www.xvideos.com/tags')
soup = BeautifulSoup(url.text,"html.parser")
both = soup.select('div ul.tags-list li a')
tag = both[40:]
country = both[:39]

a = []
for x in range(0,len(tag)):
        title = re.findall('href="/.[^"]+"', str(tag[x])) 
        title = re.findall('/[a-zA-Z0-9-?=_]+', str(title))
        title = title[1]
        title = re.findall('[^/]+', str(title))
        title = ''.join(title)
        
        view = re.findall('>[0-9,]+<', str(tag[x]))
        view = re.findall('[0-9,]+', str(view)) 
        view = view[0].split(',')
        view = ''.join(view)
        view = int(view)
        
        href = re.findall('href="/.[^"]+"', str(tag[x])) 
        href = re.findall('/[a-zA-Z0-9-?=_]+', str(href))
        href = ['https://www.xvideos.com']+href
        href = ''.join(href)
        a.append((title, view, href))

# a_sc = sc.parallelize(a)
# a_scf = a_sc.distinct().sortBy(lambda s: s[1],ascending = False).collect()
# d = pd.DataFrame(a_scf)

a = sorted(a,key=lambda s: s[1], reverse=True)
d = pd.DataFrame(a)
d.columns = ['TAG','Number','URL']

file_path = r'./tags_video.xlsx'
writer = pd.ExcelWriter(file_path)
d.to_excel(writer, index=False,encoding='utf-8',sheet_name='Sheet')
writer.save()