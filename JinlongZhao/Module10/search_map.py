import webbrowser
import sys

place=''
if len(sys.argv)>1:
    place=''.join(sys.argv[1:])

webbrowser.open("https://goole.com/maps/search/"+place)
