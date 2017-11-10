import urllib.request

#specify url
urlStart = "https://www.pokemon.com/us/pokemon-tcg/pokemon-cards/"
setNum = "4"
setCode = "sm" # sm / xy / bw
urlEnd = "?" + setNum + "-" + setCode + "=on"
url = urlStart + urlEnd
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
