#!/usr/bin/python 
#-*- coding: utf-8 -*-
import sys,crypt,os
salt=sys.argv[2][0:12]
senhaencriptada=sys.argv[2]
print ("Salt: "+ salt)
wordlist=sys.argv[1]
with open(wordlist) as arq:
	for line in arq:
		linecrypt=crypt.crypt(line.rstrip(),salt)
		if linecrypt==senhaencriptada:
			print("*---------------------------------------*")
			print("*  A senha é: "+line.rstrip())
			print("*---------------------------------------*")
			break
		else:
			print("Testando senha: "+line.rstrip())





