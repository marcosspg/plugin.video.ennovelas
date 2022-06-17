import xbmcgui
import xbmcaddon
import sys
from urllib.parse import parse_qsl
import xbmcgui
import xbmcplugin
from lib import requests
import tools
import logger 
from bs4 import BeautifulSoup

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
        logger.debug(response.text);
        # root = html.fromstring(response.text);
        # novelas = root.xpath('//div[@class="video-post clearfix"]');
        # for novela in novelas:
        #     titulo = novela.xpath('a/p/text()')[0];
        #     url = novela.xpath('a/@href')[0];
        #     portada = str(novela.xpath('a/div[@class="thumb"]/@style')[0]).replace(")", "").replace("background-image:url(","");
        #     tools.addItemMenu(url, portada);
getNovelas();
xbmcplugin.endOfDirectory(__handle__)
