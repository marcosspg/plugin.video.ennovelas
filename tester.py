import requests
from bs4 import ResultSet, BeautifulSoup
urlNovelasActuales = "https://www.ennovelas.com/novelas";



def getNovelas():
    with requests.Session() as s:
        response = s.get(urlNovelasActuales);
        for novela in BeautifulSoup(response.content).find_all("div",attrs={"class":"video-post clearfix"}):
            titulo = novela.find("a").find("p").text;
            url = novela.find("a")["href"];
            portada = str(novela.find("a").find("div", attrs={"class":"thumb"})["style"]).replace(")", "").replace("background-image:url(","");
            tools.addItemMenu(url, portada);
getNovelas();