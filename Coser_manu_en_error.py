#-*- coding:utf-8 -*-

#This software is distributed with the sole aim of study of coding,
#I will take NO responsibilities of any kind of the results of improper using.


import base64

import diao
import starting

import StringIO



from Tk import *
from Tk import Image as other


##import warnings

# warnings.filterwarnings("ignore")

MAX_WIDTH = 800
MAX_HEIGHT = 800

import ImageTk

import webbrowser

from PIL import Image


import random


import socket
socket.setdefaulttimeout(180)
import json
from sys import exit
import os
import urllib
import urllib2
from time import time, sleep

from multiprocessing.dummy import Pool as ThreadPool

Format = ['bmp', 'gif', 'jpg', 'png']

rate = 50


def process(file):
    extension = os.path.splitext(file)[1].lower()[1:]
    if extension in Format:

        try:

            img = Image.open(file)
            size=os.path.getsize(file)/1000
            
            if size>2000:
                rate=40
            elif size>1500:
                rate=50
            elif size>1000:
                rate=60
            elif size>500:
                rate=75
            elif size>200:
                rate=90
            else:
                rate=100
                


            
            img.thumbnail((img.size[0] * rate / 100, img.size[1] * rate / 100))

            name = os.path.basename(file)
            path = name.split('_')[0] + '/small/' + name[:-4] + '_re.jpg'

            img.save(path)

            print '%',
        except:
            print 'cannot do the processing, wtf'
            pass


def multiimage(id):
    print 'processing pics......'
    start = time()

    lis = os.listdir(id)

    lis = map(lambda x: str(id) + '/' + x, lis)

    pool = ThreadPool(8)

    results = pool.map(process, lis)

    pool.close()
    pool.join()

    end = time()

    elapse = end - start


    print '\n' + str(len(lis) - 1) + ' images total time =%.3fs' % float(elapse)
    print 'imaging every pic used %.3fs' % (elapse / float(len(lis)))
    print 'processed: ' + str(len(lis) - 1) + ' images'

    global remaining
    remaining=len(content)
    


def creathtml(id):
   
    


    global outp
    outp = id
    
    lis = os.listdir(id)
    lis.remove('small')

    f = open(id + '/index.html', 'w+')

    g = open(id + '.html', 'w+')

    webf = '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\
<title>your photos</title></head>\
<font color="cyan"><div class="text" style="text-align:center;">\
    <h1> All yours! </h1></div></font><body bgcolor="lavender">'

    webg = '<!DOCTYPE html><html><head><meta http-equiv="content-type" content="text/html; charset=utf-8"/>\
<title>your photos</title></head>\
<font color="cyan"><div class="text" style="text-align:center;">\
    <h1> All yours! </h1></div></font><body bgcolor="lavender">'

    for i in lis:
        webf += '<a href="' + i + '">' + \
                '<img src="small/' + i[:-4] + '_re.jpg" title="big big big !!!" width=200 />&nbsp;</a>'

        webg += '<a href="' + id + '/' + i + '">' + \
                '<img src="' + id + '/small/' + i[:-4] + '_re.jpg" title="big big big !!!" width=200 />&nbsp;</a>'

    webf += '</body></html>'
    webg += '</body></html>'

    f.write(webf)
    f.close()

    g.write(webg)
    g.close()

    


def small(fold):
    path=os.listdir(fold+'/small')
    have=list(map(lambda x:fold+'/small/'+x,path))
    random.shuffle(have)
    return have



def another(fold):
    path=os.listdir(fold)
    path.remove('small')
    path.remove('index.html')

    have=list(map(lambda x:fold+'/'+x,path))
    random.shuffle(have)
    return have

def download(ininin):
    
    

    
    try:
        name=ininin[0].split('_')[0]+'_'+ininin[0].split('_')[1]+'.jpg'
        urllib.urlretrieve(url=ininin[1],filename=name)

        size=os.path.getsize(name)/1000    
        how=str(size)+' KB' if size <1000 else str(size/1000)+' MB'


    except Exception,e:
        print 'try %s again for 30s passed'%name.split('/')[-1]
