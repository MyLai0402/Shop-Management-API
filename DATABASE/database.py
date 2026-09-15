######################################### SQL KẾT NỐI DATABASE ##########################################################################

import sqlite3 # sử dụng sqlite3 để kết nối 
conn=sqlite3.connect("database.db") # tạo kết nối database
#conn.execute(""" CREATE TABLE hocsinh(id INTEGER,ten TEXT,tuoi INTEGER ,diem REAL)""") # thực hiện kết nối database và tạo bảng ,
                                                                                        #(""") : tạo một chuỗi nhiều dòng
#conn.execute(""" INSERT INTO hocsinh (id,ten,tuoi,diem) VALUES (2,'Bình',19,7)""")

conn.commit() # lưu thay đổi sau khi kết nối 

                #(7-10): check TABLE
#cursor =conn.cursor()   #cursor được hiểu công cụ làm việc giữa database và kq sql
#result =cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall() # trong datatabase cso nhưng table nào?, 
                                                                                        #fetchall: lấy tất cả kết quả 
#print(result) #KQ

                # (16-18) :CHECK INSERT
#cursor =conn.cursor()   #cursor được hiểu công cụ làm việc giữa database và kq sql
#result =cursor.execute("SELECT *fROM hocsinh").fetchall() 
#print(result) #KQ


                # SELECT TRONG PYTHON
#cursor =conn.cursor()   
#result =cursor.execute("SELECT ten,diem fROM hocsinh").fetchall() 
#print(result) 

                #SELECT WHERE
#cursor =conn.cursor()   
#result =cursor.execute("SELECT ten,diem fROM hocsinh WHERE diem >=7").fetchall() 
#print(result)

#cursor =conn.cursor()   
#result =cursor.execute("SELECT ten,diem fROM hocsinh WHERE tuoi >=18 and diem <8").fetchall() 
#print(result)


#cursor =conn.cursor()   
#result =cursor.execute("SELECT ten,diem fROM hocsinh WHERE tuoi=19 or diem =7").fetchall() 
#print(result)



                            #ORDER BY : SX DỮ LIỆU
                            #(ASC (ascending)): TĂNG DẦN => CÓ THỂ KHÔNG GHI VÌ SQL MẶC ĐỊNH TĂNG DẦN TỰA NHƯ SORT 
                            #(DESC(descending)):GIẢM DẦN
#cursor =conn.cursor()   
#result =cursor.execute("SELECT ten,diem fROM hocsinh ORDER BY diem DESC").fetchall() 
#print(result)


                            #ORDER BY + WHERE
#cursor =conn.cursor()   
#result =cursor.execute("SELECT ten,diem fROM hocsinh WHERE diem>=5 ORDER BY diem DESC").fetchall() 
#print(result)


                            #LIMIT: GIỚI HẠN  SỐ LƯỢNG "KQ MUỐN LẤY"
#cursor =conn.cursor()   
#result =cursor.execute("SELECT ten,diem fROM hocsinh ORDER BY diem DESC LIMIT 2").fetchall() 
#print(result)

                            #LIMIT +WHERE +ORDER by
#cursor =conn.cursor()   
#result =cursor.execute("SELECT ten,diem fROM hocsinh WHERE diem >=5 ORDER BY diem DESC LIMIT 2").fetchall() 
#print(result)


                            #OFFSET :BỎ QUA BAO NHIÊU DÒNG TRƯỚC KHI LẤY KQ 
                            # lưu ý nên dịch offset trước khi dùng limit 
#cursor =conn.cursor()   
#result =cursor.execute("SELECT ten,diem fROM hocsinh ORDER BY diem DESC LIMIT 2 OFFSET 1").fetchall() 
                        # lấy tên và điểm từ bảng hocsinh sx cao đến thấp, offset bỏ qua 1 ng đầu tiên và limit kq lấy 2 người tiếp theo 
                        # lưu ý nên dịch offset trước khi dùng limit 
#print(result)

                        #COUNT():ĐẾM SỐ DÒNG TRONG BẢNG 
#cursor =conn.cursor()
#result =cursor.execute("SELECT COUNT (*) FROM hocsinh").fetchall() 
#print(result)


                        #COUNT +WHERE
#cursor =conn.cursor()
#result =cursor.execute("SELECT COUNT (*) FROM hocsinh WHERE diem>=5").fetchall() 
#print(result)

                        #SUM : TỔNG 
#cursor =conn.cursor()
#result =cursor.execute("SELECT SUM (diem) FROM hocsinh ").fetchall() # tổng điểm trong bảng hocsinh
#print(result)


                        #AVG():TÍNH DTB ( dtb tính cho cả bảng )
#cursor =conn.cursor()
#result =cursor.execute("SELECT AVG (diem) FROM hocsinh ").fetchall() # tổng điểm trong bảng hocsinh
#print(result)


                        #MIN : THẤP NHẤT
#cursor =conn.cursor()
#result =cursor.execute("SELECT MIN (diem) FROM hocsinh ").fetchall() # tổng điểm trong bảng hocsinh
#print(result)

                        #MAX: CAO NHẤT
#cursor =conn.cursor()
#result =cursor.execute("SELECT MAX (diem) FROM hocsinh ").fetchall() # tổng điểm trong bảng hocsinh
#print(result)   

                        #UPDATE : SỮA DỮ LIỆU (UPDATE ....SET)
                        #SET : MỤC ĐÍCH ĐẶT GIÁ TRỊ MỚI CHO CỘT CẦN THAY ĐỔI SỬA 

#cursor =conn.cursor()
#result =cursor.execute("UPDATE hocsinh SET tuoi= 20 WHERE id=2  ").fetchall() 
#conn.commit()
#print(result) 


                        # kiểm tra xem có update thành công sửa hs tuoi=20 chưa?
#cursor =conn.cursor()
#result =cursor.execute("SELECT *FROM hocsinh WHERE id=2 ").fetchall() 
#print(result) 


                        #DELETE :XÓA DỮ LIỆU
#cursor = conn.cursor()
#result= cursor.execute("DELETE FROM hocsinh WHERE id=2").fetchall()
#conn.commit()
#print(result)
                        #KT DỮ LIỆU ĐÃ XÓA CHƯA?

#cursor = conn.cursor()
#result= cursor.execute("SELECT * FROM hocsinh").fetchall()

#print(result)


#############________________________GROUP BY __________________###################################
                            # INSERT ĐỂ CÓ DỮ LIỆU LÀM GROUP BY
#import sqlite3
#conn=sqlite3.connect("database.db")
#conn.execute(""" INSERT INTO hocsinh (id,ten,tuoi,diem) VALUES (1,'My',20,7),(2,'Như',20,4),(3,'Hải',23,9)""")
#conn.commit()
                            #KIỂM TRA LẠI DỮ LIỆU (142-144)
#cursor = conn.cursor()
#result= cursor.execute("SELECT * FROM hocsinh").fetchall()
#print(result)

                            #GROUP BY: GOM NHỮNG DÒNG CÓ CÙNG GIÁ TRỊ THÀNH TỪNG NHÓM 

#cursor = conn.cursor()
#result= cursor.execute("SELECT tuoi FROM hocsinh GROUP BY tuoi").fetchall() # gôm tuổi bằng nhau cùng 1 nhóm 
#print(result)


                            #GROUP BY + COUNT
