import os
import sys

def createsrcfile(path):
    os.system('''echo "deb http://%s kali-last-snapshot main non-free contrib
deb-src http://%s kali-last-snapshot main non-free contrib
deb http://%s kali-experimental main non-free contrib
deb-src http://%s kali-experimental main non-free contrib
deb http://%s kali-rolling main non-free contrib
deb-src http://%s kali-rolling main non-free contrib"| sudo tee /etc/apt/sources.list''' % (path, path, path, path, path, path))

if __name__ == "__main__":
    packname = sys.argv[1]
    # Name to search########
    # packname = 'dirsearch' #####    
    ########################
    os.system("sudo cp /etc/apt/sources.list ./sources.listold")

    os.system("touch sources.list")
    # timelist = []
    urls = ['ftp.harukasan.org/kali','kali.download/kali','ftp.jaist.ac.jp/pub/Linux/kali','kali.itsec.am/kali','mirror-1.truenetwork.ru/kali','mirror.lagoon.nc/kali','hlzmel.fsmg.org.nz/kali','wlglam.fsmg.org.nz/kali','ftp.acc.umu.se/mirror/kali.org/kali','mirror.karneval.cz/pub/linux/kali','mirror.serverion.com/kali','mirrors.dotsrc.org/kali','mirror.pyratelan.org/kali','ftp.halifax.rwth-aachen.de/kali','ftp2.nluug.nl/os/Linux/distr/kali','ftp1.nluug.nl/os/Linux/distr/kali','mirror.erickochen.nl/kali','mirror.neostrada.nl/kali','archive-4.kali.org/kali']
    urls2 = ['ftp.belnet.be/mirror/kali/kali', 'ftp.free.fr/pub/kali', 'ftp.cc.uoc.gr/mirrors/linux/kali/kali', 'kali.koyanet.lv/kali', 'mirrors.netix.net/kali', 'mirrors.ocf.berkeley.edu/kali', 'archive.linux.duke.edu/kalilinux/kali', 'mirror.cedia.org.ec/kali', 'ftp.ne.jp/Linux/packages/kali/kali', 'ftp.riken.jp/Linux/kali', 'linux3.yz.yamagata-u.ac.jp/pub/Linux/kali', 'mirror.serverius.net/kali', 'mirror.ufro.cl/kali', 'us.mirror.nsec.pt/kali']
    urls2.extend(urls)
    for url in urls2:
        os.system("sudo cp ./sources.list /etc/apt/sources.list")
        createsrcfile(url)
        os.system("sudo apt search "+ packname + " | grep " + packname + "> datasearch")
        if os.stat("datasearch").st_size != 0:
            print(url)
            break
    # os.system("sudo apt install "+ packname)
    print("=====================================================================================")
    print("===||   "+ packname+"  in : " + url)
    print("=====================================================================================")
    os.system("sudo cp ./sources.listold /etc/apt/sources.list")
    os.system("sudo rm ./datasearch")
    

    