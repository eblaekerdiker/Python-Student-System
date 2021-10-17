while True:
    print("Toros Üniversitesi Mühendislik Fakültesi Öğrenci Bilgi Sistemi")
    fsection=['(1)Bölümleri Listele','(2)Öğrenci Ara','(3)Çıkış']
    print(fsection)
    choose=input("Seçiminiz:")
    if choose=='1':
        department=['(1)Yazılım Mühendisliği','(2)İnşaat Mühendisliği','(3)Endüstri Mühendisliği','(4)Elektrik Mühendisliği']
        print(department)
        depnumber=input("İşlem yapmak istediğiniz bölümün numarasını giriniz:")
        classes=input("İşlem yapmak istediğiniz sınıfı seçiniz:")
        if (depnumber=='1' and classes=='1'):
           listit=['(1)Öğrencileri Listele','(2)Dersleri Listele','(3)Not girişi','(4)Öğrenci Ekle/Sil','(5)Ders Ekle/Sil','(6)Ana Menü']
           print(listit)
           chooselist=input("Seçenek Giriniz:")
           if chooselist=='1':
               import sqlite3
               vt = sqlite3.connect('pythonproject.db')
               im = vt.cursor()
               im.execute("""SELECT * FROM students""")
               veriler = im.fetchall()
               print(veriler)
           if chooselist=='2':
               import sqlite3
               vt = sqlite3.connect('pythonproject.db')
               im = vt.cursor()
               im.execute("""SELECT * FROM classes""")
               classes = im.fetchall()
               print(classes)
           if chooselist=='3':
               number=input("Öğrenci no:")
               import sqlite3
               vt = sqlite3.connect('pythonproject.db')
               im = vt.cursor()
               im.execute("""SELECT * FROM classes""")
               classes = im.fetchall()
               print(classes)
               vt.close()
               ders=input("Hangi ders için not girmek istersiniz:")
               if ders=="CSE203":
                   choice=input("(1)Vize (2)Final:")
                   if choice=='1':
                       input("Vize notunu giriniz:")
                       print("Öğrencinin notu başarıyla girildi")
                   if choice=='2':
                       input("Final notunu giriniz:")
                       print("Öğrencinin notu başarıyla girildi")
           if chooselist=='4':
               kaydet=input("Öğrenci kaydetmek için kaydet, öğrencinin kaydını silmek için ise sil yazınız:")
               if kaydet=="kaydet":
                   import sqlite3
                   try:           
                       with sqlite3.connect("pythonproject.db", timeout=10) as conn:
                           name = input("Ad :")
                           lastname= input("Soyad :")
                           conn.execute("""INSERT INTO students1 (name,lastname) \ VALUES (?,?);""",(name,lastname,))
                           conn.close()
                   except sqlite3.IntegrityError :
                               print("error")
               if kaydet=="sil":
                import sqlite3
                vt = sqlite3.connect('pythonproject.db')
                im = vt.cursor()
                name = input("Ad :")
                lastname= input("Soyad :")
                im.execute('''DELETE FROM students WHERE name =?''')
                vt.close()
           if chooselist=='5':
               kaydet1=input("ders kaydetmek için kaydet, ders silmek için ise sil yazınız:")
               if kaydet=="kaydet":
                   import sqlite3
                   try:           
                       with sqlite3.connect("pythonproject.db", timeout=10) as conn:
                           classcode = input("Code :")
                           classname= input("Name :")
                           conn.execute("""INSERT INTO students1 (classcode,classname) \ VALUES (?,?);""",(classcode,classname,))
                           conn.close()
                   except sqlite3.IntegrityError :
                               print("error")
               if kaydet=="sil":
                import sqlite3
                vt=sqlite3.connect('pythonproject.db')
                im=vt.cursor()
                classcode=input("Ders Kodu:")
                sql='DELETE classes WHERE classcode=?' 
           if chooselist=='6':
                  listit=['(1)Öğrencileri Listele','(2)Dersleri Listele','(3)Not girişi','(4)Öğrenci Ekle/Sil','(5)Ders Ekle/Sil','(6)Ana Menü']
                  print(listit)
        if (depnumber=='1' and classes=='2'):
           listit=['(1)Öğrencileri Listele','(2)Dersleri Listele','(3)Not girişi','(4)Öğrenci Ekle/Sil','(5)Ders Ekle/Sil','(6)Ana Menü']
           print(listit)
           chooselist=input("Seçenek Giriniz:")
           if chooselist=='1':
               import sqlite3
               vt = sqlite3.connect('pythonproject.db')
               im = vt.cursor()
               im.execute("""SELECT * FROM students2""")
               veriler = im.fetchall()
               print(veriler)
           if chooselist=='2':
               import sqlite3
               vt = sqlite3.connect('pythonproject.db')
               im = vt.cursor()
               im.execute("""SELECT * FROM classes""")
               classes = im.fetchall()
               print(classes)
           if chooselist=='3':
               number=input("Öğrenci no:")
               import sqlite3
               vt = sqlite3.connect('pythonproject.db')
               im = vt.cursor()
               im.execute("""SELECT * FROM classes""")
               classes = im.fetchall()
               print(classes)
               vt.close()
               ders=input("Hangi ders için not girmek istersiniz:")
               if ders=="CSE203":
                   choice=input("(1)Vize (2)Final:")
                   if choice=='1':
                       input("Vize notunu giriniz:")
                       print("Öğrencinin notu başarıyla girildi")
                   if choice=='2':
                       input("Final notunu giriniz:")
                       print("Öğrencinin notu başarıyla girildi")
           if chooselist=='4':
               kaydet=input("Öğrenci kaydetmek için kaydet, öğrencinin kaydını silmek için ise sil yazınız:")
               if kaydet=="kaydet":
                   import sqlite3
                   try:           
                       with sqlite3.connect("pythonproject.db", timeout=10) as conn:
                           name = input("Ad :")
                           lastname= input("Soyad :")
                           conn.execute("""INSERT INTO students2 (name,lastname) \ VALUES (?,?);""",(name,lastname,))
                           conn.close()
                   except sqlite3.IntegrityError :
                               print("error")
               if kaydet=="sil":
                import sqlite3
                vt = sqlite3.connect('pythonproject.db')
                im = vt.cursor()
                name = input("Ad :")
                lastname= input("Soyad :")
                im.execute('''DELETE FROM students2 WHERE name =?''')
                vt.close()
           if chooselist=='5':
               kaydet1=input("ders kaydetmek için kaydet, ders silmek için ise sil yazınız:")
               if kaydet=="kaydet":
                   import sqlite3
                   try:           
                       with sqlite3.connect("pythonproject.db", timeout=10) as conn:
                           classcode = input("Code :")
                           classname= input("Name :")
                           conn.execute("""INSERT INTO students1 (classcode,classname) \ VALUES (?,?);""",(classcode,classname,))
                           conn.close()
                   except sqlite3.IntegrityError :
                               print("error")
               if kaydet=="sil":
                import sqlite3
                vt=sqlite3.connect('pythonproject.db')
                im=vt.cursor()
                classcode=input("Ders Kodu:")
                sql='DELETE classes WHERE classcode=?' 
           if chooselist=='6':
                 listit=['(1)Öğrencileri Listele','(2)Dersleri Listele','(3)Not girişi','(4)Öğrenci Ekle/Sil','(5)Ders Ekle/Sil','(6)Ana Menü']
                 print(listit)
        if (depnumber=='1' and classes=='3'):
           listit=['(1)Öğrencileri Listele','(2)Dersleri Listele','(3)Not girişi','(4)Öğrenci Ekle/Sil','(5)Ders Ekle/Sil','(6)Ana Menü']
           print(listit)
           chooselist=input("Seçenek Giriniz:")
           if chooselist=='1':
               import sqlite3
               vt = sqlite3.connect('pythonproject.db')
               im = vt.cursor()
               im.execute("""SELECT * FROM students3""")
               veriler = im.fetchall()
               print(veriler)
               vt.close()
           if chooselist=='2':
               import sqlite3
               vt = sqlite3.connect('pythonproject.db')
               im = vt.cursor()
               im.execute("""SELECT * FROM classes""")
               classes = im.fetchall()
               print(classes)
               vt.close()
           if chooselist=='3':
               number=input("Öğrenci no:")
               import sqlite3
               vt = sqlite3.connect('pythonproject.db')
               im = vt.cursor()
               im.execute("""SELECT * FROM classes""")
               classes = im.fetchall()
               print(classes)
               vt.close()
               ders=input("Hangi ders için not girmek istersiniz:")
               if ders=="CSE203":
                   choice=input("(1)Vize (2)Final:")
                   if choice=='1':
                       input("Vize notunu giriniz:")
                       print("Öğrencinin notu başarıyla girildi")
                   if choice=='2':
                       input("Final notunu giriniz:")
                       print("Öğrencinin notu başarıyla girildi")
           if chooselist=='4':
               kaydet=input("Öğrenci kaydetmek için kaydet, öğrencinin kaydını silmek için ise sil yazınız:")
               if kaydet=="kaydet":
                   import sqlite3
                   try:           
                       with sqlite3.connect("pythonproject.db", timeout=10) as conn:
                           name = input("Ad :")
                           lastname= input("Soyad :")
                           conn.execute("""INSERT INTO students3 (name,lastname) \ VALUES (?,?);""",(name,lastname,))
                           conn.close()
                   except sqlite3.IntegrityError :
                               print("error")
               if kaydet=="sil":
                import sqlite3
                vt = sqlite3.connect('pythonproject.db')
                im = vt.cursor()
                name = input("Ad :")
                lastname= input("Soyad :")
                im.execute('''DELETE FROM students3 WHERE name =?''')
                vt.close()
           if chooselist=='5':
               kaydet1=input("ders kaydetmek için kaydet, ders silmek için ise sil yazınız:")
               if kaydet=="kaydet":
                   import sqlite3
                   try:           
                       with sqlite3.connect("pythonproject.db", timeout=10) as conn:
                           classcode = input("Code :")
                           classname= input("Name :")
                           conn.execute("""INSERT INTO students3 (classcode,classname) \ VALUES (?,?);""",(classcode,classname,))
                           conn.close()
                   except sqlite3.IntegrityError :
                               print("error")
               if kaydet=="sil":
                 import sqlite3
                 vt=sqlite3.connect('pythonproject.db')
                 im=vt.cursor()
                 classcode=input("Ders Kodu:")
                 sql='DELETE classes WHERE classcode=?' 
           if chooselist=='6':
                 listit=['(1)Öğrencileri Listele','(2)Dersleri Listele','(3)Not girişi','(4)Öğrenci Ekle/Sil','(5)Ders Ekle/Sil','(6)Ana Menü']
                 print(listit)
        if (depnumber=='1' and classes=='4'):
           listit=['(1)Öğrencileri Listele','(2)Dersleri Listele','(3)Not girişi','(4)Öğrenci Ekle/Sil','(5)Ders Ekle/Sil','(6)Ana Menü']
           print(listit)
           chooselist=input("Seçenek Giriniz:")
           if chooselist=='1':
               import sqlite3
               vt = sqlite3.connect('pythonproject.db')
               im = vt.cursor()
               im.execute("""SELECT * FROM students4""")
               veriler = im.fetchall()
               print(veriler)
           if chooselist=='2':
               import sqlite3
               vt = sqlite3.connect('pythonproject.db')
               im = vt.cursor()
               im.execute("""SELECT * FROM classes""")
               classes = im.fetchall()
               print(classes)
           if chooselist=='3':
               number=input("Öğrenci no:")
               import sqlite3
               vt = sqlite3.connect('pythonproject.db')
               im = vt.cursor()
               im.execute("""SELECT * FROM classes""")
               classes = im.fetchall()
               print(classes)
               vt.close()
               ders=input("Hangi ders için not girmek istersiniz:")
               if ders=="CSE203":
                   choice=input("(1)Vize (2)Final:")
                   if choice=='1':
                       input("Vize notunu giriniz:")
                       print("Öğrencinin notu başarıyla girildi")
                   if choice=='2':
                       input("Final notunu giriniz:")
                       print("Öğrencinin notu başarıyla girildi")
           if chooselist=='4':
               kaydet=input("Öğrenci kaydetmek için kaydet, öğrencinin kaydını silmek için ise sil yazınız:")
               if kaydet=="kaydet":
                   import sqlite3
                   try:           
                       with sqlite3.connect("pythonproject.db", timeout=10) as conn:
                           name = input("Ad :")
                           lastname= input("Soyad :")
                           conn.execute("""INSERT INTO students4 (name,lastname) \ VALUES (?,?);""",(name,lastname,))
                           conn.close()
                   except sqlite3.IntegrityError :
                               print("error")
               if kaydet=="sil":
                import sqlite3
                vt = sqlite3.connect('pythonproject.db')
                im = vt.cursor()
                name = input("Ad :")
                lastname= input("Soyad :")
                im.execute('''DELETE FROM students4 WHERE name =?''')
                vt.close()
           if chooselist=='5':
               kaydet1=input("ders kaydetmek için kaydet, ders silmek için ise sil yazınız:")
               if kaydet=="kaydet":
                   import sqlite3
                   try:           
                       with sqlite3.connect("pythonproject.db", timeout=10) as conn:
                           classcode = input("Code :")
                           classname= input("Name :")
                           conn.execute("""INSERT INTO classes (classcode,classname) \ VALUES (?,?);""",(classcode,classname,))
                           conn.close()
                   except sqlite3.IntegrityError :
                               print("error")
               if kaydet=="sil":
                import sqlite3
                vt=sqlite3.connect('pythonproject.db')
                im=vt.cursor()
                classcode=input("Ders Kodu:")
                sql='DELETE classes WHERE classcode=?' 
           if chooselist=='6':
                 listit=['(1)Öğrencileri Listele','(2)Dersleri Listele','(3)Not girişi','(4)Öğrenci Ekle/Sil','(5)Ders Ekle/Sil','(6)Ana Menü']
                 print(listit)
    if choose=='2':
               import sqlite3
               vt = sqlite3.connect('pythonproject.db')
               im = vt.cursor()
               studentid=input("Öğrenci no:")
               im.execute("""SELECT id,name,lastname         
    FROM students
    INNER JOIN students2        
    ON id,name,lastname
    INNER JOIN students3        
    ON id,name,lastname
    INNER JOIN students4       
    ON id,name,lastname
    WHERE studentid='?';""")
               veriler = im.fetchall()
               print(veriler)
    if choose=='3':
        print("Çıkış yaptınız...")