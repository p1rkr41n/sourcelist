import os
import sys

def createsrcfile(path):
    os.system('''echo "deb http://http.kali.org/kali kali-rolling main non-free contrib
deb-src http://http.kali.org/kali kali-rolling main non-free contrib
deb http://kali.cs.nctu.edu.tw/kali kali-rolling main non-free contrib
deb-src http://kali.cs.nctu.edu.tw/kali kali-rolling main non-free contrib
deb http://%s kali-last-snapshot main non-free contrib
deb-src http://%s kali-last-snapshot main non-free contrib
deb http://%s kali-experimental main non-free contrib
deb-src http://%s kali-experimental main non-free contrib
deb http://%s kali-rolling main non-free contrib
deb-src http://%s kali-rolling main non-free contrib"| sudo tee /etc/apt/sources.list''' % (path, path, path, path, path, path))

if __name__ == '__main__':
    packname = sys.argv[1]
    sources = sys.argv[2]
    os.system("cp /etc/apt/sources.list ./sources.listold")
    createsrcfile(sources)
    os.system("sudo apt install " + packname)
    os.system("sudo cp ./sources.listold /etc/apt/sources.list")
