# Codded By BL4CK DR460N
# copyright (c) 2019 @BL4CK_DR460N
# coding=utf-8
import requests,os,sys,traceback,urllib
base_url = "http://tinyurl.com/api-create.php"

class tiny:
	def main(self,url):
		try:
			s_url = base_url+ "?" \
				+urllib.parse.urlencode({"url": url})
			r = requests.get(s_url)
			if "Error" in r.text:
				print ("\033[31m[-] Url Not Found")
				sys.exit()
			else:
				print ("\033[33m[+] Shorted : \033[32m"+r.text)
				sys.exit()
		except Exception as e:
			print ("\033[31m[-] ERROR: \033[37m"+e)
			sys.exit()

if __name__ == '__main__':
	print ("\033[37m[+] Url Shorten tinyurl By BL4CK DR460N")
	print ("\033[34m[+] Codded By BL4CK DR460N")
	print ("\033[33m"+40*"=")
	url = input("\033[37m[?] Url To Short : \033[32m")
#	url = "https://github.com"
	tiny().main(url)

