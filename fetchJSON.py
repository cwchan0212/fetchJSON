import urllib, json, codecs
from urllib import request, parse
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


def fetchJSON(url: str) -> dict:
    print("url", url)

    userAgent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}

    req = Request(url, headers=userAgent)
    try:
        print(req.header_items())
        response = urlopen(req)
        with urllib.request.urlopen(req) as f:
            pass
        print(f.status)
    except HTTPError as e:
        print('Error code: ', e.code)
    except URLError as e:
        # do something
        print('Reason: ', e.reason)
    else:
        # do something
        out = codecs.decode(response.read()) # byte
        
        f = open("./out.txt", "w")
        f.write(out)
        f.close()

        jsonList = json.loads(out)
        print("Type:", type(jsonList))

        print('good!')
