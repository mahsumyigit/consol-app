from time import sleep
giris_hakki=3
while giris_hakki > 0:
 giris_hakki -= 1

class Musteri:
    def __init__(self, isim: str, soyisim: str, parola: str, idno: str):
        self.__isim = isim
        self.__parola = parola
        self.__soyisim = soyisim
        self.__idno = idno

    def getIsim(self):
        return self.__isim

    def getsoyIsim(self):
        return self.__soyisim

    def getIdno(self):
        return self.__idno

    def getParola(self):
        return self.__parola


class Shopping:
    def __init__(self, isim: str):
        self.__isim = isim
        self.__musteriler = list()

    def musteriVarmi(self, idno: str, parola: str):
        for i in self.__musteriler:
            if i.getIdno() == idno and i.getParola() == parola:
                return i


        return False

    def musteriol(self, isim: str, soyisim: str, idno: str, parola: str):
        self.__musteriler.append(Musteri(isim, soyisim, idno, parola))

    def ElektronikEsya(self, musteri: Musteri):
        print("""
            1 - Telefon
                    samsung
                        1920 x 1080 HDR : 4529?
                        
                        1280 x 720 : 2999?
                    iphone
                        1920 x 1080 HDR : 4239?
                        
                        1280 x 720 : 2750?
                    htc
                        4K HDR WideScreen 16:9 : 8990?
                        1920 x 1080 HDR : 4009?
                        1280 x 720 : 2650?
                    huwei
                        4K HDR WideScreen 16:9 : 9129?
                        1920 x 1080 HDR : 4459?
                        1280 x 720 : 2690?
            2 - Ses ve müzik
                        jbl : 259?
                        hoparlör : 159?
                        sinema ses sistemi : 86?
            3 - TV ve Görüntü
                        Philips 
                            1920 x 1080 HDR : 3529?
                            1280 x 720 : 2899?
                        Sony
                            4K HDR WideScreen 16:9 : 9929?
                            1920 x 1080 HDR : 4529?
                            1280 x 720 : 2999?
                        LG
                            4K HDR WideScreen 16:9 : 11129?
                            1920 x 1080 HDR : 4459?
                            1280 x 720 : 2690?
            4 - Foto & Camera
                        Sony
                            HDR 16 MP DSLR : 4589?
                        CANON
                            DSLR 44MP EOS : 6000?
                        Nikon
                            Digital Camera : 2200?        
            5 - Bilgisayar bileşenleri
                        Playstation PRO : 3299?
                        Xbox One S : 2800?
            """)

    def Supermarket(self, musteri: Musteri):
        print("""
            1 - Abur & Cubur
                    alpella : 34?
                    doritos : 47?
            2 - Meyve & Sebze
                    Domates :1,5
                    Biber :2
                    Patlıcan : 2
            3 - Nohutgiller
                    Fasulye : 2,5
                    mercimek :5
                    Nohut : 4
            4 - Kişisel Bakım
                    Deodorant :52
                    Duş jeli : 12
                    sabun :51
            6 - Kırtasiye
                    defter : 6
                    kalem : 1
                    Uç : 0,5
                    ayrac : 4
        """)

    def BeyazEsya(self, musteri: Musteri):
        print("""
            1 - Çamaşır Makinesi
                    Arçelik : 5684
                    Beko : 5645
                    Siemens : 6845
            2 - Bulaşık Makinesi
                    Arçelik : 6564
                    Beko : 5685
                    Siemens :7868
            3 - Buzdolabı
                    Arçelik : 4564
                    Beko : 4534
                    Siemens :4535
            4 - Davlumbaz
                    Arçelik : 4568
                    Beko : 4334
                    Siemens :4538



        """)

    def Bilgisayarlar(self, musteri: Musteri):
        print("""
        Bilgisayar Kategorisi
            1 - Laptops
                    LG  
                        Ultro Book : 4879
                        Notebook :9989
                    Apple 
                        Macbook : 7998
                    Omen 
                        Gaming Book :8789


            2 - Masaüstü
                    LG : 5764
                    Dell : 5687
                    HP : 6575
                    Lenovo : 7564
                    Apple iMac :15675



        """)


