class öğrenci() :
    def __init__(self,ad = "bilgi yok",soy_ad = "bilgi yok",yaş = "bilgi yok",sınıf = "bilgi yok",diller = "bilgi yok"):
        self.ad = ad
        self.soy_ad = soy_ad
        self.yaş = yaş
        self.sınıf = sınıf
        self.diller = diller
    def sınıf_degistir(self,sınıf):
        self.sınıf = sınıf
        print("grup değiştirildi.")
    def bilgileri_göster(self):
        print("""
            öğrenci bilgileri :
        isim : {}
        soyisim : {}
        yaş : {}
        sınıf : {}
        diller : {}
        
        """.format(self.ad,self.soy_ad,self.yaş,self.sınıf,self.diller))
    def dil_ekleme(self,dil):
        self.diller.append(dil)
        print("dil eklendi")
