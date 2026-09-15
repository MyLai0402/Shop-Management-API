
#path_database: k cần viết lại dường kết nối 
# Dùng import đủ và dùng dữ liệu cũ bảng database query_data để làm dữ liệu tính bên đây luôn 

from sqlalchemy import create_engine
engine =create_engine("sqlite:///./path_data.db")

from sqlalchemy.orm import relationship,joinedload 
#relationship: tạo đường kết nối 2 bảng ( dối tượng tương ứng đối tượng )
# joinedload: để load sẵn relationship" tức là lấy luôn đường liên kết cái bảng còn lại để lấy dữ liệu trong đó "
# options : tùy chọn cách lây của query (nơi chứa cách chọn / lấy )



from sqlalchemy.exc import IntegrityError
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session

from typing import Optional
from fastapi import FastAPI ,Query, HTTPException ,Depends ,Body
app= FastAPI()
from pydantic import BaseModel,ConfigDict
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase, sessionmaker
sessionLocal=sessionmaker (bind=engine)
db=sessionLocal()
# mỗi khi cần làm việc với database , lây sessionLocal tạo cho mình một db Session để enponin nhận nó 
# mục đích dùng để: db.query(), db.add(),db.commit(),db.delete()
# mỗi request nên có session riêng vì : session k những là phiên làm việc với database mà còn giữ trạng thái làm việc tốt với 1 request ( dễ bị lẫn trạng thái yêu cầu)

                # Tạo lại db để kết nối ở dưới vì bị trùng get_db nên không import get_db được 

def get_db(): # get_db: tên tự đặt để tạo db
    db=sessionLocal() # tạo db để kết nối , làm việc , mỗi phiên làm việc với database( khi có database thì sd db)
    try:
        yield db # chạy thử db với fastapi và enpoin
    finally:
        db.close() #chạy thử hay không thì cũng đóng lại

class Base (DeclarativeBase):
    pass

class path_data (Base):
    __tablename__="path_data"
    id:Mapped[int] = mapped_column (primary_key=True)
    ten:Mapped[str] =mapped_column ()
    tuoi:Mapped[int] = mapped_column ()
    dia_chi:Mapped[str] = mapped_column ()
    san_pham= relationship("path_data_join",back_populates="nguoi") # thêm dòng này để path_data đang nối với bảng nào và bảng đó chính là dữ liệu của nó 

class path_data2 (Base):                            # tạo thêm để join 2 bảng và lọc
    __tablename__="sanpham"
    id:Mapped[int] =mapped_column (primary_key=True)
    ten_sp:Mapped[str] = mapped_column()
    gia :Mapped[int] =mapped_column ()


class path_data_join (Base):                            # tạo thêm để join 2 bảng và lọc
    __tablename__="sp2"
    id:Mapped[int] =mapped_column (primary_key=True)
    path_id :Mapped[int] =mapped_column (ForeignKey("path_data.id"))
    ten_sp:Mapped[str] = mapped_column()
    gia :Mapped[int] =mapped_column ()
    nguoi = relationship("path_data",back_populates="san_pham") # relationship:tạo liên kết vứi bảng kia , back_populates: tạo liên kết 2 chiều


class path_test(BaseModel):
    id: Optional[int] =None
    ten:str
    tuoi:int
    dia_chi: str
    model_config=ConfigDict(from_attributes=True)



class UpdateDiaChi (BaseModel):
    dia_chi:str
     
    model_config=ConfigDict(from_attributes=True)



class path_test_sp (BaseModel):
    id:int
    ten_sp:str
    gia:int


class path_data_sp2(BaseModel):
    path_id:int
    ten_sp:str
    gia:int


class nguoi_san_pham(BaseModel):
    id:int
    ten:str
    tuoi:int
    san_pham:list[path_test_sp] =[] # thêm default[]để tránh lỗi nếu rỗng 
                                    # rela1 bắt buột giống tên relationship ở trên mới ra được kq dữ liệu mỗi sv ,
                                    #còn nếu tên relationship k trùng thì sẽ ra kq [] rỗng 
    model_config=ConfigDict(from_attribute=True)


