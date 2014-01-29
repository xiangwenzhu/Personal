import os
import re

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

def getlinks(s):
    reg=r'<a href="(\w*?.\w*?)">'
    groups = re.findall(reg,s,re.M)
    if groups:
        return groups;
    return []

def CheckUnusedHtmlFiles():
    files = gethtmlfiles();
    for f in files:
        fobj = open(f,'r')
        for line in fobj:
            links = getlinks(line)
            for link in links:
                if(not any(link in item for item in links)):
                    print(f + "    " + link)
            
import CheckUnusedImages

if __name__ == '__main__':
    CheckUnusedImages.PrintUnusedImages()
