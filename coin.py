from hashlib import sha256
from pydoc import classname
import time
from turtle import st


class block:
    def __init__(self,zaman,veri,oncekiHash= " "):
        self.zaman = zaman
        self.veri =veri
        self. oncekiHash = oncekiHash
        self.deneme = 0
        self.hash = self.denemSsayisi()

    def denemSsayisi(self):
        while True:
            self.deneme = self.deneme +1
            sonuc = sha256((str(self.zaman)+str(self.veri)+str(self.oncekiHash)+str(self.deneme)).encode()).hexdigest()
            if sonuc[0:4]=="0000":
                break
        return sonuc

class blockChain: #blokzinciri
    def __init__(self):
        self.chain=[self.ilkblok()]
    
    def ilkblok(self):
        return block(time.ctime(),"boş")

    def ekle(self,veri):
        dugum = block(time.ctime(),veri,self.chain[-1].hash)
        self.chain.append(dugum)

    def kontrolEtme(self):
        for i in range(len(self.chain)):
            if i!=0:
                ilk =self.chain[i-1].hash
                suan =self.chain[i].oncekiHash
                if ilk != suan:
                    return "Zincir Oluşmamış"
                if sha256((str(self.chain[i].zaman)+str(self.chain[i].veri)+str(self.chain[i].oncekiHash)+str(self.chain[i].deneme)).encode()).hexdigest() !=self.chain[i].hash:
                    return "Zincir Oluşmamış"
        return "Zincir mevcut"

    def liste(self):
        print("Blokchain = \n")
        for i in range(len(self.chain)):
            print(str(i)+".nci Block","\n Hash = ",str(self.chain[i].hash),"\n Zaman= ",str(self.chain[i].zaman),"\n Veri = ",str(self.chain[i].veri),"\nDeneme sayısı = ",str(self.chain[i].deneme),"\n Önceki Hash = ",str(self.chain[i].oncekiHash))

Coin = blockChain()

while True:
    print("Şeçim yapınız \n 1-Blok Ekle\n 2-BlockChain'i gör\n 3-Zinciri Kontrol Et \n 4-Çıkış")
    data = int(input())
    if data == 1:
        print("Coin miktarı: ")
        miktar =int(input())
        Coin.ekle(miktar)
    elif data== 2:
        Coin.liste()
    elif data== 3:
        print(str(Coin.kontrolEtme()))
    elif data== 4:
        break
    elif data>4:
        print("Lütfen 1 ile 4 arasında sayı giriniz..")