class response_tt (BaseModel):
    ten:str
    ten_sp:str
    gia:int
    gia_sau_giam:int
    model_config=ConfigDict(from_attribute=True)


class xep_loai (BaseModel):
    ten_sp:str
    gia:int
    xep_loai:str
    model_config=ConfigDict(from_attribute=True)


class summary (BaseModel):
    so_luong:int
    max_sp: list[str]
    min_sp:list[str]
    trung_binh_all:float
    model_config=ConfigDict(from_attribute=True)


class nhom_all (BaseModel):
    ten_sp:str
    so_luong:int
    tong_gia_sp:float
    model_config=ConfigDict(from_attribute=True)

class tim_nhom_max(BaseModel):
    ten_sp:list[str]
    tong_gia_sp:float
    model_config=ConfigDict(from_attribute=True)

class valu_data(BaseModel):
    ten:str
    tuoi:Optional[int] =None
    dia_chi:str
    model_config=ConfigDict(from_attribute=True)





Base.metadata.create_all(engine)

@app.post("/hs",response_model=path_test)
def path_test(data:path_test): # thêm dữ liệu vào bảng database   
    sv =path_data(id=data.id,ten=data.ten,tuoi=data.tuoi)
    db.add(sv)
    db.commit()
    return sv

#@app.get("/hs/{id}") # lấy theo id
#def path_hs(id:int): 
    #sv=db.query(path_data).filter(path_data.id == id).first()
    #return sv


#@app.get("/path_hs") # xem lại vì sao để khuôn response_model k ra kq báo lỗin , khi xóa response đi thì ra chuẩn kq ???
#def path_hs(page:int =Query(),limit:int =Query()):
    #offset=(page-1)*limit
    #sv=db.query(path_data).offset(offset).limit(limit).all()
    #return sv 


                                    #SORT DATABASE
                                    #ACS : tăng dần , có thể k ghi vào ucng được vì mặc định sort là tăng dần 
                                    #desc() : GIẢM DẦN 

@app.get("/sort_data")
def sort_data():
    sv =db.query(path_data).order_by(path_data.tuoi).all()
    return sv

                                #SORT THEO FIELD:

#@app.get("/sort_data")
#def sort_data(sort_by:str =Query()):
    #if sort_by =="tuoi":
        #sv=db.query(path_data).order_by(path_data.tuoi).all()
    #elif sort_by =="ten":
        #sv=db.query(path_data).order_by(path_data.ten).all()
    #return sv

                            #SORT +PAGINATION

#@app.get("/sort_pagination")
#def sort_pagi (sort_by:str =Query(),page:int =Query(),limit :int = Query()):
    #if sort_by == "tuoi":
        #sv=db.query(path_data).order_by(path_data.tuoi).offset((page-1)*limit).limit(limit).all()
    #if sort_by == "ten":
        #sv=db.query(path_data).order_by(path_data.ten).offset((page-1)*limit).limit(limit).all()
    #return sv



                            # FILTER 1 DK

#@app.get("/filter1")
#def filter_1(tuoi:int =Query()):
    #sv=db.query(path_data).filter(path_data.tuoi== tuoi).all()
    #if not sv:
        #raise HTTPException(status_code=404,detail="k tìm thây tuổi hợp lệ")
    #return sv

                            #FILTER lấy khoản max và min
#@app.get("/filter_khoan")
#def filter_khoan (max_tuoi:int =Query(),min_tuoi:int=Query()):
    #sv =db.query(path_data).filter(path_data.tuoi >= min_tuoi, path_data.tuoi <= max_tuoi).all()
    #return sv


                            #FILTER nhiều dk 

#@app.get("/filter_nhieu")
#def filter_nhieu (ten:str = Query(),tuoi:int =Query()):
    #sv =db.query(path_data).filter(path_data.tuoi == tuoi, path_data.ten.ilike(f"%{ten}%")).all()
    #return sv


                            # TÌM DỮ LIỆU : PATH

