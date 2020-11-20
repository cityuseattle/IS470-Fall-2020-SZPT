import webbrowser
import sys

place=''
if len(sys.argv)>1:
    place=''.join(sys.argv[1:])

webbrowser.open("https://ditu.amap.com/"+place)
#webbrowser.open("https://google.com/maps/search/"+place)