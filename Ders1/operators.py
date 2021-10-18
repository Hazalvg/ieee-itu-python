"""
    @author : Gorkem Aktas
    @date : 18.10.2021
    @brief : Bu dokuman icerisinde Python dilinde yer alan operatorler
    bahsedilecektir. Operatorlerin nasil kullanilabilecegini ogreneceksiniz
"""
#==============================================================================
# ----------------------OPERATORLER ve ACIKLAMALARI----------------------------
#==============================================================================
"""
################################################################################
___________________________ARITMETIK OPERATORLER_______________________________
################################################################################
    + -> Toplama Islemini Yapar
    - -> Cikarma Islemini Yapar
    * -> Carpma Islemini Yapar
    / -> Bolme Islemini Yapar
    % -> Mod Alma Islemini Yapar
    // -> Kalansiz Bolme Islemi Yapar
    ** -> Sayinin Ussunu Alir
    = -> Atama Operatoru Olarak Kullanilir
################################################################################
_____________________________LOJIK OPERATORLER__________________________________
################################################################################
    & -> AND Islemini Yapar
    | -> OR Islemini Yapar
    ^ -> XOR Islemini Yapar
    << -> Sola Kaydirma (Left Shifting) Islemini Yapar
    >> -> Saga Kaydirma (Right Shiftin) Islemini Yapar

    Bu operatorler binary formatinda islem yaparlar. Genellikle MicroPython gibi
    gomulu sistemler alaninda daha cok kullanilirlar.
"""
#Ornek Hesap Makinesi Yapimi
"""
number1 = int(input("Birinci Sayiyi Giriniz -> "))
number2 = int(input("Ikinci Sayiyi Giriniz -> "))
sum = number1 + number2
sub = number1 - number2
product = number1 * number2
div = number1 / number2
print(f"{number1} ve {number2}'nin ")
print(f"Toplami -> {sum}")
print(f"Farki -> {sub}")
print(f"Carpimi -> {product}")
print(f"Bolumu -> {div}")
"""
# Ornek 2 Optimize edilmis bir hesap Makinesi
"""
number1 = int(input("Birinci Sayiyi Giriniz -> "))
number2 = int(input("Ikinci Sayiyi Giriniz -> "))
print(f"{number1} ve {number2}'nin ")
print(f"Toplami -> " + str(number1+number2))
print(f"Farki -> " + str(number1-number2))
print(f"Carpimi -> " + str(number1*number2))
print(f"Bolumu -> " + str(number1/number2))
"""
