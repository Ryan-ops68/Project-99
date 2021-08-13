import os
from posix import RTLD_NODELETE
import shutil
import time
def main():
    dfc = 0
    dic = 0
    path = "/"
    days = 30
    seconds = time.time()-(days*24*60*60)
    if os.path.exists(path):
        for root, folder, file in os.walk(path):
            if seconds>=getffage(root):
                removeFolder(root)
                dfc+=1
            else: 
                for f in folder:
                    fpath = os.path.join(root,folder)
                    if seconds>=getffage(fpath):
                        removeFolder(fpath)
                        dfc+=1
                for fi in file:
                    fipath = os.path.join(root,file)
                    if seconds>=getffage(fipath):
                        removeFolder(fipath)
                        dic+=1
    else:
        print ("path not found")
    print(dfc)
    print(dic)
def removeFolder(path):
    if not os.remove(path):
        print("removed successfully")
    else:
        print("Unable to delete") 
def getffage(path):
    ctime = os.stat(path).st_ctime
    return ctime
main()   
            
                        
