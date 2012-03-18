import urllib
import BeautifulSoup
import unicodedata
while (1):
	print "Enter the Word"
	word=raw_input()
	word1=urllib.quote(word)
	f=urllib.urlopen("http://www.merriam-webster.com/dictionary/"+word1)
	s=f.read()
	htmlcontent=BeautifulSoup.BeautifulSoup(s,convertEntities='html')
	results=htmlcontent.findAll('div',attrs={'class':'KonaBody'})
	if results:
		meaning=unicodedata.normalize('NFKD',results[0].getText()).encode('ascii','ignore')
		print meaning
	else:	
		print "Sorry no description available"



