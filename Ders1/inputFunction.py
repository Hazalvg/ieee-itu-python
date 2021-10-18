"""
    @author : Gorkem Aktas
    @date : 12.07.2021
    @brief : Bu dokuman icerisinde input fonksiyonu ile tanisacaksiniz.
    Ayrica kullanimina iliskin genis ornekler bulacaksiniz
"""

#==============================================================================
# ---------------------------input() FONKSIYONU--------------------------------
#==============================================================================
"""
    @function : input()
    @param : [prompt]
    @brief : Bu fonksiyon kullanici tarafindan girilen degeri okur.
"""
#==============================================================================
# ---------------------------KULLANIM KILAVUZU---------------------------------
#==============================================================================
"""
    degisken = input(kullaniciya_gorunecek_bilgi)
"""
#==============================================================================
# ---------------------------ACIKLAMA KISMI------------------------------------
#==============================================================================
"""
    Bu fonksiyon kullanici tarafindan girilen veriyi okur. Fakat sadece okur.
    Bir sonraki satira gectiginde veri kaybolur. Kaybolmamasi icin genellikle
    bir degisken icerisine aktarilir. Ayrica ekrana bir cikti vermez.
    Bu sebeple orneklerde cikti alabilmek icin print() kullanacagiz
"""
#==============================================================================
# ---------------------------ORNEK KOD BLOGU-----------------------------------
#==============================================================================
"""
    Kodu calistirmak icin kodun asagisindaki ve yukarisindaki cift tirnaklari
    siliniz. Diger ornek kodlari calistirirken sikinti yasamamak icin de
    cift tirnaklari ornek kullanimdan sonra yerine koyunuz.
"""
#Ornek 1 verinin alinip ekrana yazdirilmasi
"""
    name = input("Adinizi Giriniz -> ")
    print(f"Hosgeldin {name}")
    # log -> Adinizi Giriniz ->
    # Holgediniz {girdiginiz_isim}
"""
#Ornek 2 tip donusturuculer ile birlikte kullanilmasi
"""
    string = input("Bir seyler yazin -> ")
    number = int(input("Bir sayi giriniz -> "))
    print(type(string))
    print(type(number))
    # log -> <class 'str'>
             <class 'int'>
"""
