from sqlalchemy import create_engine
engine= create_engine ("sqlite:///./shop_management_api.db")

from sqlalchemy.orm import sessionmaker
sessionLocal =sessionmaker (bind=engine)
db= sessionLocal()

from datetime import datetime
from sqlalchemy import and_ , or_
from sqlalchemy.orm import relationship,joinedload
from sqlalchemy.orm import DeclarativeBase
class Base (DeclarativeBase):
    pass

from sqlalchemy import ForeignKey, text
from pydantic import BaseModel,ConfigDict

from fastapi import FastAPI,HTTPException
app=FastAPI()


from sqlalchemy.orm import Mapped, mapped_column
class shop_mana(Base):
    __tablename__= "shop_management"
    id:Mapped[int] = mapped_column (primary_key=True)
    ten_shop:Mapped[str] =mapped_column()
    rela1=relationship("shop_ql",back_populates="rela2")


class shop_ql(Base):
    __tablename__="myshop_ql"
    id:Mapped[int] = mapped_column (primary_key=True)
    shop_id:Mapped[int] =mapped_column (ForeignKey("shop_management.id"))
    ten_khach:Mapped[str] =mapped_column()
    sp:Mapped[str] =mapped_column()
    gia:Mapped[float] =mapped_column()
    so_luong:Mapped[int] =mapped_column()
    rela2 =relationship("shop_mana",back_populates="rela1")




class lich_su_xoa_db(Base):
    __tablename__="ls_xoa"
    id:Mapped[int] = mapped_column (primary_key=True)
    shop_id:Mapped[int] =mapped_column (ForeignKey("shop_management.id"))
    ten_khach:Mapped[str] =mapped_column()
    sp:Mapped[str] =mapped_column()
    gia:Mapped[float] =mapped_column()
    so_luong:Mapped[int] =mapped_column()
    thoi_gian_xoa:Mapped[datetime] = mapped_column(default=datetime.now) # lưu ý : now không thêm ngoặc () vì datetime.now dc sqlalchemy gọi lại mỗi khi ghi 1 bản lịch sử mới




class shop_manage (BaseModel):
    id:int
    ten_shop:str
    model_config= ConfigDict(from_attributes =True)

class shop_qlshop(BaseModel):
    id:int
    shop_id:int
    ten_khach:str
    sp:str
    gia:float
    so_luong:int
    model_config= ConfigDict(from_attributes =True)


class tong_hop (BaseModel):
    id: int
    ten_shop:str
    rela1: list[shop_qlshop] =[]
    model_config= ConfigDict(from_attributes =True)


class sp_all(BaseModel):
    ten_shop:str
    ten_khach:str
    gia:float   
    model_config= ConfigDict(from_attributes =True)


class lich_su_xoa(BaseModel):
    id:int
    shop_id:int
    ten_khach:str
    sp:str
    gia:float
    so_luong:int
    thoi_gian_xoa: datetime = datetime.now() # nhớ import datetime
    model_config= ConfigDict(from_attributes =True)

Base.metadata.create_all(engine)



#db.execute(text("ALTER TABLE myshop_ql ADD COLUMN so_luong INTEGER;")) 
#db.commit() 
# mục đích thêm cột mới vào bảng theo sqlalchemy hoặc có thể viết cách khác bằng SQL thuần ( xem trong ghi chú dt )


#db.execute(text("""UPDATE myshop_ql SET so_luong=0 WHERE so_luong IS NULL"""))
#db.commit()
#update cập nhật lại trong bảng shop_ql
# SET tìm dòng so_luong gán giá trị bằng 0 
#where : chỉ sửa những giá trị bằng null



@app.post("/them_b1",response_model=shop_manage)
def xem_b1 (data:shop_manage):
    shop= shop_mana(id=data.id,ten_shop=data.ten_shop)
    db.add(shop)
    db.commit()
    return shop


@app.get("/xem_b1",response_model=list[shop_manage])
def xem_tc():
    shop=db.query(shop_mana).all()
    return shop




@app.post("/them_b2",response_model=shop_qlshop)
def them_dl_b2 (data:shop_qlshop):
    khach= shop_ql(id= data.id ,shop_id= data.shop_id ,ten_khach=data.ten_khach,sp=data.sp,gia=data.gia)
    db.add(khach)
    db.commit()
    return khach


@app.get("/xem_b2",response_model=list[shop_qlshop])
def xem_b2():
    khach=db.query(shop_ql).all()
    return khach



@app.get("/xem_b1_b2")
def xem_b1_2():
    tong_hop= db.query(shop_mana).options(joinedload(shop_mana.rela1)).all()
    
    return {"kq":[{"id":x.id,"ten_shop":x.ten_shop,"rela1":[{"id":i.id,"ten_khach":i.ten_khach,"sp":i.sp,"gia":i.gia,"shop_id":i.shop_id,"so_luong":i.so_luong } for i in x.rela1]}for x in tong_hop]}
                                                            #thêm id vào trong rela1 mục đích xem mỗi người có íd = mấy? tìm dữ liệu cho dễ



