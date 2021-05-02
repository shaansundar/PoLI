import hashlib
import datetime
import os


def filesize(filename):
    return str(os.path.getsize(filename))

def hashitup(name,timestamp,filesize):
    var="{}{}{}".format(filesize,timestamp,name).encode('utf-8')
    hashed_var = hashlib.sha256(var).hexdigest()
    return hashed_var

def timestamp():
    return str(datetime.datetime.now())

def hashval(name):
    return hashitup(name, timestamp(), filesize(name))

