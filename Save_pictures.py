import requests
from bs4 import BeautifulSoup 

# In this file, I have two purposes. One is how to requests the picture; 
# another one is how to save the binary picture.

# And, I also compared two kinds of different methods. 
# Once, I used the content of requests to save the picture. 
# Another once, I used the shutil.copyfileobj to save the pic.


def content(url):
    """Use the content of requests 
    the file name is content_img.jpg."""

    r = requests.get(url)
    r2 = r.content
    file_name = url.split('/')[-1]
    pic_out = open('content_img_'+file_name+'.jpg','wb')
    pic_out.write(r2)
    pic_out.close()

def shutil(url):
    import shutil
    """Use the shutil.copyfileobj
    the file name is shutil_img.jpg."""

    sh = requests.get(url,stream=True)
    file_name = url.split('/')[-1]
    pic_out = open('shutil_img_'+file_name+'.jpg','wb')
    shutil.copyfileobj(sh.raw,pic_out)
    pic_out.close()

url = 'https://s1.imgs.cc/img/aaaaaAlIU.jpg?_w=750'
content(url)
shutil(url)
print('We can see the shutil which cannot get the picture from this page, but content can get successfully.')

url = 'https://files.ckcdn.com/attachments/forum/201905/02/013301re4yvl9vvv191hgy.png.thumb.jpg'
content(url)
shutil(url)
print('But if our url has the name of jpg, then both can get successfully.')
print('So I will say content method is more flexible on here.')
