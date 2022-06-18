import xbmcaddon
import sys
from urllib.parse import parse_qsl
import xbmcgui
import xbmcplugin
import requests
import tools
import logger 
from bs4 import BeautifulSoup, ResultSet


__addon__ = xbmcaddon.Addon();
__addonname__ = __addon__.getAddonInfo("name");

line1 = "jolalaaaaa";


#Muestra una ventana de dialogo para confirmar
#xbmcgui.Dialog().ok(__addonname__, line1);

# Get the plugin url in plugin:// notation.
__url__ = sys.argv[0]
# Get the plugin handle as an integer number.
__handle__ = int(sys.argv[1])



urlNovelasActuales = "https://www.ennovelas.com/novelas";




def getNovelas():
    with requests.Session() as s:
        response = s.get(urlNovelasActuales);
        for novela in BeautifulSoup(response.content).find_all("div",attrs={"class":"video-post clearfix"}):
            titulo = novela.find("a").find("p").text;
            url = str(novela.find("a")["href"]);
            portada = str(novela.find("a").find("div", attrs={"class":"thumb"})["style"]).replace(")", "").replace("background-image:url(","");
            tools.addItemMenu(titulo, portada, url);
getNovelas();
xbmcplugin.endOfDirectory(__handle__)
