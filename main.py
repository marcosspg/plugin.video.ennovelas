import os
import xbmcaddon
import sys
from urllib.parse import urlparse, parse_qs
import xbmcgui
import xbmcplugin
import actions
import tools
import logger 

__url__ = sys.argv[0]
__handle__ = int(sys.argv[1])

args = parse_qs(sys.argv[2][1:]);

action = args.get('action', None);

if action != None:
    action = action[0];

#Acciones    
if action == None:
    tools.addItemMenu("Buscar", os.path.join(tools.get_runtime_path(),"resources","buttons","search.png"), tools.build_url({"action":"buscar"}), isFolder=True);
    tools.addItemMenu("Lista de novelas", os.path.join(tools.get_runtime_path(),"resources","buttons","list.png"), tools.build_url({"action":"listaNovelas"}),isFolder=True);
elif action == "listaNovelas":
    actions.getNovelas();
elif action == "verNovela":
    url = args.get('url', None)[0];
    actions.getCapitulos(url);
elif action == "verCapitulo":
    url = args.get('url', None)[0];
    actions.verCapitulo(url);
xbmcplugin.endOfDirectory(__handle__)