#cursor = conn.cursor()
#result= cursor.execute("SELECT tuoi,COUNT (*) FROM hocsinh GROUP BY tuoi").fetchall() # "gom" và "đếm" tuổi bằng nhau cùng 1 nhóm 
#print(result)


                            #GROUP BY +AVG
#cursor = conn.cursor()
#result= cursor.execute("SELECT tuoi,AVG (diem) FROM hocsinh GROUP BY tuoi").fetchall() # "gom tuổi cùng nhóm " và "tính dtb của nhóm đó "
#print(result)

                            #GROUP BY +SUM

#cursor = conn.cursor()
#result= cursor.execute("SELECT tuoi,SUM(diem) FROM hocsinh GROUP BY tuoi").fetchall() # "gom tuổi cùng nhóm " và "tính tong diem của nhóm đó "
#print(result)

                            #GROUP BY + MIN
#cursor = conn.cursor()
#result= cursor.execute("SELECT tuoi,MIN(diem) FROM hocsinh GROUP BY tuoi").fetchall() # "gom tuổi cùng nhóm " và "tính diem NHỎ NHẤT  của nhóm đó "
#print(result)

                            #GROUP BY +MAX
#cursor = conn.cursor()
#result= cursor.execute("SELECT tuoi,MAX(diem) FROM hocsinh GROUP BY tuoi").fetchall() # "gom tuổi cùng nhóm " và "tính diem LỚN  NHẤT  của nhóm đó "
#print(result)


                            #GROUP BY +WHERE 
#cursor = conn.cursor()
#result= cursor.execute("SELECT tuoi,AVG (diem) FROM hocsinh WHERE diem >= 5 GROUP BY tuoi").fetchall() 
                    # LỌC điều kiện => gom nhóm => Tính dtb nhóm đó 
#print(result)

                            #GROUP BY + COUNT + WHERE

#cursor = conn.cursor()
#result= cursor.execute("SELECT tuoi,COUNT (*) FROM hocsinh WHERE diem >= 5 GROUP BY tuoi").fetchall() 
                    
#print(result)


                            #HAVING : LỌC THEO NHÓM CÓ TỪ 2 GIÁ TRỊ GIỐNG NHAU TRỞ LÊN 
#cursor = conn.cursor()
#result= cursor.execute("SELECT tuoi,COUNT (*) FROM hocsinh WHERE diem >= 5 GROUP BY tuoi HAVING COUNT(*) >=2 ").fetchall() 
                    # LỌC DK WHERE TRC => NHÓM THEO GROUP TUÔI => ĐẾM => HAVING NẾU THỎA DK THÌ LẤY 
#print(result)

                            #HAVING + GROUP + COUNT
#cursor = conn.cursor()
#result= cursor.execute("SELECT tuoi,COUNT (*) FROM hocsinh GROUP BY tuoi HAVING COUNT(*) >=2 ").fetchall()  
#print(result)

                            #HAVING +AVG
#cursor = conn.cursor()
#result= cursor.execute("SELECT tuoi,AVG (diem) FROM hocsinh GROUP BY tuoi HAVING AVG(diem) >=7 ").fetchall()  
#print(result)

#############_______PRIMARY KEY (MÃ DUY NHẤT CỦA MỖI DÒNG)_______________#####################################################################
                # ID : K ĐƯỢC TRÙNG "UNIQUE"
                # NULL : nếu dữ liệu = NULL thì SQL sẽ tự cấp cho id mới
#import sqlite3
#conn= sqlite3.connect("database.db")
#conn.execute("""CREATE TABLE sinhvien (id INTEGER PRIMARY KEY, ten TEXT ,tuoi INTEGER, diem REAL)""")
#conn.commit()

#import sqlite3
#conn= sqlite3.connect("database.db")
#conn.execute("""INSERT INTO sinhvien ( id,ten,tuoi,diem)VALUES (1,'LÂM',23,6),(2,'My',30,9),(NULL,'HOA',22,9)""")
#conn.commit()

#import sqlite3
#conn= sqlite3.connect("database.db")
#conn.execute("""INSERT INTO sinhvien ( id,ten,tuoi,diem)VALUES (NULL,'HOA',22,9)""")


#cursor = conn.cursor()
#result= cursor.execute("SELECT * FROM sinhvien ").fetchall()  
#print(result)

   ###########_________FOREIGN KEY(LIÊN KẾT 2 BẢNG)________###################################################################################
            #CHỨA BẢNG CHA (PRIMARY KEY) VÀ BẢNG CON (FOREIGN KEY)

#conn.execute("""CREATE TABLE lop ( id INTEGER PRIMARY KEY,ten_lop TEXT)""")
#conn.execute("DROP TABLE IF EXISTS hocsinh") # DROP TABLE :xóa all DỮ LIỆU và CẤU TRÚC BẢNG nếu có , IF EXISTS :nếu không tồn tại thì bỏ qua
            # DROP ... EXITST : CHỈ DÙNG KHI MUỐN TẠO LẠI BẢNG TỪ ĐẦU VÀ ĐỨNG TRƯỚC CREATE TABLE
            # KHÁC VỚI DELETE FROM CHỈ XÓA DỮ LIỆU , CẤU TRÚC BẢNG VẨN CÒN
#conn.execute("""CREATE TABLE hocsinh (id INTEGER PRIMARY KEY, ten TEXT, lop_id INTEGER,FOREIGN KEY (lop_id) REFERENCES lop(id))""")
                                                                        # hocsinh.lop_id (foreign key)kết nối với bảng cha primary lop(id)


#conn.execute("""INSERT INTO lop (id,ten_lop ) VALUES( 1, 'Python'),(2,'FastAPI')""")
#conn.commit()

#cursor = conn.cursor()
#result= cursor.execute("SELECT * FROM lop ").fetchall()  
#print(result)

#conn.execute("""INSERT INTO hocsinh (id,ten,lop_id ) VALUES( 1, 'An',1),(2,'Bình',2),(3,'Lan',1)""")
#conn.commit()


#cursor = conn.cursor()
#result= cursor.execute("SELECT * FROM hocsinh").fetchall()  
#print(result)


                      #  FOREIGN KEY 1:1
#conn.execute (""" CREATE TABLE nguoi(id INTEGER PRIMARY KEY, ten TEXT)""")
#conn.execute("""CREATE TABLE can_cuoc(id INTEGER PRIMARY KEY, nguoi_id INTEGER UNIQUE, so_cccd TEXT,FOREIGN KEY (nguoi_id) REFERENCES nguoi(id))""")


#conn.execute("""INSERT INTO nguoi (id,ten)VALUES (1, 'An'),(2,'Bình')""")
#conn.commit()

#conn.execute("""INSERT INTO can_cuoc (id,nguoi_id,so_cccd)VALUES (1, 1,'456789'),(2,2,'8765432')""")
#conn.commit()

#cursor = conn.cursor()
#result= cursor.execute("SELECT *FROM can_cuoc").fetchall()
#print(result)

#print("DA CHAY FILE")

                    #FOREIGN KEY 1:N