#@app.get("/surch_keywork")
#def surch_key (keywwork: str = Query()):
    #sv=db.query(path_data).filter(path_data.ten.ilike(f"%{keywwork}%")).all()
    #return sv


                    ## NỐI 2 BANG ĐỂ LỌC ##

#@app.post("/path_test_join2")
#def join_2 (data:path_test_sp):
    #sv=path_data2(id=data.id,ten_sp=data.ten_sp,gia=data.gia)
    #db.add(sv)
   # db.commit()
    #return sv




@app.get("/path_join")
def join_path (id:int):
    sv=db.query(path_data2).filter(path_data2.id ==id).first()
    return sv


#@app.get("/join")
#def join (id:int):
    #sv=db.query(path_data.id,path_data.ten,path_data2.ten_sp,path_data2.gia).join(path_data2,path_data.id==path_data2.id).filter(path_data.id ==id).first()
    #return {"id":sv.id,"ten":sv.ten,"ten_sp":sv.ten_sp,"gia":sv.gia}


                                   
@app.post("/path_data_sp2",response_model=path_data_sp2)
def path_sp2 (data:path_data_sp2):
    sv = path_data_join(path_id= data.path_id,ten_sp=data.ten_sp,gia=data.gia)
    db.add(sv)
    db.commit()
    return sv

                            #RESPONSE + phép tính

@app.get("/response_tt",response_model=list[response_tt])
def response_tt ():
    sv= db.query (path_data,path_data_join).all()
    kq=[]
    for x,sp in sv: #( tức là x in sv(path_data) và sp in sv(path_data_join))
        gia_sau_giam = sp.gia * 90/100 # tức là giảm 10% , tính tắt là nhân 90% cho nhanh khỏi trừ lại làm 2 bước 
        kq.append({"ten":x.ten,"ten_sp":sp.ten_sp,"gia":sp.gia,"gia_sau_giam":gia_sau_giam})
    return kq


@app.get("/xep_loai",response_model=list[xep_loai])
def xep_loai():
    sv= db.query(path_data_join).all()
    #print(len(sv))
    #print(sv)
    kq=[]

    for v in sv:
        if v.gia >= 200:        
            gia = v.gia
            ten_sp = v.ten_sp
            xep_loai ="cao"
        elif 80<=  v.gia < 200:          
            gia =v.gia
            ten_sp = v.ten_sp
            xep_loai ="TB"
        else :           
            gia=v.gia
            ten_sp =v.ten_sp
            xep_loai ="thấp"
        kq.append({"ten_sp":v.ten_sp,"gia":v.gia,"xep_loai":xep_loai}) # chỉ xep_loai k được v.xep_loai vì trong for k có xep_loai
    return kq


                            #SUMMARY TÍNH TOÁN

@app.get("/thong_ke_summary",response_model=list[summary])
def thong_ke():
    sv=db.query(path_data_join).all()
    max_1=0
    min_2=999
    tonggia =0
    kq=[]  
    ds_max=[]
    ds_min=[] 
    for k in sv:
        tonggia += k.gia
        
        if k.gia > max_1:
            max_1=k.gia
            max_sp = k.ten_sp  
            ds_max=[k.ten_sp]  # reset lại tên trung
        if k.gia == max_1 and k.ten_sp not in ds_max: # thêm dk nếu có 2 max bằng
            ds_max.append(k.ten_sp)  
            
        if k.gia < min_2:
            min_2 = k.gia
            min_sp = k.ten_sp 
            ds_min=[k.ten_sp] # reset lại tên trung
        if k.gia == min_2 and k.ten_sp not in ds_min: # thêm dk nếu có 2 min bằng 
            ds_min.append(k.ten_sp)  
    trung_binh_all = tonggia / len(sv)
    print(max_1)   
    print(ds_max)   
    kq = [{"so_luong":len(sv),"trung_binh_all":trung_binh_all,"max_sp":ds_max,"gia_max":max_1,"min_sp":ds_min,"gia_min":min_2}]        
    return kq 



                        #SUMMARY TÍNH TOÁN VÀ TRẢ THEO NHÓM 

