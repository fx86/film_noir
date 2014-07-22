import mechanize as mech
from bs4 import BeautifulSoup as bs

URL = "http://technoir.nl/page/"

data = []
for i in range(1, 46):

  br = mech.Browser()
  br = br.open(URL + str(i))
  soup = bs(br.read())
  all_anchors = soup.findAll('a')

  for tagnum, tag in enumerate(all_anchors):
    kids = tag.findChildren('img')
    if  len(kids) == 1:
      nextel = all_anchors[tagnum + 1]
      imdb = nextel['href'] if nextel.has_attr('href') else ''
      moviename = nextel['title'] if nextel.has_attr('title') else ''
      tn_src = tag['href']
      alt = kids[0]['alt']
      gif_src = kids[0]['src']
      print "\t", moviename, alt

      data.append([moviename, imdb, tn_src, alt, gif_src])

  print "done with page %d" %i