import urllib.request
import pandas as pd
import os

catname = 'Tunics'
# catname = Top

def getimg(url,count):
    localpath = '{0}/{1}.jpg'.format(catname, count)
    urllib.request.urlretrieve(url, localpath)

# data = pd.read_csv("top_urls.csv")
data = pd.read_csv("tunic_urls.csv")
print(data.head())
URLS = data["imageURL"]

for count, url in enumerate(URLS):
    try:
        name = data['ProductId'][count]
        getimg(url,name)
        print(count)
    except:
        print("unable to fetch {}".format(count))


print("************************************************************")

