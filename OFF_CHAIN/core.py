import sys
sys.path.insert(0, './src')
from IO import docToHashedPoli
from similaritycheck import similarity
from ethacc import *
from hash import timestamp

HashedPoliFile1=docToHashedPoli("paper1.pdf")
HashedPoliFile2=docToHashedPoli("paper2.pdf")
print(HashedPoliFile1)
print(HashedPoliFile2)
print("\n")
infringedVal=(similarity(HashedPoliFile1, HashedPoliFile2))
time=timestamp()
print("Infringement value is: "+str(infringedVal))
if(infringedVal<30):
    print("Input metadata fields in order (author, title)")
    author,title=input().split(',')
    print("Type Tags of your document seperated by commas(tag1,tag2,...)")
    tags=input().split(',')
    writeContract(HashedPoliFile1, time, node_acc2,author,title,tags)
else:
    print("Infringed Document, blockchain publication failure")