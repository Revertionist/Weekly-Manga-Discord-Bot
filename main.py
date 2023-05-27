import requests
from bs4 import BeautifulSoup

data = []
count = 0
req = requests.get("https://www.viz.com/read/shonenjump/section/hot-series")
soup = BeautifulSoup(req.content, 'html.parser')
lit = soup.find_all("a", class_="disp-bl color-white o_chapters-link")
lit2 = soup.find_all("a", class_ = "o_inner-link pad-x-rg pad-y-sm mar-b-rg type-bs type-sm--sm type-rg--lg type-center line-solid hover-bg-dark-red color-white")
for i in lit:
    link = "https://www.viz.com"+i["href"]
    image = i.find("img")["src"]
    titleDiv = i.find("div", class_ = "pad-x-rg pad-t-rg pad-b-sm type-sm type-rg--sm type-md--lg type-center line-solid")
    title = titleDiv.getText().strip()
    chapter = lit2[count].find("span").getText().strip()
    dic = {
        "title": title,
        "link": link,
        "img": image,
        "chapter": chapter
    }
    data.append(dic)
    count += 1
print (data)
