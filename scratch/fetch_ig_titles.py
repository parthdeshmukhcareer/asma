import urllib.request
import re
import json

ids = ['Dc_aB3TTvyS', 'Dc7oLIpTtWo', 'DcVzyqYTu3d', 'DcJGyNlTHUU']

for vid in ids:
    try:
        url = f"https://www.instagram.com/reel/{vid}/"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        title_match = re.search(r'<title>(.*?)</title>', html)
        if title_match:
            print(f"ID: {vid} | Title: {title_match.group(1)}")
        else:
            print(f"ID: {vid} | Title not found")
    except Exception as e:
        print(f"ID: {vid} | Error: {e}")
