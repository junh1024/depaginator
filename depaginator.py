import urllib
import urllib.request
# import bs4

#depaginator, to dump a series of pages into a html file based on url pattern. Written by junh1024 in 2016
baseurl="http://example.com/category/categoryname/page/" #change as desired
# baseurl="http://example.com/tag/tagname/page/"

file = open('pages.htm','wb') #change as desired. Write Binary is a must, since pages may be unicode, and pythong will herp a derp otherwise and you'll generally have a hard time getting unicode pages to dump.
for i in range (1,30): #page range, change as desired
	# file.write ( "=====page====="+str(i) +'\n')
	request=urllib.request.Request(baseurl+str(i), headers={'User-Agent' : "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"} )
	response=urllib.request.urlopen(request)
	document = response.read()
	file.write(document)
	
	# soup = bs4.BeautifulSoup(x)
	# h2=soup.find_all('h2')

	# for thing in h2: #from 1-100
		# f.write(thing.string.encode('cp850','replace').decode('cp850')+'\n')
