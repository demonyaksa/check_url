#coding=utf8
import requests

f = open("D:/url.txt", "r")
for line in f.readlines():
	line = line.strip('\n')#忽略换行符
	try:
		res = requests.get(line,timeout=2)
		if res.status_code == 200:
			print(res.url + " " +str(res.status_code))
		else:
			pass
	except:
		pass
f.close()