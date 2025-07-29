# 09-melon-search.py

import time
import requests
import json

def melon_search(query : str) -> list:
    # ? 앞 부분이 http로 서버 주소 + 서버 내의 리소스 위치
    search_url = 'https://www.melon.com/search/keyword/index.json'

    # ? 뒤에 오는 부분이 Query Parameters
    # params = {
    # 'jscallback' : 'jQuery19104406029060066261_1753756079350',
    # 'query' : 'idol',
    # '_': '1753756079354',
    # }


    params = {
    'jscallback' : '_',
    'query' : 'idol',
    '_': int(time.time()),
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
    } 

    res = requests.get(search_url, params=params, headers=headers)
    

    if res.status_code == 200:
        # return res.json()
        # response format: json(O), jsonp(O)
        jsonp_string = res.text
        jsonp_string = jsonp_string[2:-2] # hard coding
        return json.loads(jsonp_string)
    return []

# 현재 소스파일이 파이썬 실행의 진입점일 때 
if __name__ == '__main__':
    print(melon_search('idol'))