##        print e
        how='nothing'
        try:
            urllib.urlretrieve(url=ininin[1],filename=name)
            size=os.path.getsize(name)/1000    
            how=str(size)+' KB' if size <1000 else str(size/1000)+' MB'
        except:
            print 'try %s last time for another 30s passed'%name.split('/')[-1]
            try:
                urllib.urlretrieve(url=ininin[1],filename=name)
                size=os.path.getsize(name)/1000    
                how=str(size)+' KB' if size <1000 else str(size/1000)+' MB'
            except:
                print 'give up %s '%name.split('/')[-1]
                how='nothing'
                pass
        

    try:
        print 'get: '+str(ininin[0]).split('_')[-2]+'_'\
              +str(ininin[0]).split('_')[-1]+'      |  size:  '+how
    except Exception,e:
##        print e
        print('retrieving: '+name.split('/')[-1])+'      |  size:  '+how

    


def gogogo(member_id, stuff):
    socket.setdefaulttimeout(20)
    start = time()

    if not os.path.exists(member_id):
        os.makedirs(member_id)

    if not os.path.exists(member_id + '/small'):
        os.makedirs(member_id + '/small')

    pool = ThreadPool(8)

    results = pool.map(download, stuff)

    pool.close()
    pool.join()

    end = time()

    elapse = end - start

    


        
    print ' '
    print str(len(content)) + ' images used total time =%.3fs' % float(elapse)
    print 'for every pic used %.3fs' % (elapse / float(len(content)))


def normal(id, stuff):
    if not os.path.exists(id):
        os.makedirs(id)

    start = time()

    ct = 0

    for i in stuff:
        urllib.urlretrieve(url=i[1], filename=i[0])
        ct += 1
        print
        'singleline succeed + %d' % ct

    end = time()

    elapse = end - start

    print
    'total time =' + str(elapse)
    print
    'for every pic used %.3fs' % (elapse / float(len(content)))




content = []


def main(member_id, cho, page=1, index=0):

    global having
    




    if member_id.strip().lower() == 'q10086':
        print('thx, hope u enjoy~')
        exit(0)

    if page > 5000:
        print 'wtf? something must go wrong!'
        exit(0)

    if len(member_id) < 2:
        print '\ngive me a coser ID like 18943 or whatever'
        


        main(member_id=raw_input('coser ID :  '), cho='-m', page=1, index=0)

    url = 'http://worldcosplay.net/en/api/member/photos?member_id=%s&page=%s&limit=100000&rows=16&p3_photo_list=1' % (
        member_id, page)
    try:
        r = urllib2.urlopen(url, timeout=10)



    except Exception,e:

        e = str(e)
        if e == '<urlopen error timed out>' or e == 'timed out':
            print '!!reloading page %2d for trying more than 10s' % page+' total images: %d' % index
            main(member_id, cho=cho, page=page , index=index)
        elif e == 'HTTP Error 404: Not Found':
            
            print  'coser ID NOT exist, choose another one'
            main(member_id=raw_input('one more ID Please~~~:  '), cho='-m', page=1, index=0)
        else:
            print e
            
            print 'donnot know what happened, starting again.'
            main(member_id=raw_input('coser ID Please~~~:  '), cho='-m', page=1, index=0)

    if r.code == 200:

        data = json.loads(r.read())

        if data['has_error'] != 0:
            print 'connection failed'
            exit(1)

        photo_data_list = data['list']

        print 'loading page %2d' % page + ' total images: %d' % index

        if not photo_data_list:
            print 'there are %s pages, about to pull %s images' % (page, index)

            if index >= 10:

                kk = raw_input('download %s pics ?[y/n] '%index)
                kk = str(kk).strip().lower()
                
                if kk == 'y':
                    
                    print 'starting ' + str(len(content)) + ' images in total'
                else:
                    print 'exiting'
                    
                    main(member_id=raw_input('feed me an ID~~~:'), cho='-m', page=1, index=0)
                    

            elif index == 0:
                print 'this coser has 0 pic, choose another one'
                main(member_id=raw_input('another ID please~~~ :'), cho='-m', page=1, index=0)
            else:
                pass

            if cho == '-m':

                gogogo(member_id, content)

            else:

                normal(member_id, content)

            multiimage(member_id)

            creathtml(member_id)

            having=another(member_id)
            



            print 'with all : ' + str(len(content)) + '  images'


            print '\nanother round'
            
            main(member_id=raw_input('23333 or another ID : '), cho='-m', page=1, index=0)

        for photo_data in photo_data_list:

            url = photo_data['photo']['sq300_url']
            subject = photo_data['photo']['subject']

            try:

                url = url.replace('/sq300', '')
                subject = subject.replace('/', '_')
            except:
                print '?',
                pass

            filename = '%s/%s_%s_%s.jpg' % (member_id, member_id, index, subject)

            content.append((filename, url))

            index += 1

        page += 1

        main(member_id, cho=cho, page=page, index=index)  # recursion

    else:
        print 'connection failed'
        exit(1)


