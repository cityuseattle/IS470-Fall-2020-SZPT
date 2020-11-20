import webbrowser
import sys

place=''
if len(sys.argv)>1:
    place=''.join(sys.argv[1:])

webbrowser.open("https://map.baidu.com/"+place)