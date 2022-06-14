# encoding:utf-8

while True:
    print("\n1- Hobi Setleri\t 2-Ahşap Ürünler\t3-Boya\t4-Polyester\t 5-Tuhafiye\t 6-Kalemler\t 7-Yardımcı Ürünler\t 8-Fırça\t 9-Tuval ve Şövale\t10-Standart Gönderi")

    sınıf=int(input("Hangi kategoride gönderi oluşurmak istiyorsunuz: "))

    ucuzahobi="www.ucuzahobi.com'da"
    link="Hemen sahip olmak için link profilde 👉🏻 @ucuzahobi 🐧"
    hashtag="#hobi #hobimalzemleri #sanat #boyama #sanatmalzemleri #sanatetkinligi #sanatatolyesi #sanatetkinlikleri " \
            "#hobidunyası #hobilerim #art #artcraft #artwork #hobby #hobbytime #craft #evdekal #karantina #pandemi"
    boyahashtag="#boya #boyama #multisurfaces #multisurface #multisurfacesboya #multisurfacepaint #boyamateknikleri #eskiyiyenile"
    if sınıf==1:
        while True:
            ad=input("Hobi Setinin adını giriniz: ")
            print("•{}\nSence yeni bir hobi edinmenin vakti gelmedi mi? {} ve daha onlarca hobi seti {} seni bekliyor.\n{}".format(ad.upper(),ad.upper(),ucuzahobi,link))
            print("\n\n\n\n",hashtag)
            islem=input("\nçıkmak için q ya basın: ")
            if islem=="q" or islem=="Q":
                break
    elif sınıf==2:
        while True:
            ad=input("Ekleyeceğiniz AHŞAP ürünün adını giriniz: ")
            print("\nKarantinada evde canın sıkılmasın diye ucuzahobi seninle!\n• AHŞAP {}\nAHŞAP {} ve daha onlarca ahşap obje çeşitleri {}\n"
                    "Dilediğin ahşap objeyi hemen al, boya ve evini renklendirmeye başla 🎨\n{}"
                    .format(ad.upper(),ad.upper(),ucuzahobi,link))
            print("\n\n\n\n #ahşap #ahşapboyama #ahsap #ahsapboyama #ahsaptasarım #boya #boyama #boyamateknikleri #akrilikboya #akrilikboyama #dekorasyon #dekoratifurunler"
              ,boyahashtag,hashtag)
            islem = input("\nçıkmak için q ya basın: ")
            if islem == "q" or islem == "Q":
                break


    elif sınıf==3:
        while True:
            print("\n1-Multisurface\t2-Akrilik\t3-Chalked\t4-Vernikli Boya\t5-Yağlı Boya\t6-Guaj Boya\t7-Kumaş Boya\t8-Taş Sulu Boyama")
            boyacesit=int(input("Hangi çeşit boyada gönderi oluşturmak istiyorsunuz: "))
            if boyacesit==1:
                while True:
                    marka=input("\nSadece firma adını giriniz: ")
                    print("\nKarantinada eşyalarını baştan aşağı yenilemeye ne dersin?\n• {} Multisurfaces Boyaları ile artık eski eşyalarını yenilemek çok kolay!\n"
                      "Aradığın Multisurfaces boya çeşitleri ve daha onlarca boya çeşiti {}\n"
                      "{}".format(marka.upper(),ucuzahobi,link))
                    print("\n\n\n\n #eskiyiyenileme #neydineoldu",hashtag,boyahashtag)
                    islem = input("\nçıkmak için q ya basın: ")
                    if islem == "q" or islem == "Q":
                        break

            elif boyacesit==2:
                while True:
                    marka = input("\nSadece firma adını giriniz: ")
                    print("\nSıkıldığın şu karantina günlerinde hayatını biraz renklendirmeye ne dersin?\n•{} Akrilik Boyaları ile hayatına renk kat 🎨\n"
                      "{} Akrilik Boya çeşitleri ve daha onlarca boya çeşiti {} sizlerle...\n"
                      "{}".format(marka.upper(),marka.upper(),ucuzahobi,link))
                    print("\n\n\n\n #akrilik #akrilikboyama #akrilikboya #ahşapboyama #tuvalboyama",hashtag,boyahashtag)
                    islem = input("\nçıkmak için q ya basın: ")
                    if islem == "q" or islem == "Q":
                        break
            elif boyacesit==3:
                print("\nEşyalarını yenilemek istiyorsun ama vaktin mi yok?\n"
                      "Ultra kapatıcı özelliğiyle RİCH CHALKED Boyaları ile eşyalarını yenilemek artık çok daha kolay.\n"
                      "RİCH CHALKED Boya çeşitleri ve daha onlarca boya çeşidi seninle buluşmak için {} bekliyor...\n"
                      "{}".format(ucuzahobi,link))
                print("\n\n\n\n", boyahashtag,"#chalked #chalkedpaint #rich #richmultisurface #richmultisurfaces #richchalked #neydineoldu",hashtag)

            elif boyacesit==4:
                print("\n•RİCH SELFY DECOR VERNİKLİ BOYA\nBoyadığın ürünlere vernik atmak ile uğraşmak istemiyor musun?\n"
                      "O zaman RİCH SELFY DECOR VERNİKLİ BOYA {} seni bekliyor.\n"
                      "{}".format(ucuzahobi,link))
                print("\n\n\n\n #vernikliboya #vernik #varnish #rich #rich #selfydecor #richartcraft #neydineoldu",boyahashtag,hashtag)
            elif(boyacesit==5):
                while True:
                    marka=input("\nMarka adını giriniz: ")
                    print("\n•{} Yağlı Boya\nHayalindeki çizimleri {} YAĞLI BOYALARI ile renklendirmeye var mısın?\n"
                      "{} Yağlı Boya ve daha onlarca boya çeşidi {} seninle buluşuyor.\n"
                      "{}".format(marka.upper(),marka.upper(),marka.upper(),ucuzahobi,link))
                    print("\n\n\n\n #yağlıboyatablo #yaglıboya #yağlıboyaresim #yaglıboya #yagliboyatablo #yagliboya #yağliboya "
                          "#yagliboyaresim #vangogh",boyahashtag,hashtag)
                    islem = input("\nçıkmak için q ya basın: ")
                    if islem == "q" or islem == "Q":
                        break
            elif(boyacesit==6):
                print("\n•TALENS GUAJ BOYA\nTALENS GUAJ BOYALARI ile hayatını renklendir.\nTALENS GUAJ BOYA ve daha onlarca boya çeşidi {}\n"
                      "{}".format(ucuzahobi,link))
                print("\n\n\n\n #guajboyama #ahşapboyama #tuvalboyama #guajboyaçalışması #guajboya #guage",boyahashtag,hashtag)


            elif boyacesit==7:
                print("\n1-Toz\t2-Fırça\t3-Sprey")
                çesit=int(input("\nHangi çeşit boya ile gönderi oluşturmak istiyorsunuz: "))
                if çesit==1:
                    print("\n•Viktoria Toz Kumaş Boyası\nVİKTORİA TOZ KUMAŞ BOYASI ile lekeli,solmuş,eski kıyafetlerini yeniden renklendirmeye ne dersin?\n"
                          "VİKTORİA TOZ KUMAŞ BOYASI ve daha onlarca boya çeşidi  {} seni bekliyor...\n"
                          "{}".format(ucuzahobi,link))
                    print("\n\n\n\n #kumas #kumaş #kumaşboyası #kumaşboyama #kumasboyasi"
                          "#tasarla #tasarım #tasarim #tozboya",boyahashtag,hashtag)
                elif çesit==2:
                    print("")
                elif çesit==3:
                    print("\n•RİCH FUNNY KİDS SPREY KUMAŞ BOYASI\nKıyafetlerine şekiller vererek renklendirmeye ne dersin?\n"
                          "RİCH FUNNY KİDS SPREY KUMAŞ BOYASI onlarca boya çeşitleri ile beraber {}\n"
                          "{}".format(ucuzahobi,link))
                    print("\n\n\n\n #kumas #kumaş #kumaşboyası #kumaşboyama #kumasboyasi #spreyboya #funnykids #tasarla #tasarım #tasarim #tozboya", boyahashtag, hashtag)
                else:
                    print("Böyle bir kategori bulunmamaktadır. ulaşmak istediğiniz kategoriyi tekrar giriniz: ")


            elif boyacesit==8:
                while True:
                    marka=input("\nMarka Adını giriniz: ")
                    print("\n Karantinada hayal gücünü serbest bırak!\n {} TAŞ SULU BOYAMA ile hayalini gerçeğe dönüştür.\n"
                      "{} TAŞ SULU BOYAMA ve daha onlarca hobi malzemesi {}\n{}".format(marka.upper(),marka.upper(),ucuzahobi,link))
                    islem = input("\nçıkmak için q ya basın: ")
                    if islem == "q" or islem == "Q":
                        break
            else:
                print("Böyle bir kategori bulunmamakta.")


    elif sınıf==4:
        print("\nEvine, ofisine yeni dekorlar eklemek ister misin?\nOnlarca POLYESTER çeşidi {} sizi bekliyor.\n"
              "{}".format(ucuzahobi,link))
        print("\n\n\n\n #seramik #seramikhamur #polyester #seramikatölyesi #seramikboyama #seramiksanatı 3polyesterboyama",hashtag)
    elif sınıf==5:
        while True:
            ad=input("\nÜrün adını giriniz:  ")
            print("\n•{}\n{} ve daha onlarca çeşit {}\n{}".format(ad.upper(),ad.upper(),ucuzahobi,link))
            print("\n\n\n\n #takı #takımalzemeleri #takıtasarım #takımodelleri #ip #halatip #tuhafiye",hashtag)
            islem = input("\nçıkmak için q ya basın: ")
            if islem == "q" or islem == "Q":
                break
    elif sınıf==6:
        while True:
            marka=input("\nKalem Markasını giriniz: ")
            tür=input("Kalemin türünü giriniz (örn:SULU BOYA KALEMİ): ")
            print("\nŞimdi hayalindeki resmi canlandırma vakti!\n{} {} ve daha onlarca çeşit {}\n{}".format(marka.upper(),tür.upper(),ucuzahobi,link))
            print("\n\n\n\n #kalem #karakalem #karakalemçizimi #karakalemportre #karakalemçizim #karakalemresim #karakalemçizimleri #kalemler #kalemlerim",hashtag)
            islem = input("\nçıkmak için q ya basın: ")
            if islem == "q" or islem == "Q":
                break
    elif sınıf ==7:
        while True:
            ad=input("\nÜrün adın giriniz: ")
            print("\n•{}\n"
              "{} ve daha onlarca hobi malzemesi {}\n{}".format(ad.upper(),ad.upper(),ucuzahobi,link))
            print("\n\n\n\n", hashtag)
            islem = input("\nçıkmak için q ya basın: ")
            if islem == "q" or islem == "Q":
                break
    elif sınıf == 8:
        print("\nKarantinada boya yapmak mı istiyorsun?\n@ucuzahobi onlarca FIRÇA çeşidi ve hobi malzemleriyle yanında.\nFırça çeşitleri {}\n{}"
                .format(ucuzahobi, link))
        print("\n\n\n\n #fırça #firca #fırçaseti #fırca #firça #fircaseti #fırçalar",hashtag)


    elif sınıf==9:
        while True:
            çeşit=int(input("\n1-Tuval\t 2-Şövale: "))
            if çeşit==1:
                print("\nCanın sıkıldıysa bir TUVAL kap ve çiz!\nOnlarca TUVAL çeşitleri ve hobi malzemeleri {}\n{}".format(ucuzahobi,link))
                print("\n\n\n\n #tuval #tuvalboyama #tuvaleğitimi #tuvalçalışması #vangogh #şövale #şovale"
                      "#fırça #firca #fırçaseti #fırca #firça #fircaseti #fırçalar"
                      "#yağlıboyatablo #yaglıboya #yağlıboyaresim #yaglıboya #yagliboyatablo #yagliboya #yağliboya #yagliboyaresim",hashtag)
            elif çeşit==2:
                print("\n•ŞÖVALE\nŞÖVALE ve onlarca hobi ürünü {}\n{}".format(ucuzahobi,link))
                print("\n\n\n\n #tuval #tuvalboyama #tuvaleğitimi #tuvalçalışması #vangogh #şövale #şovale"
                      "#fırça #firca #fırçaseti #fırca #firça #fircaseti #fırçalar"
                      "#yağlıboyatablo #yaglıboya #yağlıboyaresim #yaglıboya #yagliboyatablo #yagliboya #yağliboya #yagliboyaresim",
                      hashtag)
                islem = input("\nçıkmak için q ya basın: ")
                if islem == "q" or islem == "Q":
                    break
            else:
                print("Belirtilen ürün bulunamadı.")
                break



    elif sınıf==10:
        while True:
            ad = input("\nÜrün adın giriniz: ")
            print("•{}\n"
              "{} ve daha onlarca hobi malzemesi {}\n{}".format(ad.upper(), ad.upper(), ucuzahobi, link))
            print("\n\n\n\n ",hashtag)
            islem = input("\nçıkmak için q ya basın: ")
            if islem == "q" or islem == "Q":
                break
    else:
        print("Böyle bir kategori bulunamadı: ")

    islem = input("\nçıkmak için Q ya basın: ")
    if islem == "q" or islem == "Q":
        break