def st():
    main(member_id=raw_input('feed me an ID~~~: '), cho='-m', page=1, index=0)
    




def ini():
    
    try:
        print '\nprogram written by: Shichao Ji'
        print '   '
        st()
    except:
        
        
        print 'program already started!!!'
        print 'press "Enter" to continue'





# -----------------------------------------------------------------------------------------------------------



class ImagePreview:
    def __init__(self, root):
        self.imageName = "None"
        self.imageWindow = Frame(root, width=MAX_WIDTH, height=MAX_HEIGHT, borderwidth=1, relief=SUNKEN)
        self.imageWindow.configure(width=MAX_WIDTH, height=MAX_HEIGHT)

        self.changeImage(mypic)





    def changeImage(self, filename):
        try:
            self.imageContainer.destroy()
        except:
            pass




        try:

            displayImage = Image.open(filename)
        except:

            self.imageContainer = Label(self.imageWindow, image=None, text="木有了")


        if displayImage != None:
            displayImage = self.scaleImage(displayImage)
            displayPhoto = ImageTk.PhotoImage(displayImage)



            self.imageContainer = Label(self.imageWindow, image=displayPhoto, text=None, height=MAX_HEIGHT)
            self.imageContainer.image = displayPhoto

        self.imageContainer.pack()



    
    def scaleImage(self, image):
        imageSize = image.size

        if imageSize[0] > MAX_WIDTH or imageSize[1] > MAX_HEIGHT:
           
            scaleXDiff = float(MAX_WIDTH) / imageSize[0]
            scaleYDiff = float(MAX_HEIGHT) / imageSize[1]

         
            if scaleXDiff < scaleYDiff:
                scale = scaleXDiff
            else:
                scale = scaleYDiff

            image = image.resize(((int(imageSize[0] * scale)), int(imageSize[1] * scale)), Image.BILINEAR)

        return image






    def pack(self):
        self.imageWindow.pack(fill='both', expand=1, pady=0)
        self.imageContainer.pack()




class pics:
    def __init__(self, root):
 
        self.root=root

##        self.root.wm_iconbitmap(StringIO.StringIO(diao.cute().decode('base64')))
        self.root.iconbitmap('diao.ico')

        self.root.wm_attributes('-alpha', 0.98)

        self.root.geometry('800x830-400+50')

      
##        self.root.resizable(width=False, height=False)
        self.root.minsize(width=600, height=600 +30)
        self.root.maxsize(width=1000, height=1000 +30)
        self.root.title("a fun program --Shichao Ji")

        self.root.bind("<Escape>", self.gun)


        

        self.butt1=Button(self.root, text='website ranking page', command=lambda:webbrowser.open\
            ('http://worldcosplay.net/zh-hans/ranking/member/cosplayer'), \
                  fg='purple', font=('Calibri', 16), width=30)
        self.butt1.pack(side='top',anchor='w')




        self.butt2=Button(self.root, text='Start', fg='blue',\
                  font=('Calibri', 14, 'normal'), wraplength=1,\
                   command=ini,bd=2,width=2,padx=10,height=6)
        
        self.butt2.pack(side='left',anchor='n')
##        op0.place(relx=-1, rely=0, relwidth=0.08, relheight=0.43)



        
        self.butt3=Button(self.root, text='Look', fg='darkgreen',\
                  font=('Calibri', 14, 'normal'), wraplength=1,\
                   command=self.changing,bd=2,width=2,padx=10,height=6)
        
