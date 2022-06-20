import logger
import re
import requests;
from bs4 import BeautifulSoup
import tools
urlNovelasActuales = "https://www.ennovelas.com/novelas";

def getNovelas():
    with requests.Session() as s:
        response = s.get(urlNovelasActuales);
        for novela in BeautifulSoup(response.content, "html.parser").find_all("div",attrs={"class":"video-post clearfix"}):
            titulo = novela.find("a").find("p").text;
            url = str(novela.find("a")["href"]);
            portada = str(novela.find("a").find("div", attrs={"class":"thumb"})["style"]).replace(")", "").replace("background-image:url(","");
            tools.addItemMenu(titulo, portada, tools.build_url({"action":"verNovela", "url":url}), isFolder=True);
        s.close();
def getCapitulos(url):
    with requests.Session() as s:
        response = s.get(url);
        #La url original no se le puede poner un límite de páginas, pero en el botón de siguiente página si, así que se obtiene la url de ese botón y se modifica el límite
        urlBotonSiguientePagina = BeautifulSoup(response.content, "html.parser").find("div",attrs={"class":"paging"}).find("a")["href"]
        urlBotonSiguientePagina = re.sub(r'per_page=[0-9]+', 'per_page=10000', urlBotonSiguientePagina)
        urlBotonSiguientePagina = re.sub(r'&page=[0-9]+', '&page=1', urlBotonSiguientePagina)
        response = s.get(urlBotonSiguientePagina);

        for capitulo in BeautifulSoup(response.content, "html.parser").find_all("div", attrs={"class":"videobox"}):
            url = capitulo.find_all("a")[0]["href"];
            thumbnail = str(capitulo.find_all("a")[0].find("div")["style"]).replace("background-image: url('", "").replace("')", "");
            title = capitulo.find_all("a")[1].text;
            tools.addItemMenu(label=title, thumbnail=thumbnail, url=tools.build_url({"action":"verCapitulo", "url":url}), isFolder=True);

        s.close();

def verCapitulo(url):
    with requests.Session() as s:
        response = s.get(url);
        urlVideo = re.findall("sources: \[{src: \".*v.mp4", response.text)[0].replace("sources: [{src: \"", "")
        logger.debug(urlVideo);
        #tools.play_video("Ver online", urlVideo);
        tools.addItemMenu("Ver online", "", urlVideo, "true", isVideo=True)
        s.close();