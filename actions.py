import logger
import re
import requests;
from bs4 import BeautifulSoup
import tools
import xbmc

host = "zonevipz.com";
urlNovelasActuales = "https://"+host+"/?op=categories_all&per_page=60&page=";

capitulosVistos = list(tools.getCapitulosVistos());


def getNovelas(pagina):
    if pagina == None or pagina == "0":
        pagina = 1;
    try:
        pagina = int(pagina);
    except:
        pagina = 1;
    with requests.Session() as s:
        response = s.get(urlNovelasActuales+str(pagina));
        #logger.debug(response.text);
        # with open(__file__.replace("actions.py", "test.html").replace("\\", "/"), "w", encoding="utf-8") as out:
        #     out.write(response.text);
        #     out.close();
        for novela in BeautifulSoup(response.content, "html.parser").find_all("div",attrs={"class":"video-post clearfix"}):
            titulo = novela.find("a").find("p").text;
            url = str(novela.find("a")["href"]);
            portada = str(novela.find("a").find("div", attrs={"class":"thumb"})["style"]).replace(")", "").replace("background-image:url(","");
            tools.addItemMenu(titulo, portada, tools.build_url({"action":"verNovela", "url":url}), isFolder=True);
        tools.addItemMenu("Página "+str(pagina+1), None, tools.build_url({"action":"listaNovelas", "pagina": str(pagina+1)}), isFolder=True);
        s.close();

def getCapitulos(url):
    with requests.Session() as s:
        response = s.get(url);
        #La url original no se le puede poner un límite de páginas, pero en el botón de siguiente página si, así que se obtiene la url de ese botón y se modifica el límite
        try:
            urlBotonSiguientePagina = BeautifulSoup(response.content, "html.parser").find("div",attrs={"class":"paging"}).find("a")["href"]
            urlBotonSiguientePagina = re.sub(r'per_page=[0-9]+', 'per_page=10000', urlBotonSiguientePagina)
            urlBotonSiguientePagina = re.sub(r'&page=[0-9]+', '&page=1', urlBotonSiguientePagina)
            response = s.get(urlBotonSiguientePagina);
        except:
            None;
        capitulos = BeautifulSoup(response.content, "html.parser").find_all("div", attrs={"class":"videobox"})
        logger.debug(str(capitulosVistos));
        for capitulo in capitulos:
            url = capitulo.find_all("a")[0]["href"];
            thumbnail = str(capitulo.find_all("a")[0].find("div")["style"]).replace("background-image: url('", "").replace("')", "");
            title = capitulo.find_all("a")[1].text;
            
            if url in capitulosVistos:
                title+= " (Visto)";
            tools.addItemMenu(label=title, thumbnail=thumbnail, url=tools.build_url({"action":"verCapitulo", "url":url}), isFolder=True);
        if capitulos.__len__() == 0:
            tools.addItemMenu("No hay capítulos", None, "");
        s.close();

def verCapitulo(url):
    with requests.Session() as s:
        response = s.get(url);
        urlVideo = re.findall("sources: \[{src: \".*v.mp4", response.text)[0].replace("sources: [{src: \"", "")
        #tools.play_video("Ver online", urlVideo);
        tools.addItemMenu("Ver online", "", urlVideo, "true", isVideo=True)
        tools.marcarVisto(url);
        s.close();


def buscar():
    searchStr = "";
    keyboard = xbmc.Keyboard(searchStr,'Buscar novelas')
    keyboard.doModal()
    if (keyboard.isConfirmed() == False):
        return
    searchStr = keyboard.getText().replace(' ','+')  # sometimes you need to replace spaces with + or %20
    
    logger.debug("Búsqueda: "+str(searchStr))
    if len(searchStr) == 0:
        return
    else:
        buscarNovela(searchStr);
        return searchStr


def buscarNovela(busqueda):
    buscarURL = "https://"+host+"/?op=categories_all&name="+busqueda;
    with requests.Session() as s:
        response = s.get(buscarURL);
        novelas = BeautifulSoup(response.content, "html.parser").find_all("div",attrs={"class":"video-post clearfix"});
        for novela in novelas:
            titulo = novela.find("a").find("p").text;
            url = str(novela.find("a")["href"]);
            portada = str(novela.find("a").find("div", attrs={"class":"thumb"})["style"]).replace(")", "").replace("background-image:url(","");
            tools.addItemMenu(titulo, portada, tools.build_url({"action":"verNovela", "url":url}), isFolder=True);
        if novelas.__len__() == 0:
            tools.addItemMenu("No se ha encontrado ninguna novela", None, "");
        s.close();