@app.delete("/xoa_loi")
def xoa (id:int):
    xoa=db.query(shop_ql).filter(shop_ql.id == id).first()
    db.delete(xoa)
    db.commit()
    return xoa




#CÁCH XÓA CÒN LƯU LỊCH SỬ XÓA
@app.delete("/lich_su_xoa")
def ls_xoa(shop_id:int):
    xoa= db.query(shop_ql).filter(shop_ql.shop_id == shop_id).all()
    if not xoa:
        return{"kq": "k có shop_id để xóa"}
    ds_lich_su=[]
    for x in xoa:
        lich_su= lich_su_xoa_db(shop_id=x.shop_id,ten_khach=x.ten_khach,so_luong=x.so_luong,sp=x.sp,gia=x.gia)
        db.add(lich_su)
        db.delete(x)
        ds_lich_su.append({"shop_id":x.shop_id,"ten_khach":x.ten_khach,"so_luong":x.so_luong,"sp":x.sp,"gia":x.gia})
    db.commit()
    ds_con_lai= db.query(shop_ql).all()
    return {"xoa":ds_lich_su ,"kq còn lại":ds_con_lai}
# lưu ý : tạo base lich_su_xoa_db mục đích chứa add kết quả xóa vào nơi đó ( lịch sư xóa)





# KHÔI PHỤC DS ĐÃ XÓA (POST)
@app.post("/khoi_phuc_xoa")
def ls_kp(shop_id:int):
    ls= db.query(lich_su_xoa_db).filter(lich_su_xoa_db.shop_id == shop_id).all()
    if not ls:
        raise HTTPException(status_code=404,detail="k có shop_id phù hợp để khôi phục")
    ds_khoi_phuc=[]
    for kp in ls:
        ds_kp=shop_ql(shop_id=kp.shop_id,ten_khach=kp.ten_khach,so_luong=kp.so_luong,sp=kp.sp,gia=kp.gia)
        db.add(ds_kp)
        ds_khoi_phuc.append({"shop_id":kp.shop_id,"ten_khach":kp.ten_khach,"so_luong":kp.so_luong,"sp":kp.sp,"gia":kp.gia})
        db.delete(kp)
    db.commit()
    return {"đã khôi phục":ds_khoi_phuc}

# Lưu ý : - LỖI TRƯỚC commit thì dung rollback khôi phục được 
#         - LỖI SAU commit k được dùng rollback mà dùng post để lấy lại dữ liệu đã xóa nếu dữ liệu xóa đó còn lưu lại lịch sử



@app.post("/them_so_luong")
def them_sl(shop_id:int,so_luong:int):
    sl= db.query(shop_ql).filter(shop_ql.shop_id == shop_id).all() # lấy all shop_id trùng để thêm đầu đủ số lượng vào mỗi người 
    for x in sl: # cho biến x chạy trong sl 
        x.so_luong = so_luong # gán giá trị biến x.so_luong = so_luong
    db.commit()
    return x


@app.get("/tim_sp/{id}",response_model=shop_qlshop)
def tim (id:int):
    tim= db.query(shop_ql).filter(shop_ql.id == id).first()
    if not tim:
        raise HTTPException(status_code=404,detail="k tìm thấy hs ")
    return tim


@app.post("/themsp_test",response_model=shop_qlshop)
def them_test(data:shop_qlshop):
    them= shop_ql(id=data.id,shop_id=data.shop_id,ten_khach=data.ten_khach,sp=data.sp,gia=data.gia,so_luong=data.so_luong)
    db.add(them)
    db.commit()
    if data.gia <0 :
        raise HTTPException(status_code=400,detail="giá k được âm")
    return them


@app.post("/kt_trung3",response_model=shop_qlshop)
def kt_trung3 (data:shop_qlshop):
    kt=db.query(shop_ql).filter(and_(shop_ql.shop_id == data.shop_id,shop_ql.sp == data.sp,shop_ql.ten_khach== data.ten_khach)).first()
    if kt:
        raise HTTPException(status_code=409,detail=" tên,id,sp bị trùng")

    them=shop_ql(shop_id=data.shop_id,sp=data.sp,ten_khach=data.ten_khach,so_luong=data.so_luong,gia=data.gia)   
    db.add(them)
    db.commit()
    return them


@app.put("/sua_gia_null/{id}",response_model=shop_qlshop)
def sua(id:int,gia:float):
    sua=db.query(shop_ql).filter(and_(shop_ql.id== id,shop_ql.gia==None)).first()
    if not sua:
        raise HTTPException(status_code=400,detail="k tìm thấy id phù hợp để sửa giá")
    sua.gia = gia
    db.commit()
    return sua


@app.put("/them_capnhat",response_model=shop_qlshop)
def cap_nhat(id:int,data:shop_qlshop):
    cn=db.query(shop_ql).filter(shop_ql.id == id).first()
    if not cn:
        raise HTTPException(status_code=404,detail=" k tìm thấy ìd phù hợp")
    cn.ten_khach = data.ten_khach
    cn.sp= data.sp
    cn.gia = data.gia
    cn.so_luong = data.so_luong
    db.commit()
    return cn