#conn.execute("DROP TABLE IF EXISTS lop1")
#conn.execute("DROP TABLE IF EXISTS hocsinh1")
#conn.execute("""CREATE TABLE lop1(id INTEGER PRIMARY KEY,ten_lop TEXT)""")
#conn.execute("""CREATE TABLE hocsinh1(id INTEGER PRIMARY KEY,ten TEXT, lop_id INTEGER, FOREIGN KEY (lop_id) REFERENCES lop1(id))""")

#conn.execute("""INSERT INTO lop1(id,ten_lop)VALUES(1,'Python'),(2,'FastAPI')""")
#conn.commit()

#conn.execute("""INSERT INTO hocsinh1(id,ten,lop_id)VALUES (1,'An',1),(2,'Bình',1),(3,'Ngọc',1),(4,'Nghĩa',2)""")
#conn.commit()

#cursor=conn.cursor()
#result=cursor.execute("SELECT*FROM hocsinh1").fetchall()
#print(result)


                    #FOREIGN KEY N:N

#conn.execute ("DROP TABLE IF EXISTS sinhvien1")
#conn.execute ("DROP TABLE IF EXISTS monhoc1")
#conn.execute ("DROP TABLE IF EXISTS sinhvien1_monhoc1")

#conn.execute("""CREATE TABLE sinhvien1(id INTEGER PRIMARY KEY,ten TEXT)""")
#conn.execute("""CREATE TABLE monhoc1(id INTEGER PRIMARY KEY,ten_mon TEXT)""")
#conn.execute("""CREATE TABLE sinhvien1_monhoc1(sinhvien1_id INTEGER,monhoc1_id INTEGER,FOREIGN KEY (sinhvien1_id)REFERENCES sinhvien(id),FOREIGN KEY(monhoc1_id)REFERENCES monhoc1(id))""")


#conn.execute("""INSERT INTO sinhvien1(id,ten)VALUES(1,'An'),(2,'Yến'),(3,'Ngọc')""")
#conn.execute("""INSERT INTO monhoc1(id,ten_mon) VALUES (1,'Python'),(2,'FastAPI')""")
#conn.commit()

#conn.execute("""INSERT INTO sinhvien1_monhoc1(sinhvien1_id,monhoc1_id) VALUES (1,1),(1,2),(2,1),(2,2),(3,1),(3,2)""")
#conn.commit()

#cursor = conn.cursor()
#result= cursor.execute("SELECT *FROM sinhvien1_monhoc1").fetchall()
#print(result)

                    #JOIN:NỐI (NHIỆM VỤ:  LẤY RA)

#cursor= conn.cursor()
#result= cursor.execute("""SELECT sinhvien1.ten,monhoc1.ten_mon 
                        #FROM sinhvien1_monhoc1 
                        #JOIN sinhvien1 
                        #ON sinhvien1.id=sinhvien1_monhoc1.sinhvien1_id
                        #JOIN monhoc1
                        #ON monhoc1.id =sinhvien1_monhoc1.monhoc1_id""" ).fetchall()
#print(result)


#cursor = conn.cursor()
#result=cursor.execute("""SELECT monhoc1.ten_mon,sinhvien1.ten
                        #FROM sinhvien1_monhoc1
                        #JOIN monhoc1
                        #ON monhoc1.id = sinhvien1_monhoc1.monhoc1_id
                        #JOIN sinhvien1
                        #ON sinhvien1.id =sinhvien1_monhoc1.sinhvien1_id""").fetchall()
#print(result)

                        #JOIN_WHERE : Nối_dk 
#cursor= conn.cursor()
#result= cursor.execute("""SELECT sinhvien1.ten,monhoc1.ten_mon 
                        #FROM sinhvien1_monhoc1 
                        #JOIN sinhvien1 
                        #ON sinhvien1.id=sinhvien1_monhoc1.sinhvien1_id     
                        #JOIN monhoc1
                        #ON monhoc1.id =sinhvien1_monhoc1.monhoc1_id
                        #WHERE monhoc1.id = 1 """).fetchall()
#print(result)



#cursor= conn.cursor()
#result= cursor.execute("""SELECT sinhvien1.ten,monhoc1.ten_mon 
                        #FROM sinhvien1_monhoc1 
                        #JOIN sinhvien1 
                        #ON sinhvien1.id=sinhvien1_monhoc1.sinhvien1_id     
                        #JOIN monhoc1
                        #ON monhoc1.id =sinhvien1_monhoc1.monhoc1_id
                        #WHERE sinhvien1.ten = 'An' OR sinhvien1.ten='Ngọc'
                        #ORDER BY monhoc1.ten_mon ASC """).fetchall()
#print(result) # kq môn Fastapi đứng trước vì sx theo bảng chữ cái  "ALPHABET"


                        #JOIN + WHERE + ORDER BY +LIMIT

#cursor= conn.cursor()
#result= cursor.execute("""SELECT sinhvien1.ten,monhoc1.ten_mon 
                        #FROM sinhvien1_monhoc1 
                        #JOIN sinhvien1 
                        #ON sinhvien1.id=sinhvien1_monhoc1.sinhvien1_id     
                        #JOIN monhoc1
                        #ON monhoc1.id =sinhvien1_monhoc1.monhoc1_id
                        #WHERE sinhvien1.ten = 'An' OR sinhvien1.ten='Ngọc'
                        #ORDER BY monhoc1.ten_mon ASC
                        # 2 """).fetchall()
#print(result) 

                       #JOIN + WHERE + ORDER BY +LIMIT +OFFSET
#cursor= conn.cursor()
#result= cursor.execute("""SELECT sinhvien1.ten,monhoc1.ten_mon 
                        #FROM sinhvien1_monhoc1 
                        #JOIN sinhvien1 
                        #ON sinhvien1.id=sinhvien1_monhoc1.sinhvien1_id     
                        #JOIN monhoc1
                        #ON monhoc1.id =sinhvien1_monhoc1.monhoc1_id
                        #WHERE sinhvien1.ten = 'An' OR sinhvien1.ten='Ngọc'
                        #ORDER BY monhoc1.ten_mon ASC
                        #LIMIT 2 
                        #OFFSET 1""").fetchall()
#print(result) 


#cursor= conn.cursor()
#result= cursor.execute("""SELECT sinhvien1.ten,monhoc1.ten_mon 
                        #FROM sinhvien1_monhoc1 
                        #JOIN sinhvien1 
                        #ON sinhvien1.id=sinhvien1_monhoc1.sinhvien1_id     
                        #JOIN monhoc1
                        #ON monhoc1.id =sinhvien1_monhoc1.monhoc1_id
                        #WHERE (sinhvien1.ten ='An' OR sinhvien1.ten='Ngọc') AND monhoc1.ten_mon ='FastAPI'""").fetchall()
                        # QUY TẮC:
                           # +chỉ lấy môn FASTAPI cho AN VÀ NGỌC 
                           # +NẾU CHỈ MUỐN LẤY 1 MÔN CHO 2 NGƯỜI THÌ QUY TẮC NGOẶC LẠI () ĐỂ SQL HIỂU LÀ 2 NGƯỜI CHỈ LẤY 1 MÔN
                           # +NẾU KHÔNG CÓ DẤU NGOẶC THÌ SQL HIỂU LÀ " AN VÀ (NGỌC +FASTAPI), lúc này An k bắt buột chỉ lấy mon FASTAPI
                        
