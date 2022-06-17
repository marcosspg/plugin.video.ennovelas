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


def addItemMenu(label, thumbnail, isPlayable = 'false', isFolder = False):
    __handle__ = init(sys.argv[1])
    li = xbmcgui.ListItem(label=label, thumbnailImage=thumbnail);
    li.setProperty("IsPlayable", isPlayable);

    xbmcplugin.addDirectoryItems(__handle__, li, len(li));