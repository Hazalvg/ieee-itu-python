"""
    @author : Gorkem Aktas
    @date : 18.10.2021
    @brief : Bu dokuman icerisinde print fonksiyonu ile tanisacaksiniz.
    Ayrica kullanimina iliskin genis ornekler bulacaksiniz
"""

#==============================================================================
# ---------------------------print() FONKSIYONU--------------------------------
#==============================================================================
"""
    @function : print()
    @param : *objects , sep, end, file, flush
    @brief : Bu fonksiyon ekrana cikti vermenizi saglar
"""
#==============================================================================
# ---------------------------KULLANIM KILAVUZU---------------------------------
#==============================================================================
"""
    degisken = degisken_degeri
    print(degisken)
    log --> degisken_degeri
"""
#==============================================================================
# ---------------------------ACIKLAMA KISMI------------------------------------
#==============================================================================
"""
    Bu kod ile ekrana cikti verebiliyoruz. Yukaridaki ornegi incelersek bir
    degiskenimiz bulunmakta. Devaminda da bu degiskenimizi print icerisine
    yazarak ekrana cikti alabiliyoruz. Egitim boyunca log ifadesi terminal
    ciktisini belirtmek icin kullanilacaktir.
"""
#==============================================================================
# ---------------------------ORNEK KOD BLOGU-----------------------------------
#==============================================================================
"""
    Kodu calistirmak icin kodun asagisindaki ve yukarisindaki cift tirnaklari
    siliniz. Diger ornek kodlari calistirirken sikinti yasamamak icin de
    cift tirnaklari ornek kullanimdan sonra yerine koyunuz.
"""
#Ornek
"""
    name = "Gorkem"
    print(name)
    # log -> Gorkem
"""
#Ornek 2 direkt cikti verilmesi
"""
    print("Hello World")
    # log -> Hello World
"""
#Ornek 3 degisken ve direkt mesajin birlikte kullanilmasi
"""
    name = "Gorkem"
    print("Hosgeldin" + name)
    # log -> Hosgeldin Gorkem
    # @attention : Eger birlesik yazilmasini istemiyorsaniz "Hosgeldiniz"
    # ifadesini "Hosgeldiniz " seklinde icinde sonuna bosluk atarak kullanin
"""
#Ornek 4 formatlama
"""
    name = "Gorkem"
    surname = "Aktas"
    print(f"Hosgeldiniz {name} {surname}")
    # log -> Hosgeldiniz Gorkem Aktas
"""
#Ornek 5 baska bir formatlama ornegi
"""
    name = "Gorkem"
    surname = "Aktas"
    print("Hosgeldiniz {} {}".format(name,surname))
    # log -> Hosgeldiniz Gorkem Aktas
"""
#Ornek 6 ayrac kullanma -> sep parametresi
"""
    print("yumurta","civciv","tavuk",sep="->")
    # log -> yumurta->civciv->tavuk
"""
#Ornek 7 end parametresi
"""
    print("IEEE",end="")
    print(" ITU")
    # log -> IEEE ITU
"""
