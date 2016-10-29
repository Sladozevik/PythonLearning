import os 
import urllib.request
import urllib.parse 

quotes = open(r'C:\Users\aslado\OneDrive\_Learning\Python\Udacity\movie_quotes.txt')
content_of_file = quotes.read()
   # print(content_of_file)
quotes.close()

    # Check for curse words
url_link = 'http://www.wdylike.appspot.com/?q='
content_of_file_quoted = urllib.parse.quote(content_of_file)
url_full = url_link + content_of_file_quoted
print(url_full)

connection = urllib.request.urlopen(url_full)
output = connection.read()
print(output)
connection.close()