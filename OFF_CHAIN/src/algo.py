asciinum=list(range(47,58,1))
asciivow=[65,69,73,79,85,97,101,105,111,117]

def doctopoli (words):
    letters=list(words)
    cypher=[]
    for i in letters:
        cypher.append(ord(i))
    for j in cypher:
        if j==32:
            cypher.remove(j)
    for j in range(0,len(cypher)):
        if cypher[j] in asciinum:
            cypher[j]=cypher[j]-48
        elif cypher[j] in asciivow:
            if cypher[j]==65:
                cypher[j]=(int(cypher[j]/5)-1)
            else:
                cypher[j]=int(cypher[j]/5)
    return(cypher)

#TEST WITH: print(doctopoli('Shaan here 1 2 9 0'))
