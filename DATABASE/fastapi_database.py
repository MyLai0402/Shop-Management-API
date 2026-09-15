#############################  PHẦN 4: FASTAPI KẾT NỐI DATABASE #############################################

                            # GET,FASTAPI KẾT NỐI DATABASE(get database ->Fastapi->json)
#from sqlalchemy import create_engine
#engine= create_engine("sqlite:///database.db")   # engine giúp SQLAICHEMY kết nối cụ thể database nào?  

#from sqlalchemy.orm import sessionmaker           #sessionmaker:tạo "khuôn " để tạo session 
#SessionLocal = sessionmaker (bind=engine)     #sessionLocal:tên đặt cho khuôn đó , bind= engine: session sử dụng cho engine nào, phiên làm việc với data
#db = SessionLocal()       # tạo 1 session thực thể thao tác dữ liệu 

#from sqlalchemy.orm import DeclarativeBase  #DeclarativeBase: nền của SQLAIchemy để tạo model
#class Base (DeclarativeBase):       #base: tên tự đặt 
  #pass  #pass: chưa có nội dung riêng 



#rom pydantic import BaseModel,ConfigDict
#from fastapi import FastAPI 
#app=FastAPI()
#from sqlalchemy.exc import IntegrityError
#from sqlalchemy.orm import Mapped,mapped_column
#class sinhvienmoi(Base):
 # __tablename__="sinhvienmoi"       #=>>>BẢNG DỮ LIỆU DATABASE 
  #id: Mapped[int] = mapped_column(primary_key=True)   #mapped :ánh xạ/ được liên kết với ...
  #ten:Mapped[str]
  #tuoi:Mapped[int]


#sv1= sinhvienmoi(id=1,ten='An',tuoi=20) #tạo dữ liệu 
#db.add(sv1) #đưa sv1 vào session chuẩn bị lưu
#db.commit() # lưu thay đổi vào database

#ds_sv=db.query(sinhvienmoi).all()
#for hs in ds_sv:
  #print(hs.id,hs.ten,hs.tuoi)

#class sinhvien_response(BaseModel):  # =>>>KHUÔN ĐỂ TRẢ DỮ LIỆU JSON (FASTAPI) ,LƯU Ý : CLASS NÀY "không lấy dữ liệu từ database"
  #id:int
  #ten:str
  #tuoi:int
  #model_config= ConfigDict(from_attributes=True) # nối với pydanatic (basemodel), được phép đọc tất cả dữ liệu như id, ten , v,v,v từ ọbject SQLAIchemy

#Base.metadata.create_all(engine) #lấy tất cả dữ liệu trên model đã khai báo trong base , rồi tạo những bảng tương ứng trong database thông qua engine



#try:
  #sv1= sinhvienmoi(id=2,ten='Bình',tuoi=22)
  #db.add(sv1)
  #db.commit()
  #print("thêm thành công")
#except IntegrityError :
  #db.rollback()
  #print(" lỗi id đã tồn tại") 


#ds_sv= db.query(sinhvienmoi).all() # xem lại kq dữ liệu tất cả trong bảng sinhvienmoi , muốn xem kq nhớ khóa comment dữ liệu ở trên cũ để tránh báo lỗi trùng dữ liệu
#for hs in ds_sv:
    #print(hs.id,hs.ten,hs.tuoi) 

# get database -> Fastapi -> Json 
#@app.get("/sinhvienmoi",response_model=list[sinhvien_response]) # RESPONSE_MODEL: QUY ĐỊNH DỮ LIỆU TRẢ VỀ CHO FASTAPI
#def get_svm():
  #ds_sv=db.query(sinhvienmoi).all() #=>>>LẤY DỮ LIỆU TỪ DATABASE
  #return ds_sv   

#post : nhận dữ liệu Fastapi -> lưu vào database 


                              #POST,FASTAPI+DATABASE ( post nhận dữ liệu từ fastapi -> database )


#from sqlalchemy import create_engine
#engine=create_engine("sqlite:///database.db")

#from sqlalchemy.orm import sessionmaker
#sessionLocal=sessionmaker (bind=engine)
#db = sessionLocal()

#from sqlalchemy.orm import DeclarativeBase
#class Base (DeclarativeBase):
  #pass

