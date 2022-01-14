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
    url = sys.argv[1]
    createsrcfile(url)