# cách trả kq gôm mỗi sp riêng để tính toán và trả kq theo nhóm sp riêng 
# có 2 cách: cách 1 có thể tạo response và tìm sp theo tham số cách cũ 
# cách 2: ở dưới tạo thêm da_co =[] và apped đã có nhằm mục đích mỗi sp chỉ xử lí tính toán 1 lần , tránh xử lí và trả kq nhiều lần , cần append dòng cuối để tránh lặp lại sp 
@app.get("/nhom_all",response_model= list[tim_nhom_max])   
def nhom_tk(db:Session=Depends(get_db)):
    sv=db.query(path_data_join).all()
    kq=[]
    da_co=[] # tạo nơi chứa để tránh xử lí 1 sp nhiều lần
    max_sl =0
    sp_max =""
    max_gia=0
    sp_maxgia=""
    dsmax=[]
    
    for i in sv:
        if i.ten_sp in da_co: # đặt sk nếu không có trong da_co thì tinh tính toán , còn nếu có thì chỉ tính 1 lần tránh bị trùng lặp
            continue # dùng continue để mỗi sp chỉ được tính toán và trả kq 1 lần 
        so_luong =0
        tong_gia_sp =0
        
        for j in sv: # cố tình đặt thêm biến j in sv để tìm ten_sp của i và j trùng nhau thì tính toán xử lí bài toán 
            if j.ten_sp == i.ten_sp: # đặt dk trùng ten_sp nhau 
                so_luong += 1
                tong_gia_sp += j.gia     
        if so_luong > max_sl:
            max_sl = so_luong
            sp_max = i.ten_sp   

        if tong_gia_sp > max_gia:
            max_gia = tong_gia_sp
            sp_maxgia = i.ten_sp
            dsmax=[i.ten_sp]
        elif tong_gia_sp == max_gia:
            dsmax.append(i.ten_sp)
        da_co.append(i.ten_sp) # để gom lại những ten_sp nào đã xử lí và không xử lí lại để tránh trùng 
    kq.append({"ten_sp":dsmax,"tong_gia_sp":max_gia})       
    return kq

        


@app.get("/xem_all")
def xem_all():
    sv=db.query(path_data_join).all()
    return sv

@app.get("/xem_path_data")
def xem_path_data():
    sv=db.query(path_data).all()
    return sv


                    
                # TẠO CỘT MỚI ALTER TABLE ( xem trong điện thoại ghi chú)
                 #THÊM DỮ LIỆU VÀO CỘT VỪA THÊM HOẶC SỮA DỮ LIỆU "PUT"

 # TẠO THÊM 1 CLASS UpdateDiaChi (BASEMODEL ) ĐỂ CHỨA NHỮNG DỮ LIỆU CẦN SỬA HOẶC THÊM 
@app.put("/sua_them_cot/{id}")
def sua_them(id:int,dia_chi_them_sua: UpdateDiaChi,db:Session =Depends(get_db)): 
    sv = db.query(path_data).filter (path_data.id == id).first()
    if not sv:
        raise HTTPException(status=404,detail="k tìm thây hs ")
    sv.dia_chi = dia_chi_them_sua.dia_chi
    db.commit()
    db.refresh(sv) # lấy lại dữ liệu  mới nhất từ database
    return sv

                    #Thêm dữ liệu mới vào ( hôm sau test lại đoạn này )
@app.post("/them_sv") #(test không ra kq dù code đúng , kiểm tra lai )
def them_sv(data:path_test,db:Session =Depends (get_db)):
    sv=db.query(path_data).all()
    if data.tuoi < 18:
        raise HTTPException(status_code=400,detail="k tìm thấy tuoi hop le")
    sv=path_data( ten = data.ten, tuoi=data.tuoi,dia_chi=data.dia_chi)
    db.add (sv)
    db.commit()
    db.refresh(sv)
    return sv


                    # kiểm tra trùng dữ liệu 
                    # nhớ import Optional ở trên để cho ra response không bị lỗi id vì id nếu đã dùng làm primary_key thì k nên kt trùng 
                    # chỉnh sửa lại phần Optional ở basemodel 