#print(result) 

                        #LEFT JOIN :GIỮ TOÀN BỘ BẢNG BÊN TRÁI 
                        #Nếu bên phải có giá trị thì lấy , nếu không bằng "NULL"
                           

#cursor = conn.cursor()
#result = cursor.execute(""" SELECT sinhvien1.ten,monhoc1.ten_mon
                        #FROM sinhvien1
                        #LEFT JOIN sinhvien1_monhoc1
                        #ON sinhvien1.id =sinhvien1_monhoc1.sinhvien1_id
                        #LEFT JOIN monhoc1
                        #ON monhoc1.id=sinhvien1_monhoc1.monhoc1_id
                      # """ ).fetchall()
#print(result)


#cursor.execute("""INSERT INTO sinhvien1 (id, ten)VALUES (4,'Bình')""")
#conn.commit()

                        #INNER JOIN: CHỈ LẤY VÀ GIỮ NHỮNG DỮ LIỆU KHỚP 2 BÊN 
                        # NẾU BÊN TRÁI CÓ DỮ LIỆU NHƯNG BÊN PHẢI KHÔNG VÀ NGƯỢC LẠI THÌ INNER JOIN LOẠI DỮ LIỆU ĐÓ

#cursor = conn.cursor()
#result = cursor.execute(""" SELECT sinhvien1.ten,monhoc1.ten_mon
                        #FROM sinhvien1
                        #JOIN sinhvien1_monhoc1
                        #ON sinhvien1.id =sinhvien1_monhoc1.sinhvien1_id
                        #LEFT JOIN monhoc1
                        #ON monhoc1.id=sinhvien1_monhoc1.monhoc1_id
                       #""" ).fetchall()
#print(result)

                        #LEFT JOIN +WHERE : giữ bảng bên trái mặc dù bên phải = null 
                        # khi gặp WHRER nếu bên phải k có dữ liệu hoặc ngoặc lại đều bị loại 

#cursor = conn.cursor()
#result = cursor.execute(""" SELECT sinhvien1.ten,monhoc1.ten_mon
                        #FROM sinhvien1
                        #LEFT JOIN sinhvien1_monhoc1
                        #ON sinhvien1.id =sinhvien1_monhoc1.sinhvien1_id
                        #LEFT JOIN monhoc1
                        #ON monhoc1.id=sinhvien1_monhoc1.monhoc1_id
                        #WHERE monhoc1.ten_mon='Python'
                       #""" ).fetchall()
#print(result)

                     #LEFT JOIN + IS NULL: TÌM bên trái không có dữ liệu khớp bên phải 
                     # kết quả : print(" lấy dữ liệu không có")

                     #RIGHT JOIN + IS NULL: Tìm bên phải k có khớp bên trái => ĐẢO BẢNG => dùng LEFT JOIN +IS NULL

#cursor = conn.cursor()
#result = cursor.execute(""" SELECT sinhvien1.ten,monhoc1.ten_mon
                        #FROM sinhvien1
                        #LEFT JOIN sinhvien1_monhoc1
                        #ON sinhvien1.id =sinhvien1_monhoc1.sinhvien1_id
                        #LEFT JOIN monhoc1
                        #ON monhoc1.id=sinhvien1_monhoc1.monhoc1_id
                        #WHERE monhoc1.id IS NULL
                       #""" ).fetchall()
#print(result)



                        #RIGHT JOIN + IS NULL: giữ bảng bên phải dù bên trái không có dữ liệu khớp 
                        #  Tìm bên phải k có khớp bên trái => ĐẢO BẢNG => dùng LEFT JOIN +IS NULL


#cursor = conn.cursor()
#result = cursor.execute(""" SELECT sinhvien1.ten
                        #FROM sinhvien1
                        #RIGHT JOIN sinhvien1_monhoc1
                        #ON sinhvien1.id =sinhvien1_monhoc1.sinhvien1_id
                       #""" ).fetchall()
#print(result)


#cursor.execute(""" INSERT INTO monhoc1(id,ten_mon)VALUES (5,'SQL'),(6,'AI Automation')""")
#conn.commit()

                     #LEFT JOIN +WHERE 

#cursor = conn.cursor()
#result = cursor.execute(""" SELECT monhoc1.id,monhoc1.ten_mon           #lấy id và monhoc
                        #FROM monhoc1                                    #từ bảng môn học
                        #LEFT JOIN sinhvien1_monhoc1                     # nối bảng trung gian, giữ toàn bộ bảng bên trái 
                        #ON monhoc1.id =sinhvien1_monhoc1.monhoc1_id     # dk: nối monhoc.id và bảng trung gian sao cho khớp với nhau
                        #WHERE sinhvien1_monhoc1.monhoc1_id IS NULL   #lấy môn không có dữ liệu khớp 
                      # """ ).fetchall()
#print(result)


#result=cursor.execute("SELECT *FROM monhoc1 ").fetchall()
#print(result)


#result=cursor.execute(""" SELECT * FROM sinhvien1_monhoc1""").fetchall()
#print(result)

#result=cursor.execute("""INSERT INTO sinhvien1_monhoc1(sinhvien1_id,monhoc1_id)VALUES (5,5)""")
#conn.commit()




#cursor = conn.cursor()
#result = cursor.execute(""" SELECT sinhvien1.ten,monhoc1.ten_mon           
                        #FROM sinhvien1                                           
                        #LEFT JOIN sinhvien1_monhoc1                     
                        #ON sinhvien1.id =sinhvien1_monhoc1.sinhvien1_id  #CỘT ID = GIÁ TRỊ BÊN TRONG ID CỦA BẢNG 'SV1' NỐI VỚI BẢNG TRUNG GIAN
                        #LEFT JOIN monhoc1
                        #ON monhoc1.id = sinhvien1_monhoc1.monhoc1_id                        
                        #WHERE monhoc1.ten_mon='SQL'    
                       #""" ).fetchall()
#print(result)
# LƯU Ý: CÙNG ID K TẠO NÊN MQH , BẢNG TRUNG GIAN QUYẾT ĐỊNH MQH GHÉP NỐI KHỚP NHAU
# NẾU DK TRONG WHERE VÀ ON CHƯA ĐỦ ĐỂ NỐI NHAU THÌ INSERT THÊM ID 

                        #LEFT JOIN +WHERE : LỌC DK CẦN , CÒN NHỮNG GÌ K CÓ GIÁ TRỊ BỊ LOẠI GIỐNG 'INNER JOIN'

#cursor = conn.cursor()
#result = cursor.execute(""" SELECT sinhvien1.ten,monhoc1.ten_mon           
                        #FROM sinhvien1                                           
                        #LEFT JOIN sinhvien1_monhoc1                     
                        #ON sinhvien1.id =sinhvien1_monhoc1.sinhvien1_id  
                        #LEFT JOIN monhoc1
                        #ON monhoc1.id = sinhvien1_monhoc1.monhoc1_id                        
                        #WHERE  monhoc1.ten_mon='SQL'   
                       #""" ).fetchall()
