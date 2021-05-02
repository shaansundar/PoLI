
def similarity(name1,name2):
    f1=open(name1,"r")
    f2=open(name2,"r")
    point=0
    text1=f1.read()
    text2=f2.read()
    minval=min(len(text1),len(text2))
    totalchecks=int(minval/2)
    for i in range(0,minval,2):
        if(text1[i:i+1]==text2[i:i+1]):
            point=point+1
    copied=point/totalchecks*100
    return copied