
import base64

filename=str(raw_input('name: '))
print (filename)

imageFile=open(filename, "rb") 
string = base64.b64encode(imageFile.read())



topy='''
def cute():
    return """%s"""
    '''%string+'''
def name():
    return """%s"""'''%filename

outname='secret.py'

fh = open(outname, "wb")

fh.write(topy)
fh.close()
print ("done")
