from urllib.request import urlopen
import bs4

def ngsm():
    link = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    html = urlopen(link)
    bsobj = bs4.BeautifulSoup(html)
    content = bsobj.find("div", {"id": "toc"}).get_text()
    print(content)

ngsm()
