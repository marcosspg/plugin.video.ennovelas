import sys
import xbmcplugin
import xbmcaddon
import re
#import urllib2
import xbmcgui




def getSetting(name):
    return xbmcaddon.Addon().getSetting(name);



# def getUrl(url):
    # f = urllib2.urlopen(url);
    # data = f.read();
    # f.close();
    # return data;
# 

def findall(pattern, text, flags):
    try:
        return re.findall(pattern=pattern, string=text, flags=flags);
    except:
        return None;


def addItemMenu(label, thumbnail, url, isPlayable = 'false', isFolder = False):
    __handle__ = int(sys.argv[1])
    li = xbmcgui.ListItem(label, None);
    li.setProperty("IsPlayable", isPlayable);

    xbmcplugin.addDirectoryItem(__handle__, listitem=li, url=url, isFolder=isFolder);