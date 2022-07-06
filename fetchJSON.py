import urllib, json, codecs
from urllib import request, parse
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

def fetchJSON(url: str) -> dict:
    print("[fetchJSON]: url -> ", url)

    userAgent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}

    req = Request(url, headers=userAgent)
    try:
        response = urlopen(req)
        with urllib.request.urlopen(req) as f:
            pass
        print("[fetchJSON]: status -> ", f.status)
    except HTTPError as e:
        print("[fetchJSON]: ", 'Error code: ', e.code)
    except URLError as e:
        # do something
        print("[fetchJSON]: ", 'Reason: ', e.reason)
    else:
        # do something
        out = codecs.decode(response.read()) # byte2Sttring
        jsonList = json.loads(out)

        if type(jsonList) == dict:
            for key, value in jsonList.items():
                print("[fetchJSON]: key =", key, ", value =", value)
        else:
            print(type(jsonList))
            for line in jsonList:
                print("[fetchJSON]:", line)

    return jsonList

url = "https://timeapi.io/api/Time/current/zone?timeZone=Asia/Hong_Kong"
#        http://worldtimeapi.org/api/timezone/Asia/Hong_Kong
#url = "https://type.fit/api/quotes"

fetchJSON(url)