#print(result)

                        # LEFT JOIN + AND : GIỮ NGUYÊN BÊN TRÁI MẶC DÙ K CÓ DỮ LIỆU BÊN KIA , VÀ K CÓ DỮ LIỆU = 'NONE'

#cursor = conn.cursor()
#result = cursor.execute(""" SELECT sinhvien1.ten,monhoc1.ten_mon           
                        #FROM sinhvien1                                           
                        #LEFT JOIN sinhvien1_monhoc1                     
                        #ON sinhvien1.id =sinhvien1_monhoc1.sinhvien1_id 
                        #LEFT JOIN monhoc1
                        #ON monhoc1.id = sinhvien1_monhoc1.monhoc1_id 
                        #AND monhoc1.ten_mon = 'SQL'                
                          
                       #""" ).fetchall()
#print(result)



#cursor = conn.cursor()
#result = cursor.execute(""" SELECT sinhvien1.ten,monhoc1.ten_mon           
                        #FROM sinhvien1                                           
                        #LEFT JOIN sinhvien1_monhoc1                     
                       # ON sinhvien1.id =sinhvien1_monhoc1.sinhvien1_id 
                       # LEFT JOIN monhoc1
                        #ON monhoc1.id = sinhvien1_monhoc1.monhoc1_id 
                        #AND monhoc1.ten_mon = 'SQL'
                        #WHERE sinhvien1.ten ='Như' OR sinhvien1.ten='An'                
                          
                      # """ ).fetchall()
#print(result)



#cursor = conn.cursor()
#result = cursor.execute(""" SELECT sinhvien1.ten,monhoc1.ten_mon           
                       # FROM sinhvien1                                           
                        #LEFT JOIN sinhvien1_monhoc1                     
                       # ON sinhvien1.id =sinhvien1_monhoc1.sinhvien1_id 
                        #LEFT JOIN monhoc1
                       # ON monhoc1.id = sinhvien1_monhoc1.monhoc1_id 
                       # WHERE (monhoc1.ten_mon = 'Python' OR monhoc1.ten_mon = 'SQL')
                          
                      # """ ).fetchall()
#print(result)

                        #INNER JOIN: chỉ trả kq khi 2 bảng có đủ DỮ LIỆU nối nhau , k đủ dữ liệu bị loại giống WHERE
#cursor = conn.cursor()
#result = cursor.execute(""" SELECT sinhvien1.ten,monhoc1.ten_mon           
                        #FROM sinhvien1                                           
                        #INNER JOIN sinhvien1_monhoc1                     
                        #ON sinhvien1.id =sinhvien1_monhoc1.sinhvien1_id 
                        #INNER JOIN monhoc1
                        #ON monhoc1.id = sinhvien1_monhoc1.monhoc1_id 
                        #WHERE monhoc1.ten_mon='SQL'
                        
                          
                     #  """ ).fetchall()
#print(result)



#cursor = conn.cursor()
#result = cursor.execute(""" SELECT sinhvien1.ten,monhoc1.ten_mon           
                        #FROM sinhvien1                                           
                        #INNER JOIN sinhvien1_monhoc1                     
                        #ON sinhvien1.id =sinhvien1_monhoc1.sinhvien1_id 
                        #INNER JOIN monhoc1
                        #ON monhoc1.id = sinhvien1_monhoc1.monhoc1_id                             
                      # """ ).fetchall()
#print(result)


                     #JOIN NÂNG CAO 1
#cursor=conn.cursor()
#result=cursor.execute("""SELECT sinhvien1.ten,COUNT(*)
                        #FROM sinhvien1
                        #INNER JOIN sinhvien1_monhoc1
                        #ON sinhvien1.id = sinhvien1_monhoc1.sinhvien1_id
                        #INNER JOIN monhoc1
                        #ON monhoc1.id = sinhvien1_monhoc1.monhoc1_id
                        #GROUP BY sinhvien1.ten
                        #HAVING COUNT(*)>=2""").fetchall()
#print(result)


                     #JOIN NÂNG CAO 2:
                     # <>: khác / không bằng , loại
#cursor= conn.cursor()
#result= cursor.execute("""SELECT sinhvien1.ten , COUNT(*)
                       #FROM sinhvien1
                       # INNER JOIN sinhvien1_monhoc1
                         #ON sinhvien1.id=sinhvien1_monhoc1.sinhvien1_id
                          #INNER JOIN monhoc1
                           #ON monhoc1.id= sinhvien1_monhoc1.monhoc1_id
                           #WHERE monhoc1.ten_mon='P'
                            #GROUP BY sinhvien1.ten
                             #HAVING COUNT(monhoc1.ten_mon) >=2
                              
                               #""" ).fetchall()
#print(result)


#cursor= conn.cursor()
#result= cursor.execute("""SELECT sinhvien1.ten , COUNT(*)
                       #FROM sinhvien1
                       # INNER JOIN sinhvien1_monhoc1
                        # ON sinhvien1.id=sinhvien1_monhoc1.sinhvien1_id
                         # INNER JOIN monhoc1
                          # ON monhoc1.id= sinhvien1_monhoc1.monhoc1_id
                           #WHERE monhoc1.ten_mon <> 'FastAPI' # lấy tất cả môn khác nhưng 'LOẠI MÔN <> FASTAPI'
                           # GROUP BY sinhvien1.ten
                            ##  """ ).fetchall()
#print(result)


                        #JOIN NÂNG CAO 3
                        #subquery:có 2 SELECT 
                              #+ SELECT trong: tính số môn
                              #+SELECT ngoài :  tính max của số môn của SELECT trong
                        #AS so_mon: đặt tên kết quả cho dễ gọi 

                                    #BÀI MẪU:BÊN DƯỚI
#cursor=conn.cursor()          
#result=cursor.execute("""SELECT MAX(so_mon)
                    # FROM (SELECT sinhvien1.ten,COUNT(*) AS so_mon
                        #FROM sinhvien1
                       # INNER JOIN sinhvien1_monhoc1
                       # ON sinhvien1.id= sinhvien1_monhoc1.sinhvien1_id
                      #  INNER JOIN monhoc1
                       # ON monhoc1.id = sinhvien1_monhoc1.monhoc1_id
                      #  GROUP BY sinhvien1.ten) """).fetchall() 
#print(result)


                        #JOIN NÂNG CAO 4
                        #DISTINCT : không đếm trùng môn
                        # IN (Python,SQL): chọn python hoặc SQL
#cursor=conn.cursor()
#result=cursor.execute("""SELECT sinhvien1.ten
                        #FROM sinhvien1
                        #INNER JOIN sinhvien1_monhoc1
                        #ON sinhvien1.id= sinhvien1_monhoc1.sinhvien1_id
                        #INNER JOIN monhoc1
                        #ON monhoc1.id= sinhvien1_monhoc1.monhoc1_id
                        #WHERE monhoc1.ten_mon IN ('Python','SQL') #cách2 viết : monhoc1.ten_mon='Pthon' OR monhoc1.ten_mon='SQL': 2 ý nghia giống nhau
                        #GROUP BY sinhvien1.ten
                        #HAVING COUNT (DISTINCT monhoc1.ten_mon)=2""").fetchall()
#print(result)


                        #JOIN NÂNG CAO DẠNG 5
                        # KHI BÀI TÌM NULL thì nên làm 2 bước 
                           #+ AND: tìm hoc sinh có môn sql và không có môn sql 
                           #+ WHERE: sau đó dùng where lọc ra đủ kq 
