import requests
from bs4 import BeautifulSoup

data = []
req = requests.get("https://www.viz.com/read/shonenjump/section/hot-series")
soup = BeautifulSoup(req.content, 'html.parser')
lit = soup.find_all("a", class_="disp-bl color-white o_chapters-link")
for i in lit:
    link = i["href"]
    image = i.find("img")["src"]
    titleDiv = i.find("div", class_ = "pad-x-rg pad-t-rg pad-b-sm type-sm type-rg--sm type-md--lg type-center line-solid")
    title = titleDiv.getText().strip()
    dic = {
        "link": link,
        "img": image,
        "title": title
    }
    data.append(dic)
    
print (data)


# chapter class = o_inner-link pad-x-rg pad-y-sm mar-b-rg type-bs type-sm--sm type-rg--lg type-center line-solid hover-bg-dark-red color-white