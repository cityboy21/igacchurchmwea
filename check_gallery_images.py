import json
import urllib.request
import sys
p='c:/Users/ADMIN/Desktop/igac 2/data/gallery.json'
with open(p) as f:
    g=json.load(f)
for item in g:
    url='http://localhost:8000/'+item['thumb'].lstrip('./')
    try:
        r=urllib.request.urlopen(url)
        print(item['title'], url, '->', r.status)
    except Exception as e:
        print(item['title'], url, '->', 'ERROR', e)
