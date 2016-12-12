from  urllib import request as req
from urllib import error as err

x = 'http://cs229.stanford.edu/materials.html'

def download(url):
	print('downloading...', url)
	try:
		html = req.urlopen(url).read()
		print('done')
	except err as e:
		print('Download error', e.reson)
		html = none
	return html

print(download(x))