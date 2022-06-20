import sys
from urllib.parse import urlencode

import urllib3
import xbmcplugin
import xbmcaddon
import re
#import urllib2
import xbmcgui
import logger
import xbmc
import xbmcvfs





def getSetting(name):
    return xbmcaddon.Addon().getSetting(name);



__settings__ = xbmcaddon.Addon(id="plugin.video.ennovelas")
__handle__ = int(sys.argv[1])
PY3 = False
if sys.version_info[0] >= 3: PY3 = True; unicode = str; unichr = chr; long = int

def translatePath(path):
    """
    Kodi 19: xbmc.translatePath is deprecated and might be removed in future kodi versions. Please use xbmcvfs.translatePath instead.
    @param path: cadena con path special://
    @type path: str
    @rtype: str
    @return: devuelve la cadena con el path real
    """
    if not path:
        return ''

    if PY3:
        if isinstance(path, bytes):
            path = path.decode('utf-8')
        path = xbmcvfs.translatePath(path)
        if isinstance(path, bytes):
            path = path.decode('utf-8')
    else:
        path = xbmc.translatePath(path)

    return path

def get_runtime_path():
    return translatePath(__settings__.getAddonInfo('Path'))



def build_url(query):
    base_url = sys.argv[0];
    return base_url + "?"+ urlencode(query)

def addItemMenu(label, thumbnail, url, isPlayable = 'false', isFolder = False, isVideo=False):
    thumbnail = str(thumbnail);
    
    li = xbmcgui.ListItem(label = label);
    li.setProperty("IsPlayable", isPlayable);
    #li.setThumbnailImage(thumbnail)
    li.setArt({'icon': thumbnail, 'thumb': thumbnail, 'poster': thumbnail,'fanart': thumbnail, 'fanart_image': thumbnail})
    if isVideo:
        li.setInfo('video', {})
    #li.setProperty('fanart_image', thumbnail)
    xbmcplugin.addDirectoryItem(__handle__, listitem=li, url=url, isFolder=isFolder);


def play_video(label, path):
    """
    Play a video by the provided path.
    :param path: str
    :return: None
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path, label=label)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(__handle__, True, listitem=play_item)