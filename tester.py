import re

from bs4 import BeautifulSoup
import requests

text = """
var holaplayer;
window.hola_player({ player: '#hola',
    				share: false,
    				poster: 'https://13-ukr-sv.ennovelas.com/i/01/00000/021bgiebgjkp_xt.jpg',
    				sources: [{src: "https://13-ukr-sv.ennovelas.com/wloopagyopz54amjhxtyi44bp5fewduxbec3xstvq2tfcvt44ce42zwtcsma/v.mp4", type: "video/mp4", res: 720, label: "720"}],
					preload: 'auto',
					controls_watermark: { image: 'https://www.ennovelas.com/LOGOO.png', tooltip: 'Ennovelas.com - Entretenimiento en tus manos', url: 'https://www.ennovelas.com' },thumbnails:{ vtt:'https://www.ennovelas.com/dl?op=get_slides&length=2661.16&url=https://13-ukr-sv.ennovelas.com/i/01/00000/021bgiebgjkp0000.jpg' },
					videojs_options: { 



"""


print(re.findall("sources: \[{src: \".*v.mp4", text)[0].replace("sources: [{src: \"", ""));