#from pydantic import BaseModel,ConfigDict
#from fastapi import FastAPI, HTTPException
#app=FastAPI()
#from sqlalchemy.orm import Mapped,mapped_column
#class post_database (Base):
  #__tablename__="post_database"
  #id:Mapped[int] = mapped_column(primary_key=True)
  #ten:Mapped[str]
  #tuoi:Mapped[int]

#class postinput(BaseModel):
  #id:int
  #ten:str
  #tuoi:int
#model_config= ConfigDict(from_attributes=True)


#Base.metadata.create_all(engine)


#sv= post_database(id=1,ten='Hải',tuoi=20)
#db.add(sv)
#db.commit()


#@app.post("/sinhvien",response_model=postinput) # vì class tạo chỉ có 1 hs nhập 1 session nên chỉ = postinput
#def them_sv(data :postinput):         # nhập nhận dữ liệu từ swagger

  #sv =post_database(id=data.id,ten=data.ten,tuoi=data.tuoi)
  #db.add(sv)
  #db.commit()
  #return sv

# sau khi nhập dữ liệu post nhận tại swagger và muốn xem chi 1 id :
#@app.get("/sinhvien/{id}",response_model=postinput) # sau khi nhập xong all dữ liệu post thì tạo get để xem dữ liệu post có thật sự vào bảng chưa?
#def get_sv_id(id:int):
  #sv=db.query(post_database).filter(post_database.id ==id ).first() # FIRST : SAU LỌC LẤY 1 DÒNG ĐẦU TIÊN 
  #if sv is None:
      #raise HTTPException(status_code=404,detail="k tìm thấy sinh viên")
  #return sv
  


# sau khi nhập dữ liệu post nhận tại swagger và muốn lấy all dữ liệu :
#@app.get("/sinhvien",response_model=list[postinput]) 
#def get_sv():   
  #ds_sv=db.query(post_database).all()
  #return ds_sv

                                #PUT + DATABASE
#from sqlalchemy import create_engine
#engine=create_engine("sqlite:///database.db")

#from sqlalchemy.orm import sessionmaker
#sessionLocal=sessionmaker (bind=engine)
#db= sessionLocal()

#from sqlalchemy.orm import DeclarativeBase
#class base (DeclarativeBase):
  #pass

#from fastapi import FastAPI,HTTPException
#app=FastAPI()

#from pydantic import BaseModel,ConfigDict

#from sqlalchemy.orm import Mapped, mapped_column
#class put_database (base):
 # __tablename__="sv_put"
  #id:Mapped[int] = mapped_column (primary_key=True)
  #ten:Mapped[str] =mapped_column()
  #tuoi:Mapped[int] =mapped_column()

#class swagger (BaseModel):
  #id:int
  #ten:str
 #tuoi:int
#model_Config = ConfigDict (from_attributes=True)

#base.metadata.create_all(engine)


#@app.post("/post_testput",response_model=swagger)
#def post_testput (data:swagger):
  #sv=put_database(id=data.id,ten=data.ten,tuoi=data.tuoi)
  #db.add(sv)
  #db.commit()
  #return sv

  
#@app.put("/put_put/{id}",response_model=swagger) # class swagger của fastapi nhận  dữ liệu đầu vào bên swagger và "TRẢ KỂU DỮ LIỆU NHƯ THẾ NÀO"
#def put_capnhat(id:int,data:swagger):
  #sv=db.query(put_database).filter(put_database.id == id).first()
  #if sv is None:
    #raise HTTPException (status_code=404,detail="k tìm thấy sv có id trong bảng ")
  #sv.ten=data.ten
  #sv.tuoi=data.tuoi
  #db.commit() # bài này k cần "db.add" vì đối tượng sv đã đang là dữ liệu trong database nên không cần add và ngược lại nếu đối tượng k nằm trong database thì "dùng add"
  #return sv # RETURN TRẢ CÁI DỮ LIỆU GÌ ?
# PHÂN BIỆT RETURN VÀ RESPONSE_MODEL Ở TRÊN 2#


                                #DELETE+ DATABASE

from sqlalchemy import create_engine
engine= create_engine ("sqlite:///database.db")

from sqlalchemy.orm import sessionmaker
sessionLocal = sessionmaker (bind=engine)
db = sessionLocal()

from sqlalchemy.orm import DeclarativeBase
class Base (DeclarativeBase):
  pass


from fastapi import FastAPI , HTTPException
from pydantic import BaseModel, ConfigDict
app= FastAPI()


