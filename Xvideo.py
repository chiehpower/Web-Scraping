import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
# If you already installed the pyspark, you can use the line 6 & 7 and line 61 & 62. 
# from pyspark import SparkContext
# sc = SparkContext()

def video(datef,Key,Pages):
    """
    datef : today, week, month, 3month, all
    Key : for example, Japanese, Chinese, or anything what you want.
    Pages : how many pages do you want to scrape?
    """
    Data = []
    for i in range(Pages):
        i = str(i)
        url = 'https://www.xvideos.com/?k='+Key+'&datef='+datef+'&p='+i
        r = requests.get(url)
        soup = BeautifulSoup(r.text,"html.parser")
        sel = soup.select("div.thumb-under")
        for j in range(len(sel)):
#             print(str(sel[j]))
            title = re.findall(' title="[^"]+"',str(sel[j]))
            if title == []:
                title = ['a']
            else:
                title = re.findall('".+"', str(title[0])) 
                title = re.findall('[^"].+', str(title[0])) 

            href = re.findall('href="/.[^"]+', str(sel[j]))[0] 
            href = re.findall('[/a-zA-Z0-9-?=_]+', str(href))[1]
            href = 'https://www.xvideos.com'+href

            time = re.findall('duration">[\w ]+', str(sel[j])) 
            time = re.findall('>[\w ]+', str(time))
            time = re.findall('[\w ]+', str(time))

            view = re.findall('[0-9\.BMk]+ <', str(sel[j])) 
            value = re.findall('[0-9\.]+', str(view))
            unit = re.findall('[BMk]', str(view))
            view = list(map(float, value))
            if unit != []:
                if unit[0] == 'B':
                    view = view[0] * 1000000000
                elif unit[0] == 'M':
                    view = view[0] * 1000000
                elif unit[0] == 'k':
                    view = view[0] * 1000
            else:
                view = view[0]
                
            title = ''.join(title)
            time = ''.join(time)
            Data.append((title,view,time,href))

    return Data

Data = video('3month','Chinese',1000)

# Data_sc = sc.parallelize(Data)
# Data_scf = Data_sc.distinct().sortBy(lambda s: s[1],ascending = False).collect()
Data = sorted(Data,key=lambda s: s[1], reverse=True)

# Here you should choose, if you use the spark to process, you should close the sorted, 
# and change the Data variable name in Next line. (like > d = pd.DataFrame(Data_scf))
d = pd.DataFrame(Data)
d.columns = ['Title','View','Time','URL']

file_path = r'./video.xlsx'
writer = pd.ExcelWriter(file_path)
d.to_excel(writer, index=False,encoding='utf-8',sheet_name='Sheet')
writer.save()
# Check the file, and name is video.xlsx. 