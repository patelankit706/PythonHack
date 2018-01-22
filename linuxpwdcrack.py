#!/usr/bin/env python

import crypt
from threading import Thread

hash=raw_input('Enter hash string')
dict=raw_input('Enter word list file')
cryptedpwd=raw_input('Enter crypted passwd')

f=open(dict,'r')

def crypthack(hash,word):
  cryptlie=crypt.crypt(word,hash)
  if cryptlie==cryptedpwd:
	print 'password is:%s'%word

for word in f.readlines():
  password=word.strip('\n')
  t=Thread(target=crypthack,args=(hash,password))
  t.start()
#  crypthack(word)