@app.post("/kt_trung/{ten}",response_model=path_test)
def trung_kt (data:path_test,db :Session =Depends (get_db)):
   
    sv=db.query(path_data).filter(path_data.ten ==data.ten).first()
    if sv:
        raise HTTPException(status_code=409,detail="trùng tên dữ liệu")
    sv=path_data(ten=data.ten, tuoi=data.tuoi,dia_chi=data.dia_chi)
    db.add(sv)
   
    try: # vì lỗi nên xem lỗi ở đâu không ra kq nên dùng try và except 
        db.commit()
        db.refresh(sv)
        return sv
    except IntegrityError :
        db.rollback()
        raise HTTPException(status_code=409,deltai="tên trùng")


                    # put: sữa tuôi
@app.put("/sua_sv/{id}")
def sua_sv(id:int,tuoi:int,db:Session =Depends(get_db)):
    sv=db.query(path_data).filter (path_data.id == id).first()
    if not sv:
        raise HTTPException(status_code=404,detail="k tìm thấy hs")
    sv= path_data(sv.tuoi ==tuoi)
    db.add(sv)
    db.commit()
    db.refresh (sv)



                    # DELETE ID
                    # thường xóa id bằng delete , còn muốn xóa chỉ riêng đối tượng tên hoặc tuôi thì dùng put hoặc patch 
@app.delete("/xoa_id")
def xoa_ìd(id:int, db:Session=Depends (get_db)):
    sv= db.query(path_data).filter(path_data.id == id).first()
    if not sv:
        raise HTTPException(status_code=404,detail="k tìm thấy id trùng để xóa")
    db.delete(sv)
    db.commit()


                    #ValueError + DATABASE
                    # raise ValueError : phát hiện và ném lỗi
                    # try/except: bắt lỗi để xử lí 
                    # HTTPException : biến lỗi của ValueError thành phản hồi HTTP cho API biết 
@app.get("/kt/{tuoi}")
def kt(tuoi:int):
    try:
        if tuoi <18:
            raise ValueError ("tuổi không hợp lệ ")
        return {"tuoi":tuoi}
    except ValueError as e:
            raise HTTPException (status_code=400,detail=str(e))


                    #POST +ValueError +DATABASE ( trước khi thêm dữ liệu phải kt tuổi trước)

@app.post("/them_tuoi_data123")
def them_tuoi(data:path_test = Body(...), db:Session =Depends(get_db)):
    try:
        if data.tuoi <18:
            raise ValueError ("tuổi k hợp lệ ")
        db_sv = path_data(ten=data.ten,tuoi=data.tuoi,dia_chi=data.dia_chi)
        db.add(db_sv)
        db.commit()
        db.refresh(db_sv)
        return db_sv
    except ValueError as e:
        raise HTTPException(status_code=400, detail =str(e))



                # Put + valueError+ database ( trc khi sửa dữ liệu kt dữ liệu trước)
                # lưu ý : +khi sv.ten = data.ten : nghĩa là lấy dữ liệu mới ghi đè lên dữ liệu cũ áp dụng khi đối tượng đã có dữ liệu trong bảng 
                #         + khi path_data(ten = data.ten): nghĩa là nếu đối tượng sv đó chưa có thì tạo mới / thêm vào dữ liệu trong bảng 
                #         + "==": 2 dấu bằng chỉ để so sánh dữ liệu 

@app.put("/sua_dulieu/{id}")
def sua_dulieu(id:int,data:path_test = Body(...),db:Session=Depends(get_db)):
    try:
        sv = db.query(path_data).filter(path_data.id == id).first()
        if data.tuoi < 18:
            raise ValueError ("tuổi bé hơn 18")
        sv.ten= data.ten 
        sv.tuoi = data.tuoi
        sv.dia_chi= data.dia_chi
        db.commit()
        db.refresh(sv)
        return sv
    except ValueError as e:
        raise HTTPException(status_code=400,detail=" tuổi k hợp lệ ")





                            #get_valueError
