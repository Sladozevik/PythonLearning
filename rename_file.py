import os
import re

def rename_files():
	# part where we make a list of names
	file_list = os.listdir(r'C:\Users\aslado\OneDrive\_Learning\Python\Udacity\prank')
	os.chdir(r'C:\Users\aslado\OneDrive\_Learning\Python\Udacity\prank')
	path = os.getcwd()
	print(path)

	# part where we reneame files
	for file_name in file_list:
		print('old name', file_name)
		os.rename(file_name, re.sub('[0-9]','',file_name)) # you can add othe names, for example if you want to rename file or replace filenam 
		print('new name', file_name)

rename_files()