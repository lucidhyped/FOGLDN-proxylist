#!/usr/bin/python
from termcolor import colored, cprint




username ="enter_fogldn_username_here"
password ="enter_fogldn_password_here"

cprint('\n@lucidhyped on Twitter', 'magenta')
print colored('What a time to be Alive!, Let\'s Cook!', 'magenta')
print ('\n\nUsing This info...\n')
cprint('\nUsername: ' +username, 'magenta')
cprint('Password: ' +password, 'magenta')
#Regions Avaialbe for FOGLDN Proxies
print'\n\nAvailable Regions..\n\n'
fogRegions = [
'Proxy-uk',
'Proxy-uk-s1',
'Proxy-uk-s2',
'Proxy-uk-s3',
'Proxy-uk-s4',
'Proxy-uk-s5',
'Proxy-us',
'Proxy-us-s1',
'Proxy-us-s2',
'Proxy-us-s3',
'Proxy-us-s4',
'Proxy-us-s5',
'Proxy-au',
'Proxy-au-s1',
'Proxy-ca',
'Proxy-ca-s1',
'Proxy-ca-s2',
'Proxy-jp-s1',
'Proxy-jp-s2',
'Proxy-de',
'Proxy-vn',
'Proxy-pl',
'Proxy-at',
'Proxy-at-s1',
'Proxy-es-s1',
'Proxy-es-s2',
'Proxy-no-s1',
'Proxy-no-s2',
'Proxy-fr',
'Proxy-nl',
'Proxy-nl-s1',
'Proxy-kith',
'Proxy-sns',
'Proxy-supreme-uk-1',
'Proxy-supreme-us-1',
'Proxy-supreme-us-2',
'Proxy-footsites',
'Proxy-mesh',
'Proxy-nike',
]

cprint('\n'.join(fogRegions), 'magenta')
#Raw Input type of proxies and what to name the .txt file
proxyType = raw_input("\n\nWhat Region of proxies?\n")
numProxies = raw_input("\n\nHow many proxies do you need?\n")
#Writting the txt file
myFile = open("proxies.txt","w")
loopTimes = int(numProxies)
timesToLoop = int(loopTimes)

for x in range(1, timesToLoop+1):
	myFile.write(proxyType+".fogldn.com:33128:"+username+"!a"+str(x)+":"+password+"\n")
myFile.close()
#@lucidhyped Twitter
cprint('\n\nSaved Proxies: ' +numProxies, 'magenta')
cprint('File Name: ' +str(myFile.name), 'magenta')