#cursor=conn.cursor()
#result= cursor.execute("""SELECT sinhvien1.ten,monhoc1.ten_mon
                        #FROM sinhvien1
                        #LEFT JOIN sinhvien1_monhoc1
                        #ON sinhvien1.id =sinhvien1_monhoc1.sinhvien1_id
                        #LEFT JOIN monhoc1
                        #ON monhoc1.id=sinhvien1_monhoc1.monhoc1_id
                        #AND monhoc1.ten_mon='SQL'
                        #WHERE monhoc1.ten_mon  IS NULL """ ).fetchall()
#print(result)



                        #JOIN NÂNG CAO 6
                        #COUNT(*): đếm tất cả 
                        #COUNT (monhoc1.ten_mon): đếm tên môn ở mỗi hoc sinh được group by

#cursor=conn.cursor()
#result= cursor.execute("""SELECT sinhvien1.ten,COUNT(monhoc1.ten_mon)
                        #FROM sinhvien1
                        #LEFT JOIN sinhvien1_monhoc1
                        #ON sinhvien1.id =sinhvien1_monhoc1.sinhvien1_id
                        #LEFT JOIN monhoc1
                        #ON monhoc1.id=sinhvien1_monhoc1.monhoc1_id
                        #GROUP BY sinhvien1.ten """ ).fetchall()
#print(result)

                        #JOIN TỔNG HỢP
                        #GROUP BY: CHIA NHÓM 
                        #GROUP_CONCAT: gom/liệt kê tất cả giá trị dữ liệu trong cùng 1 nhóm thành chuỗi 
                        # BÀI dưới nhấn run xem kq 

#cursor=conn.cursor()
#result= cursor.execute("""SELECT sinhvien1.ten,GROUP_CONCAT(monhoc1.ten_mon),COUNT(monhoc1.ten_mon)
                        #FROM sinhvien1
                        #INNER JOIN sinhvien1_monhoc1
                        #ON sinhvien1.id =sinhvien1_monhoc1.sinhvien1_id
                        #INNER JOIN monhoc1
                        #ON monhoc1.id=sinhvien1_monhoc1.monhoc1_id
                        #GROUP BY sinhvien1.ten
                        #HAVING COUNT(monhoc1.ten_mon)>=2
                        #ORDER BY COUNT ( monhoc1.ten_mon) DESC """ ).fetchall()
#print(result)


#cursor=conn.cursor()
#result=cursor.execute("""SELECT sinhvien1.ten,GROUP_CONCAT(monhoc1.ten_mon),COUNT(monhoc1.ten_mon) 
                      #FROM sinhvien1
                      #JOIN sinhvien1_monhoc1
                      #ON sinhvien1.id = sinhvien1_monhoc1.sinhvien1_id
                      #JOIN monhoc1
                      #ON monhoc1.id=sinhvien1_monhoc1.monhoc1_id
                      #GROUP BY sinhvien1.ten
                      #HAVING COUNT(monhoc1.ten_mon)>= 2
                      #ORDER BY COUNT(monhoc1.ten_mon)DESC""" ).fetchall()
#print(result)

                        #TÌM HS MAX + DỒNG HẠNG
                        # CÁCH 1:
#cursor= conn.cursor()
#result = cursor.execute( """SELECT ten,ds_mon,so_mon
                                  #FROM (SELECT sinhvien1.ten  AS ten,
                                  #GROUP_CONCAT(monhoc1.ten_mon)   AS ds_mon,
                                  #COUNT(monhoc1.ten_mon)  AS so_mon
                                  
                        #FROM sinhvien1
                       # JOIN sinhvien1_monhoc1
                       # ON sinhvien1.id = sinhvien1_monhoc1.sinhvien1_id
                        #JOIN monhoc1
                       # ON monhoc1.id= sinhvien1_monhoc1.monhoc1_id
                        #GROUP BY sinhvien1.ten )  AS ds
                        
                       #WHERE so_mon=(SELECT MAX(so_mon)
                                     # FROM (SELECT COUNT(monhoc1.ten_mon) AS so_mon
                                     # FROM sinhvien1
                                     # JOIN sinhvien1_monhoc1
                                     # ON sinhvien1.id=sinhvien1_monhoc1.sinhvien1_id
                                      #JOIN monhoc1
                                      #ON monhoc1.id=sinhvien1_monhoc1.monhoc1_id
                                      #GROUP BY sinhvien1.ten) AS max_ds)   
                        #""").fetchall()
#print(result)


                            #TÌM HS MAX +ĐỒNG HẠNG 
                            #CÁCH 2: WITH(với/tạo ra) ...AS (được tạo):nghĩa là tạo một bảng ds tạm và đặt tên nó là 'ds'
#cursor=conn.cursor()            

#result= cursor.execute("""WITH ds AS (SELECT 
                                  #sinhvien1.ten  AS ten,
                                  #GROUP_CONCAT(monhoc1.ten_mon)   AS ds_mon,
                                  #COUNT(monhoc1.ten_mon) AS so_mon 
                                  
                        #FROM sinhvien1
                        #JOIN sinhvien1_monhoc1
                        #ON sinhvien1.id = sinhvien1_monhoc1.sinhvien1_id
                        #JOIN monhoc1
                        #ON monhoc1.id= sinhvien1_monhoc1.monhoc1_id
                        #GROUP BY sinhvien1.ten )  
#SELECT ten,ds_mon,so_mon
#FROM ds
#WHERE so_mon=(SELECT MAX(so_mon)FROM ds)""").fetchall()
#print(result)



                                    # JOIN +AVG + MAX ĐỒNG HẠNG 


#conn.execute(""" CREATE TABLE diem1(id INTEGER PRIMARY KEY,    #TẠO thêm cột bảng diem1 cho hs 
                                    #sinhvien_id INTEGER,     => tạo cột này để LIÊN KẾT tương ứng điểm của hs với bảng có sẵn 'sinhvien1'
                                    #diem REAL)""")
#conn.commit()

#cursor=conn.cursor()
#result=cursor.execute("""INSERT INTO diem1(sinhvien_id,diem)VALUES (1,4),(2,6),(3,7),(4,8),(5,10)""").fetchall() #Thêm điểm
#conn.commit() 
                        
#cursor=conn.cursor()
#result=cursor.execute("""WITH ds AS(SELECT sinhvien1.ten  AS ten,
                          #AVG(diem1.diem)  AS dtb
                        #FROM sinhvien1
                        #JOIN diem1
                        #ON sinhvien1.id =diem1.sinhvien_id    # giá trị trong cột id bảng sinhvien1 khớp với giá trị stt cột sinhvien_id trong bảng diem1
                        #GROUP BY sinhvien1.ten )
#SELECT ten,dtb
#FROM ds
#WHERE dtb=(SELECT MAX(dtb) FROM ds)""").fetchall()
#print(result)



######################################  PYTHON KẾT NỐI SQLITE   ################################################################################  

