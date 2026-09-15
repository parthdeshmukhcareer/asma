import urllib.request
import re

try:
    req = urllib.request.Request(
        'https://www.youtube.com/@advaitsharemarketacademy-x5p/shorts',
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    html = urllib.request.urlopen(req).read().decode('utf-8')
    video_ids = re.findall(r'"videoId":"(.*?)"', html)
    seen = set()
    unique_ids = []
    for vid in video_ids:
        if vid not in seen and len(vid) == 11:
            seen.add(vid)
            unique_ids.append(vid)
    print("Found shorts IDs:", unique_ids[:5])
except Exception as e:
    print("Error:", e)
