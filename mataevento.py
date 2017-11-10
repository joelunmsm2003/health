import requests
import os
r=  requests.get('http://dilootu.com/html/files/robot.html')

count = len(r.text.split('evento.py'))

if count > 2:
	os.system('killall -9 pyhon')
else:
	print 'Perfect ..'
