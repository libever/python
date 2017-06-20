#coding=utf-8

import hashlib
import random
import time
import rsa
import base64
import os

def MD5(str):
    return hashlib.md5(str).hexdigest()

def RAND(f=0,t=1000):
    return random.randint(f, t)  

def Rstring(l):
    return "".join(random.sample('abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHKJKLMNOPQRSTUVWXYZ',l))

def dailyToken(token_str):
    by =  "%s_._._..%s" % (token_str,time.strftime("%Y_%m..%d")) 
    return MD5( "%s_._._..%s" % (token_str,time.strftime("%Y_%m..%d")) )

def rsa_decrypt(message,pri):
    if os.path.isfile(pri) :
        pri = rsa.PrivateKey.load_pkcs1(open(pri,"r").read())
    return rsa.decrypt(message, pri)

def rsa_encrypt(message,pub):
    if os.path.isfile(pub) :
        pub = rsa.PublicKey.load_pkcs1(open(pub,"r").read())
    return rsa.encrypt(message, pub)

def rsanewkeys(size):
    pub,pri = rsa.newkeys(size)
    return pub._save_pkcs1_pem(),pri._save_pkcs1_pem()

if __name__ == "__main__":
    pub,pri = rsanewkeys(1024)
    open("o.pub","w").write(pub)
    open("o.pri","w").write(pri)
    en = rsa_encrypt("hello world","o.pub")
    print en
    print rsa_decrypt(en,"o.pri")