@app.get("/kt_sp/{gia}/{so_luong}")
def kt_sp (gia:int, so_luong:int):
    try:
        if gia <= 0:
            raise ValueError ("giá phải lớn hơn không")
        if so_luong < 0:
            raise ValueError(" so_luong phải lớn hơn không ")
        return {"gia":gia,"sl":so_luong}
    except ValueError as e:
        raise HTTPException(status_code=400,detail="gia or sl k hợp lệ ")




                        # KIỂM TRA /ÉP GIÁ TRỊ BẰNG ValueError 
                        # Mục Đích bài này cố tình cho gia = str để bắt lỗi " gia k được là chuỗi nếu cố tình ép "
                        # lưu ý : chỉ có HTTPException mới quyết định swagger trả ra lỗi bao nhiêu , 
                        # còn valueError khi xuất hiện lỗi thì lỗi đó nằm trong python k trả ra swagger
                        #"as e ": k bắt buột mục đích muốn xem rõ lỗi (str(e))

                       
@app.get("/kt_gt/{gia}")
def kt_gt (gia:str):
    try:
        gia= float(gia)
        return gia
    except ValueError :
        raise HTTPException (status_code=400,detail="giá phải là số")


@app.get("/tinh_tong")
def tinh_tong(so1:str,so2:str):
    try:
        so1=float(so1)
        so2=float(so2)
        return {"tổng":so1 + so2}
    except ValueError :
        raise HTTPException(status_code=400,detail="dữ liệu phải là số ")



@app.post("/post_dl")
def post_dl(tuoi:int,data:valu_data):
    try:
        if tuoi >0 :
            hs = path_data(ten= data.ten, tuoi=data.tuoi,dia_chi=data.dia_chi)
            raise HTTPException(status_code=200,detail="hs thêm thành công")
        raise ValueError (" tuổi phải lớn hơn không")
    except ValueError:
        raise HTTPException(status_code=400,detail="tuổi k hợp lệ ")  
    


                    #ValueError + DATABASE 
@app.post("/valu_data")
def gia_valu(tuoi:int,data:valu_data): # có thể bỏ tuoi riêng biệt vì trong dữ liệu data: vulue bắt buột nhập tuổi mới ra kq , nên nhập 2 lần tuổi dư thừa 
    try:
        if tuoi < 0:
            raise ValueError (" tuổi k được bé hơn không")
        sp = path_data(ten =data.ten, tuoi= data.tuoi,dia_chi=data.dia_chi)
        db.add(sp)
        db.commit()
        db.refresh(sp)
        return sp
    except ValueError:
        raise HTTPException(status_code= 400, detail=" tuổi không được âm ")
    






#@app.get("/path_data_getsp2",response_model=list[path_data_sp2])
#def get_sp2_join():
    #sv=db.query(path_data_join).all()
    #return sv

                                #relationship() : kết nối trên Base+ joinedload () 
                                # (Học thêm tất cả các dạng riêng vè relationship bên file relationship.py)
#@app.get("/join1_N",response_model=list[nguoi_san_pham])
#def join ():
    #sv= db.query(path_data).options(joinedload(path_data.san_pham)).all()  # lấy nhiều người , nhiều sp 
# lấy tất cả path_data , 
# đồng thời dùng tùy chọn options ,
# joinedload để load (lấy ) sẵn relationship san_pham , 
# mục đích lấy dữ liệu bảng kia kết nối bảng này 
    #return sv


#@app.get("/join1_N/{id}",response_model=nguoi_san_pham) # tạo 1 class mới để trả kq cho 2 bảng hoặc theo cách mình muốn   
#def join1_N (id:int, db: Session = Depends (get_db)): #depends(): nhờ fastapi gọi get_db để lấy db cho enpoin sử dụng 
                                                        # nhớ tạo lại db ( get_db ) ở trên import để có db sử dụng cho api 
                                                        # nên tạo db lại cho mỗi request để tránh API rối trạng thái xử lí (An toàn hơn)
    #sv=db.query(path_data).options(joinedload(path_data.san_pham)).filter(path_data.id == id).first()
    #if not sv:
        #raise HTTPException(status_code=404,detail=" k tìm thấy id ")
    #return sv

                    




