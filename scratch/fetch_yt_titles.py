import urllib.request
import json

ids = ['RuwJDUGmMko', 'FP0KdwnWhc8', 'c-cFGIe_Kqw', 'g-dINon688c', 'loqs401dPqY']

for vid in ids:
    try:
        url = f"https://www.youtube.com/oembed?url=http://www.youtube.com/watch?v={vid}&format=json"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req).read().decode('utf-8')
        data = json.loads(res)
        print(f"ID: {vid} | Title: {data['title']}")
    except Exception as e:
        print(f"ID: {vid} | Error: {e}")
