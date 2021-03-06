import os
import sys
from typing import Text
import time

def createsrcfile(path):
    os.system('''echo "# Line commented out by installer because it failed to verify:
deb http://security.debian.org/debian-security bookworm/updates main contrib
# Line commented out by installer because it failed to verify:
deb-src http://security.debian.org/debian-security bookworm/updates main contrib
deb %s bookworm main
deb-src %s bookworm main

deb %s-security/ bookworm/updates main
deb-src %s-security/ bookworm/updates main

deb %s bookworm-updates main
deb-src %s bookworm-updates main
deb %s bookworm main contrib non-free
deb-src %s bookworm main contrib non-free

#release
deb %s bookworm-proposed-updates main contrib non-free
deb-src %s bookworm-proposed-updates main contrib non-free

deb %s-security/ bookworm/updates main contrib non-free
deb-src %s-security/ bookworm/updates main contrib non-free

deb %s bookworm-updates main contrib non-free
deb-src %s bookworm-updates main contrib non-free
deb %s bookworm-backports main contrib non-free
deb-src %s bookworm-backports main contrib non-free
deb [arch=arm64,amd64,armhf] https://packages.microsoft.com/ubuntu/20.04/mssql-server-2019 focal main
# deb-src [arch=arm64,amd64,armhf] https://packages.microsoft.com/ubuntu/20.04/mssql-server-2019 focal main"| sudo tee /etc/apt/sources.list''' % (path,path,path,path,path,path,path,path,path,path,path,path,path,path,path,path,))

def timers(path):
    urlfix = path.split('/')[0]
    start = time.time()
    os.system("sudo timeout 7 nc -vz "+urlfix+" 80 ")
    os.system("sudo timeout 7 wget "+path)
    return (time.time()-start)

def fastsources(listsource):
    print("fast sources")
    timelist = []
    urls2 = listsource
    # urls2.extend(urls)
    for url in urls2:
        temp = timers(url)
        timelist.append(temp)
    # print(timelist)
    print("=============================================================")
    for i in range(len(timelist)):
        temp = urls2[timelist.index(min(timelist))]
        print(str(i+1)+ "  : " + temp)
        timelist[timelist.index(min(timelist))] = 1000.0
    os.system("cp /etc/apt/sources.list ./sources.listfast")
    os.system("sudo rm kali.*")
    os.system("sudo rm wget-log*")
    os.system("sudo rm kali")
    return 0


