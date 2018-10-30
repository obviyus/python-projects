import requests, bs4, sys

# remove spacing, adding lowercase to match Azlyrics url format
artist=input("artist: ").replace(" ","")
song=input("song: ").replace(" ","")

# url format: www.azlyrics.com/lyrics/<artist>/<song>.html
url='http://www.azlyrics.com/lyrics/%s/%s.html' % (artist,song)


# http://stackoverflow.com/questions/33174804/python-requests-getting-connection-aborted-badstatusline-error
# using a header to hide like a browser
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }

r=requests.get(url,headers=headers)

print('\nconnected to %s' % url)

lyric_page=bs4.BeautifulSoup(r.text,"html.parser")

# a div has no name
for lyrics in lyric_page.find_all("div", {"class":""}):
  print(lyrics.text)

input("Press Enter to continue...")

import msvcrt as m
def wait():
    m.getch()