import sqlite3      #thư viên python làm việc với SQL
conn= sqlite3.connect("database.db")    # kết nối DATABASE
#cursor=conn.cursor()                #tạo bộ điều khiển để chạy SQL
#result=cursor.execute("""SELECT sinhvien1.ten, monhoc1.ten_mon       
              # FROM sinhvien1_monhoc1                          
               #JOIN sinhvien1                                   
              # ON sinhvien1.id=sinhvien1_monhoc1.sinhvien1_id   
              #JOIN monhoc1
              # ON monhoc1.id=sinhvien1_monhoc1.monhoc1_id""").fetchall()

#print(result) # In kq
#FROM :chọn bảng xuất phát nối (bất kể lấy bảng nào bắt đầu điều được , miễn nối đủ 3 bảng )
#JOIN: nối với bảng nào 
#ON: xác định nối với nhau qua bảng tủng gian nào và dk là gì


#cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
#result = cursor.fetchall()
#print(result)


#result= cursor.execute("""SELECT sinhvien1.ten,monhoc1.ten_mon
                        #FROM sinhvien1_monhoc1
                        #JOIN sinhvien1
                        #ON sinhvien1.id = sinhvien1_monhoc1.sinhvien1_id
                        #JOIN monhoc1
                        #ON monhoc1.id =sinhvien1_monhoc1.monhoc1_id
                        #WHERE monhoc1.ten_mon IN ('Python','FastAPI','SQL')""").fetchall()
#print(result)



#result= cursor.execute("""SELECT sinhvien1.id,sinhvien1.ten,monhoc1.id
                        #FROM sinhvien1_monhoc1
                        #JOIN sinhvien1
                        #ON sinhvien1.id = sinhvien1_monhoc1.sinhvien1_id
                        #JOIN monhoc1
                        #ON monhoc1.id =sinhvien1_monhoc1.monhoc1_id
                        #""").fetchall()       #fetchall có nhiệm vụ lấy tất cả kq mà SQLite vừa truy vấn đưa về python
#print(result)


#result=cursor.execute("""CREATE TABLE IF NOT EXISTS lop1(id INTEGER PRIMARY KEY, ten_lop TEXT)""")
                                      #IF NOT EXISTS : tránh bị trùng tên bảng đã tạo rồi                                               
#print(result)

#result=cursor.execute("""SELECT *FROM lop1""").fetchall()
#print(result)

#result = cursor.execute("""INSERT INTO lop1(id , ten_lop)VALUES (3,'SQL')""")
#conn.commit()

#result=cursor.execute("""SELECT *FROM lop1""").fetchall()
#print(result)


####################################PYTHON SQLITE _SECLECT###########################################################################
                                 # fetchall () : lấy tất cả
                                # fetchone ():lấy 1 dòng

#result=cursor.execute("""SELECT *
                          #FROM lop1
                          #WHERE lop1.id =2 """).fetchone()
#print(result)


#result = cursor.execute(""" SELECT ten_lop FROM lop1""").fetchall()
#for i in result:
    #print(i[0]) # lấy cốt đầu tiên của list chứa nhìu tuple i('python',),v,..,
    # i[0]: chỉ lấy vị trí đầu vì khi fetchall trả toàn bộ kq ten_lop sẽ trả dạng tuple i('python,),i(fastapi,) , nên dùng i[0] để chỉ lấy kq python 
    # còn nhìu cách viết khác ( SELECT lop1.ten_lop, for i(,)v..v.v)


#result = cursor.execute("""SELECT  * FROM lop1""")
#ds=result.fetchall() # fetchall luôn trả về dạng list chứa các tuple  ví dụ như [(1,'python'),(2,'fastapi'),(3,'SQL')]
#for lop in ds:
  #print(lop)


#result = cursor.execute("""SELECT  * FROM lop1 WHERE lop1.id =2""")
#ds=result.fetchone() # fetchone lấy 1 dòng nên k cần for 
#print(ds) 

#result= cursor.execute("""INSERT INTO lop1(id,ten_lop)VALUES (4,'Automation')""")
#conn.commit()

#result =cursor.execute("""SELECT * FROM lop1""").fetchall()
#print(result)


#result = cursor.execute("""INSERT INTO lop1(id,ten_lop)VALUES (5,'Database')""")
#conn.commit()

#result = cursor.execute("""SELECT * FROM lop1""").fetchall()
#print(result)

                          # lấy dữ liệu python truyền vào sqlite
                          # (?,?) :lấy dữ liệu python truyền vào sqlite 1 cách an toàn
                          # (lop1_id,ten_lop) : mình có thể tự đặt tên 
#lop1_id=6
#ten_lop='Automation'

#result= cursor.execute("""INSERT INTO lop1 (id,ten_lop) VALUES (?,?)""",(lop1_id,ten_lop))
#conn.commit()

#result= cursor.execute(""" SELECT * FROM lop1 """).fetchall()
#print(result)


                          # UPDATE :SỬA/CẬP NHẬT LẠI DỮ LIỆU 
#lop1_id=6
#ten_lop='Database'

#result=cursor.execute("""UPDATE lop1 SET ten_lop=? WHERE id =?""",(ten_lop,lop1_id))
#conn.commit()

#result= cursor.execute(""" SELECT * FROM lop1""").fetchall()
#print(result)


                          #DELETE PYTHON
                          #(lop1_íd,) : đây là tuple có 1 phần tử 

#result = cursor.execute(""" DELETE FROM lop1 WHERE id=?""",(lop1_id,))
#conn.commit()


#result =cursor.execute("""SELECT * FROM lop1""").fetchall()
#print(result)



                        # COMMIT():LƯU THAY ĐỔI
                        # ROLLBACK () : HỦY/KHÔI PHỤC CÁC THAY ĐỔI CHƯA COMMIT , CHỈ KHÔI PHỤC KHI ĐÃ COMMIT , KHÔNG KHÔI PHỤC ĐƯỢC KHI ĐÃ DÙNG DELETE 
#lop1_id= 6
#ten_lop='Automation'
#result= cursor.execute("""UPDATE lop1 SET ten_lop =? WHERE id=?""",(ten_lop,lop1_id))
#conn.rollback()

#result=cursor.execute("""SELECT * FROM lop1""").fetchall()  
#print(result)   

#lop1_id= 6
#ten_lop='Automation'
#result= cursor.execute("""INSERT INTO lop1 (id,ten_lop) VALUES (?,?)""",(lop1_id,ten_lop))
#conn.commit()

#result= cursor.execute("""SELECT * FROM lop1 """).fetchall()
#print(result)


#lop1_id= 6
#ten_lop='Database'
#result= cursor.execute("""UPDATE lop1 SET ten_lop =? WHERE id=?""",(ten_lop,lop1_id))
#conn.commit()

#lop1_id= 6
#ten_lop='Automation'
#result= cursor.execute("""UPDATE lop1 SET ten_lop =? WHERE id=?""",(ten_lop,lop1_id))
#conn.rollback()

#result=cursor.execute("""SELECT * FROM lop1""").fetchall()  
#print(result)  
#  xem lại phần kq này , kq đúng phải là database   
##############################  DATABASE ERROR HANDLING : XỬ LÍ LỖI TRONG DATABASE    ###################################################################
#######   #### ########try: thử lại ,nếu chưa có dữ liệu thì thêm vào , ############################################################
                      # except: nếu lỗi xử lí ở đây " báo trùng"  hoặc "lỗi khác"