from sqlalchemy.orm import Mapped, mapped_column
class delete_data (Base):
  __tablename__ ="delete_data"
  id:Mapped[int] = mapped_column (primary_key=True)
  ten:Mapped[str] =mapped_column ()
  tuoi:Mapped[int]  =mapped_column ()

class delete_test (BaseModel):
  id:int
  ten:str
  tuoi: int
model_Config = ConfigDict (from_attributes=True) 

Base.metadata.create_all(engine)


@app.post("/delete_test",response_model=delete_test)
def delete_post_test (data:delete_test):
  sv = delete_data(id=data.id,ten=data.ten,tuoi=data.tuoi)
  db.add(sv)
  db.commit()
  return sv


@app.get("/check_delete",response_model=list[delete_test])
def check_test ():
  return db.query(delete_data).all()


@app.delete("/delete_database/{id}",response_model=list[delete_test])
def delete_test(id:int):
  sv=db.query(delete_data).filter(delete_data.id == id).first()
  if sv is None:
    raise HTTPException(status_code=404,detail="k tìm thấy sv để xóa")
  db.delete(sv)
  db.commit()
  return  db.query(delete_data).all() 


                      #QUERY +DATABASE : 15 style
from sqlalchemy import engine
engine= create_engine ("sqlite:///database.db") 

from sqlalchemy.orm import sessionmaker
sessionLocal = sessionmaker(bind=engine)
db=sessionLocal()

from sqlalchemy import not_ , or_

from sqlalchemy.orm import Mapped,mapped_column
from pydantic import BaseModel,ConfigDict 
from fastapi import FastAPI,Query,HTTPException
app=FastAPI()

from sqlalchemy.orm import DeclarativeBase
class Base (DeclarativeBase):
  pass

class query_data(Base):
  __tablename__="query_data"
  id:Mapped[int] =mapped_column (primary_key=True)
  ten:Mapped[str] =mapped_column()
  tuoi:Mapped[int] =mapped_column()

class post_query (BaseModel):
  id:int
  ten:str
  tuoi:int
model_Config = ConfigDict(from_attributes=True)

Base.metadata.create_all(engine)


@app.post("/post_query",response_model=post_query)
def p_q (data:post_query):
  sv=query_data(id=data.id,ten=data.ten,tuoi=data.tuoi)
  db.add(sv)
  db.commit()
  return sv


#@app.get("/get_query",response_model=list[post_query])
#def g_q ():
  #return db.query(query_data).all()  


#@app.get("/get_query_filter",response_model=list[post_query]) # Lọc query theo dk 
#def get_query_filter(tuoi:int):
  #sv=db.query(query_data).filter(query_data.tuoi >= tuoi).all()
  #return sv


#app.get("/get_query_filter",response_model=list[post_query]) 
#def get_query_filter(tuoi:int):
  #sv=db.query(query_data).filter(query_data.tuoi == tuoi).all()
  #return sv




#@app.get("/get_query_filter",response_model=list[post_query]) 
#def get_query_filter(tuoi_max:int,tuoi_min:int):
  #sv=db.query(query_data).filter(tuoi_min <= query_data.tuoi , query_data.tuoi <= tuoi_max).all()
  #return sv
  

#@app.get("/get_query_filter",response_model=list[post_query]) 
#def get_query_filter(ten:str):
  #sv=db.query(query_data).filter(query_data.ten.ilike(f"%{ten}%")).all()
  #return sv

# Hàm ilike(): tìm chữ cái không phân biệt hoa hay thường
# f"%{ten}% : ten có chứa từ khóa(chữ cái), % : có lí tự trước hoặc sau đều được không bị lỗi  


#@app.get("/get_query_filter",response_model=list[post_query]) 
#def get_query_filter(ids:list[int]=Query(...)): #=query(): nối với Fastapi nhận ids từ URL query , vì lúc này ids:list[int] là một danh sách 
  #sv=db.query(query_data).filter(query_data.id.in_(ids)).all() #id.in(ids): id nào có trong ds thì lấy khác với max và min (max và min lấy khoản giữa dk )
  #return sv
#ids: tên dữ liệu nhận vào , bắt buột
#list[int]: danh sách số nguyên
#=Query(): nối với Fastapi nhận ids từ URL query , vì lúc này ids:list[int] là một danh sách 