if __name__ == "__main__":
    packname = sys.argv[1]
    # Name to search########
    # packname = 'dirsearch' #####
    ########################
    os.system("sudo cp /etc/apt/sources.list ./sources.listold")

    os.system("touch sources.list")
    # urls = [ 'kali.cs.nctu.edu.tw/kali', 'http.kali.org/kali','ftp.harukasan.org/kali','kali.download/kali','ftp.jaist.ac.jp/pub/Linux/kali','kali.itsec.am/kali','mirror-1.truenetwork.ru/kali','mirror.lagoon.nc/kali','hlzmel.fsmg.org.nz/kali','wlglam.fsmg.org.nz/kali','ftp.acc.umu.se/mirror/kali.org/kali','mirror.karneval.cz/pub/linux/kali','mirror.serverion.com/kali','mirrors.dotsrc.org/kali','mirror.pyratelan.org/kali','ftp.halifax.rwth-aachen.de/kali','ftp2.nluug.nl/os/Linux/distr/kali','ftp1.nluug.nl/os/Linux/distr/kali','mirror.erickochen.nl/kali','mirror.neostrada.nl/kali','archive-4.kali.org/kali']
    # urls2 = ['ftp.belnet.be/mirror/kali/kali', 'ftp.free.fr/pub/kali', 'ftp.cc.uoc.gr/mirrors/linux/kali/kali', 'kali.koyanet.lv/kali', 'mirrors.netix.net/kali', 'mirrors.ocf.berkeley.edu/kali', 'archive.linux.duke.edu/kalilinux/kali', 'mirror.cedia.org.ec/kali', 'ftp.ne.jp/Linux/packages/kali/kali', 'ftp.riken.jp/Linux/kali', 'linux3.yz.yamagata-u.ac.jp/pub/Linux/kali', 'mirror.serverius.net/kali', 'mirror.ufro.cl/kali', 'us.mirror.nsec.pt/kali']
    # urls2.extend(urls)
    urls2 = [
'http://deb.debian.org/debian',
'http://ftp.am.debian.org/debian',
'http://ftp.au.debian.org/debian',
'http://ftp.at.debian.org/debian',
'http://ftp.by.debian.org/debian',
'http://ftp.be.debian.org/debian',
'http://ftp.br.debian.org/debian',
'http://ftp.ca.debian.org/debian',
'http://ftp.cl.debian.org/debian',
'http://ftp.cn.debian.org/debian',
'http://ftp.hr.debian.org/debian',
'http://ftp.cz.debian.org/debian',
'http://ftp.dk.debian.org/debian',
'http://ftp.sv.debian.org/debian',
'http://ftp.ee.debian.org/debian',
'http://ftp.fr.debian.org/debian',
'http://ftp2.de.debian.org/debian',
'http://ftp.de.debian.org/debian',
'http://ftp.hk.debian.org/debian',
'http://ftp.hu.debian.org/debian',
'http://ftp.is.debian.org/debian',
'http://ftp.it.debian.org/debian',
'http://ftp.jp.debian.org/debian',
'http://ftp.kr.debian.org/debian',
'http://ftp.lt.debian.org/debian',
'http://ftp.md.debian.org/debian',
'http://ftp.nl.debian.org/debian',
'http://ftp.nz.debian.org/debian',
'http://ftp.pl.debian.org/debian',
'http://ftp.pt.debian.org/debian',
'http://ftp.ru.debian.org/debian',
'http://ftp.sk.debian.org/debian',
'http://ftp.si.debian.org/debian',
'http://ftp.es.debian.org/debian',
'http://ftp.ch.debian.org/debian',
'http://ftp.tw.debian.org/debian',
'http://ftp.uk.debian.org/debian',
'http://ftp.us.debian.org/debian',
'http://debian.unnoba.edu.ar/debian',
'http://mirror.sitsa.com.ar/debian',
'http://ftp.am.debian.org/debian',
'http://mirrors.asnet.am/debian',
'http://ftp.au.debian.org/debian',
'http://debian.mirror.digitalpacific.com.au/debian',
'http://debian.mirror.serversaustralia.com.au/debian',
'http://mirror.aarnet.edu.au/debian',
'http://mirror.amaze.com.au/debian',
'http://mirror.linux.org.au/debian',
'http://mirror.overthewire.com.au/debian',
'http://mirror.realcompute.io/debian',
'http://ftp.at.debian.org/debian',
'http://debian.anexia.at/debian',
'http://debian.lagis.at/debian',
'http://debian.mur.at/debian',
'http://debian.sil.at/debian',
'http://ftp.tu-graz.ac.at/mirror/debian',
'http://mirror.alwyzon.net/debian',
'http://ftp.by.debian.org/debian',
'http://ftp.byfly.by/debian',
'http://mirror.datacenter.by/debian',
'http://ftp.be.debian.org/debian',
'http://ftp.belnet.be/debian',
'http://mirror.as35701.net/debian',
'http://ftp.br.debian.org/debian',
'http://debian.c3sl.ufpr.br/debian',
'http://debian.itsbrasil.net/debian',
'http://mirror.uepg.br/debian',
'http://mirror.unesp.br/debian',
'http://debian.ipacct.com/debian',
'http://debian.mnet.bg/debian',
'http://debian.telecoms.bg/debian',
'http://ftp.uni-sofia.bg/debian',
'http://mirror.telepoint.bg/debian',
'http://mirror.sabay.com.kh/debian',
'http://ftp.ca.debian.org/debian',
'http://debian.mirror.estruxture.net/debian',
'http://debian.mirror.iweb.ca/debian',
'http://debian.mirror.rafal.ca/debian',
'http://mirror.estone.ca/debian',
'http://mirror.it.ubc.ca/debian',
'http://ftp.cl.debian.org/debian',
'http://mirror.insacom.cl/debian',
'http://mirror.ufro.cl/debian',
'http://ftp.cn.debian.org/debian',
'http://mirror.bjtu.edu.cn/debian',
'http://mirror.nju.edu.cn/debian',
'http://mirrors.163.com/debian',
'http://mirrors.bfsu.edu.cn/debian',
'http://mirrors.hit.edu.cn/debian',
'http://mirrors.huaweicloud.com/debian',
'http://mirror.sjtu.edu.cn/debian',
'http://mirrors.tuna.tsinghua.edu.cn/debian',
'http://mirrors.ustc.edu.cn/debian',
'http://debianmirror.una.ac.cr/debian',
'http://mirrors.ucr.ac.cr/debian',
'http://ftp.hr.debian.org/debian',
'http://debian.carnet.hr/debian',
'http://debian.iskon.hr/debian',
'http://ftp.cz.debian.org/debian',
'http://debian.mirror.web4u.cz/',
'http://debian.superhosting.cz/debian',
'http://ftp.cvut.cz/debian',
'http://ftp.debian.cz/debian',
'http://ftp.zcu.cz/debian',
'http://merlin.fit.vutbr.cz/debian',
'http://mirror.dkm.cz/debian',
'http://mirror.it4i.cz/debian',
'http://ftp.dk.debian.org/debian',
'http://mirror.asergo.com/debian',
'http://mirror.one.com/debian',
'http://mirrors.dotsrc.org/debian',
'http://mirrors.rackhosting.com/debian',
'http://ftp.sv.debian.org/debian',
'http://debian.salud.gob.sv/debian',
'http://ftp.ee.debian.org/debian',
'http://ftp.eenet.ee/debian',
'http://mirrors.xtom.ee/debian',
'http://ftp.fr.debian.org/debian',
'http://debian.apt-mirror.de/debian',
'http://debian.mirror.ate.info/',
'http://debian.obspm.fr/debian',
'http://debian.polytech-lille.fr/debian',
'http://debian.proxad.net/debian',
'http://debian.univ-reims.fr/debian',
'http://debian.univ-tlse2.fr/debian',
'http://deb-mir1.naitways.net/debian',
'http://ftp.ec-m.fr/debian',
'http://ftp.iut-bm.univ-fcomte.fr/debian',
'http://ftp.lip6.fr/pub/linux/distributions/debian',
'http://ftp.rezopole.net/debian',
'http://ftp.univ-pau.fr/linux/mirrors/debian',
'http://ftp.u-strasbg.fr/debian',
'http://mirror.johnnybegood.fr/debian',
'http://mirror.plusserver.com/debiandebian/',
'http://mirrors.ircam.fr/pub/debian',
'http://debian.grena.ge/debian',
'http://ftp2.de.debian.org/debian',
'http://ftp.de.debian.org/debian',
'http://artfiles.org/debian',
'http://debian.charite.de/debian',
'http://debian.inf.tu-dresden.de/debian',
'http://debian.intergenia.de/debian',
'http://debian.mirror.iphh.net/debian',
'http://debian.mirror.lrz.de/debian',
'http://debian.netcologne.de/debian',
'http://debian.uni-duisburg-essen.de/debian',
'http://de.mirrors.clouvider.net/debian',
'http://ftp.fau.de/debian',
'http://ftp.gwdg.de/debian',
'http://ftp.halifax.rwth-aachen.de/debian',
'http://ftp.hosteurope.de/mirror/ftp.debian.org/debian',
'http://ftp.mpi-sb.mpg.de/pub/linux/debian',
'http://ftp.plusline.net/debian',
'http://ftp-stud.hs-esslingen.de/debian',
'http://ftp.stw-bonn.de/debian',
'http://ftp.tu-chemnitz.de/debian',
'http://ftp.tu-clausthal.de/debian',
'http://ftp.uni-bayreuth.de/debian',
'http://ftp.uni-hannover.de/debiandebian/',
'http://ftp.uni-kl.de/debian',
'http://ftp.uni-mainz.de/debian',
'http://ftp.uni-stuttgart.de/debian',
'http://ftp.wrz.de/debian',
'http://mirror.23m.com/debian',
'http://mirror.de.leaseweb.net/debian',
'http://mirror.dogado.de/debian',
'http://mirror.ipb.de/debian',
'http://mirror.netzwerge.de/debian',
'http://mirrors.xtom.de/debian',
'http://mirror.united-gameserver.de/debian',
'http://mirror.wtnet.de/debian',
'http://packages.hs-regensburg.de/debian',
'http://pubmirror.plutex.de/debian',
'http://debian.otenet.gr/debian',
'http://ftp.hk.debian.org/debian',
'http://mirror.xtom.com.hk/debian',
'http://ftp.hu.debian.org/debian',
'http://ftp.bme.hu/debian',
'http://ftp.fsn.hu/debian',
'http://repo.jztkft.hu/debian',
'http://ftp.is.debian.org/debian',
'http://debianmirror.nkn.in/debian',
'http://kebo.pens.ac.id/debian',
'http://mirror.poliwangi.ac.id/debian',
'http://mirror.unair.ac.id/debian',
'http://debian.asis.ai/debian',
'http://debian.hostiran.ir/debian',
'http://debian.parspack.com/debian',
'http://mirror.aminidc.com/debian',
'http://mirrors.pardisco.co/debian',
'http://mirror.isoc.org.il/pub/debian',
'http://ftp.it.debian.org/debian',
'http://debian.connesi.it/debian',
'http://debian.mirror.garr.it/debian',
'http://ftp.linux.it/debian',
'http://giano.com.dist.unige.it/debian',
'http://mirror.units.it/debian',
'http://ftp.jp.debian.org/debian',
'http://debian-mirror.sakura.ne.jp/debian',
'http://dennou-k.gfd-dennou.org/debian',
'http://dennou-q.gfd-dennou.org/debian',
'http://ftp.jaist.ac.jp/debian',
'http://ftp.kddilabs.jp/pub/debian',
'http://ftp.nara.wide.ad.jp/debian',
'http://ftp.riken.jp/Linux/debiandebian/',
'http://ftp.yz.yamagata-u.ac.jp/debian',
'http://hanzubon.jp/debian',
'http://mirrors.xtom.jp/debian',
'http://debian.mirror.liquidtelecom.com/debian',
'http://ftp.kr.debian.org/debian',
'http://ftp.kaist.ac.kr/debian',
'http://mirror.anigil.com/debian',
'http://mirror.misakamikoto.network/debian',
'http://debian.koyanet.lv/debian',
'http://debian.linux.edu.lv/debian',
'http://ftp.lt.debian.org/debian',
'http://debian.mirror.vu.lt/debian',
'http://mirror.vpsnet.com/debian',
'http://debian.mirror.root.lu/debian',
'http://mirror.onevip.mk/debian',
'http://ftp.md.debian.org/debian',
'http://mirror.as43289.net/debian',
'http://mirrors.mivocloud.com/debian',
'http://debian.qontinuum.space/debian',
'http://ftp.nl.debian.org/debian',
'http://debian.mirror.cambrium.nl/debian',
'http://debian.snt.utwente.nl/debian',
'http://ftp.debian.xs4all.net/debian',
'http://mirror.dataone.nl/debian',
'http://mirror.duocast.net/debian',
'http://mirror.i3d.net/debian',
'http://mirror.nforce.com/debian',
'http://mirror.nl.datapacket.com/debian',
'http://mirror.novg.net/debian',
'http://mirror.serverius.net/debian',
'http://mirrors.xtom.nl/debian',
'http://mirror.vpgrp.io/debian',
'http://mirror.lagoon.nc/debian',
'http://ftp.nz.debian.org/debian',
'http://linux.purple-cat.net/debian',
'http://mirror.fsmg.org.nz/debian',
'http://ftp.pl.debian.org/debian',
'http://debian.inhost.pro/debian',
'http://ftp.agh.edu.pl/debian',
'http://ftp.icm.edu.pl/pub/Linux/debian',
'http://ftp.task.gda.pl/debian',
'http://ftp.pt.debian.org/debian',
'http://debian.uevora.pt/debian',
'http://ftp.eq.uc.pt/software/Linux/debian',
'http://ftp.rnl.tecnico.ulisboa.pt/pub/debian',
'http://mirrors.ptisp.pt/debian',
'http://mirrors.up.pt/debian',
'http://debian.mithril.re/debian',
'http://depot-debian.univ-reunion.fr/debian',
'http://mirror.flokinet.net/debian',
'http://mirror.linux.ro/debian',
'http://mirrors.hostico.ro/debian',
'http://mirrors.nav.ro/debian',
'http://mirrors.nxthost.com/debian',
'http://mirrors.pidginhost.com/debian',
'http://ftp.ru.debian.org/debian',
'http://ftp.psn.ru/debian',
'http://mirror.corbina.net/debian',
'http://mirror.docker.ru/debian',
'http://mirror.mephi.ru/debian',
'http://mirror.truenetwork.ru/debian',
'http://debian.petarmaric.com/debian',
'http://mirror.0x.sg/debian',
'http://mirror.coganng.com/debian',
'http://mirror.soonkeat.sg/debian',
'http://ftp.sk.debian.org/debian',
'http://ftp.debian.sk/debian',
'http://ftp.si.debian.org/debian',
'http://ftp.is.co.za/debian',
'http://mirror.hostafrica.co.za/debian',
'http://ftp.es.debian.org/debian',
'http://debian.grn.cat/debian',
'http://debian.redimadrid.es/debian',
'http://debian.redparra.com/debian',
'http://debian.uvigo.es/debian',
'http://ftp.caliu.cat/debian',
'http://ftp.cica.es/debian',
'http://ftp.udc.es/debian',
'http://mirror.librelabucm.org/debian',
'http://repo.ifca.es/debian',
'http://softlibre.unizar.es/debian',
'http://ulises.hostalia.com/debian',
'http://ftpmirror1.infania.net/debian',
'http://ftp.ch.debian.org/debian',
'http://debian.ethz.ch/debian',
'http://mirror1.infomaniak.com/debian',
'http://mirror2.infomaniak.com/debian',
'http://mirror.init7.net/debian',
'http://mirror.iway.ch/debian',
'http://mirror.sinavps.ch/debian',
'http://pkg.adfinis-sygroup.ch/debian',
'http://ftp.tw.debian.org/debian',
'http://debian.csie.ncku.edu.tw/debian',
'http://debian.csie.ntu.edu.tw/debian',
'http://debian.cs.nctu.edu.tw/debian',
'http://ftp.ntou.edu.tw/debian',
'http://opensource.nchc.org.tw/debian',
'http://tw1.mirror.blendbyte.net/debian',
'http://ftp.debianclub.org/debian',
'http://mirror.applebred.net/debian',
'http://mirror.kku.ac.th/debian',
'http://debian.gnu.gen.tr/debian',
'http://debian.astra.in.ua/debian',
'http://debian.netforce.hosting/debian',
'http://debian.volia.net/debian',
'http://mirror.mirohost.net/debian',
'http://ftp.uk.debian.org/debian',
'http://debian.mirrors.uk2.net/debian',
'http://debian.mirror.uk.sargasso.net/debian',
'http://free.hands.com/debian',
'http://ftp.ticklers.org/debian',
'http://mirror.bytemark.co.uk/debian',
'http://mirror.cov.ukservers.com/debian',
'http://mirror.lchost.net/debian',
'http://mirror.mythic-beasts.com/debian',
'http://mirror.ox.ac.uk/debian',
'http://mirror.positive-internet.com/debian',
'http://mirrors.coreix.net/debian',
'http://mirrorservice.org/sites/ftp.debian.org/debian',
'http://mirrors.m247.com/debian',
'http://mirror.sov.uk.goscomb.net/debian',
'http://ukdebian.mirror.anlx.net/debian',
'http://uk.mirrors.clouvider.net/debian',
'http://ftp.us.debian.org/debian',
'http://atl.mirrors.clouvider.net/debian',
'http://debian-archive.trafficmanager.net/debian',
'http://debian.cc.lehigh.edu/debian',
'http://debian.csail.mit.edu/debian',
'http://debian.cs.binghamton.edu/debian',
'http://debian.ec.as6453.net/debian',
'http://debian.gtisc.gatech.edu/debian',
'http://debian.mirror.constant.com/debian',
'http://debian.osuosl.org/debian',
'http://debian.uchicago.edu/debian',
'http://la.mirrors.clouvider.net/debian',
'http://mirror.cogentco.com/debian',
'http://mirror.keystealth.org/debian',
'http://mirror.pit.teraswitch.com/debian',
'http://mirrors.accretive-networks.net/debian',
'http://mirrors.advancedhosters.com/debian',
'http://mirrors.bloomu.edu/debian',
'http://mirrors.edge.kernel.org/debian',
'http://mirrors.gigenet.com/debian',
'http://mirror.siena.edu/debian',
'http://mirrors.lug.mtu.edu/debian',
'http://mirrors.ocf.berkeley.edu/debian',
'http://mirror.steadfast.net/debian',
'http://mirrors.vcea.wsu.edu/debian',
'http://mirrors.wikimedia.org/debian',
'http://mirrors.xtom.com/debian',
'http://mirror.us.leaseweb.net/debian',
'http://mirror.us.oneandone.net/debian',
'http://nyc.mirrors.clouvider.net/debian',
'http://plug-mirror.rcac.purdue.edu/debian',
'http://repo.ialab.dsu.edu/debian',
'http://debian.repo.cure.edu.uy/debian',
'http://debian.xtdv.net/debian',
'http://mirror.bizflycloud.vn/debian'] 
    searchlist = []
    for url in urls2:
        os.system("sudo cp ./sources.list /etc/apt/sources.list")
        createsrcfile(url)
        os.system("sudo apt search "+ packname + " | grep " + packname + "> datasearch")
        if os.stat("datasearch").st_size != 0:
            # os.system("cat datasearch")
            with open("datasearch") as f:
                text = f.read()
                print(text)
                if 'residual' in text and text.count('\n') == text.count('residual'):
                    continue

            searchlist.append(url)
            os.system("cat ./datasearch ; sudo rm ./datasearch")
            break

    fastsources(searchlist)

    os.system("sudo cp ./sources.listold /etc/apt/sources.list")
    os.system("sudo rm ./datasearch")