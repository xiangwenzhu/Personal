#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import os
import re

print(__name__)

def gethtmlfiles():
    path = "C:\\Users\\xwzhu\\Desktop\\TestHelpFiles"
    files=[]
    for f in os.listdir(path): 
        file = os.path.join(path,f)
        if(os.path.isfile(file)):
            ext = os.path.splitext(f)[1]
            if(ext == ".html" or ext==".htm"):
                files.append(file)
    return files

def getimages():
    path = "C:\\Users\\xwzhu\\Desktop\\TestHelpFiles\images"
    files=[]
    for f in os.listdir(path): 
        file = os.path.join(path,f)
        if(os.path.isfile(file)):
           files.append(file)
    return files

def getlinks(s):
    #reg=r'<img\s\w*?href="(\w*?.[jpg|png])"'
    reg=r'<img.+?src=".*?images/(.+?\.\w*?)"'
    groups = re.findall(reg,s,re.M or re.I)
    if groups:
        return groups;
    return []

def PrintUnusedImages():
    files = gethtmlfiles();
    images=[(x).upper() for x in getimages()]   
    
    count=0
    for f in files:
        fobj = open(f,'r')
        for line in fobj:
            links = getlinks(line)            
            for link in links:
                count+=1
                print(f+"   "+link)
                image=("C:\\Users\\xwzhu\\Desktop\\TestHelpFiles\\images\\"+link).upper()
                
                if(image in images):
                    print(image)
                    images.remove(image)                    
    print(len(images))
    for unusedImg in images:
        os.remove(unusedImg)