##        op1.pack(side='left',anchor='ne')
        self.butt3.place(relx=0., rely=0.27)
        

        self.butt5=Button(self.root, text='S', fg='hotpink',\
                  font=('Calibri', 14, 'normal'), wraplength=1,\
                   command=self.small,bd=2,width=2,padx=10,height=1)
        
##        op1.pack(side='left',anchor='ne')
        self.butt5.place(relx=0., rely=0.48)


        self.butt6=Button(self.root, text='M', fg='mediumvioletred',\
        font=('Calibri', 14, 'normal'), wraplength=1,\
        command=self.middle,bd=2,width=2,padx=10,height=1)

        ##        op1.pack(side='left',anchor='ne')
        self.butt6.place(relx=0., rely=0.53)


        self.butt7=Button(self.root, text='L', fg='red',\
        font=('Calibri', 14, 'normal'), wraplength=1,\
        command=self.big,bd=2,width=2,padx=10,height=1)

        ##        op1.pack(side='left',anchor='ne')
        self.butt7.place(relx=0., rely=0.581)


        self.butt8=Button(self.root, text='Exit', fg='red',\
        font=('Calibri', 14, 'normal'), wraplength=1,\
        command=self.gun,bd=2,width=2,padx=10,height=4)

        ##        op1.pack(side='left',anchor='ne')
        self.butt8.place(relx=0., rely=0.85)




        self.butt4=Button(self.root, text='local browsing webpage after download', fg='orange', \
                  font=('Calibri', 16, 'normal'),\
                   command=self.out,width=32)
##        op2.pack(side='right',anchor='n')
        self.butt4.place(relx=.50, rely=0.0)


        
        self.setupLayout()
        self.packLayout()


        

    def setupLayout(self):
        self.imageWindow = ImagePreview(self.root)

        self.windowRefs = [self.imageWindow]

    def packLayout(self):
        for window in self.windowRefs:
            window.pack()




        

class Husky(pics):

    def __init__(self, root):
        pics.__init__(self, root)

        self.root=root


    def gun(self,kidding=0):

        exit(0)

    
    def out(self):


        try:
            os.system( '%s.html'%outp )
        except:
            print 'get pics first!'

    def folder(self):
        
        try:
            curr=os.getcwd()
            
            os.system('cd '+curr+'\\%s'%outp)
        except:
            print 'first get pics!'

    def changing(self):
        global remaining
        
        try:
            self.Label1.destroy()
            self.Label1 = Label(self.root, text=remaining\
                    ,font=('宋体', 14, 'normal'),fg='darkblue')

        except:
            pass

        self.Label1 = Label(self.root, text=remaining\
                ,font=('宋体', 14, 'normal'),fg='darkblue')       
        self.Label1.place(relx=0.015, rely=0.7)

              
        try:
            
            self.imageWindow.changeImage(having.pop())
        except:
            self.imageWindow.changeImage(mypic)
            print(0)
            
        
        remaining=len(having)

    def small(self):
        global MAX_WIDTH, MAX_HEIGHT
        MAX_WIDTH = 600
        MAX_HEIGHT = 600
        
        self.root.geometry('600x630-400+50')
        
        
        
        
    
    def middle(self):
        global MAX_WIDTH, MAX_HEIGHT
        MAX_WIDTH = 800
        MAX_HEIGHT = 800
        
        self.root.geometry('800x830-400+50')
     
    
    def big(self):

        global MAX_WIDTH, MAX_HEIGHT
        MAX_WIDTH = 1000
        MAX_HEIGHT = 1000
        
        self.root.geometry('1000x1030-400+50')  







if __name__=='__main__':

    icostring=diao.cute()
    icoimage=icostring.decode('base64')
    ff = open('diao.ico', "wb")
    ff.write(icoimage)
    ff.close()


    mypic=StringIO.StringIO(starting.cute().decode('base64'))




    remaining=0
    
    having=[]

    
    print('Declaimer: This software is distributed with the sole aim of study of coding, \
I will take NO responsibilities of any kind of the results of improper using.')
    Hokie=Tk()
    
    Husky(Hokie).root.mainloop()
