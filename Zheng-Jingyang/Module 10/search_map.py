import webbrowser
import sys

place = ''
if len(sys.argv)>1:
    place=''.join(sys.argv[1:])

webbrowser.open("https://google.com/maps/search/"+place)

try:
    res.raise_for_status()
    print("Status Code:", res.status_code)
    print("Length of the text:", len(res.text))
    print(res.text[:103])
except Exception as exc:
    print("Oh no: %s" %(exc))