from appearance.hue import *
import zipfile
def zipfile():
	print (info("Files have to be in the same directory - Include .zip or .txt in file name"))
	zipfilename = raw_input(que('Zip file:' ))
	dictionary = raw_input(que('Dictionary file: '))
	print (run("Cracking..."))
	password = None
	zip_file = zipfilename
	with open(dictionary, 'r') as f:
		for line in f.readlines():
			password = line.strip('\n')
			try:
				zip_file.extractall(pwd=password)
			except:
				pass
	print (good("Password found: " + password))