#Mục đích IN_(): là lấy nhiều và những dữ liệu cần tìm đúng trong danh sách , khác với max và min lấy khoản x <=  N  <= x 

#GET+ dữ liệu đơn (tuoi,ten) -> Query
#GET +dữ liệu list -> Query(...)



#@app.get("/get_query_filter",response_model=list[post_query]) 
#def get_query_filter(ds_tuoi:list[int]=Query(...)): 
  #sv=db.query(query_data).filter(query_data.tuoi.in_(ds_tuoi)).all()
  #return sv


#@app.get("/get_query_filter",response_model=list[post_query]) 
#def get_query_filter(tuoi:int=Query(...)): 
  #sv=db.query(query_data).filter(not_(query_data.tuoi == tuoi)).all() 
                                #not_(query_data.tuoi==tuoi) : not_() loại ( tuổi nhập vào = tuổi có trong bảng database)
  #return sv



#@app.get("/get_query_filter",response_model=list[post_query]) 
#def get_query_filter(tuoi1:int=Query(...),tuoi2:int=Query(...)): 
  #sv=db.query(query_data).filter(or_(query_data.tuoi == tuoi1 ,query_data.tuoi== tuoi2)).all() # lấy 1 trong 2 dữ liệu
  #return sv


#@app.get("/get_query_filter",response_model=list[post_query]) 
#def get_query_filter(): 
  #sv=db.query(query_data).order_by(query_data.tuoi).all() # order_by : sx tăng dần 
  #return sv


#@app.get("/get_query_filter",response_model=list[post_query]) 
#def get_query_filter(): 
  #sv=db.query(query_data).order_by(query_data.tuoi.desc()).all() # order_by ... desc(): sx dữ liệu giảm dần
  #return sv


#@app.get("/get_query_filter",response_model=list[post_query]) 
#def get_query_filter(): 
  #sv=db.query(query_data).limit(2).all() # limit(): giới hạn , lấy dữ liệu sau khi query và lấy đầu tiên kq của query xuống ( lấy top2 ,3, 4)
  #return sv



#@app.get("/get_query_filter",response_model=list[post_query]) 
#def get_query_filter(): 
  #sv=db.query(query_data).offset(1).limit(2).all() # ofset: bỏ qua từ đầu danh sách  , limit(): giới hạn , lấy tiếp theo phần bỏ qua
  #return sv


#@app.get("/get_query_filter",response_model=list[post_query]) 
#def get_query_filter(page:int=Query(1),limit:int=Query(2)): 
  #sv=db.query(query_data).offset((page-1)*limit).limit(limit).all() 
  #return sv
# công thức tính offset=(page-1)*limit


#@app.get("/get_query_filter",response_model=list[post_query]) 
#def get_query_filter(ten:str=Query(),tuoi:int=Query()): 
  #sv=db.query(query_data).filter(query_data.ten.ilike(f"%{ten}%") , query_data.tuoi == tuoi).all() # lọc 2 dk: tên chứa từ khóa và tuổi
  #if not sv:
    #raise HTTPException(status_code=404,detail="k tìm thấy sv")
  #return sv   



# response sd khi kq trả về đối tượng hoạc ds như ds table hiện có , 
# trường hợp trả về "con số" thì có thể bỏ hoặc sd respone thì "tạo 1 class mới" 
# Mục đích :để response nhận class đó  và class đó "phải có cấu trúc như kq trả"
#@app.get("/get_query_filter") 
#def get_query_filter_dem(tuoi:int=Query()): 
  #sv=db.query(query_data).filter( query_data.tuoi == tuoi).count()
  #return {"số lượng": sv} 



#@app.get("/get_query_filter",response_model=list[post_query]) 
#def get_query_filter_dem(ten:str=Query(),tuoi:int=Query(),limit:int |None = None): 
  #sv=db.query(query_data).filter(query_data.ten.ilike(f"%{ten}%"), query_data.tuoi >=tuoi).order_by(query_data.tuoi).limit(limit).all()
  #return sv


#@app.get("/get_query_filter",response_model=list[post_query]) 
#def get_query_filter(ten:str=Query,tuoi:int=Query,offset:int |None=None,limit:int |None=None): 
  #sv=db.query(query_data).filter(query_data.ten.ilike(f"%{ten}%"),query_data.tuoi >= tuoi).offset(offset).limit(limit).all()
  #return sv


  