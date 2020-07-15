from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
import sys
import random
from cmath import sqrt
from math import *
import random
import numpy as np
import matplotlib.pyplot as plt
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot

rastgele=[]
app = QApplication(sys.argv)
window = QWidget()
window.setGeometry(750, 300, 400, 300)
window.setWindowTitle("K-MEANS")
window.setWindowIcon(QIcon("icon.ico"))

liste=[]
liste1=[]
genel=[]
birinci = QLineEdit()
birinci1 = QLineEdit()
ikinci = QLineEdit()
ikinci1 = QLineEdit()
ücüncü = QLineEdit()
ücüncü1 = QLineEdit()
dort = QLineEdit()
dort1 = QLineEdit()
alti=QLineEdit()
yedi=QLineEdit()
bes=QLineEdit()
label8 = QLabel("Küme Merkezleri:")
label10=QLabel("")
label11=QLabel("")
veri=[[],[],[],[]]
rastgele_noktalar=[]
merkez=[]
c=[]
d=[]
indextut=[]
merkez1=[]
yedek=[]
sırala=[]
veriler=[[],[]]
renk_index=[]
merkezler=[[],[]]
sayac=0
def pencere():
    v_box=QVBoxLayout()
    h1_box=QHBoxLayout()
    label1=QLabel("{}: ".format(1))
    h1_box.addWidget(label1)
    h1_box.addWidget(birinci)
    h1_box.addWidget(birinci1)
    h2_box=QHBoxLayout()
    label2=QLabel("{}: ".format(2))

    h2_box.addWidget(label2)
    h2_box.addWidget(ikinci)
    h2_box.addWidget(ikinci1)
    h3_box=QHBoxLayout()
    label3=QLabel("{}: ".format(3))

    h3_box.addWidget(label3)
    h3_box.addWidget(ücüncü)
    h3_box.addWidget(ücüncü1)
    h4_box=QHBoxLayout()
    label4=QLabel("{}: ".format(4))

    h4_box.addWidget(label4)
    h4_box.addWidget(dort)
    h4_box.addWidget(dort1)
    h5_box=QHBoxLayout()
    label5=QLabel("")
    label6=QLabel("X")
    label7=QLabel("Y")
    label6.setFont(QFont("Times New Roman",11,QFont.Bold))
    label7.setFont(QFont("Times New Roman",11,QFont.Bold))
    h5_box.addWidget(label5)
    h5_box.addWidget(label6)
    h5_box.addWidget(label7)
    h6_box=QHBoxLayout()
    sonuc=QPushButton("SONUÇ")
    ekleme=QPushButton("EKLE")
    label9=QLabel("Küme Sayısı:")
    label9.setFont(QFont("Times New Roman",11,QFont.Bold,Qt.red))
    label8.setFont(QFont("Times New Roman",11,QFont.Bold))
    h6_box.addWidget(label9)
    h6_box.addWidget(bes)
    h6_box.addWidget(ekleme)
    h6_box.addWidget(sonuc)
    h7_box=QHBoxLayout()
    h7_box.addWidget(label8)
    h7_box.addWidget(alti)
    h7_box.addWidget(yedi)
    h8_box=QHBoxLayout();
    sil=QPushButton("SİL")
    label10.setFont(QFont("Times New Roman", 11, QFont.Bold))
    h8_box.addWidget(label10)
    h8_box.addWidget(sil)

    v_box.addLayout(h5_box)
    v_box.addLayout(h1_box)
    v_box.addLayout(h2_box)
    v_box.addLayout(h3_box)
    v_box.addLayout(h4_box)
    v_box.addLayout(h6_box)
    v_box.addLayout(h7_box)
    v_box.addLayout(h8_box)

    v_box.addStretch()
    window.setLayout(v_box)
    sil.clicked.connect(silme)
    ekleme.clicked.connect(ekle)
    sonuc.clicked.connect(goster)
    window.show()
    sys.exit(app.exec())
def silme():
    if len(liste)>0 and len(liste1)>0:
        liste.clear()
        liste1.clear()
        label10.clear()
        alti.clear()
        yedi.clear()
    bes.setEnabled(True)
    alti.setEnabled(True)
    yedi.setEnabled(True)
    bes.clear()
def ekle():
    if int(bes.text())<=len(veri):
        label10.clear()
        if bes.text()!="":
            bes.setEnabled(False)
        if len(liste)!=int(bes.text()) and len(liste1)!=int(bes.text()):
            if alti.text()!="" and yedi.text()!="":
                liste.append(int(alti.text()))
                liste1.append(int(yedi.text()))
                genel.append(alti.text)
                genel.append(yedi.text)
                if len(liste)>=int(bes.text()):
                    label10.setText("Küme Merkezleri Girildi!")
                    alti.setEnabled(False)
                    yedi.setEnabled(False)
                else:
                    label10.setText("Eklendi")
                alti.clear()
                yedi.clear()

    else:
        label10.setText("Büyük Sayı Girdiniz.")