@app.delete("/xoa_sp/{id}",response_model=shop_qlshop)
def xoa_sp(id:int):
    xoa= db.query(shop_ql).filter(shop_ql.id == id).first()
    if not xoa:
        raise HTTPException(status_code=404,detail="k tìm thấy id để xóa")
    db.delete(xoa)
    db.commit()
    return xoa



@app.get("/tim_ten",response_model=list[shop_qlshop])
def tim (ten:str):
    tim= db.query(shop_ql).filter(shop_ql.ten_khach.ilike(f"%{ten}%")).all()
    if not tim:
        raise  HTTPException(status_code=404,detail=" k tìm thấy từ khóa tên hợp lệ ")
    return tim


@app.get("/tìm_gia",response_model=list[shop_qlshop])
def tim (gia:float):
    gia=db.query(shop_ql).filter(shop_ql.gia >= gia ).all()
    if not gia:
        raise ValueError(" giá k phù hợp")
    return gia



@app.get("/tim_nhieu",response_model=list[shop_qlshop])
def tim_nhieu(ten_khach:str |None = None, gia:float |None =None):
    nhieu= db.query(shop_ql).filter(or_(shop_ql.ten_khach.ilike(f"%{ten_khach}%"),shop_ql.gia==gia)).all()
    if not nhieu:
        raise HTTPException(status_code=404,detail=" k tìm thấy tên và giá thỏa dk ")
    return nhieu


@app.get("/phantrang")
def phan_trang (page:int,limit:int):
    pt = db.query(shop_ql).offset((page-1)*limit).limit(limit).all()
    return pt


@app.get("/all_sp",response_model=list[sp_all])
def sp_123 ():
    all =db.query(shop_mana.ten_shop,shop_ql.ten_khach,shop_ql.gia).join(shop_ql,shop_mana.id==shop_ql.shop_id).all()
    return all



                                # [dict(r._mapping) for r in loc ]
#lọc dữ liệu cách mới:
@app.get("/loc_sp_join/{gia}"   )
def loc(gia:float):
    loc= db.query(shop_mana.ten_shop,shop_ql.ten_khach,shop_ql.gia)\
        .join(shop_ql,shop_mana.id==shop_ql.shop_id)\
            .filter(shop_ql.gia >= gia).all()
    return [dict(r._mapping) for r in loc] 
#  [dict(r._mapping)for r in loc] : lấy từng Row(r) -> đổi thành dictionary{} -> trả về danh sách list[] chưa dict{}

#"\" : bắt buột phía sau không có khoản cách hoặc kí tự nào , nếu k muốn "\" có thể thay tuble() và bỏ "\"đi . Ví dụ loc=(db.query....all())

# mục đích sử dụng khi : query nhiều cột mà kq trả về là hàng(row) , muốn chuyển kq hàng(row) thành dạng DICT(response_model=list[])



#lọc dữ liệu cách cũ
@app.get("/loc_sp12/{gia}",response_model=list[sp_all])
def loc(gia:float):
    loc= db.query(shop_mana.ten_shop,shop_ql.ten_khach,shop_ql.gia).join(shop_ql,shop_mana.id==shop_ql.shop_id).filter(shop_ql.gia >= gia).all()
    return loc



@app.get("/tim_shop/{id}",response_model=list[tong_hop])
def timm(id:int):
    tim=db.query(shop_mana).filter(shop_mana.id == id).all()
    if not tim:
        raise HTTPException(status_code=404, detail="k tìm thấy shop")
    return tim


@app.get("/gia1/{gia}")
def gia_1 (gia:float):
    if gia <0:
        raise HTTPException(status_code=400,detail=" giá k dc âm")
    gia= (db.query(shop_ql).filter(shop_ql.gia >=gia).all())
    if not gia:
        raise HTTPException(status_code=400,detail=" dữ liệu k hợp lệ")
    return gia


@app.get("/k_co_quyen/{id}")
def quyen(id:int):
    if id != 1:
        raise HTTPException(status_code=403,detail=" chỉ có id = 1 mới được truy cập")
    return {"kq":" bạn được phép truy cập hợp lệ"}



@app.get("/sp_sp",response_model=list[shop_qlshop])
def sp1 (sp:str):
    sp= db.query(shop_ql).filter(shop_ql.sp == sp).all()
    if not sp:
        raise HTTPException(status_code=404,detail=" k tìm thấy sp")
    return sp  


0
@app.get("/chia/{a}/{b}")
def chia( a:float,b:float):
    try:
        x=a/b
        return {"kq":x}
    except ZeroDivisionError:
        raise HTTPException(status_code=400,detail=" k thế chia cho không")


    
@app.get("/test500")
def test():
    try:
        nam= db.query(shop_ql).all() #shop_123 để lấy ví dụ dữ liệu k có để bắt lỗi k có dữ liệu 
        return nam
    except Exception:
        raise HTTPException(status_code=500,detail=" lỗi sever khi truy vấn dữ liệu ( k có dữ liệu của shop) ")