#check= cursor.execute("SELECT * FROM lop1 WHERE id=?",(7,)).fetchone()
#print("check7",check)


#result= cursor.execute("""INSERT INTO lop1 (id,ten_lop)VALUES (?,?)""",(7,'Automation'))
#conn.commit()

                              #try,except :báo lỗi trùng PRIMARY KEY 
                              #IntegrityError: trùng ID 
#try :
    #result= cursor.execute("""INSERT INTO lop1 (id,ten_lop)VALUES (?,?)""",(7,'Automation')) 
    #conn.commit()
#except sqlite3.IntegrityError:
    #print('ID đã tồn tại')

#result=cursor.execute("""SELECT * FROM lop1""").fetchall()  
#print(result)  



                              #try,except :
                              #OperationalError : sai SQL , bảng không tồn tại
#try: 
  #result= cursor.execute("""SELECT * FROM lop1""").fetchall()
  #print(result)
#except  sqlite3.OperationalError:
   #print(" bảng k tồn tại")

                    #try,except:
                    #sqlite3.Error: lỗi database nói chung (lỗi chung chung trong database , k báo lỗi cụ thể như integrity và operational )

#try: 
  #result= cursor.execute("""SELECT * FROM lop999""").fetchall()
  #print(result)
#except  sqlite3.Error:
   #print("lỗi chung chung trong database , k báo lỗi cụ thể ")
   

                #try,except + Error handling
                #commit + rollback() trong quy trình làm việc qua nhiều bước kiểm tra dữ liệu :
                                              #NẾU DỮ LIỆU KT KHỚP Và ĐÚNG HET MỚI "COMMIT" TẤT CẢ, 
                                              # nếu 1 tromng số gd bị sai thì "EXCEPT" để trả kq sai 

#try:
  #result=cursor.execute("""UPDATE lop1 SET ten_lop=? WHERE id=?""",('AI Automation',6))
  #result=cursor.execute("""SELECT * FROM lop999 """).fetchall() #=>># cố tình tạo 1 gd kt sai dữ liệu để báo except
  #conn.commit()
#except sqlite3.Error:
  #conn.rollback()
  #print('có lỗi, đã rollback ')   


              #try, except : Nếu lỗi báo except
              # else: nếu k lỗi ra kq else
#result = cursor.execute("""SELECT * from sinhvien1""").fetchall()
#print(result)


#try :
  #result= cursor.execute("""INSERT INTO sinhvien1(id,ten)VALUES (?,?)""",(6,'Quỳnh'))
  #conn.commit()
#except sqlite3.IntegrityError:
 # print(" ID PRIMARY KEY đã tồn tại")
#else:
  #print("thêm hs thành công ")


              #try,except :
              # finally : CÓ LỖI HAY KHÔNG LỖI THÌ finally VẨN CHẠY 
#try:
  #result =cursor.execute("SELECT * FROM sinhvien123")
  #print("lấy dữ liệu thành công")
#except sqlite3.Error:
  #print("có lỗi database")
#finally:
  #print(" đã kết thúc chạy database ")

              #try,except 
              # as e: lấy lỗi ra để xem /biêt nội dung lỗi thật cụ thể là gì ?, được dùng kết hợp tất cả "except"
#try: 
  #result = cursor.execute("SELECT * FROM sinhvien999").fetchall() # cố tình tạo lỗi để text " as e"
#except sqlite3.Error as e:
  #print("lỗi", e)


              #try, except 
              #raise : chủ động tìm lỗi 
#try:
  #tuoi = -5
  #if tuoi<0:
    #raise ValueError ("tuôi k được âm")
  #print(" dữ liệu hợp lệ")
#except ValueError as e:
  #print("lôi",e)

#result= cursor.execute("""SELECT * FROM sinhvien1 """).fetchall()
#print(result)


#try: 
  #id_sv=4
  #ten_lop='Nghĩa'
  #result = cursor.execute("""SELECT * FROM sinhvien1 WHERE id =?""",(id_sv,)).fetchone()
  #if result:
    #raise ValueError("id trùng")
  #result= cursor.execute("""INSERT INTO sinhvien1 (id,ten)VALUES (?,?)""",(id_sv,ten_lop)).fetchone()
  #conn.commit()
  #print(" tất cả dữ liệu đúng , đã lưu thanh công")
#except ValueError as e:
  #print(" dữ liệu kt sai",e)


                      #TRY,EXCEPT 
                      # ĐỔI ID NHƯNG ĐỔI BỊ TRÙNG KQ ID KHÁC

#try:
  #result=cursor.execute("""UPDATE sinhvien1 SET id=? WHERE id=?""",(6,1)) # id sau SET: id mới -> đổi thành 6
  #conn.commit()                                                           #ID sau WHERE :id cũ -> tìm id =1 có trong bảng để đổi
  #print("cập nhật thành công")
#except sqlite3.IntegrityError:
  #print(" ID đổi thành ID khác bị trùng ")


                      # TỔNG HỢP
#id_sv=1
#ten_sv='An'
#try:
  #result= cursor.execute("""INSERT INTO sinhvien1(id,ten)VALUES (?,?)""",(id_sv,ten_sv)).fetchall()
  #conn.commit()

#except sqlite3.IntegrityError :
  #print(" trùng id")
#else:
  #print (" dữ liệu k bị trùng , đã lưu thành công")
#finally:
  #print("  đã xử lí xong ")


#############################  PHẦN 4: FASTAPI KẾT NỐI DATABASE #############################################
              #qua trang fastapi_database.py chạy vì bên đây dễ bị trùng dữ liệu cũ 
from sqlalchemy import create_engine
engine= create_engine("sqlite:///database.db")   # engine giúp SQLAICHEMY kết nối cụ thể database nào?

from sqlalchemy.orm import sessionmaker           #sessionmaker:tạo "khuôn " để tạo session 
SessionLocal = sessionmaker (bind=engine)     #sessionLocal:tên đặt cho khuôn đó , bind= engine: session sử dụng cho engine nào, phiên làm việc với data
db = SessionLocal()       # tạo 1 session thực thể thao tác dữ liệu 

from sqlalchemy.orm import DeclarativeBase  #DeclarativeBase: nền của SQLAIchemy để tạo model
class Base (DeclarativeBase):       #base: tên tự đặt 
  pass  #pass: chưa có nội dung riêng 

from sqlalchemy.orm import Mapped,mapped_column
class sinhvienmoi(Base):
  __tablename__="sinhvienmoi"
  id: Mapped[int] = mapped_column(primary_key=True)   #mapped :ánh xạ/ được liên kết với ...
  ten:Mapped[str]
  tuoi:Mapped[int]
Base.metadata.create_all(engine) #lấy tất cả dữ liệu trên model đã khai báo trong base , rồi tạo những bảng tương ứng trong database thông qua engine

sv1= sinhvienmoi(id=1,ten='An',tuoi=20) #tạo dữ liệu 
db.add(sv1) #đưa sv1 vào session chuẩn bị lưu
db.commit() # lưu thay đổi vào database

ds_sv=db.query(sinhvienmoi).all()
for hs in ds_sv:
  print(hs.id,hs.ten,hs.tuoi)