def goster():
    label10.clear()

    if birinci.text()!="" and birinci1.text()!="" and  ikinci1.text()!="" and ikinci.text()!="" and ücüncü.text()!="" and ücüncü1.text()!="" and dort.text()!="" and dort1.text()!="" and bes.text()!="" and len(liste)==int(bes.text()) and len(liste1)==int(bes.text()):
        try:
            veri[0].append(int(birinci.text()))
            veri[0].append(int(birinci1.text()))
            veri[1].append(int(ikinci.text()))
            veri[1].append(int(ikinci1.text()))
            veri[2].append(int(ücüncü.text()))
            veri[2].append(int(ücüncü1.text()))
            veri[3].append(int(dort.text()))
            veri[3].append(int(dort1.text()))

            for i in range(int(bes.text())):
                c.append(list())
                d.append(list())
                indextut.append(list())
                merkez1.append(list())
                yedek.append(list())
            for s in range(int(bes.text())):
                merkez.append(list())
                for m in range(2):
                    merkez1[s].append(0)
                    yedek[s].append(0)
            for s in range(len(veri)):
                veriler[0].append(veri[s][0])
                veriler[1].append(veri[s][1])

            for k in range(len(veri)):
                renk_index.append(1)
            """

            while len(rastgele_noktalar) != int(bes.text()):
                sayi = random.randint(0, len(veri) - 1)
                if sayi in rastgele_noktalar:
                    pass
                else:
                    rastgele_noktalar.append(sayi)

            for t in range(int(bes.text())):
                nokta = rastgele_noktalar[t]
                for g in range(2):
                    merkez[t].append(veri[nokta][g])"""

            for t in range(int(bes.text())):
                for g in range(2):
                    if g==0:
                        merkez[t].append(liste[t])
                    else:
                        merkez[t].append(liste1[t])


            while yedek != merkez:
                for i in range(len(veri)):
                    for k in range(len(merkez)):
                        kareal = 0
                        for j in range(len(merkez[k])):
                            kareal += pow((merkez[k][j] - veri[i][j]), 2)
                        if type(pow(kareal, 0.5)) is float:
                            c[k].append(round(pow(kareal, 0.5), 2))
                        else:
                            c[k].append(pow(kareal, 0.5))

                for m in range(len(veri)):
                    for r in range(len(c)):
                        sırala.append(c[r][m])
                    index1 = sırala.index(min(sırala))

                    for s in range(len(d)):
                        if s == index1:
                            d[s].append(1)
                        else:
                            d[s].append(0)
                    sırala.clear()

                for k in range(len(d)):
                    for m in range(len(d[k])):
                        if d[k][m] == 1:
                            indextut[k].append(m)

                for i in range(len(indextut)):
                    sutun1 = 0
                    sutun2 = 0
                    for s in indextut[i]:
                        sutun1 += veri[s][0]
                    merkez1[i][0] = round(sutun1 / len(indextut[i]), 2)

                    for m in indextut[i]:
                        sutun2 += veri[m][1]
                    merkez1[i][1] = round(sutun2 / len(indextut[i]), 2)

                for t in range(len(merkez)):
                    merkezler[0].append(merkez[t][0])
                    merkezler[1].append(merkez[t][1])
                plt.title("Merkezler:{}".format(merkez))
                plt.scatter(veriler[0], veriler[1], c=renk_index, s=75)
                plt.scatter(merkezler[0], merkezler[1], c="red", s=250, alpha=0.5, marker="*")
                plt.show()
                renk_index.clear()
                for n in range(len(d)):
                    sayi = d[n].count(1)
                    for m in range(sayi):
                        renk_index.append(n + 1)

                for k in range(len(indextut)):
                    indextut[k].clear()

                for s in range(len(d)):
                    d[s].clear()

                for t in range(len(c)):
                    c[t].clear()
                for s in range(len(merkezler)):
                    merkezler[s].clear()
                for s in range(len(merkez)):
                    for m in range(len(merkez[s])):
                        yedek[s][m] = merkez[s][m]

                for s in range(len(merkez1)):
                    for m in range(len(merkez1[s])):
                        merkez[s][m] = merkez1[s][m]
        except:
            print("hatalı")
        for s in range(int(bes.text())):
            del merkez[0]
            del c[0]
            del indextut[0]
            del merkez1[0]
            del yedek[0]
            del d[0]
        for l in range(len(veriler)):
            veriler[l].clear()
        for i in range(len(veri)):
            veri[i].clear()
        for f in range(len(merkezler)):
            merkezler[f].clear()
        rastgele_noktalar.clear()
        renk_index.clear()
    else:
        label10.setText("Boş Yer Bırakma!")
if __name__=="__main__":
    pencere()