def main():
    shopping = Shopping("yigit shopping")

    while True:
        print("""[1] Lütfen kayıt Olun [2] Kaydınız varsa lütfen giriş yapın [3] Sadece gezinmek istiyorum""")

        secim1 = input("Seçim : ")

        if secim1 == "1":
            isim = input("isim : ")
            soyisim = input("soyisim : ")
            idno = input("ID : ")
            parola = input("parola : ")
            shopping.musteriol(isim, soyisim, idno, parola)
            input("Ana menüye dönmek için enter'e basınız")

        elif secim1 == "3":

            secim2 = input(
                "[1]Bilgisayarlar\n[2]Beyaz Eşya\n[3]Supermarket\n[4]Elektronik Eşya\n[Q]Quit\n\nişleminiz : ")

            if secim2 == "1":
                shopping.Bilgisayarlar(Musteri)
                input("ana menüye dönmek için 'enter'e bas!")

            elif secim2 == "2":
                shopping.BeyazEsya(Musteri)
                input("ana menüye dönmek için 'enter'e bas!")

            elif secim2 == "3":
                shopping.Supermarket(Musteri)
                input("ana menüye dönmek için 'enter'e bas!")


            elif secim2 == "4":
                shopping.ElektronikEsya(Musteri)
                input("ana menüye dönmek için 'enter'e bas!")

            elif secim2 == "Q" or secim2 == "q":
                print("çıkışlanıyorsun...")


                sleep(1.5)
                break


        elif secim1 == "2":
            idno = input("ID : ")
            parola = input("Parola : ")
            if shopping.musteriVarmi(idno, parola):
                print("""[1]Bilgisayarlar \n[2]Beyaz Eşya \n [3]Supermarket\n [4]Elektronik Eşya\n [Q]Quit""")
            elif (idno==idno) and (parola!=parola):
                print("yanlış parola!! şifrenizi değiştirmek isterseniz (B) ye tıklayınız devam etmek istiyorsanız(E)ye tıklayınız")
                a=input("")
                if a == "E":
                    idno = input("kullanıcı adınızı giriniz:")
                    parola = input("parolanızı giriniz:")
                if a=="B":
                    yeni_parola=input("yeni şifreyi giriniz:")
                    yeni_parola=parola
                    print("yeni şifreniz oluşturulmuştur")
                    idno = input("kullanıcı adınızı giriniz:")
                    parola = input("parolanızı giriniz:")
                    if idno==idno and parola==parola:
                                        print("Hoşgeldiniz")

            else:
                (idno == idno) and (parola != parola)
                print("hatalı şifre")
                print(
                    "yanlış parola!! şifrenizi değiştirmek isterseniz (B) ye tıklayınız devam etmek istiyorsanız(E)ye tıklayınız")
                a = input("")
                if a == "E" or a=="e":
                    idno = input("kullanıcı adınızı giriniz:")
                    parola = input("parolanızı giriniz:")
                if a == "B" or a=="b":
                    yeni_parola = input("yeni şifreyi giriniz:")
                    yeni_parola = parola

                    print("yeni şifreniz oluşturulmuştur")
                    idno = input("kullanıcı adınızı giriniz:")
                    parola = input("parolanızı giriniz:")
                    if idno == idno and parola == parola:
                        print("Hoşgeldiniz")
                        print("""[1]Bilgisayarlar \n[2]Beyaz Eşya \n [3]Supermarket\n [4]Elektronik Eşya\n [Q]Quit""")
                        secim2 = input(
                        " işleminiz : ")

                    if secim2 == "1":
                        shopping.Bilgisayarlar(Musteri)
                        input("ana menüye dönmek için 'enter'e bas!")

                    elif secim2 == "2":
                        shopping.BeyazEsya(Musteri)
                        input("ana menüye dönmek için 'enter'e bas!")

                    elif secim2 == "3":
                        shopping.Supermarket(Musteri)
                        input("ana menüye dönmek için 'enter'e bas!")


                    elif secim2 == "4":
                        shopping.ElektronikEsya(Musteri)
                        input("ana menüye dönmek için 'enter'e bas!")

                    elif secim2 == "Q" or secim2 == "q":
                        print("çıkışlanıyorsun reis...")
                        sleep(1.5)
                        break







            secim2 = input(
                " işleminiz : ")

            if secim2 == "1":
                shopping.Bilgisayarlar(Musteri)
                input("ana menüye dönmek için 'enter'e bas!")

            elif secim2 == "2":
                 shopping.BeyazEsya(Musteri)
                 input("ana menüye dönmek için 'enter'e bas!")

            elif secim2 == "3":
                shopping.Supermarket(Musteri)
                input("ana menüye dönmek için 'enter'e bas!")


            elif secim2 == "4":
                shopping.ElektronikEsya(Musteri)
                input("ana menüye dönmek için 'enter'e bas!")

            elif secim2 == "Q" or secim2 == "q":
                print("çıkışlanıyorsun reis...")
                sleep(1.5)
                break


            else:
                print("hatalı giriş!")
            input("ana menüye dönmek için 'enter'e bas!")

        else:
            print("kayıt yok! hatalı parola girdiniz")

    else:
        print("hatalı giriş yaptınız!")
        if __name__ == "__main__":
            main()
main()