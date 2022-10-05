import random 
import json

# Kullanlacak karakterler
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-"

while True:
    # Kullanıcıdan eylem seçmesini istiyoruz
    eylem = input("------------------------\nŞifre oluşturmak için [1]\nŞifreleri görüntülemek için [2]\n------------------------\nSeçiminiz: ")
    
    if eylem != "1" and eylem != "2":
        print("Lütfen geçerli bir eylem seçin")
        continue

    if eylem == "1":
        # Hangi hesap için şifre oluştuğunu belirliyoruz
        account = input("Account: ")
     
        # Kullanıcıdan kaç karakterli şifre istediğini soruyoruz
        try :
            pass_len = int(input("Şifre uzunluğu: "))
        except ValueError:
            print("\n************\nLütfen geçerli bir sayı girin\n************")
            continue
        if pass_len < 1:
            print("\n************\nŞifre uzunluğu 1'den küçük olamaz!\n************")
            continue
        
        #kullanıcıya ne tür şifre istediğini soruyoruz
        pass_type = int(input("Şifreniz hangi karakterlerden oluşmalı?\n   1 : Sayılardan  | 2 : Harflerden | 3 : Sayı-Sembol-Harf | 4 : Sayı ve Harf |  "))
        if pass_type <=0 or pass_type > 4:
            print("\n************\nLütfen geçerli bir seçim yapınız!\n************")
            continue  
        
        password = []

        # password istediğmiz uzunlukta olana kadar rastgele karakterler seçiyoruz
        while len(password) < pass_len:
            if pass_type == 2 or pass_type == 3 or pass_type == 4:
                password.append(random.choice(lower+upper))
            if len(password) ==  pass_len:
                break
            if pass_type == 1 or pass_type == 3 or pass_type == 4:
                password.append(random.choice(numbers))
            if len(password) ==  pass_len:
                break
            if pass_type == 3:
                password.append(random.choice(symbols))
                
        # password listesini stringe çeviriyoruz
        password = "".join(password)
        print(f"-------------\nŞifreniz: {password} ve uzunluğu {len(password)} karakterdir.\n-------------")

        # json dosyasına okuma 
        with open("passwords.json", "r") as file:
            data = json.load(file)
        
        # json dosyasını güncelleme
        data["%s"%account] = "%s"%password
        
        # json dosyasına yazma
        with open("passwords.json", "w") as file:
            json.dump(data, file)
       
        
    if eylem == "2":
        #hangi hesabın şifresini görmek istediğini soruyoruz
        account = input("Hangi Hesabın Şifesini Öğrenmek İstiyorsun ? : ")
        # json dosyasını okuyoruz
        with open("passwords.json", "r") as file:
            data = json.load(file)
            if account in data:
                print(f"{account} için şifreniz: [ {data[account]} ]")
            else:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n! Böyle bir hesap bulunmuyor !\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
    
    # programı tekrar çalıştırmak isteyip istemediğimizi soruyoruz
    tekrar = input("\n??????????????????????????????????????\n? Tekrar çalıştırmak istiyor musunuz ?\n??????????????????????????????????????\n (E/H): ")
    if tekrar == "E" or tekrar == "e":
        continue
    else:
        break

