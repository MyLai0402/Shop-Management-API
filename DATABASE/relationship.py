

                #LÀM LẠI VBAIF RELATIONSHIP + 6 DẠNG RELATIONMSHIP()

from sqlalchemy import create_engine
engine = create_engine ("sqlite:///./relationship.db")

from sqlalchemy.orm import sessionmaker
sessionLocal = sessionmaker (bind =engine)
db= sessionLocal()

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

from sqlalchemy.orm import session

from sqlalchemy import or_

from sqlalchemy import select, func



from fastapi import FastAPI,Depends,HTTPException 
app=FastAPI()

from sqlalchemy.orm import relationship,joinedload

from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy import ForeignKey

from pydantic import BaseModel,ConfigDict

from sqlalchemy.orm import DeclarativeBase
class Base (DeclarativeBase):
    pass

class my_pham_1 (Base):
    __tablename__="nguoi_dung"
    id:Mapped[int] = mapped_column (primary_key=True)
    ten: Mapped [str] =mapped_column ()
    rela1 = relationship("my_pham_3",back_populates="rela2")


class my_pham_3 (Base):
    __tablename__="mypham"
    id:Mapped[int] =mapped_column (primary_key=True)
    paid_id: Mapped[int] =mapped_column (ForeignKey ("nguoi_dung.id") )
    ten_sp :Mapped[str] =mapped_column ()
    gia: Mapped[int] = mapped_column ()
    rela2 =relationship("my_pham_1",back_populates="rela1")


class my_pham_2 (BaseModel):
    id:int
    ten:str

model_Config = ConfigDict(from_attribute=True)


class my_pham_4 (BaseModel): # không cần thêm id vì khi cho giá trị nối thì database sẽ tự cho stt id 
    paid_id: int 
    ten_sp:str
    gia:int

model_Config = ConfigDict(from_attribute=True)


class mp1_mp3 (BaseModel):
    id:int
    ten:str
    rela1:list[my_pham_4] =[] # rela1 bắt buột giống tên relationship ở trên mới ra được kq dữ liệu mỗi sv ,
                               #còn nếu tên relationship k trùng thì sẽ ra kq [] rỗng 
model_Config=ConfigDict(from_attributes=True)

Base.metadata.create_all(engine)


@app.post("/my_pham_1",response_model=my_pham_2)
def m_p (data:my_pham_2):
    sv= my_pham_1(id=data.id,ten=data.ten)
    db.add(sv)
    db.commit()
    return sv

@app.post("/my_pham_3",response_model=my_pham_4)
def my_pham_3t (data:my_pham_4):
    sv= my_pham_3(paid_id=data,ten_sp=data.ten_sp,gia=data.gia)
    db.add(sv)
    db.commit()
    return sv 

@app.get("/mp1_mp3")
def relationship_join():
    sv=db.query(my_pham_1).options(joinedload(my_pham_1.rela1)).all()
    return {"kq":[{"ID":x.id,"ten":x.ten,"rela1":[{"ten_sp":i.ten_sp,"gia":i.gia}for i in x.rela1]}for x in sv]}
    #có 2 cách trả return :
    #cách1 : như trên trả dict 
    #cách 2: trả return sv ( cần response_model, khi trả có để lại lịch sử paid_id , trả theo response an toàn hơn )
    # cả 2 cách đều cần dùng relationship 

@app.get("/mp1_mp3_2",response_model=mp1_mp3)
def relationship_join(id:int):
    sv=db.query(my_pham_1).options(joinedload(my_pham_1.rela1)).filter(my_pham_1.id == id).first()
    return sv

@app.get("/tim_sp_tu_khoa/{ten}",response_model=list[mp1_mp3])
def tim_tu_khoa (ten:str,db:session = Depends(get_db)):
    sv=db.query(my_pham_1).options(joinedload(my_pham_1.rela1)).filter(my_pham_1.ten.ilike(f"%{ten}%")).all() #dữ liệu ở filter quyết định tìm từ khóa có chứa dữ liệu trong bảng đó 
    if not sv:
        raise HTTPException(status_code=404,detail="k tìm thấy sp ")
    return sv



@app.get("/tim_tk_2bang/{ten}",response_model=list[mp1_mp3])
def tim_tu_khoa (ten:str,db:session = Depends(get_db)):
    sv=db.query(my_pham_1).join(my_pham_1.rela1).options(joinedload(my_pham_1.rela1)).filter(or_(my_pham_1.ten.ilike(f"%{ten}%"),my_pham_3.ten_sp.ilike(f"%{ten}%"))).all() 
                        #JOIN: là nơi tìm dữ liệuTRUY VẤN / LỌC DỮ LIỆU 
                        #JOINEDLOAD = JOIN nhưng dùng để nạp dữ liệu relationship lấy và trả kq nó ra
    if not sv:
        raise HTTPException(status_code=404,detail="k tìm thấy sp ")
    return sv




@app.get("/tim_son/{ten}",response_model=list[mp1_mp3])
def tim_tu_khoa (ten:str,db:session = Depends(get_db)):
    sv=db.query(my_pham_1).join(my_pham_1.rela1).filter(or_(my_pham_1.ten.ilike(f"%{ten}%"),my_pham_3.ten_sp.ilike(f"%{ten}%"))).all() 
                        #JOIN: là nơi tìm dữ liệu TRUY VẤN / LỌC DỮ LIỆU 
                        #JOINEDLOAD = JOIN nhưng dùng để nạp dữ liệu relationship lấy và trả kq nó ra
    if not sv:
        raise HTTPException(status_code=404,detail="k tìm thấy sp ")
    return sv



                        #  Trước lúc xóa id trùng trong bảng Foreign thì mở ra xem đúng số lần nhập vào 
                        # lưu ý xóa id bảng my_pham_3 tức là bảng phụ , chi chọn id số lần nhập bên tronmg mỗi người 
                        # tránh tưởng rằng xóa id mỗi người có trong bảng 

