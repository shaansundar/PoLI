from algo import doctopoli
from hash import hashval
import PyPDF2

def readfile (name):
    f=open(str(name),"r")
    k=list(f.read())
    render=(doctopoli(k))
    return render

def readfilePDF (name):
    PDFobj = open(name, 'rb')
    textData=""
    PDFdata = PyPDF2.PdfFileReader(PDFobj)
    totalPages=PDFdata.numPages
    for i in range(1,totalPages):
        pageObj = PDFdata.getPage(i)
        pageData= pageObj.extractText()
        textData=textData+pageData
    return(textData)


def writefile (name,content):
    k=hashval(name)
    f = open(k, "a")
    for i in content:
        f.write(str(i))
    f.close()
    return(k)

def docToHashedPoli(filename):
    extension=list(filename.split('.'))
    if(extension[1]=="pdf"):
        convertedVal=readfilePDF(filename)
        newName="{}.txt".format(''.join(extension[:-1]))
        f=open(newName,"a")
        f.write(convertedVal)
        f.close()
        renderedval=readfile(newName)
    else:
        renderedval=readfile(filename)

    return(writefile(filename,renderedval))

