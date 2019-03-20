import cv2
import pandas as pd
import numpy as np

data = pd.read_csv("small-2oq-c1r.csv", error_bad_lines=False)

data.head()

a = data['productId']
b = data['title']
c = data['description']
d = data['imageUrlStr']

e = []
for i , url in enumerate(list(b)):
    url = str(url)
    a = url.split()
    print(a)
    if a[-1]=='Top':
        e.append(d[i])


E = pd.DataFrame(e,columns=["imageURL"])
E.to_csv("top_urls.csv", header=True)
req_data = pd.concat([a,b,c,E],axis=1)

req_data.to_csv("small_tunics.csv",header=True)