@app.get("/xem_all")
def xem_all (db:session =Depends(get_db)):
    sv = db.query(my_pham_1).all()
    for x in sv:
        print({"id":x.id,"tên":x.ten})
        for xx in x.rela1:
            print (xx.id,xx.paid_id,xx.ten_sp,xx.gia)
    return sv



                        # XÓA TRONG BẢNG FOREIGNKEY (PHỤ)
                        # Cách xóa dữ liệu khi nhập 1 dữ liệu trùng nhiều lần 
                        # chỉ áp dụng khi bị trùng và nhập lại nhiều lần , nếu dữ liệu trùng nhưng tách 2 giá trị riêng biệt thì k nên xóa 
                        # nên tạo 1 enpoin riêng để xóa cho an toàn 
                        # áp dụng cho khóa phụ Foreign_key , áp dụng cho dữ liệu bên trong 

@app.get("/xoa_sp/{id}")
def xoa_sp(id:int,db:session =Depends (get_db)):
    xoa = db.query(my_pham_3).filter(my_pham_3.id == id).first()
    if not xoa:
        raise HTTPException(404, " k tìm thây id")
    db.delete(xoa)
    db.commit()
    return{"xoa":"đã xóa"}



                #DISTINCT() : TRÁNH TRÙNG DỮ LIỆU (CHỈ XÓA TRONG KHÓA CHÍNH PRIMARY_KEY)
                #  distinct chỉ tranh lỗi trùng trong bảng query khóa chính , k liên quan tránh trùng trong bảng phụ my_pham_3)
                # chỉ dùng khi 1 dữ liệu nhưng lỡ nhập 2 lần , còn nếu trùng tên  nhưng 2 dữ liệu mang giá trị  khác nhau thì k nên dùng distinct 
                # khác với xóa foreign_key ở trên           
@app.get("/tranh_trung_distinct",response_model=list[str])
def distinct_trung (db:session =Depends(get_db)):
    sv=db.query(my_pham_1.ten).join(my_pham_1.rela1).filter(my_pham_3.ten_sp=="son").distinct().all()
    return [x[0] for x in sv]


                                    #NỐI DK 2 BẢNG: 2 cách viết 
                                    # cách 1 : SQL THUẦN 
                                    # CÁCH 2: SQLALCHEMY


# cách 1 : SQL THUẦN 
#import sqlite3
#conn=sqlite3.connect("relationship.db")
#conn.commit()

#khi viết SQL thuần(dấu hiệu: cursor.execute) thì dùng tên tablename trên class , k được dùng tên class 
#lúc này SQL nói chuyên trực tiếp database
# khi viết SQLALCHEMY ORM khi ứng dụng fastapi của mình đã dùng model + session (dấu hiệu: sv= select(path_data),result = db.execute(stmt)) lúc này dùng tên của class/model
#cursor = conn.cursor()
#result = cursor.execute("""SELECT nguoi_dung.ten, mypham.gia  # ng_dung và mypham lấy tên từ tablename
                        #FROM nguoi_dung                      
                        #JOIN mypham
                        #ON nguoi_dung.id = mypham.paid_id
                        #WHERE nguoi_dung.ten = "Lâm" AND mypham.gia > 50 """).fetchall()
#print (result)


# công thức xem tên bảng thật tablename hoặc kéo lên class xem 
#cursor =conn.cursor()
#result = cursor.execute(""" SELECT name FROM sqlite_master WHERE type ='table' """).fetchall()
#print (result) 


#CÁCH 2 :SQLALCHEMY
# nhớ import select 
#khi viết sqlchemy sd tên class/ model để lấy dữ liệu 

#stmt = (select(my_pham_1.ten,my_pham_3.gia).join(my_pham_3).where(my_pham_1.ten =='Lâm',my_pham_3.gia >50))
# my_pham_1 và my_pham_3 lấy tên từ class /model
#result = db.execute(stmt).all() # thực thi chạy stmt

#print (result)


                                # SQLALCHEMY + COUNT +GROUP_BY
#  import thêm func (function: hàm ) để đếm count hoặc max,min ,vv.vvv.. khi hàm count hay ham khác lỗi thêm func đế tính toán
# bài này dùng đến func vì k còn để lọc thôi mà còn để tính toán dữ liệu 
stmt = (select (my_pham_1.ten,(func.count(my_pham_3.ten_sp))).join(my_pham_3).group_by(my_pham_1.ten))

result = db.execute(stmt).all()
print (result)

                                 # SQLALCHEMY + SUM +GROUP_BY

stmt = (select(my_pham_1.ten,func.sum(my_pham_3.gia)).join(my_pham_3).group_by(my_pham_1.ten))
result = db.execute(stmt).all()
print(result)


                                # SQLALCHEMY + AVG +GROUP_BY     
stmt = (select(my_pham_1.ten,func.avg(my_pham_3.gia)).join (my_pham_3).group_by(my_pham_1.ten))   
result = db.execute(stmt).all()
print(result)                