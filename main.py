from fastapi import FastAPI
name = FastAPI()
@name.get("/")

def home():
    return{"message":"Xin chào Bé Mỹ"}

@name.get("/about")
def hello():
    return{"message":"Tôi đang học Fastapi"}
@name.get("/hello/{ten}")
def hello(ten):
    return{"message":f"xin chào{ten}"}  
@name.get("/hoc")
def hoc(monhoc):
    return{"message":f"tôi đang học{monhoc}"}
@name.get("/nguoi")
def nguoi(ten,tuoi):
    return {"ten":ten,"tuoi":tuoi}
@name.get("/hocsinh")
def hocsinh(ten:str,tuoi:int):
    return{"ten":ten,"tuoi":tuoi}
@name.get("/lophs")
def lophs(ten:str,tuoi:int=18,lop:str="12A1"):
    return{"ten":ten,"tuoi":tuoi,"lop":lop}
@name.get("/hocsinh/{id}")
def hsid(id:int,ten:str):
    return{"id":id,"ten":ten}
@name.get("/product")
def product(name:str,price:int):
    return{"name":name,"price":price}
@name.get("/nhanvien")
def nhanvien(ten:str,tuoi:int,luong:int,phong:str|None=None):
    return{"ten":ten,"tuoi":tuoi,"luong":luong,"phong":phong}    
@name.post("/hello")
def hello():
    return{"message":"xin chào Bé Mỹ"}    
from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class diem(BaseModel):
    ten:str
    diem:float
    hanhkiem:str
@app.post("/xeploai")
def tao_diem(data:diem):
    if data.diem>=8 or data.hanhkiem =="Tốt":
        kq= "khen Thưởng"
      
    else:
       kq="không khen thưởng"
    return{"ten":data.ten,"diem":data.diem,"hanhkiem":data.hanhkiem,"ketqua":kq}       
class dulieu(BaseModel):
    Hoc_sinh:hocsinh
class hocsinh(BaseModel):
    ds_ten:list[str]
    ds_diem:list[float]
@app.post("/dsdiem")
def diem (data:hocsinh):
    dsmoi1=[]
    dsmoi2=[]
    kq=[]
    for ten in data.ds_ten:
        dsmoi1.append(ten)
        print(dsmoi1)
    for diem in data.ds_diem:
        dsmoi2.append(diem)
        print(dsmoi2)
    for ten,diem in zip(dsmoi1,dsmoi2):
        kq.append([ten,diem])
    print(kq)
    return kq
class diem_TB(BaseModel):
    ds_diem:list[float]
@app.post("/diemtb")
def diem_tb(data:diem_TB):
    tong=0
    dem=0
    for diem in data.ds_diem:
       
        tong += diem
        dem += 1
        diemtrungbinh=tong/dem
    print (diemtrungbinh)
    return{"diemtrungbinh":diemtrungbinh}
class HocSinh(BaseModel):
    ds:list[list]
@app.post("/hoc_sinh")
def hoc_sinh(data:HocSinh):
    tong=0
    for mon,diem in data.ds:
        tong+=diem
    print(tong)
    return tong
class hs(BaseModel):
    ten:str
    diem:dict
@app.post("/hs_dict")
def hs_dict(data:hs):
    print(data.diem["toan"])
    return data.diem["toan"]
class ten_lop(BaseModel):
    ds_diem:list[float]
class hs_nested(BaseModel):
    ten:list[str]
    ten_lop:ten_lop
@app.post("/nested")
def dict_nested(data:hs_nested):
    kq=[]
    for ten,diem in zip(data.ten,data.ten_lop.ds_diem):
        kq.append([ten,diem])
        print(kq)
    return kq

class SanPham(BaseModel):
    ten:str
    gia:int
class dssp(BaseModel):
    sanpham:list[SanPham]
@app.post("/sp")
def sp (data:dssp):
    dem=0
    tong=0
    for sp in data.sanpham:
        dem+=1
        tong += sp.gia
    return{"Tổng sp":dem,"Tổng Tiền":tong}
class mypham(BaseModel):
    ten:str
    soluong:int
class donhang(BaseModel):
    mypham:list[mypham]
@app.post("/mypham")
def dh_mypham(data:donhang):
    dem=0
    tong=0
    for sp in data.mypham:
        dem+=1
        tong+= sp.soluong
    return{"Tổng dh":dem,"Tổng giá":tong}
class thucung(BaseModel):
    ten:str
    tuoi:int
class ds_thucung(BaseModel):
    thucung:list[thucung]
@app.post("/thucung")
def thucung(data:ds_thucung):
    dem=0
    tong=0
    for i in data.thucung:
        dem +=1
        tong+= i.tuoi
    return{"Tổng thú cưng":dem,"Tổng tuổi":tong}
class sanpham(BaseModel):
    ten:str
    gia:int
class ten_cua_hang(BaseModel):
    ten_CH:str
    mypham:list[sanpham]
@app.post("/cuahang_ngao")
def cuahang_ngao(data:ten_cua_hang):
    dem=0
    tong=0
    for i in data.mypham:
        dem+=1
        tong+=i.gia
    return{"tên cửa hàng":data.ten_CH,"tổng mỹ phẩm":dem,"tổng giá":tong}
class mypham(BaseModel):
    ten:str
    gia:int
class chu_shop(BaseModel):
    ten:str
    tuoi:int
class cuahang(BaseModel):
    ten_CH:str
    shop:chu_shop
    sanpham:list[mypham]
@app.post("/CH_ngao")
def CH_Ngao(data:cuahang):
    dem=0
    tong=0
    for i in data.sanpham:
        dem+=1
        tong+=i.gia
    return{"tên cửa hàng":data.ten_CH,"Tên chủ shop":data.shop.ten,"SL mỹ phẩm":dem,"Tổng giá":tong}
class sanpham(BaseModel):
    ten:str
    gia:int
class khachhang(BaseModel):
    ten:str
    sdt:str
class donhang(BaseModel):
    ma_don:int
    khach:khachhang
    sp:list[sanpham]
@app.post("/donhangkhach")
def dhkhach(data:donhang):
    dem=0
    tong=0
    for i in data.sp:
        dem+=1
        tong+=i.gia
    return{"mã đơn":data.ma_don,"tên khách":data.khach.ten,"SLSP":dem,"Tổng giá":tong}  
class giaovien(BaseModel):
    ten:str
    tuoi:int
class truonghoc(BaseModel):
    ten_lop:str
    gv:giaovien
@app.post("/giaovien")
def giaovien_day(data:truonghoc):
    return{"Tên lớp":data.ten_lop,"Tên giáo viên":data.gv.ten}
class hoc_sinh(BaseModel):
    ten:str
    tuoi:int
class truonghoc(BaseModel):
    hs:list[hoc_sinh]
    tenlop:str
@app.post("/hs_truonghoc")
def hs_truonghoc(data:truonghoc):
    dem=0
    for i in data.hs:
        dem +=1
    return{"tên lớp":data.tenlop,"Số hs":dem}
class hoc_sinh(BaseModel):
    ten:str
    tuoi:int
class lop_hoc(BaseModel):
    ten_lop:str
    hs:list[hoc_sinh]
class truong(BaseModel):
    ten_truong:str
    lophoc:lop_hoc
@app.post("/truongdaynghe")
def truongdaynghe(data:truong):
    for i in data.lophoc.hs:
        len(data.lophoc.hs)
    return{"Tên trường":data.ten_truong,"Tên Lớp":data.lophoc.ten_lop,"số HS":len(data.lophoc.hs)}   
class hs(BaseModel):
    ten:str
    tuoi:int
    email:str |None=None
@app.post("/hs_hs")
def hs_hs(data:hs):
    return{"Tên":data.ten,"email":data.email}

class ds_hoc_sinh(BaseModel):
    
    ds_diem:list[float]
   
class xep_loai(BaseModel):
    ten_lop:str
    dshs:list[ds_hoc_sinh]
@app.post("/xeploai")
def xeploai(data:xep_loai):
    tong=0
    dem=0
    kq=[]
    diemtb=0
    for k in data.dshs:
        for v in k.ds_diem:
            tong+=v
            dem+=1
            diemtb =tong/dem
        if diemtb>=8:
            xeploai="Giỏi"
        elif diemtb>=6.5:
            xeploai="khá"
        else:
            xeploai="TB"
        kq.append({"Tên":k.ten,"Điểm":diemtb,"Loại":xeploai})
    return{"Tên lớp":data.ten_lop,"kết quả":kq}

class mypham(BaseModel):
    ten:str
    gia:float
class tenkhach(BaseModel):
    ten_kh:str
    sp: list[mypham]
@app.post("/mypham_kh")
def mypham_kh(data:tenkhach):
    tong=0
    for i in data.sp:
        tong+= i.gia
    return{"Ten khach":data.ten_kh,"tong gia":tong}

class ds_sp(BaseModel):
    ten:str
    gia:float
class ds_don_hang(BaseModel):
    ten_don:str
    dssp:list[ds_sp]
class khach(BaseModel):
    ten_kh:str
    dsdh:list[ds_don_hang]
@app.post("/dsdh_kh")
def kh_my(data:khach):
    tong_don=0
    tong_ten=0
    tong_gia=0
    for i in data.dsdh:
        tong_don +=1
        for k in i.dssp:
            tong_ten+=1
            tong_gia+= k.gia
    return{"tong don":tong_don,"tong sp":tong_ten,"Tong gia":tong_gia}

class ds_hoc_sinh(BaseModel):
    ten:str
    diem:float
class ds_my(BaseModel):
    ten_lop:str
    dshs:list[ds_hoc_sinh]
@app.post("/ds_my")
def danhsach(data:ds_my):
    tong=0
    dem=0
    dtb =0
    dem_dsdau=0
    for i in data.dshs:
        tong += i.diem
        dem +=1
        dtb = tong/dem
        if dtb >= 5:
            dem_dsdau += 1
        else:
            print("khong dau")
    return{"ten lop":data.ten_lop,"Tong diem":tong,"Diem tb":dtb,"HS dau":dem_dsdau}

class ds_sp(BaseModel):
    ten: str
    gia:float
class ds_mua(BaseModel):
    ten_khach:str
    dssp:list[ds_sp]
@app.post("/dssp_mp")
def dssp_mp(data:ds_mua):
    tong=0
    dem=0
    for i in data.dssp:
        tong += i.gia
        dem +=1
    return{"Tên khách":data.ten_khach,"Tổng":tong,"Đếm":dem}

class monhoc(BaseModel):
    ten_mon:str
    diem: float
class Hocsinh(BaseModel):
    tenhs:str
    ds_mon:list[monhoc]
class lophoc(BaseModel):
    tenlop:str
    ds_hoc_sinh:list[Hocsinh]
@app.post("/monhoc_hs")
def monhoc(data:lophoc):
    ds=[]
    for i in data.ds_hoc_sinh:
        print("Tenhs:",i.tenhs)
        for k in i.ds_mon:
            print("Ten hs:",i.tenhs,"Tenmon:",k.ten_mon)
            if k.diem>=8:
                print("Ten:",i.tenhs,"Mon:",k.ten_mon,"Diem:",k.diem)
                ds.append({"Ten":i.tenhs,"Mon":k.ten_mon,"Diem":k.diem})

    return ds

class ds_mon(BaseModel):
    ten_mon:str
    diem:float
class ds_hoc_sinh(BaseModel):
    tenhs:str
    dsmon:list[ds_mon]
class list_hs(BaseModel):
    tenlop:str
    dshs:list[ds_hoc_sinh]
@app.post("/list_hs)")
def list_hs(data:list_hs):
    tong=0
    max_diem=0
    max_tenhs= ""
    max_mon= ""
    for i in data.dshs:
        for k in i.dsmon:
            tong += k.diem
            print("Ten:",i.tenhs,"Tong:",k.diem)
            if k.diem > max_diem:
                max_diem=k.diem
                max_tenhs= i.tenhs
                max_mon=k.ten_mon
            else:
                print("Khong dat")
    return {"Max_ten":max_tenhs,"Max_mon":max_mon,"max_diem":max_diem}

class dsmon(BaseModel):
    ten_mon:str
    diem:float
class ds_hs(BaseModel):
    tenhs:str
    ds_mon:list[dsmon]
class max_tong(BaseModel):
    tenlop:str
    dshs:list[ds_hs]
@app.post("/max_tong")
def max_tong(data:max_tong):
    max_tong=0
    max_diem=0
    max_mon=""
    max_tenhs=""
    ds=[]
    for i in data.dshs:
        tong=0
        for v in i.ds_mon:
            tong += v.diem
        if tong > max_tong:
                max_tong= tong
                max_mon =v.ten_mon
                max_tenhs= i.tenhs
                ds.append({"tenhs":max_tenhs,"tong":max_tong})
    return {"ds":ds}

class dsmon(BaseModel):
    ten_mon:str
    diem:float
class dshs(BaseModel):
    tenhs:str
    ds_mon:list[dsmon]
class tonghop(BaseModel):
    tenlop:str
    ds_hs:list[dshs]
@app.post("/tonghop")
def tonghop(data:tonghop):
    dem =0
    max_dtb=0
    min_dtb=999
    min_ten="" 
    max_ten=""
    ds=[]
    tong=0
    dtb =0
    for k in i.ds_mon:
        tong +=k.diem
        dtb = tong/len(i.ds_mon)
        if k.diem < 5:
            dem += 1
            ds.append({"dem":dem,"tenmon":k.ten_mon})
    if dtb > max_dtb:
        max_dtb = dtb
        max_ten=i.tenhs
    if dtb < min_dtb:
        min_dtb = dtb
        min_ten= i.tenhs    
    return{"ten hs cao nhat":max_ten,"diemmax":max_dtb,"ten hs diem nho nhat":min_ten,"diem":min_dtb,"tong so mon duoi 5":ds}

class ds_mon (BaseModel):
    ten_mon:str
    diem:float
class ds_hs(BaseModel):
    tenhs:str
    ds_mon:list[ds_mon]
class tim_max(BaseModel):
    tenlop:str
    dshs:list[ds_hs]
@app.post("/tim_max")
def tim_max (data:tim_max):
    max_diem=0
    max_ten= "" 
    max_mon=""
    for i in data.dshs:
        for k in i.ds_mon:
            if k.diem> max_diem:
                max_diem= k.diem
                max_ten= i.tenhs
                max_mon=k.ten_mon
    return{"TEN":max_ten,"DIEM":max_diem,"MON":max_mon}

class ds_mon(BaseModel):
    ten_mon:str
    diem:float
class dshs(BaseModel):
    tenhs:str
    ds_mon:list[ds_mon]
class tim_min(BaseModel):
    tenlop:str
    ds_hs:list[dshs]
@app.post("/tim_min")
def tim_min(data:tim_min):
    min_diem= 999
    min_ten="" 
    min_mon=""
    for i in data.ds_hs:
        for k in i.ds_mon:
            if k.diem < min_diem:
                min_diem=k.diem
                min_ten=i.tenhs
                min_mon=k.ten_mon
    return {"DIEM":min_diem,"TEN":min_ten,"MON":min_mon}

class ds_mon(BaseModel):
    ten_mon:str
    diem:float
class ds_hs(BaseModel):
    tenhs:str
    dsmon:list[ds_mon]
class tong (BaseModel):
    tenlop:str
    dshs:list[ds_hs]
@app.post("/tong")
def tong (data:tong):
    max_dtb= 0
    max_ten="" 
    
    for i in data.dshs:
        tong =0
        
        for k in i.dsmon:
            tong+= k.diem
            
            dtb = tong/len(i.dsmon)
            if dtb >max_dtb:
                max_dtb=dtb
                max_ten=i.tenhs
    return {"DTB":max_dtb,"TEN":max_ten}

class dsmon(BaseModel):
    ten_mon:str
    diem:float
class dshs(BaseModel):
    tenhs:str
    ds_mon:list[dsmon]
class dem_mon(BaseModel):
    tenlop:str
    ds_hs:list[dshs]
@app.post("/dem_mon")
def dem_mon(data:dem_mon):
    ds=[]
    for i in data.ds_hs:
        dem=0
        for k in i.ds_mon:
            if k.diem<5:
                dem+=1
        ds.append({"TEN":i.tenhs,"Tổng số môn dưới 5":dem,})
    return ds
      
class ds_mon(BaseModel):
    ten_mon:str
    diem:list[float]
class ds_hoc_sinh(BaseModel):
    ten:str
    dsmon:list[ds_mon]
class tinh_max(BaseModel):
    ten_lop:str
    dshs:list[ds_hoc_sinh]
@app.post("/tinh_max")
def tinh_max(data:tinh_max):
    max_diem=0
    max_ten=""
    max_mon=""
    
    for i in data.dshs:
        ds=[]
        for k in i.dsmon:
            for v in k.diem:
                if v >max_diem:
                    max_diem=v
                    max_ten=i.ten
                    max_mon=k.ten_mon
        ds.append({"ten":max_ten,"diem":max_diem,"mon":max_mon})
    return ds

from fastapi import FastAPI
from pydantic import BaseModel,Field
app =FastAPI()
class Sanpham(BaseModel):
    ten:str=Field(min_length=3)
    gia:float=Field(gt=0)
@app.post("/sanpham")
def tao_san_pham(sp:Sanpham):
    return{"ten":sp.ten,"gia":sp.gia}

from pydantic import BaseModel ,Field, field_validator
app = FastAPI()
class Hocsinh(BaseModel):
    diem:list[float]     
    @field_validator("diem")
    def check_diem(cls,diem):
        dsloi=[]
        for i in diem:
            if i >10 or i <0:
                dsloi.append(i)
        if len(dsloi)>0:
            raise ValueError(f"{dsloi}không hợp lệ")
            return diem
@app.post("/hocsinh")
def kt_diem(ds:Hocsinh):
    return {"DIEM":ds.diem}

from pydantic import BaseModel, Field, field_validator 
app=FastAPI()
class Hocsinh(BaseModel):
    diem:list[float]     
    @field_validator("diem")
    def check_diem(cls,diem):
        dsdiem=[]
        for i in diem:
            if 0<i<10:
                dsdiem.append(i)
        return dsdiem
@app.post("/hocsinh")
def kt_diem(ds:Hocsinh):
    return {"DIEM":ds.diem}   

from pydantic import BaseModel, Field, field_validator 
app=FastAPI()
class Hocsinh (BaseModel):
    diem:list[float]
    @field_validator("diem")
    def check_diem(cls,diem):
        dsloi=[]
        if len(diem)==0:
            raise ValueError("bi rong")
        for i in diem:
            if i<0 or i>10:
                dsloi.append(i)
                if len(dsloi)>0:
                    raise ValueError(f"{dsloi}khong hop le")
        return diem
@app.post("/hs_diem")
def Kt_diem(ds:Hocsinh):
    return ds.diem



from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class Timhocsinh(BaseModel):
    ten:str
dshs=["lan","ngoc","quynh"]
@app.post("/timhs")
def Timhs(ds:Timhocsinh):
    dsten=[]
    if ds.ten not in dshs:
        dsten.append(ds.ten)
        raise HTTPException(status_code=404,detail=f"{dsten} k tim thay")
    return ds.ten

from fastapi import FastAPI
from pydantic import BaseModel,Field,field_validator
class Hocsinh(BaseModel):
    ten:str
    @field_validator("ten")
    def check_ten(cls,ten):
        if len(ten)<3:
            raise ValueError("khong hop le")
        return ten
@app.post("/check_ten")
def check_ten(ds:Hocsinh):
    return ds.ten


from fastapi import FastAPI
from pydantic import BaseModel,Field, field_validator
class check_tuoi(BaseModel):
    tuoi:int
    @field_validator("tuoi")
    def check_tuoi(cls,tuoi):
        if tuoi <18 or tuoi>60:
            raise ValueError("khong hop le")
        return tuoi
@app.post("/check_tuoi")
def check_tuoi(ds:check_tuoi):
    return ds.tuoi

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class check_hs(BaseModel):
    id:int
dsid=[2,3,4]
@app.get("/chekc_hs/{id}")
def check_hs(id:int):
    if id != 1:
        raise HTTPException(status_code=404,detail="khong tim thay hoc sinh")
    return id


from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field, field_validator
app=FastAPI()
class check_diem(BaseModel):
    diem:float
    @field_validator("diem")
    def check_diem(cls,diem):
        if diem<0 or diem>10:
            raise ValueError("Khong hop le")
        return diem
@app.post("/check_diem")
def check_diem(ds:check_diem):
    if ds.diem<5:
        raise HTTPException(status_code=400,detail="Thi Rot")
    return {"Thi Dau":ds.diem}


class diem(BaseModel):
    Anh:float
    Van:float
@app.post("/diem/{id}")
def Hocsinh(id:int,d:diem,ten:str,tuoi:int):
    return {"id":id,"ten":ten,"tuoi":tuoi,"Anh":d.Anh,"Van":d.Van}


class Hocsinh(BaseModel):
    diem_toan:float
    diem_van:float
@app.post("/Hocsinh/{id}")
def Hocsinh(id:int,ten:str,hs:Hocsinh):
    return{"id":id,"ten":ten,"diem_toan":hs.diem_toan,"diem_van":hs.diem_van}

class Monhoc(BaseModel):
    Anh:float
    Van:float
@app.post("/Monhoc/{id}")
def Monhoc(id:int,ten:str,MH:Monhoc):
    return {"id":id,"ten":ten,"Anh":MH.Anh,"Van":MH.Van}

class Monhoc_hs(BaseModel):
    Anh:float
    Van:float
@app.post("/Monhoc_hs/{id}")
def Monhoc(id:int,ten:str,MH:Monhoc_hs):
    if id <= 0:
        raise HTTPException(status_code=400,detail="khong hop le")
    return{"id":id,"ten":ten,"Anh":MH.Anh,"Van":MH.Van}




from fastapi import FastAPI,HTTPException
from pydantic import BaseModel, Field,field_validator
class MH_HS(BaseModel):
    Anh:float
    Van:float
    @field_validator("Anh")
    def MH_HS (cls,v):
        if v <0:
            raise ValueError("diem k hop le")
        return v
@app.post("/MH_HS/{}")
def MH_HS(id:int,ten:str,MH:MH_HS):
    if id <= 0:
        raise HTTPException(status_code=400,detail="id k hop le")
    return {"ID":id,"ten":ten,"Anh":MH.Anh,"Van":MH.Van}


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field,field_validator
class Hocsinh(BaseModel):
    toan:float
    van:float
    @field_validator("toan")
    def kt_toan(cls,i):
        if i <0:
            raise ValueError ("diem k hop le")
        return i
@app.post("/kt_toan/{id}")
def kt_toan(id:int,ten:str,MH:Hocsinh):
    if id<= 0:
        raise HTTPException(status_code=400,detail="id k hơp le")
    return{"ten":ten,"ID":id,"Toan":MH.toan,"Van":MH.van}


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
class Hocsinh(BaseModel):
    ten:str
    tuoi:int
@app.post("/hocsinh")
def Hocsinh(hs:Hocsinh):
    if hs.tuoi<18:
        raise HTTPException(status_code=400,detail="tuoi k hop le")
    return {f("ten:{hs.ten} ,du tuoi,tuoi:{hs.tuoi}")}


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator
app=FastAPI() 
class HocSinh(BaseModel):
    ten:str
    tuoi:int=Field(ge=1,le=100)
    diem:float
    @field_validator("ten")
    def check_diem(cls,ten):
        if len(ten)==0:
            raise ValueError ("Tên Bị Rỗng")
        if len(ten)<3:
            raise ValueError("Tên không hợp lệ")
        return ten
@app.post("/HocSinh")
def check_ten(data:HocSinh):
    return {"ten":data.ten,"tuoi":data.tuoi,"diem":data.diem}
@app.get("/HocSinh/{diem}")
def check_diem(diem:float,ten:str):
    if diem<0 or diem>10:   
        raise HTTPException(status_code=400,detail="Diem k hop lệ")
    if diem <5:
        raise HTTPException(status_code=400,detail="HS rớt")
    return {f"ten:{ten},Điểm :{diem},HỌC SINH ĐẬU"}  



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,Field, field_validator
app =FastAPI()
class ketqua (BaseModel):
    ten:str
    tuoi:int= Field(ge=1,le=100)
    diem:float
    @field_validator("ten")
    def kq (cls,ten):
        if len(ten)<3:
            raise ValueError("Tên k hợp lệ")
        return ten
@app.post("/ketqua")
def ketqua (data:ketqua):
    if data.diem<= 0 or data.diem >= 10:
        raise HTTPException(status_code=400,detail="Điểm k hợp lệ")
    if data.diem <5:
        raise HTTPException(status_code=400,detail="HS RỚT")
    return {f"ten:{data.ten},Điểm:{data.diem}, HS ĐẬU"}


ds=[[1,"my"],[2,"nguyen"],[3,"khanh"]]
app= FastAPI()
@app.get("/timhs/{id}")
def timhs(id:int):
    return{"id":ds[id][0],"ten":ds[id][1]} 


 
app=FastAPI()
@app.get("/timhs_for/{id}")
def tim_hs(id:int):
    for hs in ds:
        if hs[0]==id:
            return{"id":hs[0],"ten":hs[1]}
        

from pydantic import BaseModel
from typing import Union
class demds (BaseModel):
    ds:list[list[Union[int,str]]]
app=FastAPI()
@app.post("/dem")
def dem_ds(data:demds):
    dem =0
    for hs in data.ds:
        dem += 1 
    return dem

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app=FastAPI()
class DS(BaseModel):
    ds:list[list[int|str]]
@app.post("/tim/{id}")
def tim_ds(id:int,data:DS):
    dsmoi=[]
    for hs in data.ds:
        if hs[0] ==id:
            dsmoi.append({hs[0],hs[1]})
    if len(dsmoi)>0:
        return dsmoi
    raise HTTPException(status_code=404,detail="k tìm thấy")


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app=FastAPI()
class DS(BaseModel):
    ds:list[list[int|str]]
@app.post("/timten/{ten}")
def timten(data:DS,ten:str):
    dsmoi=[]
    for hs in data.ds:
        if hs[1]==ten:
            dsmoi.append([hs[0],hs[1]])
    if len(dsmoi)>0:
        return dsmoi
    raise HTTPException(status_code=404,detail="k tìm thây")


from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class hsdau(BaseModel):
    ds:list[list[str|int]]
@app.post("/hsdau")
def hsdau(data:hsdau):
    dsmoi=[]
    for hs in data.ds:
        if hs[1]>5:
            dsmoi.append([hs[0],hs[1]])
    if len(dsmoi)>0:
        return dsmoi
    raise HTTPException(status_code=404,detail="hs rớt")


from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class tim_min_nhat(BaseModel):
    ds:list[list[str|int]]
@app.post("/tim_min")
def tim_min(data:tim_min_nhat):
    min_diem=999
    hs_min=""
    for hs in data.ds:
        if hs[1]<min_diem:
            min_diem=hs[1]  
            hs_min=hs[0]
    return {"kq":f"hs điểm thấp nhất:{hs_min},{min_diem}"}



from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class demhs(BaseModel):
    ds:list[list[str|int]]
@app.post("/demhs")
def dem_hs(data:demhs):
    count=0
    tong=0
    tb= 0
    for hs in data.ds:
        tong += hs[1]
        tb= tong/len(data.ds)
        if hs[1]<5:
            count +=1
    return {"Đếm hs":count,"Tổng":tong,"TB":tb}



from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class tonghop_max(BaseModel):
    ds:list[list[str|int]]
@app.post("/tongmax")
def tonghop_max(data:tonghop_max):
    tong=0
    tb= 0
    max_diem=0
    ten_max=""
    for hs in data.ds:
        tong += hs[1]
        tb= tong/len(data.ds)
        if hs[1]>max_diem:
            max_diem=hs[1]
            ten_max=hs[0]
    return {"HS điẻm cao nhất":max_diem,"ten hs max":ten_max,"Tổng":tong,"TB":tb}


from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class HocSinh_moi(BaseModel):
    ten:str
    diem:float
class Nested_moi(BaseModel):
    ds:list[HocSinh_moi]
@app.post("/nested")
def Nested_hs (data:Nested_moi):
    max_diem=data.ds[0].diem
    ten_max=data.ds[0].ten
    for hs in data.ds:
        if hs.diem>max_diem:
            max_diem=hs.diem
            ten_max=hs.ten
    return{"ĐIẺM HS CAO NHẤT":max_diem,"Tên Hs":ten_max}



from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

class data_ds (BaseModel):
    ten:str
    diem:list[float]
class data_diem(BaseModel):
    ds:list[data_ds]
@app.post("/data_diem1")
def data_ds_diem(data:data_diem):
    max_dtb= 0
    ten_max=""
    min_dtb=999
    ten_min=""
    for hs in data.ds:
        tong =0 
        dtb =0 
        for diem in hs.diem: 
            tong += diem
            dtb =tong/len(hs.diem)
            if dtb > max_dtb:
                max_dtb = dtb
                ten_max = hs.ten
            if dtb < min_dtb:
                min_dtb = dtb
                ten_min= hs.ten
        
    return{"Tên hs dtb cao nhất":ten_max,"dtb":max_dtb,"tên hs dtb thấp nhât":ten_min,"min_dtb":min_dtb} 




from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class Danhsach(BaseModel):
    ten:str
    diem:list[float]
class DS(BaseModel):
    ds:list[Danhsach]
@app.post("/tonghopnested")
def tonghopnested(data:DS):
    max_diem=0
    min_diem=999
    ten_max=""
    ten_min=""
    dsmoi=[]
    dsduoi5 =[]
    
    for hs in data.ds:
        tong=0
        dtb=0
        tenhs_diem=""
        count =0
        for diem in hs.diem:
            tong += diem
            
            dtb=tong/len(hs.diem)
            if dtb >max_diem:
                max_diem=dtb
                ten_max=hs.ten
            if dtb< min_diem:
                min_diem= dtb
                ten_min=hs.ten
            if diem <5:
                count += 1
                tenhs_diem=hs.ten
        dsduoi5.append({"ten":tenhs_diem,"diem duoi 5":count})
    dsmoi.append({"ten hs dtb cao nhất":ten_max,"dtb_max":max_diem,"ten hs dtb nhỏ nhẩt":ten_min,"dtb_min":min_diem,"Điem duoi 5":dsduoi5})
    return dsmoi



from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class ds_danhsach(BaseModel):
    ten:str
    diem:list[float]
class ds_ds(BaseModel):
    ds:list[ds_danhsach]
@app.post("/ds_danhsach")
def ds_danhsach(data:ds_ds):
    max_count=0
    min_count=999
    ten_max="" 
    ten_min=""
    dsmoi=[]
    for hs in data.ds:
        count =0
        for diem in hs.diem:
            if diem <5:
                count += 1
            if count > max_count :
                max_count = count
                ten_max= hs.ten
            if count < min_count:
                min_count=count
                ten_min= hs.ten
    dsmoi.append({"Tên hs max":ten_max,"tổng max":max_count,"Tên hs min":ten_min,"tổng min":min_count})
    return dsmoi



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,Field ,field_validator
app=FastAPI()
class dshs(BaseModel):
    ten:str=Field(min_length=3, max_length=20,description="danh sách tên")
    diem:list[float]=Field(min_length=2,max_length=5,description="danh sách điểm")
    @field_validator("diem")
    def check_diem(cls,diem):
        dsmoi=[]
        dsdat=[]
        for i in diem:
            if i<0 or i> 10:
                dsmoi.append(i)
                if len(dsmoi)>0:
                    raise ValueError("ds k hợp lệ")
            dsdat.append(i)   
        return dsdat
class danhsach(BaseModel):
    ds:list[dshs]
@app.post("/check_diem")
def check_diem(data:danhsach):
    return {"ds":data.ds}


from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field,field_validator
app= FastAPI()
class Hocsinh (BaseModel):
    ten:str=Field(min_length=0,max_length=0,description="Độ dài tên 3<ten<20")
    diem:list[float]=Field(min_length=0,max_length=0,description="list điểm chỉ có 2-5 phần tử")
    @field_validator("diem")
    def check_diem(cls,diem):
        
        for i in diem:
            if i<0 or i>10:
                raise ValueError("điểm k hơp lệ")
            
        return diem
class Lophoc(BaseModel):
    ds:list[Hocsinh]=Field(min_length=0,max_length=0,description="dshs")
@app.post("/kiem_tra_hs_123")
def kt_hs(data:Lophoc):
    if len(data.ds)==0:
        raise HTTPException(status_code=400,detail="ds rỗng k hợp lệ")
    tenmax_duoi5=""
    max_duoi5=0
    min_duoi5=999
    tenmin_duoi5=""
    for hs in data.ds:   
        diem_duoi5 =0
        ten_min=""
        for i in hs.diem:
            if i<5 :
                diem_duoi5 += 1
                if diem_duoi5>max_duoi5:
                    max_duoi5= diem_duoi5
                    tenmax_duoi5 = hs.ten
                if diem_duoi5<min_duoi5:
                    min_duoi5=diem_duoi5
                    tenmin_duoi5=hs.ten
    return{"tổng hs là":len(data.ds),"hs điểm duoi5 max":tenmax_duoi5,"điểm max":max_duoi5,"hs có điểm dưới 5 ít nhẩt":tenmin_duoi5,"điểm min":min_duoi5}



from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field,field_validator
app=FastAPI()
class HS (BaseModel):
    ten:str=Field(min_length=2,max_legth=30)
    diem:list[float]=Field(min_length=1,max_length=10)
    @field_validator("diem")
    def check_diem(cls,diem):
        for i in diem:
            if i<0 or i>10:
                raise ValueError("điểm k hợp lệ")
        return diem
class LH (BaseModel):
    ds:list[HS]=Field(min_length=2,max_length=5)
@app.post("/tonghopnestedfieldhttp")
def th_nested_field_http(data:LH):
    max_count=0
    ten_max5 =""
    min_count =999
    ten_min5=""
    tonghs=len(data.ds)
    
    dtb=0
    max_diem=0
    ten_max=""
    min_diem=999
    ten_min=""
    for hs in data.ds:
        count =0
        dtb=sum(hs.diem)/len(hs.diem)
        if dtb >max_diem:
            max_diem= dtb
            ten_max=hs.ten
        if dtb <min_diem:
            min_diem= dtb
            ten_min=hs.ten
        for i in hs.diem:
            if i < 5:
                count +=1 
            if count > max_count:
                max_count =count
                ten_max5= hs.ten
            if count< min_count:
                min_count=count 
                ten_min5=hs.ten
            if count ==0:
                raise HTTPException(status_code=404,detail={"thông báo":"k có hs duoi 5","maxdtb":max_diem,"mindtb":min_diem})
           
    return {"max5":max_count,"min5":min_count,"maxdtb":max_diem,"mindtb":min_diem}


from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,field_validator
app =FastAPI()
class HS_1(BaseModel):
    ten:str
    @field_validator("ten")
    @classmethod
    def check_ten (cls,ten):
        dsten =[]
        if len(ten) == 0:
            raise ValueError ("tên k được rỗng")
        return ten
        if ten == ten :
            raise ValueError ("tên bị trùng")
        dsten.append(ten)
        return dsten
    diem:list[float]
    @field_validator("diem")
    @classmethod
    def check_diem(cls,diem):
        dsdiem=[]
        for i in diem:
            if i<0 or i >10:
                dsdiem.append(i)
            if len(dsdiem)>0:
                raise ValueError (" điểm k hợp lệ")
        return diem
class DS_1(BaseModel):
    ds:list[HS_1]
    @field_validator("ds")
    @classmethod
    def check_ds(cls,ds):
        dsten =[]
        if len(ds)==0:
            raise ValueError("ds k được rổng")
        for hs in ds:
            if hs.ten in dsten:
                raise ValueError ("tên bị trùng")
            dsten.append(hs.ten)
        return ds
    
@app.post("/TH_DSHS_1")
def TH_DSHS_1(data:DS_1):
    tonghs=0
    max_1=0
    min_1=999
    ten_max1=""
    ten_min1=""
    ten_maxc=""
    ten_minc=""
    dsmoi=[]
    max_count=0
    min_count=999
    tongcount=0
    tongcountmax =0
    diem_max=data.ds[0].diem[0]
    diem_min=data.ds[0].diem[0]
    tenmin_diem=""
    tenmax_diem="" 
    dsdiemmax=[]
    dsdiemmin=[]  
    for hs in data.ds:
        tonghs += 1
        dtb=sum(hs.diem)/len(hs.diem)
        count =0 
        if dtb> max_1:
            max_1=dtb
            ten_max1=hs.ten
        if dtb< min_1:
            min_1=dtb
            ten_min1=hs.ten
        for i in hs.diem:
            if i >diem_max:
                diem_max=i
                tenmax_diem=hs.ten
                dsdiemmax=[hs.ten]
            elif i == diem_max:
                dsdiemmax.append(hs.ten)
            if i <diem_min:
                diem_min= i
                tenmin_diem=hs.ten
                dsdiemmin=[hs.ten]
            elif i == diem_min:
                dsdiemmin.append(hs.ten)
            if i>5:
                tongcountmax += 1 
            if i <5:
                count += 1
                tongcount += 1
        if count > max_count:
            max_count=count
            ten_maxc= hs.ten
        if count < min_count:
            min_count=count
            ten_minc =hs.ten
    dsmoi.append({"maxc":max_count,"tenmax":ten_maxc,"minc":min_count,"tenmin":ten_minc})
    return{" tong hs":tonghs,"max_dtb":max_1,"min_dtb":min_1,"ten1":ten_max1,"ten_min1":ten_min1,"dscount":dsmoi,"tongcount":tongcount,"tongcountmax":tongcountmax,"diem_max":diem_max,"tenmax_diem":dsdiemmax,"diem_min":diem_min,"tenmin_diem":dsdiemmin}



from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class HS2(BaseModel):
    ten:str
    diem:list[float]
class lop2(BaseModel):
    ds:list[HS2]
@app.post("/hoc_them_code_trung")
def check_codetrung(data:lop2):
    tonghs =0
    max_dtb=0
    tenmax_dtb=[]
    min_dtb=10
    tenmin_dtb=[]
    dsduoi5=[]
    for hs in data.ds:
        thongbao=""
        tonghs +=1
        tongtunghs =0
        dtb=0
        tenhsduoi5=""
        for i in hs.diem:
            tongtunghs += i
            dtb = tongtunghs/len(hs.diem)
            if i<5:
                tenhsduoi5 =hs.ten
        if tenhsduoi5 != "":
            dsduoi5.append(hs.ten)
        if len(dsduoi5)==0:
            thongbao="không có học sinh duoi 5"
        else:
            thongbao="k có hs dưới 5"
        if dtb >max_dtb:
            max_dtb =dtb
            tenmax_dtb=[hs.ten]
        elif dtb == max_dtb:
            tenmax_dtb.append(hs.ten)
            tenmax_dtb.append(hs.ten)
        if dtb<min_dtb:
            min_dtb=dtb
            tenmin_dtb=[hs.ten]
        elif dtb == min_dtb:
            tenmin_dtb.append(hs.ten)
           
            
    return{"tonghs":tonghs,"max_dtb":max_dtb,"tenmax":tenmax_dtb,"min_dtb":min_dtb,"tenmin":tenmin_dtb,"tên duoi 5":dsduoi5,"thông báo":thongbao  }



from fastapi import FastAPI
app = FastAPI()
ds_hs=[{"ten":"My","tuoi":19},{"ten":"linh","tuoi":20},{"ten":"lam","tuoi":23}]
@app.get("/hoc_sinh/{ten}")

def check_hocsinh(ten:str):
    for hs in ds_hs:
        if hs["ten"]==ten:
            return {"tong":len(ds_hs),"danh sach":hs["ten"]}  
        
from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
data=DS(ds=[{"ten":"My","diem":[2,3,4]},{"ten":"linh","diem":[2,3,4]},{"ten":"lam","diem":[1,2,3]}])

class HS (BaseModel):
    ten:str
    diem:list[float]
class DS (BaseModel):
    ds:list[HS]
@app.get("/nested_tonghop")
def nested_tonghop3():
    dtb=0
    max_dtb = 0
    min_dtb=float("inf")
    ten_max=[]
    ten_min=[]
    dstenmax=[]
    dstenmin =[]
    tonghs=0
    
    tongdtb=0
    for hs in data.ds:
        
        tonghs += 1
        tongdtb =sum(hs.diem)
        dtb=tongdtb/len(hs.diem)
        if dtb >max_dtb:
            max_dtb = dtb
            ten_max= [hs.ten]
            dstenmax=[]
            dstenmax.append({"ten":hs.ten,"diem":max_dtb})
        elif dtb == max_dtb:
            dstenmax.append({"ten":hs.ten,"diem":max_dtb})
        if dtb< min_dtb:
            min_dtb = dtb
            ten_min= [hs.ten]
            dstenmin=[]
            dstenmin.append({"ten":hs.ten,"diem":min_dtb})
        elif dtb == min_dtb:
            dstenmin.append({"ten":hs.ten,"diem":min_dtb})
    return({"tonghs":tonghs,"max":dstenmax,"min":dstenmin})


from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
data=DS(ds=[{"ten":"My","diem":[7,3,5]},{"ten":"linh","diem":[2,3]},{"ten":"lam","diem":[5,3,5]}])

class dshs(BaseModel):
    ten:str
    diem:list[float]
class ds_10(BaseModel):
    ds:list[dshs]
@app.get("/dshs_10")
def check_mon ():
    tonghs=0
    tongmon=0
    tongdiem=0
    dsdiemtren2=[]
    dsdiemmax=[]
    ten_max=""
    max_diem=data.ds[0].diem[0]
    max_count =0
    tenmax_count =""
    dsmaxcount =[]
    for hs in data.ds:
        count =0
        tonghs += 1
        tongmon += len(hs.diem)
        tongdiem += sum(hs.diem)
        for diem in hs.diem: 
            if diem>max_diem:
                max_diem= diem
                dsdiemmax=[]             
                dsdiemmax.append(hs.ten)
            elif diem == max_diem:
                if hs.ten not in dsdiemmax:
                    dsdiemmax.append(hs.ten)
        for diem in hs.diem:
            if diem> 2:
                dsdiemtren2.append(hs.ten)
                break
        for diem in hs.diem:
            if diem>2:
                count += 1
                if count > max_count:
                    max_count= count
                    tenmax_count = hs.ten
                    dsmaxcount=[]
                    dsmaxcount.append(hs.ten)
                elif count == max_count:
                    dsmaxcount.append(hs.ten)
    return{"tonghs":tonghs,"tongmon":tongmon,"tongdiem":tongdiem,"diemtren2":dsdiemtren2,"diemmax":dsdiemmax,"maxcount":dsmaxcount}



from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
data=DS(ds=[{"ten":"My","diem":[5,8,5]},{"ten":"linh","diem":[2,5]},{"ten":"lam","diem":[7,8,5]}])
class list_2(BaseModel):
    ten:str
    diem:list[float]
class list_1(BaseModel):
    ds:list[list_2]
@app.get("/list_all")
def check_list_all ():
    tonghs =0
    tongdiem =0
    dtb =0
    dsmax=[]
   
    max_diem=0
    tenmax=""
    for hs in data.ds:
        dem =0
        tong_1 =0
        dtb_1=0
        tonghs += 1
        tongdiem += sum(hs.diem)
        dtb = tongdiem/tonghs
        for i in hs.diem:
            
            dem += 1
            tong_1 += i
        dtb_1 = tong_1/dem
        
        if dtb_1 > max_diem:
            max_diem = dtb_1
            tenmax =hs.ten
            dsmax=[]
            dsmax.append({"ten":hs.ten,"diem":dtb_1})
        elif dtb_1 == max_diem:
            dsmax.append({"ten":hs.ten,"diem":dtb_1})
    
    return {"tonghs":tonghs,"tongdiem":tongdiem,"dtb":dtb,"dsmax":dsmax}



from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
data=DS(ds=[{"ten":"My","diem":[1,1,5]},{"ten":"linh","diem":[1,5]},{"ten":"lam","diem":[1,1,5]}])
class ds_hs_2(BaseModel):
    ten:str
    diem:list[float]
class hs_2(BaseModel):
    ds:list[ds_hs_2]
@app.get("/onbai")
def onbai():
    tonghs=0
    tongdiem=0
    dtb_tong=0
    max_diem =0
    dsmaxdiem=[]
    ten_max =""
    min_diem=999
    dsmindiem=[]
    ten_min=""
    count15=0
    count10=0
    dsten10 =[]
    max_dtb=0
    dsmaxdtb=[]
    tenmax_dtb=""
    min_dtb=999
    dsmindtb=[]
    tenmin_dtb=""

    for hs in data.ds:
        tonghs += 1
        tongdiem += sum(hs.diem)
        dtb_tong= tongdiem/tonghs
        tongmax =0
        dtb=0
        for diem in hs.diem:
            tongmax += diem
        if tongmax> max_diem:
            max_diem= tongmax
            dsmaxdiem =[]
            dsmaxdiem.append(hs.ten)
        if tongmax == max_diem:
            if hs.ten not in dsmaxdiem:
                ten_max = hs.ten
                dsmaxdiem.append(hs.ten)
        for diem in hs.diem:
            if tongmax < min_diem:
                min_diem = tongmax
                ten_min=[hs.ten]
                dsmindiem=[]
                dsmindiem.append(hs.ten)
            if tongmax == min_diem:
                if hs.ten not in dsmindiem:
                    dsmindiem.append(hs.ten)  
        if tongmax >15:
            count15 += 1
        if tongmax <10:
            count10 += 1
            dsten10.append(hs.ten)
        for diem in hs.diem:
            dtb= tongmax/len(hs.diem)
            if dtb > max_dtb:
                max_dtb=dtb
                tenmax_dtb=[hs.ten]
                dsmaxdtb=[]
                dsmaxdtb.append(hs.ten)
            if dtb== max_dtb:
                if hs.ten not in dsmaxdtb:
                    dsmaxdtb.append(hs.ten)
            if dtb < min_dtb:
                min_dtb=dtb
                tenmin_dtb=[hs.ten]
                dsmindtb=[]
                dsmindtb.append(hs.ten)
            if dtb== min_dtb:
                if hs.ten not in dsmindtb:
                    dsmindtb.append(hs.ten)                
    return {"tong hoc sinh": tonghs,"tong diem":tongdiem,"dtb_tong":dtb_tong,"dsmaxdiem":dsmaxdiem,"dsmindiem":dsmindiem,"count15":count15,"count10":dsten10,"dsmaxdtb":dsmaxdtb,"dsmindtb":dsmindtb}


from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
data=DS(ds=[{"ten":"My","diem":[7,1,5]},{"ten":"linh","diem":[1,5]},{"ten":"lam","diem":[1,1,5]}])
class ds_hs_3(BaseModel):
    ten:str
    diem:list[float]
class get_nangcaoxiu(BaseModel):
    ds:list[ds_hs_3]
@app.get("/getnangcaoxiu")
def getnangcaoxiu(): 
    dscount5=[]
    tencount5=""
    max_count5=0
    tenmaxcount5=""
    dsmaxcount5=[]
    for hs in data.ds:
        count5=0
        for diem in hs.diem:
            if diem <5 :
                count5 += 1
        dscount5.append({"ten":hs.ten,"diem":count5})
        if count5 >max_count5:
            max_count5= count5 
            dsmaxcount5=[]  
            tenmaxcount5=[hs.ten]
            dsmaxcount5.append(hs.ten)
        elif count5 ==max_count5:
            dsmaxcount5.append(hs.ten) 
    return {"dscount5":dscount5,"dsmaxcount5":dsmaxcount5}


from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
data=DS(ds=[{"ten":"My","diem":[1,1,4]},{"ten":"lan","diem":[1,1,3]},{"ten":"nam","diem":[1,4,3]},{"ten":"linh","diem":[2,1,7]}])
class hs (BaseModel):
    ten:str
    diem:list[float]
class ds_hs_rot(BaseModel):
    ds:list[hs]
@app.get("/ds_hs_rot")
def check_hs_rot():
    dscount5=[]
    tenhs=""
    tonghsrot=0
    max_count5=0
    tenmax_count5=""
    dsmaxcount5=[]
    for hs in data.ds:
        count5 =0
        for diem in hs.diem:
            if diem < 5:
                count5 += 1                
        if count5 >= 2:
            tonghsrot += 1                        
            dscount5.append({"ten":hs.ten,"diemduoirot":count5})
        if count5> max_count5:
            max_count5=count5
            tenmax_count5=[hs.ten]
            dsmaxcount5=[]
            dsmaxcount5.append({"ten":hs.ten,"so mon rot":count5})
        elif count5== max_count5:
            dsmaxcount5.append({"ten":hs.ten,"so mon rot":count5})
    return {"dsrot":dscount5,"tonghsrot":tonghsrot,"max_rot":dsmaxcount5}


from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
data=DS(ds=[{"ten":"My","diem":[1,1,9]},{"ten":"lan","diem":[1,1,8]},{"ten":"nam","diem":[1,4,6]},{"ten":"linh","diem":[10,1,7]}])
class hs_dang1(BaseModel):
    ten:str
    diem:list[float]
class ds_hs_dang1(BaseModel):
    ds:list[hs_dang1]
@app.get("/tonghopgetnangcao1")
def tonghopgetnangcao1():
    tonghs=0
    dscount5=[]    
    dtb=0
    dsdtb=[]
    dsmaxdtb=[]
    max_dtb=0
    tenmax_dtb=""
    tongcount5=0
    for hs in data.ds:
        tonghs += 1              
        dtb= sum(hs.diem)/ len(hs.diem)
        dsdtb.append({"ten":hs.ten,"dtb":dtb})
    if dtb >max_dtb:
        max_dtb = dtb
        tenmax_dtb=[hs.ten]
        dsmaxdtb.append({"ten":hs.ten,"dtb":dtb})
    elif dtb== max_dtb:
        dsmaxdtb.append({"ten":hs.ten,"dtb":dtb})
    for hs in data.ds:      
        count5=0
        for diem in hs.diem:                      
            if diem <5:
                count5 += 1
        if count5 >= 2:
            tongcount5+= 1               
            dscount5.append({"tenhsrot":hs.ten,"so mon rot":count5})
    return {"dsdtb":dsdtb,"dscount5":dscount5,"dsmaxdtb":dsmaxdtb, "tonghsrot":tongcount5}



from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
data=DS(ds=[{"ten":"My","diem":[6,1,9]},{"ten":"lan","diem":[7,1,8]},{"ten":"nam","diem":[1,4,6]},{"ten":"linh","diem":[10,1,7]}])
class get2 (BaseModel):
    ten:str
    diem:list[float]
class tonghop_get2(BaseModel):
    ds:list[get2]
@app.get("/tonghop_get2")
def tonghop_get2():
    dscount5=[]
    tonghsdat=0
    for hs in data.ds:
        count5=0
        for diem in hs.diem:
            if diem >=5:
                count5 += 1
        if count5 >= 2:
            tonghsdat +=1
            dscount5.append({"tenhs_dat":hs.ten,"diemtren5":count5})
    return {"dscount5":dscount5,"tonghsdat":tonghsdat}



from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
data=DS(ds=[{"ten":"My","diem":[5,6,6]},{"ten":"lan","diem":[6,4,7]},{"ten":"nam","diem":[3,4,2]},{"ten":"linh","diem":[4,4,1]}])
class get3(BaseModel):
    ten:str
    diem:list[float]
class tonghop_get3(BaseModel):
    ds:list[get3]
@app.get("/tonghop_get3")
def tonghop_get3(dshs:str):
    dshsgioi=[]
    dshskha=[]
    dshstb=[]
    dshsyeu=[]
    tenhsgioi=""
    tenhskha=""
    tenhstb=""
    tenhsyeu=""
    for hs in data.ds:
        dtb=0
        for diem in hs.diem:
            dtb= sum(hs.diem)/len(hs.diem)
        if dtb >=8 :
            tenhsgioi=[hs.ten]
            dshsgioi.append({"tenhsgioi":tenhsgioi,"dtb":dtb})
        elif 6.5<=dtb <8:
            tenhskha =[hs.ten]            
            dshskha.append({"tenhskha":tenhskha,"dtb":dtb})
        elif 5<= dtb< 6.5:
            tenhstb=[hs.ten]           
            dshstb.append({"tenhstb":tenhstb,"dtb":dtb})
        else:
            tenhsyeu=[hs.ten]           
            dshsyeu.append({"tenhsyeu":tenhsyeu,"dtb":dtb})
    return {"dshsgioi":dshsgioi,"dshskha":dshskha,"hshstb":dshstb,"dshsyeu":dshsyeu} 


from fastapi import FastAPI 
from pydantic import BaseModel
app= FastAPI()
data=DS(ds=[{"ten":"My","diem":[10,10,10]},{"ten":"lan","diem":[10,10,10]},{"ten":"nam","diem":[10,10,10]},{"ten":"linh","diem":[10,10,10]}])
class get4(BaseModel):
    ten:str
    diem:list[float]
class tonghop_get4(BaseModel):
    ds:list[get4]
@app.get("/tonghop_get4")
def tonghop_get4():
    max_count10=0
    tenmax_count10=""
    dsmaxcount10=[]
    for hs in data.ds:
        count10=0
        for diem in hs.diem:
            if diem== 10:
                count10 += 1
        if count10 > max_count10:
            max_count10 = count10
            tenmax_count10=[hs.ten]
            dsmaxcount10=[]
            dsmaxcount10.append({"tenmax":tenmax_count10,"tongmax":count10})
        elif count10 == max_count10:
            if hs.ten not in dsmaxcount10:
                tenmax_count10=[hs.ten]
            dsmaxcount10.append({"tenmax":tenmax_count10,"tongmax":count10})
    return dsmaxcount10


from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
data=DS(ds=[{"ten":"My","diem":[10,10,10]},{"ten":"lan","diem":[4,5,6]},{"ten":"nam","diem":[10,10,10]},{"ten":"linh","diem":[10,10,10]},{"ten":"quynh","diem":[7,6,5]},{"ten":"lam","diem":[7,8,9]}])
class get4(BaseModel):
    ten:str
    diem:list[float]
class tim3max(BaseModel):
    ds:list[get4]
@app.get("/tim3max")
def tim3max():
    dsdtb=[]
    
    for hs in data.ds:
        dtb =0
        diemhs=0
        for diem in hs.diem:
            diemhs += diem
        dtb=diemhs/len(hs.diem)
        dsdtb.append({"ten":hs.ten,"dtb": dtb})
    dsdtb.sort(key=lambda x: x["dtb"])
    top3= dsdtb[:3]
    return {"top3 hs đầu ":top3}

from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
data=DS(ds=[{"ten":"My","diem":[10,10,10]},{"ten":"lan","diem":[10,5,6]},{"ten":"nam","diem":[4,10,10]},{"ten":"linh","diem":[10,10,10]},{"ten":"quynh","diem":[9,6,5]},{"ten":"lam","diem":[10,8,9]}])
class get5(BaseModel):
    ten:str
    diem:list[float]
class timtop3(BaseModel):
    ds:list[get5]
@app.get("/timtop3")
def timtop3():
    dscount10 =[]
    for hs in data.ds:
        count=0
        for diem in hs.diem:
            if diem ==10:
                count +=1 
        dscount10.append({"ten":hs.ten,"count10":count})
    dscount10.sort(key=lambda x: x["count10"],reverse=True)
    top3= dscount10[:3]
    return{" ba hs có điểm 10 nhiều nhất ":top3}



from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
data=DS(ds=[{"ten":"My","diem":[1,4,10]},{"ten":"lan","diem":[1,5,6]},{"ten":"nam","diem":[4,2,2]},{"ten":"linh","diem":[8,10,10]},{"ten":"quynh","diem":[2,6,5]},{"ten":"lam","diem":[4,8,4]}])
class get6(BaseModel):
    ten:str
    diem:list[float]
class timtop3diem5(BaseModel):
    ds:list[get6]
@app.get("/timtop3diem5")
def timtop3diem5():
    dscount5=[]
    for hs in data.ds:
        count5=0
        for diem in hs.diem:
            if diem<5:
                count5 += 1
        dscount5.append({"ten":hs.ten,"diem duoi5":count5})
    dscount5.sort(key=lambda x: x["diem duoi5"],reverse=True)
    top3duoi5= dscount5[:3]
    return {"3 hs duoi 5 nhieu nhat":top3duoi5}



from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
data=DS(ds=[{"ten":"My","diem":[1,4,10]},{"ten":"lan","diem":[7,5,6]},{"ten":"nam","diem":[4,2,2]},{"ten":"linh","diem":[8,10,10]},{"ten":"quynh","diem":[2,6,5]},{"ten":"lam","diem":[10,8,5]}])
class get7(BaseModel):
    ten:str
    diem:list[float]
class timhsdat(BaseModel):
    ds:list[get7]
@app.get("/timhsdat")
def timhsdat():  
    dshsdat=[]  
    for hs in data.ds:
        count5=0
        dtb=0
        diemhs=0
        for diem in hs.diem:
            diemhs += diem
        dtb= diemhs/len(hs.diem)
        for diem in hs.diem:    
            if diem<5:
                count5 += 1
        if dtb >=5 and count5 ==0:
            dshsdat.append({"ten":hs.ten,"hs dat dtb":dtb})
    return dshsdat




from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
data=DS(ds=[{"ten":"My","diem":[1,4,10]},{"ten":"lan","diem":[10,9,7]},{"ten":"nam","diem":[4,2,2]},{"ten":"linh","diem":[8,10,10]},{"ten":"quynh","diem":[2,6,5]},{"ten":"lam","diem":[10,8,5]}])
class get8(BaseModel):
    ten:str
    diem:list[float]
class phanloaihs(BaseModel):
    ds:list[get8]
@app.get("/timhsdat")
def phanloaihs(): 
    dshsgioi=[]
    dshskha=[]
    dshstb=[]
    dshsyeu=[]
    countgioi =0
    countkha=0
    counttb=0
    countyeu=0
    
    for hs in data.ds:
        diemhs=0
        dtb=0    
        for diem in hs.diem:
            diemhs += diem 
        dtb= diemhs/len(hs.diem)
        if dtb >= 8:
            countgioi += 1
            dshsgioi.append({"tenhsgioi":hs.ten}) 
        elif 6.5<= dtb<8:
            countkha +=1
            dshskha.append({"tenhskha":hs.ten})
        elif 5 <= dtb <6.5:
            counttb += 1
            dshstb.append({"tenhstb":hs.ten})
        else:
            countyeu +=1
            dshsyeu.append({"tenhsyeu":hs.ten})
    return {"gioi":dshsgioi,"slgioi":countgioi,"khá":dshskha,"slkha":countkha,"tb":dshstb,"sltb":counttb,"yếu":dshsyeu,"slyeu":countyeu}
    
        
from fastapi import FastAPI
from pydantic import BaseModel,Field ,field_validator
app=FastAPI()
class hs (BaseModel):
    ten:str
    tuoi:int
class dshs10(BaseModel):
    ds:list[hs]
    @field_validator("ds")
    def check_trung_ten(cls,ds):
        dsten=[]
        for hs in ds:
            if hs.ten in dsten:
                raise ValueError(f"ten hs trùng {hs.ten}")
            dsten.append(hs.ten)
        return dsten
@app.post("/timhstrungten")
def check_trung_ten(data:dshs10):
    return data.ds


from fastapi import FastAPI
from pydantic import BaseModel,Field ,field_validator
app=FastAPI()
class hs (BaseModel):
    ten:str
    tuoi:int
class dshs10(BaseModel):
    ds:list[hs]
    @field_validator("ds")
    def check_trungten(cls,ds):
        dsten=[]
        for hs in ds:
            if hs.ten=="":
                raise ValueError("tên rỗng")
            if hs.ten in dsten:
                raise ValueError("trùng tên")
            if hs.tuoi< 18 or hs.tuoi > 60:
                raise ValueError(" tuoi")
            dsten.append(hs.ten)
        return ds
@app.post("/trungtentrungtuoi")
def trungtentrungtuoi(data:dshs10):
    return data.ds


from fastapi import FastAPI
from pydantic import BaseModel,Field ,field_validator
app=FastAPI()
class hs_trung (BaseModel):
    ten:str
    @field_validator("ten")
    @classmethod
    def check_ten(cls,ten):
        for ky_tu in ten:
            if ky_tu.isdigit() == True:
                raise ValueError (f"tên k chứa số{ky_tu}")
        return ten.strip()
    tuoi:int
    @field_validator("tuoi")   
    def check_tuoi(cls,tuoi):    
        if tuoi <0 or tuoi>120:
                raise ValueError(f"tuoi không được âm {tuoi}")
        return tuoi
class dshs10(BaseModel):
    ds:list[hs_trung]
    @field_validator("ds")
    @classmethod
    def check_hstrung (cls,ds):
        print(len(ds))
        dstentuoi=[]
        for hs in ds:
            if (hs.ten,hs.tuoi) in dstentuoi:
                raise ValueError("hs trùng tên  và trùng tuổi")
            dstentuoi.append((hs.ten,hs.tuoi))
        return ds
@app.post("/trungten_trungtuoi_10")
def check_trungten_trungtuoi(data:dshs10):
    return data.ds





from fastapi import FastAPI
from pydantic import BaseModel,Field ,field_validator
app=FastAPI()
class tonghop (BaseModel):
    ten:str
    @field_validator("ten")
    @classmethod
    def check_ten(cls,ten):
        if ten=="":
            raise ValueError("tên k được rỗng")
        if len(ten.strip())<2:
            raise ValueError("tên trên 2 kí tự")
        for ky_tu in ten:
            if ky_tu.isdigit()==True:
                raise ValueError("tên không được có số")
        return ten.strip()
    tuoi:int
    @field_validator("tuoi")
    def check_tuoi(cls,tuoi):
        if tuoi<0 or tuoi>120:
            raise ValueError("tuổi không hợp lệ")
        return tuoi
class tonghop_validator(BaseModel):
    ds:list[tonghop]
    @field_validator("ds")
    def check_tentrung(cls,ds):
        dstrung=[]
        for hs in ds:
            if (hs.ten,hs.tuoi) in dstrung:
                raise ValueError("tên và tuổi k được trùng nhau")
            dstrung.append((hs.ten,hs.tuoi))
        return ds
@app.post("/tonghop_validator")
def tonghop_validator(data:tonghop_validator):
    return data.ds




from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
ds=[{"ten":"My","tuoi":20},{"ten":"nhung","tuoi":50},{"ten":"linh","tuoi":20}]
class HTTP (BaseModel):
    ten:str
    tuoi:int
class HTTP_nangcao(BaseModel):
    ds:list[HTTP]
@app.get("/HTTP_nangcao")
def HTTP(ten:str):
    for hs  in ds:
        if hs["ten"] != ten:
            raise HTTPException(status_code=404,detail="k tìm thấy hs")
        return hs  
    

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
ds=[{"ten":"My","tuoi":10},{"ten":"nhung","tuoi":60},{"ten":"linh","tuoi":20},{"ten":"nguyen","tuoi":20}]
class HTTP (BaseModel):
    ten:str
    tuoi:int
class HTTP_tuoi(BaseModel):
    ds:list[HTTP]
@app.get("/HTTP_tuoi")
def check_tuoi(tuoi:int):
    dsbangtuoi=[]
    for hs in ds:    
        if hs["tuoi"]== tuoi:
            dsbangtuoi.append({"ten":hs["ten"],"tuoi":hs["tuoi"]})
    if len(dsbangtuoi)==0:
        raise HTTPException(status_code=404,detail="khong hoc sinh nào bằng tuổi")   
    return dsbangtuoi


from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
ds=[{"ten":"My","tuoi":10},{"ten":"nhung","tuoi":60},{"ten":"linh","tuoi":30},{"ten":"nguyen","tuoi":20}]
class HTTP1 (BaseModel):
    ten:str
    tuoi:int
class HTTP1_tuoi(BaseModel):
    ds:list[HTTP]
@app.get("/HTTP1_tuoi")
def check_tuoi(tuoi:int):
    demsl=0
    dstuoi=[]
    for hs in ds:
        if hs["tuoi"] == tuoi:
            demsl +=1
            dstuoi.append({"tuoi":hs["tuoi"],"sl":demsl})
    if len(dstuoi) ==0:
        raise HTTPException(status_code=404,detail="k có hs nào bang tuoi")
    return dstuoi



from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
ds=[{"ten":"My","tuoi":10},{"ten":"nhung","tuoi":60},{"ten":"linh","tuoi":30},{"ten":"nguyen","tuoi":20}]
class HTTP2 (BaseModel):
    ten:str
    tuoi:int
class HTTP2_tuoi(BaseModel):
    ds:list[HTTP]
@app.get("/HTTP2_tuoi")
def check_tuoi(tuoi:int,ten:str):
    for hs in ds:
        if (hs["ten"],hs["tuoi"])==(ten,tuoi):
            return hs
    raise HTTPException(status_code=404,detail="k có hs bang ten tuoi")
        
    
        
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
ds=[{"ten":"My","tuoi":10},{"ten":"nhung","tuoi":60},{"ten":"linh","tuoi":30},{"ten":"nguyen","tuoi":20}]
class HTTP3 (BaseModel):
    ten:str
    tuoi:int
class HTTP3_tuoi(BaseModel):
    ds:list[HTTP]
@app.get("/HTTP3_tuoi")
def check_tuoi(tuoi:int,ten:str):
    dstentuoi=[]
    for hs in ds:
        if (hs["ten"],hs["tuoi"])==(ten,tuoi):
            dstentuoi.append({"ten":hs["ten"],"tuoi":hs["tuoi"]})
            return dstentuoi
    raise HTTPException(status_code=404,detail="k có hs bang ten tuoi")
   
    

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
ds=[{"ten":"thien","tuoi":30},{"ten":"linh","tuoi":65},{"ten":"linh","tuoi":30},{"ten":"linh","tuoi":20}]
class HTTP4 (BaseModel):
    ten:str
    tuoi:int
class HTTP4_tuoi(BaseModel):
    ds:list[HTTP]
@app.get("/HTTP4_tuoi")
def check_tentuoi(tuoi_min:int,ten:str):
    dstentuoi=[]
    for hs in ds:
        if hs["ten"]==ten and hs["tuoi"] >= tuoi_min:
            dstentuoi.append({"ten":hs["ten"],"tuoi_min":hs["tuoi"]})    
    if len(dstentuoi)==0:
        raise HTTPException(status_code=404,detail="k tìm thấy hs phù hợp")
    return dstentuoi


from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
ds=[{"ten":"thien","tuoi":30},{"ten":"linh","tuoi":65},{"ten":"linh","tuoi":30},{"ten":"linh","tuoi":20}]
class HTTP5 (BaseModel):
    ten:str
    tuoi:int
class HTTP5_tuoi(BaseModel):
    ds:list[HTTP]
@app.get("/HTTP5_tuoi")
def check_tentuoi(ten:str,tuoi_min:int,tuoi_max:int):
    dsmaxmin=[]
    for hs in ds:
        if hs["ten"]== ten and tuoi_min <= hs["tuoi"] <= tuoi_max:
            dsmaxmin.append({"ten":hs["ten"],"tuoi":hs["tuoi"]})
    if len(dsmaxmin)==0:
        raise HTTPException(status_code=404,detail="k tìm thấy tên tuoi phù hợp")
    return dsmaxmin

        

    
        
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
ds=[{"ten":"thien","tuoi":30},{"ten":"linh truong","tuoi":65},{"ten":"linh như","tuoi":30},{"ten":"linh thảo","tuoi":20}]
class HTTP6 (BaseModel):
    ten:str
    tuoi:int
class HTTP6_tuoi(BaseModel):
    ds:list[HTTP]
@app.get("/HTTP6_tuoi")
def check_tentuoi(keyword:str,tuoi_min:int,tuoi_max:int):
    dsmaxmin=[]
    for hs in ds:
        if keyword.lower() in hs["ten"].lower() and tuoi_min <= hs["tuoi"] <= tuoi_max:
            dsmaxmin.append({"ten":hs["ten"],"tuoi":hs["tuoi"]})
    if len(dsmaxmin)==0:
        raise HTTPException(status_code=404,detail="k tìm thấy tên tuoi phù hợp")
    return dsmaxmin      



from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
ds=[{"ten":"thien","tuoi":30},{"ten":"nhi","tuoi":65},{"ten":"linh","tuoi":30},{"ten":"linh","tuoi":20}]
class HTTP7 (BaseModel):
    ten:str
    tuoi:int
class HTTP7_tuoi(BaseModel):
    ds:list[HTTP]
@app.get("/HTTP7_tuoi")
def check_tentuoi(ten:str,tuoi_min:int):
    dsten=[]
    for hs in ds:
        if hs["tuoi"]>= tuoi_min and hs["ten"]== ten:
            dsten.append({"ten":hs["ten"]})
        raise HTTPException(status_code=404,detail="k tìm thấy tên hs")
    return dsten



from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
ds=[{"ten":"thien","tuoi":30},{"ten":"nhi linh","tuoi":65},{"ten":"linh ngọc","tuoi":50},{"ten":"linh linh","tuoi":40}]
class HTTP8 (BaseModel):
    ten:str
    tuoi:int
class HTTP8_tuoi(BaseModel):
    ds:list[HTTP]
@app.get("/HTTP8_tuoi")
def check_tentuoi(keyword:str,tuoi_min:int):
    dsten=[]
    for hs in ds:
        if keyword.lower() in hs["ten"].lower() and hs["tuoi"] >= tuoi_min:
            dsten.append({"ten":hs["ten"]})
    if len(dsten) == 0:
        raise HTTPException(status_code=404,detail=" k tìm thấy hs")
    return dsten



from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
ds=[{"ten":"thien","tuoi":30},{"ten":"nhi linh","tuoi":20},{"ten":"linh ngọc","tuoi":40},{"ten":"linh linh","tuoi":40}]
class HTTP9 (BaseModel):
    ten:str
    tuoi:int
class HTTP9_tuoi(BaseModel):
    ds:list[HTTP]
@app.get("/HTTP9_tuoi")
def check_tentuoi(tuoi:int):
    demtuoi =0
    dsten=[]
    for hs in ds:
        if hs["tuoi"]>= tuoi:
            demtuoi += 1
            dsten.append({"ten":hs["ten"]})
    if demtuoi ==0:
        raise HTTPException(status_code=404,detail="k có hs nào tuổi >=")
    return {"ten":dsten,"tong số hs":demtuoi}


from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
ds=[{"ten":"thien","tuoi":30},{"ten":"nhi linh","tuoi":20},{"ten":"linh ngọc","tuoi":40},{"ten":"linh linh","tuoi":40}]
class HTTP10 (BaseModel):
    ten:str
    tuoi:int
class HTTP10_tuoi(BaseModel):
    ds:list[HTTP]
@app.get("/HTTP10_tuoi")
def check_tentuoi(tuoi:int):
    demtuoi =0
    dsten=[]
    for hs in ds:
        if hs["tuoi"]== tuoi:
            demtuoi += 1
            dsten.append({"ten":hs["ten"]})
    if demtuoi ==0:
        raise HTTPException(status_code=404,detail="k có hs nào bằng tuoi nhập vào ")
    return {"ten":dsten,"tong số hs":demtuoi}




from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
ds=[{"ten":"thien","tuoi":30},{"ten":"nhi linh","tuoi":20},{"ten":"linh ngọc","tuoi":40},{"ten":"linh linh","tuoi":40}]
class HTTP11 (BaseModel):
    ten:str
    tuoi:int
class HTTP11_tuoi(BaseModel):
    ds:list[HTTP]
@app.get("/HTTP11_tuoi")
def check_tentuoi(tuoi:int):
    demtuoi =0
    dsten=[]
    for hs in ds:
        if hs["tuoi"] <= tuoi:
            demtuoi += 1
            dsten.append({"ten":hs["ten"]})
    if demtuoi ==0:
        raise HTTPException(status_code=404,detail="k có hs nào <= tuoi nhập vào ")
    return {"ten":dsten,"tong số hs":demtuoi} 





from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class hoc_sort(BaseModel):
    ten:str
    tuoi:int
class sort (BaseModel):
    ds:list[hoc_sort]
ds=[hoc_sort(ten="thien",tuoi=30),hoc_sort (ten="nhilinh",tuoi=20),hoc_sort(ten="linh ngọc",tuoi=40),hoc_sort(ten="linh linh",tuoi=40)]
@app.get("/hocsort1")
def hoc_sort():
    ds.sort(key=lambda hs: hs.tuoi)
    return ds



from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class hoc_sort(BaseModel):
    ten:str
    tuoi:int
class sort (BaseModel):
    ds:list[hoc_sort]
ds=[hoc_sort(ten="thien",tuoi=30),hoc_sort (ten="nhilinh",tuoi=20),hoc_sort(ten="linh ngọc",tuoi=40),hoc_sort(ten="linh linh",tuoi=40)]
@app.get("/hocsort2")
def hoc_sort():
    ds.sort(key=lambda hs: hs.ten)
    return ds
   
   
    

from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class hoc_sort(BaseModel):
    ten:str
    tuoi:int
class sort (BaseModel):
    ds:list[hoc_sort]
ds=[hoc_sort(ten="thien",tuoi=30),hoc_sort (ten="nhilinh",tuoi=20),hoc_sort(ten="linh ngọc",tuoi=40),hoc_sort(ten="linh linh",tuoi=40)]
@app.get("/hocsort3")
def hoc_sort():
    ds.sort(key=lambda hs: hs.tuoi,reverse=True)
    return ds  
   
   
   
from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class hoc_sort(BaseModel):
    ten:str
    tuoi:int
class sort (BaseModel):
    ds:list[hoc_sort]
ds=[hoc_sort(ten="thien",tuoi=30),hoc_sort (ten="nhilinh",tuoi=20),hoc_sort(ten="ngọc",tuoi=40),hoc_sort(ten="linh linh",tuoi=40)]
@app.get("/hocsort4")
def hoc_sort():
    ds.sort(key=lambda hs:(hs.tuoi,hs.ten))
    return ds  
       

from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class hoc_sort(BaseModel):
    ten:str
    tuoi:int
class sort (BaseModel):
    ds:list[hoc_sort]
ds=[hoc_sort(ten="thien",tuoi=10),hoc_sort (ten="nhilinh",tuoi=20),hoc_sort(ten="ngọc",tuoi=30),hoc_sort(ten="linh linh",tuoi=40)]
@app.get("/hocsort6")
def hoc_sort(tuoi:int,skip:int,limit:int):
    dsten=[]
    for hs in ds:
        if hs.tuoi >= tuoi:
            dsten.append({"ten":hs.ten,"tuoi":hs.tuoi})
            dsten.sort(key=lambda hs: hs["tuoi"])
    if dsten ==0:
        raise HTTPException(status_code=404,detail="k tìm thấy học sinh nào ")
    return {"ds lọc": dsten[skip:limit]}   



from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class hoc_sort(BaseModel):
    ten:str
    tuoi:int
class sort (BaseModel):
    ds:list[hoc_sort]
ds=[hoc_sort(ten=" nhi thien",tuoi=10),hoc_sort (ten="nhi Linh",tuoi=20),hoc_sort(ten="Ngọc nhi",tuoi=20),hoc_sort(ten="linh nhi",tuoi=40)]
@app.get("/hocsort7")
def hoc_sort(keyword:str,tuoi:int,skip:int,limit:int):
    dsten=[]
    for hs in ds:
        if hs.tuoi >= tuoi and keyword.lower() in hs.ten.lower():
            dsten.append({"ten":hs.ten,"tuoi":hs.tuoi})
            dsten.sort(key=lambda hs: (hs["tuoi"],hs["ten"]))
    if dsten == 0:
        raise HTTPException(status_code=404,detail="k có hs nào phù hợp")
    return {"ds":dsten,"tong tìm dc hs":len(dsten),"tong hiển thị":len(dsten[skip:skip+limit]),"dữ liệu cần":dsten[skip:skip+limit]}


from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class hoc_sort(BaseModel):
    ten:str
    tuoi:int
class sort (BaseModel):
    ds:list[hoc_sort]
ds=[hoc_sort(ten="nhi thien",tuoi=10),hoc_sort(ten="nhi Linh",tuoi=20),hoc_sort(ten="Ngọc nhi",tuoi=20),hoc_sort(ten="linh nhi",tuoi=40)]
@app.get("/hocsort8")
def hoc_sort(keyword:str,tuoi:int,skip:int,limit:int):
    dstentuoi=[]
    for hs in ds:
        if keyword.lower() in hs.ten.lower() and hs.tuoi >= tuoi:
            dstentuoi.append({"ten":hs.ten,"tuoi":hs.tuoi})
            dstentuoi.sort(key=lambda hs: (hs["tuoi"],hs["ten"]))
            tuoi_lon_nhat=dstentuoi[-1]["tuoi"]
            tuoi_nho_nhat=dstentuoi[0]["tuoi"]
    if len(dstentuoi) ==0:
        raise HTTPException(status_code=404,detail="k tìm thấy hs phù hợp")
    return{"ds":dstentuoi,"tong tìm được":len(dstentuoi),"tổng hiển thị kq":len(dstentuoi[skip:skip+limit]),"max":tuoi_lon_nhat,"min":tuoi_nho_nhat,"dữ liệu cần":dstentuoi[skip:skip+limit]}


   
from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class hoc_sort(BaseModel):
    ten:str
    tuoi:int
class sort (BaseModel):
    ds:list[hoc_sort]
ds=[hoc_sort(ten="nhi thien",tuoi=10),hoc_sort(ten="nhi Linh",tuoi=20),hoc_sort(ten="Ngọc nhi",tuoi=20),hoc_sort(ten="linh nhi",tuoi=40)]
@app.get("/hocsort9")
def hoc_sort(skip:int,limit:int,keyword:str|None=None,tuoi:int|None=None,reverse:bool ="False"):
    dstentuoi=[]
    max_tuoi=0
    min_tuoi=0
    for hs in  ds:
        if keyword == None:
            if hs.tuoi >= tuoi:
                dstentuoi.append({"ten":hs.ten,"tuoi":hs.tuoi})
                dstentuoi.sort (key=lambda hs: hs["tuoi"],reverse=reverse)
        if keyword != None:
            if keyword.lower() in hs.ten.lower() and hs.tuoi >= tuoi:
                dstentuoi.append({"ten":hs.ten,"tuoi":hs.tuoi})
                dstentuoi.sort(key=lambda hs: (hs["tuoi"],hs["ten"]),reverse=reverse)        
    if reverse:
            max_tuoi= dstentuoi[0]["tuoi"]
            min_tuoi=dstentuoi[-1]["tuoi"]
    else:
            max_tuoi=dstentuoi[-1]["tuoi"]
            min_tuoi=dstentuoi[0]["tuoi"]
    if len(dstentuoi)==0:
        raise HTTPException(status_code=404,detail= " k tìm thây học sinh")
    return{"ds":dstentuoi,"tong kq tìm được":len(dstentuoi),"tuoi max":max_tuoi,"tuoi min":min_tuoi,"pagination":dstentuoi[skip:limit+skip]}
                       

from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class hoc_sort(BaseModel):
    ten:str
    tuoi:int
class sort (BaseModel):
    ds:list[hoc_sort]
ds=[hoc_sort(ten="nhi thien",tuoi=10),hoc_sort(ten="nhi Linh",tuoi=20),hoc_sort(ten="Ngọc nhi",tuoi=20),hoc_sort(ten="linh nhi",tuoi=40)]
@app.get("/hocsort10")
def hoc_sort(sort_by:str,reverse:bool):
    dstentuoi=[]
    for hs in ds:
        dstentuoi.append({"ten":hs.ten,"tuoi":hs.tuoi})
    if sort_by =="ten":
        dstentuoi.sort(key= lambda hs: hs["ten"],reverse=reverse)
    elif sort_by =="tuoi":
        dstentuoi.sort(key=lambda hs: hs["tuoi"],reverse=reverse)
    return {"dstentuoi":dstentuoi}

from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class hoc_sort(BaseModel):
    ten:str
    tuoi:int
class sort (BaseModel):
    ds:list[hoc_sort]
ds=[hoc_sort(ten="nhi thien",tuoi=10),hoc_sort(ten="nhi Linh",tuoi=20),hoc_sort(ten="Ngọc nhi",tuoi=20),hoc_sort(ten="linh nhi",tuoi=40)]
@app.get("/hocsort11")
def hoc_sort(sort_by:str,reverse:bool,skip:int,limit:int):
    dstentuoi=[]
    for hs in ds:
        dstentuoi.append({"ten":hs.ten,"tuoi":hs.tuoi})
        if sort_by == "tuoi":
            dstentuoi.sort(key= lambda hs: (hs["tuoi"],hs["ten"]),reverse=reverse)
    return {"dstentuoi":dstentuoi,"kq lấy":dstentuoi[skip:limit+skip]}



from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class hoc_sort(BaseModel):
    ten:str
    tuoi:int
class sort (BaseModel):
    ds:list[hoc_sort]
ds=[hoc_sort(ten="nhi thien",tuoi=10),hoc_sort(ten="nhi Linh",tuoi=20),hoc_sort(ten="Ngọc nhi",tuoi=30),hoc_sort(ten="linh nhi",tuoi=40)]
@app.get("/hocsort12")
def hoc_sort(skip:int,limit:int,keyword:str|None=None,tuoi:int | None=None):    
    dstentuoi=[]
    dem =0
    max_tuoi =0
    max_ten=""
    min_tuoi=float("inf") 
    min_ten=""
    dsmin=[]
    dsmax=[]
    max2_tuoi=0
    max2_ten=""
    dsmax2=[]
    min2_tuoi=float("inf")
    min2_ten=""
    dsmin2=[]
    max3_tuoi=0
    min3_ten=""
    dsmax3=[]
    for hs in ds:
        if keyword ==None:
            if hs.tuoi >= tuoi:
                dem += 1
                dstentuoi.append({"ten":hs.ten,"tuoi":hs.tuoi})
                dstentuoi.sort(key=lambda hs: (hs["tuoi"],["ten"]))
        elif keyword != None:
            if keyword.lower() in hs.ten.lower() and hs.tuoi >= tuoi:
                dem += 1
                dstentuoi.append({"ten":hs.ten,"tuoi":hs.tuoi})
                dstentuoi.sort(key=lambda hs: (hs["ten"],["tuoi"]))
    if len(dstentuoi) ==0:
        raise HTTPException(status_code=404,detail="k tìm được hs ") 
    for i in dstentuoi:
        if i["tuoi"]> max_tuoi:
            max_tuoi= i["tuoi"]
            max_ten= i["ten"]
    for i in dstentuoi:
        if i["tuoi"]==max_tuoi:
            dsmax.append({"tenmax":i["ten"],"tuoi":i["tuoi"]})
    for i in dstentuoi:
        if i["tuoi"]<max_tuoi and i["tuoi"]>max2_tuoi:
            max2_tuoi=i["tuoi"]
            max2_ten= i["ten"]
    for i in dstentuoi:
        if i["tuoi"]==max2_tuoi:
            dsmax2.append({"tenmax2":i["ten"],"tuoimax2":i["tuoi"]})
    for i in dstentuoi:
        if i["tuoi"]< max2_tuoi and i["tuoi"]>max3_tuoi:
            max3_tuoi=i["tuoi"]
            max3_ten=i["ten"]
    for i in dstentuoi:
        if i["tuoi"]== max3_tuoi:
            dsmax3.append({"tenmax3":i["ten"],"tuoimax3":i["tuoi"]})
    for i in dstentuoi:
        if i["tuoi"] <min_tuoi:
            min_tuoi = i["tuoi"]
            min_ten = i["ten"]
    for i in dstentuoi:   
        if i["tuoi"]== min_tuoi:
            dsmin.append({"tenmin":i["ten"],"tuoi":i["tuoi"]})
    for i in dstentuoi:
        if i["tuoi"]> min_tuoi and i["tuoi"]< min2_tuoi:
            min2_tuoi=i["tuoi"]
            min2_ten=i["ten"]
        if i["tuoi"] == min2_tuoi:
            dsmin2.append({"tenmin2":i["ten"],"tuoimin2":i["tuoi"]})
    return {"ds":dstentuoi,"tổng số hs sau lọc":len(dstentuoi[skip: skip+limit]),"tonghs":len(dstentuoi),"tong hs đạt":dem,"max":dsmax,"dsmin":dsmin,"dsmax2":dsmax2,"dsmin2":dsmin2,"dsmax3":dsmax3}


from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class hoc_sort(BaseModel):
    ten:str
    tuoi:int
class sort (BaseModel):
    ds:list[hoc_sort]
ds=[hoc_sort(ten="nhi thien",tuoi=10),hoc_sort(ten="nhi Linh",tuoi=50),hoc_sort(ten="Ngọc nhi",tuoi=40),hoc_sort(ten="linh nhi",tuoi=40)]
@app.get("/hocsort13")
def hoc_sort(skip:int,limit:int,tuoi:int | None=None):
    dstuoi=[]
    for hs in ds:
        if hs.tuoi >= tuoi:
            dstuoi.append({"ten":hs.ten,"tuoi":hs.tuoi})
            dstuoi.sort(key=lambda hs: (hs["tuoi"],["ten"]),reverse= True)
    top3= dstuoi[skip:skip+limit]
    return top3



from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class hoc_sort(BaseModel):
    ten:str
    tuoi:int
class sort (BaseModel):
    ds:list[hoc_sort]
ds=[hoc_sort(ten="nhi thien",tuoi=10),hoc_sort(ten="nhi Linh",tuoi=50),hoc_sort(ten="Ngọc nhi",tuoi=40),hoc_sort(ten="linh nhi",tuoi=40),hoc_sort(ten="An An",tuoi=40)]
@app.get("/hocsort14")
def hoc_sort(skip:int,limit:int,tuoi:int | None=None):
    dstuoi=[]
    for hs in ds:
        if hs.tuoi >= tuoi:
            dstuoi.append({"ten":hs.ten,"tuoi":hs.tuoi})
            dstuoi.sort(key=lambda hs: (-hs["tuoi"],hs["ten"].casefold()))
    top3= dstuoi[skip:skip+limit]
    return top3



from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class hoc_sort(BaseModel):
    ten:str
    tuoi:int
class sort (BaseModel):
    ds:list[hoc_sort]
ds=[hoc_sort(ten="nhi thien",tuoi=10),hoc_sort(ten="nhi Linh",tuoi=50),hoc_sort(ten="Ngọc nhi",tuoi=40),hoc_sort(ten="linh nhi",tuoi=40),hoc_sort(ten="An An",tuoi=40)]
@app.get("/hocsort15")
def hoc_sort(skip:int,limit:int,tuoi:int | None=None, keyword:str|None=None,reverse:bool="False"):
    dstentuoi=[]
    dsloc=[]
    max_tuoi=0
    max_ten=""
    dsmaxtuoi=[]
    min_tuoi= float("inf")
    min_ten=""
    dsmintuoi=[]
    for hs in ds:
        if keyword == None:
            if hs.tuoi>= tuoi:
                dstentuoi.append({"ten":hs.ten,"tuoi":hs.tuoi})
                dstentuoi.sort(key=lambda hs: hs["tuoi"],reverse=reverse)
            dsloc=dstentuoi
        if keyword != None and keyword.lower() in hs.ten.lower():
            dstentuoi.append({"ten":hs.ten,"tuoi":hs.tuoi})
            dstentuoi.sort(key=lambda hs: hs["ten"],reverse=reverse)
            dsloc=dstentuoi
    if len(dstentuoi)==0:
        raise HTTPException(status_code=404,detail=" k tìm đươc hs ")
    for hs in ds:
        dsloc.sort(key=lambda hs: (-hs["tuoi"],hs["ten"].casefold()))
    for i in dstentuoi:
        if i["tuoi"]>max_tuoi:
            max_tuoi=i["tuoi"]
            max_ten=i["ten"]
    for i in dstentuoi:
        if i["tuoi"]== max_tuoi:
            dsmaxtuoi.append({"tenmax":i["ten"],"tuoimax":i["tuoi"]})
    for i in dstentuoi:
        if i["tuoi"]< min_tuoi:
            min_tuoi=i["tuoi"]
            min_ten=i["ten"]
    for i in dstentuoi:
        if i["tuoi"]==min_tuoi:
            dsmintuoi.append({"tenmin":i["ten"],"tuoimin":i["tuoi"]})
    return {"dstentuoi":dstentuoi,"dsloc":dsloc,"dsmax":dsmaxtuoi,"dsmin":dsmintuoi}


from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class monhoc(BaseModel):
    tenmon:str
    diem:float
class hocsinh(BaseModel):
    ten:str
    ds_mon:list[monhoc]
class lophoc(BaseModel):
    ds:list[hocsinh] 
@app.post("/onlaitonghop")
def tonghop(data:lophoc):
    demmon =0
    demhs =0
    tongdiem =0
    dtb =0
    max_diem=0
    dsmax=[]
    max_mon=""
    ten_max=""
    min_diem =float("inf")
    dsmin=[]
    min_mon=""
    ten_min=""
    ds_dtb_moihs=[]
    dsmaxdtb=[]
    max_dtb=0
    tenmax_dtb=""
    for hs in data.ds:
        demhs += 1 
        dtb_moihs=0
        demmon_hs=0
        tongdiem_hs=0
        for i in hs.ds_mon:
            demmon +=1
            tongdiem += i.diem
            dtb = tongdiem/demhs
            demmon_hs += 1
            tongdiem_hs += i.diem
            dtb_moihs= tongdiem_hs/ demmon_hs
        ds_dtb_moihs.append({"ten":hs.ten,"dtb":dtb_moihs})
        if dtb_moihs > max_dtb:
            max_dtb = dtb_moihs
            tenmax_dtb =hs.ten
            dsmaxdtb.append({"ten":hs.ten,"dtb":dtb_moihs})
        elif dtb_moihs == max_dtb:
            dsmaxdtb.append({"ten":hs.ten,"dtb":dtb_moihs})
        for i in hs.ds_mon:
            if i.diem > max_diem:
                max_diem = i.diem
                max_mon=[i.tenmon]
                ten_max = [hs.ten]
                dsmax=[]
                dsmax.append({"ten":hs.ten,"max_mon":i.tenmon,"diem":i.diem})
            elif i.diem == max_diem:
                dsmax.append({"ten":hs.ten,"max_mon":i.tenmon,"diem":i.diem})
            if i.diem < min_diem:
                min_diem=i.diem
                min_mon=[i.tenmon]
                ten_min=[hs.ten]
                dsmin=[]
                dsmin.append({"ten":hs.ten,"min_mon":i.tenmon,"diem":i.diem})
            elif i.diem ==min_diem:
                dsmin.append({"ten":hs.ten,"min_mon":i.tenmon,"diem":i.diem})
    return {"demhs":demhs,"demmon":demmon,"tongdiem":tongdiem,"dtb":dtb,"hs điểm lớn nhất":dsmax,"hs điểm nhỏ nhất":dsmin,"dtb_moihs":ds_dtb_moihs,"dsmaxdtb":dsmaxdtb}

        


from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class monhoc(BaseModel):
    tenmon:str
    diem:float
class hocsinh(BaseModel):
    ten:str
    ds_mon:list[monhoc]
class lophoc(BaseModel):
    ds:list[hocsinh] 
@app.post("/nestedpost")
def tonghop(data:lophoc):
    dsmaxtong=[]
    max_tong=0
    tenmax_tong=""
    dsdiemtong=[]
    min_tong= float("inf")
    tenmin_tong=""
    dsmintong=[]
    dshsdat=[]
    max_demhsdat=0
    tenmax_demhsdat=""
    dsmaxhsdat=[]
    max_5=0
    tenmax5=""
    dsmax5=[]
    for hs in data.ds:
        tongdiem_moihs=0 
        demhsdat =0
        dem5=0  
        for i in hs.ds_mon:
            tongdiem_moihs += i.diem
        dsdiemtong.append({"ten":hs.ten,"diem":tongdiem_moihs})
        if tongdiem_moihs >max_tong:
            max_tong= tongdiem_moihs
            tenmax_tong=hs.ten
            dsmaxtong=[]
            dsmaxtong.append({"ten":hs.ten,"diem tong":tongdiem_moihs})
        elif tongdiem_moihs == max_tong:
            dsmaxtong.append({"ten":hs.ten,"diem tong":tongdiem_moihs})
        if tongdiem_moihs <min_tong:
            min_tong=tongdiem_moihs
            tenmin_tong=hs.ten
            dsmintong=[]
            dsmintong.append({"ten":hs.ten,"diemtong":tongdiem_moihs})
        elif tongdiem_moihs == min_tong:
            dsmintong.append({"ten":hs.ten,"diemtong":tongdiem_moihs})
        for i in hs.ds_mon:
            if i.diem >= 8:
                demhsdat += 1 
        dshsdat.append({"ten":hs.ten,"demhsdat":demhsdat})
        if demhsdat > max_demhsdat:
            max_demhsdat = demhsdat
            tenmax_demhsdat =hs.ten
            dsmaxhsdat.append({"ten":hs.ten,"dsmaxhsdat8":demhsdat})
        for i in hs.ds_mon:
            if i.diem <= 5:
                dem5 += 1
        if dem5 > max_5:
            max_5 =dem5
            tenmax5=hs.ten
            dsmax5=[]
            dsmax5.append({"ten":hs.ten,"max5":dem5})
        elif dem5 == max_5:
            dsmax5.append({"ten":hs.ten,"max5":dem5})            
    return {"dsdiemtong":dsdiemtong,"maxtong":dsmaxtong,"mintong":dsmintong,"hs trên 8":dshsdat,"dsmaxhsdat":dsmaxhsdat,"dsmax5":dsmax5}

from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class monhoc(BaseModel):
    tenmon:str
    diem:float
class hocsinh(BaseModel):
    ten:str
    ds_mon:list[monhoc]
class lophoc(BaseModel):
    ds:list[hocsinh] 
@app.post("/nestedpostmoi")
def tonghop(data:lophoc):
    max_diem=0
    tenmax_mon=""
    tenmax_diem=""
    dsmaxdiem=[]
    min_diem=float("inf")
    tenmin_mon=""
    tenmin_diem=""
    dsmindiem=[]
    for hs in data.ds:
        for i in hs.ds_mon:
            if i.diem > max_diem:
                max_diem= i.diem
                tenmax_mon=i.tenmon
                tenmax_diem=hs.ten
                dsmaxdiem=[]
                dsmaxdiem.append({"ten":hs.ten,"Môn":i.tenmon,"diem":i.diem})
            elif i.diem == max_diem:
                dsmaxdiem.append({"ten":hs.ten,"Môn":i.tenmon,"diem":i.diem})
            if i.diem < min_diem:
                min_diem = i.diem
                tenmin_mon=i.tenmon
                tenmin_diem=hs.ten
                dsmindiem.append({"ten":hs.ten,"Môn":i.tenmon,"diem":i.diem})
            elif i.diem == min_diem:
                dsmindiem.append({"ten":hs.ten,"Môn":i.tenmon,"diem":i.diem})
    return{"dsmaxdiem":dsmaxdiem,"dsmindiem":dsmindiem}



from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class monhoc(BaseModel):
    tenmon:str
    diem:float
class hocsinh(BaseModel):
    ten:str
    ds_mon:list[monhoc]
class lophoc(BaseModel):
    ds:list[hocsinh] 
@app.post("/nested15")
def tonghop(data:lophoc):
    dshsgioi=[]
    dshskha=[]
    dshstb=[]
    dshsyeu=[]
    for hs in data.ds:
        tongdiem=0
        demhs=0
        dtb_hs=0
        demloai =0
        for i in hs.ds_mon:
            tongdiem += i.diem
            demhs += 1
        dtb_hs = tongdiem/demhs 
        if dtb_hs >= 8:
            ten8 = hs.ten
            dtb8 =dtb_hs
            demloai += 1
            dshsgioi.append({"ten":hs.ten,"dtb":dtb8 , "tong":demloai})
        elif 6.5 <= dtb_hs < 8:
            ten7 =hs.ten
            dtb7 =dtb_hs
            demloai += 1
            dshskha.append({"ten":hs.ten,"dtb":dtb7,"tong":demloai})
        elif 5<= dtb_hs <6.5:
            ten6 =hs.ten
            dtb6 = dtb_hs
            demloai += 1
            dshstb.append({"ten":hs.ten,"dtb":dtb6,"tong":demloai})
        else:
            ten5 = hs.ten
            dtb5 = dtb_hs
            demloai += 1
            dshsyeu.append({"ten":hs.ten,"dtb":dtb5,"tong":demloai})
    return {"gioi":dshsgioi,"kha":dshskha,"tb":dshstb,"yeu":dshsyeu}


from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class monhoc(BaseModel):
    tenmon:str
    diem:float
class hocsinh(BaseModel):
    ten:str
    ds_mon:list[monhoc]
class lophoc(BaseModel):
    ds:list[hocsinh] 
@app.post("/nested16")
def tonghop(data:lophoc):
    ds8=[]
    ten8 =""
    dsdtbgioi=[]
    tendtbgioi=""
    
    for hs in data.ds:
        co_mon_duoi_5=False
        dem8=0
        demhs =0
        tonghs= 0
        dtb_hs = 0
        for i in hs.ds_mon:
            demhs += 1
            tonghs += i.diem
            dtb_hs = tonghs/demhs
            if i.diem >= 8:
                ten8 = hs.ten
                dem8 +=1
        if dem8 >= 2:
            ds8.append({"ten":ten8,"dem8":dem8}) 
        for i in hs.ds_mon:
            if i.diem < 5:
                co_mon_duoi_5 =True
        if dtb_hs >= 8 and not co_mon_duoi_5:
            dsdtbgioi.append({"ten":hs.ten,"dtb":dtb_hs})
    return {"ds8":ds8,"dsdtbgioi":dsdtbgioi}



from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class ten_mon (BaseModel):    
    tenmon: str
    diem:float
class lophoc(BaseModel):
    tenlop:str
    tenhs:str
    hs:list[ten_mon]
class lop(BaseModel):
    ds:list[lophoc]
@app.post("/lophoc10")
def lophoc10 (data:lop):
    dsdtb= {}
    for hs in data.ds:
        tongdiem=0
        diemhs=0   
        dtb_hs=0
        for i in hs.hs:
            tongdiem += i.diem
            diemhs += 1
        dtb_hs= tongdiem/diemhs
        if hs.tenlop not in dsdtb:
            dsdtb[hs.tenlop]=[]
        dsdtb[hs.tenlop].append({"ten":hs.tenhs,"dtb":dtb_hs})
    return dsdtb




from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class ten_mon (BaseModel):    
    tenmon: str
    diem:float
class lophoc(BaseModel):
    tenlop:str
    tenhs:str
    hs:list[ten_mon]
class lop(BaseModel):
    ds:list[lophoc]
@app.post("/lophoc11")
def lophoc10 (data:lop):
    dsdtb={}
    for hs in data.ds:
        tongdiem=0
        diemhs=0
        dtb=0
        for i in hs.hs:
            tongdiem += i.diem
            diemhs += 1
            dtb = tongdiem/diemhs
        if hs.tenlop not in dsdtb:
            dsdtb[hs.tenlop]={"tonghs":0,"hsdat":0,"danhsach":[]}
        dsdtb[hs.tenlop]["tonghs"]+= 1
        if dtb >= 8:
            dsdtb[hs.tenlop]["hsdat"] += 1
            dsdtb[hs.tenlop]["danhsach"].append({"ten":hs.tenhs,"dtb":dtb})
    return dsdtb



from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class ten_mon (BaseModel):    
    tenmon: str
    diem:float
class lophoc(BaseModel):
    tenlop:str
    tenhs:str
    hs:list[ten_mon]
class lop(BaseModel):
    ds:list[lophoc]
@app.post("/lophoc12")
def lophoc10 (data:lop):
    dsdtb={}
    for hs in data.ds:
        tongdiem=0
        diemhs=0
        dtb=0
        for i in hs.hs:
            tongdiem += i.diem
            diemhs += 1
            dtb = tongdiem/diemhs
        if hs.tenlop not in dsdtb:
            dsdtb[hs.tenlop]={"ten":hs.tenhs,"dtb":dtb}
        else:
            if dtb > dsdtb[hs.tenlop]["dtb"]:
                dsdtb[hs.tenlop]={"ten":hs.tenhs,"dtbmax":dtb}
    return dsdtb



            
from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class ten_mon (BaseModel):    
    tenmon: str
    diem:float
class lophoc(BaseModel):
    tenlop:str
    tenhs:str
    hs:list[ten_mon]
class lop(BaseModel):
    ds:list[lophoc]
@app.post("/lophoc13")
def lophoc10 (data:lop):
    dsdtb={}
    for hs in data.ds:
        tongdiem=0
        diemhs=0
        dtb=0
        for i in hs.hs:
            tongdiem += i.diem
            diemhs += 1
            dtb = tongdiem/diemhs
        if hs.tenlop not in dsdtb:
            dsdtb[hs.tenlop]={"max":dtb,"danhsach":[{"ten":hs.tenhs,"dtbmax":dtb}]}
        else:
            if dtb > dsdtb[hs.tenlop]["max"] :
                dsdtb[hs.tenlop]["max"]=dtb
                dsdtb[hs.tenlop]["danhsach"]=[{"ten":hs.tenhs,"dtbmax":dtb}]
            elif dtb == dsdtb[hs.tenlop]["max"] :
                dsdtb[hs.tenlop]["danhsach"].append({"ten":hs.tenhs,"dtbmax":dtb})
    return dsdtb



from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class ten_mon (BaseModel):    
    tenmon: str
    diem:float
class lophoc(BaseModel):
    tenlop:str
    tenhs:str
    hs:list[ten_mon]
class lop(BaseModel):
    ds:list[lophoc]
@app.post("/lophoc14")
def lophoc10 (data:lop):
    dsdtb={}
    for hs in data.ds:
        tongdiem=0
        diemhs=0
        dtb=0
        for i in hs.hs:
            tongdiem += i.diem
            diemhs += 1
            dtb = tongdiem/diemhs
        if hs.tenlop not in dsdtb:
            dsdtb[hs.tenlop]={"min":dtb,"danhsach":[{"ten":hs.tenhs,"dtb":dtb}]}
        else:
            if dtb < dsdtb[hs.tenlop]["min"]:
                dsdtb[hs.tenlop]["min"]=dtb
                dsdtb[hs.tenlop]["danhsach"]={"ten":hs.tenhs,"dtb":dtb}
            elif dtb== dsdtb[hs.tenlop]["min"]:
                dsdtb[hs.tenlop]["danhsach"].append({"ten":hs.tenhs,"dtb":dtb})
    return dsdtb




from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class ten_mon (BaseModel):    
    tenmon: str
    diem:float
class lophoc(BaseModel):
    tenlop:str
    tenhs:str
    hs:list[ten_mon]
class lop(BaseModel):
    ds:list[lophoc]
@app.post("/lophoc15")
def lophoc10 (data:lop):
    dsmon={}
    for hs in data.ds:
        for i in hs.hs:
            if hs.tenlop not in dsmon:
                dsmon[hs.tenlop]={"max":i.diem,"danhsach":[{"ten":hs.tenhs,"diem":i.diem}]}
            else:
                if i.diem > dsmon[hs.tenlop]["max"]:
                    dsmon[hs.tenlop]["max"]= i.diem
                    dsmon[hs.tenlop]["danhsach"]=[{"ten":hs.tenhs,"diem":i.diem}]
                elif i.diem == dsmon[hs.tenlop]["max"]:
                    dsmon[hs.tenlop]["danhsach"].append({"ten":hs.tenhs,"diem":i.diem})
    return dsmon  



from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class ten_mon (BaseModel):    
    tenmon: str
    diem:float
class lophoc(BaseModel):
    tenlop:str
    tenhs:str
    hs:list[ten_mon]
class lop(BaseModel):
    ds:list[lophoc]
@app.post("/lophoc15")
def lophoc10 (data:lop):
    ds5={}
    for hs in data.ds:
        dem5=0
        for i in hs.hs:
            if i.diem <5:
                dem5 += 1
        if hs.tenlop not in ds5:
            ds5[hs.tenlop]={"maxdem5":dem5,"danhsach":[{"ten":hs.tenhs,"duoi5":dem5}]}
        elif dem5 > ds5[hs.tenlop]["maxdem5"]:
            ds5[hs.tenlop]["maxdem5"]=dem5
            ds5[hs.tenlop]["danhsach"]=[{"ten":hs.tenhs,"duoi5":dem5}]
        elif dem5 ==ds5[hs.tenlop]["maxdem5"]:
            ds5[hs.tenlop]["danhsach"].append({"ten":hs.tenhs,"duoi5":dem5})
    return ds5


            

from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class tenmon(BaseModel):
    tenmon:str
    diem:float
class hocsinh(BaseModel):
    tenhs:str
    dsmon:list[tenmon]
class lophoc(BaseModel):
    tenlop:str
    dshs:list[hocsinh]
class ds(BaseModel):
    ds:list[lophoc]
@app.post("/tonghopgroupby")
def tonghop (data:ds):
    kq={}
    tongdat =0
    tongkhongdat =0
    for lop in data.ds:
        tonghslop =0
        tongdtblop=0
        tongdtbhs =0
        tonghs_all=0
        for hs in lop.dshs:
            tonghs_all += len(lop.dshs)
            tongdiem=0
            tongmon=0
            dtbmoihs=0
            for mon in hs.dsmon:
                tongdiem += mon.diem
                tongmon += 1
            dtbmoihs=tongdiem/tongmon
            tongdtbhs += dtbmoihs
            tonghslop += 1
            tongdtblop= tongdtbhs/tonghslop                        
            if lop.tenlop not in kq:
                kq[lop.tenlop]={"tonghs":len(lop.dshs),"max":dtbmoihs,"min":dtbmoihs,"dtblop":tongdtblop,"Đat":0,"Khongdat":0,"danhsachmax":[{"ten":hs.tenhs,"dtb":dtbmoihs}],"danhsachmin":[{"ten":hs.tenhs,"dtb":dtbmoihs}]}
            else:
                if dtbmoihs > kq[lop.tenlop]["max"]:
                    kq[lop.tenlop]["max"]=dtbmoihs
                    kq[lop.tenlop]["danhsachmax"]=[{"ten":hs.tenhs,"dtb":dtbmoihs}]
                elif dtbmoihs == kq[lop.tenlop]["max"]:
                    kq[lop.tenlop]["danhsachmax"].append({"ten":hs.tenhs,"dtb":dtbmoihs})
                if dtbmoihs < kq[lop.tenlop]["min"]:
                    kq[lop.tenlop]["min"]=dtbmoihs
                    kq[lop.tenlop]["danhsachmin"]=[{"ten":hs.tenhs,"dtb":dtbmoihs}]
                elif dtbmoihs == kq[lop.tenlop]["min"]:
                    kq[lop.tenlop]["danhsachmin"].append({"ten":hs.tenhs,"dtb":dtbmoihs})
            if dtbmoihs >= 5:
                kq[lop.tenlop]["Đat"] += 1
                tongdat += 1
            else:
                kq[lop.tenlop]["Khongdat"] += 1
                tongkhongdat += 1
            kq[lop.tenlop]["dtblop"]=tongdtblop
    return {"tonghs_all":tonghs_all,"kq":kq ,"Đạt":tongdat,"khongdat":tongkhongdat}


    


from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class tenmon(BaseModel):
    tenmon:str
    diem:float
class hocsinh(BaseModel):
    tenhs:str
    dsmon:list[tenmon]
class lophoc(BaseModel):
    tenlop:str
    dshs:list[hocsinh]
class ds(BaseModel):
    ds:list[lophoc]
@app.post("/tonghopgroupby2")
def tonghop (data:ds):
    kq={}
    
    for hs in data.ds:
        tongdiemlop =0
        demhslop =0
        dtbmoilop =0
        tongmon =0
        for i in hs.dshs:
            dtbhs =0
            demmon =0
            tongdiem=0
            tongmon += 1
            for k in i.dsmon:               
                tongdiem += k.diem
                demmon += 1
            dtbhs = tongdiem/demmon
            tongdiemlop += tongdiem
            demhslop += 1
            dtbmoilop = tongdiemlop/demhslop
            if hs.tenlop not in kq:
                kq[hs.tenlop]={"tonghs":len(hs.dshs),"tongmon":tongmon,"tongdiem":tongdiemlop,"dtblop":dtbmoilop,"hsgioi":[],"hskha":[],"hstb":[],"hsyeu":[]}
            if dtbhs  >= 8:
                kq[hs.tenlop]["hsgioi"].append(i.tenhs) 
            elif  6.5 <= dtbhs <8:
                    
                kq[hs.tenlop]["hskha"].append(i.tenhs)
            elif 5 <= dtbhs <6.5:
                kq[hs.tenlop]["hstb"].append(i.tenhs)
            else:
                kq[hs.tenlop]["hsyeu"].append(i.tenhs)
            kq[hs.tenlop]["tongmon"]=tongmon
            kq[hs.tenlop]["tongdiem"]=tongdiemlop
            kq[hs.tenlop]["dtblop"]=dtbmoilop
    return kq



from fastapi import FastAPI
from pydantic import BaseModel 
app= FastAPI()
class monhoc(BaseModel):
    ten_mon:str
    diem:float
class hocsinh(BaseModel):
    ten:str
    lop:str
    ds_mon:list[monhoc]
class dshs(BaseModel):
    ds:list[hocsinh]
@app.post("/tonghoppostgroupby35")
def check_tonghopgroupby(data:dshs):
    ds={}
    for hs in data.ds:  
        dtb=0
        tong =0
        dem = 0  
        for i in hs.ds_mon: 
            tong += i.diem
            dem += 1
        dtb = tong/dem 
        if hs.lop not in ds:
            ds[hs.lop]=[]

        ds[hs.lop].append({"ten":hs.ten,"dtb":dtb})
    for lop in ds:
        dtb2 =0
        max_dtb= ds[lop][0]["dtb"]
        min_dtb= ds[lop][0]["dtb"]
        for hs_2 in ds[lop]:
            dtb2 += hs_2["dtb"]
        dtb2 =dtb2/len(ds[lop])
        if hs_2["dtb"]>max_dtb:
            max_dtb= hs_2["dtb"]
        if hs_2["dtb"]<min_dtb:
            min_dtb = hs_2["dtb"]
        for item in ds[lop]:
            item["dtb2"] = dtb2
            item["maxdtb"]= max_dtb
            item["mindtb"]=min_dtb
    return{"ds":ds,"max":max_dtb,"min":min_dtb} 





from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class hoc_gb(BaseModel):
    lop:str
    ten:str
    dtb: float
class groupby(BaseModel):
    ds: list[hoc_gb]
@app.post("/hoc_groupby")
def hoc_groupby(data:groupby):
    kq={}
    tonghs =0
    for hs in data.ds:
        tonghs += 1
        if hs.lop not in kq:
            kq[hs.lop]={"slhs":0,"hsdat":0,"hschuadat":0,"dtb":hs.dtb}
            kq[hs.lop]["slhs"] += 1
        if kq[hs.lop]["dtb"] >= 5:
            kq[hs.lop]["hsdat"] += 1
        if kq[hs.lop]["dtb"] <= 5:
            kq[hs.lop]["hschuadat"] += 1
    return {"kq":kq,"tonghs":tonghs}


            
from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class hoc_gb(BaseModel):
    lop:str
    ten:str
    dtb: float
class groupby(BaseModel):
    ds: list[hoc_gb]
@app.post("/hoc_groupby123")
def hoc_groupby(data:groupby):
    kq={}
    for hs in data.ds:
        if hs.lop not in kq:
            kq[hs.lop]={"sltonghs":0,"tongdtb":0,"dtblop":0}
        kq[hs.lop]["sltonghs"] += 1
        kq[hs.lop]["tongdtb"]+= hs.dtb
        kq[hs.lop]["dtblop"]= kq[hs.lop]["tongdtb"]/kq[hs.lop]["sltonghs"]
    return kq   

from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class hoc_gb(BaseModel):
    lop:str
    ten:str
    dtb: float
class groupby(BaseModel):
    ds: list[hoc_gb]
@app.post("/hoc_groupby1234")
def hoc_groupby(data:groupby):
    kq={}
    for hs in data.ds:
        if hs.lop not in kq:
            kq[hs.lop]={"slhs":0,"maxdtb":hs.dtb,"mindtb":hs.dtb,"dsmax":[],"dsmin":[]}
        kq[hs.lop]["slhs"] += 1
        if hs.dtb >kq[hs.lop]["maxdtb"]:
            kq[hs.lop]["maxdtb"]= hs.dtb
            kq[hs.lop]["dsmax"]=[{"ten":hs.ten,"dtb":hs.dtb}]
        elif kq[hs.lop]["maxdtb"]== hs.dtb:
            kq[hs.lop]["dsmax"].append({"ten":hs.ten,"dtb":hs.dtb})
        if hs.dtb < kq[hs.lop]["mindtb"]:
            kq[hs.lop]["mindtb"]=hs.dtb
            kq[hs.lop]["dsmin"]=[{"ten":hs.ten,"dtb":hs.dtb}]
        elif kq[hs.lop]["mindtb"]== hs.dtb:
            kq[hs.lop]["dsmin"].append({"ten":hs.ten,"dtb":hs.dtb})
    return kq


from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class hoc_gb(BaseModel):
    lop:str
    ten:str
    dtb: float
class groupby(BaseModel):
    ds: list[hoc_gb]
@app.post("/hoc_groupby12345")
def hoc_groupby(data:groupby):
    kq={}
    dtbdat_all=0
    tongdat_all=0
    tongdiemchuadat=0
    for hs in data.ds:
        
        if hs.lop not in kq:
            kq[hs.lop]={"slhs":0,"tongdtb":0,"dtblop":0,"hsdat":0,"hschuadat":0,"tongdat":0,"dsmax":[],"dsmin":[],"maxdtb":hs.dtb,"mindtb":hs.dtb}
        kq[hs.lop]["slhs"] += 1
        kq[hs.lop]["tongdtb"] += hs.dtb
        kq[hs.lop]["dtblop"] = kq[hs.lop]["tongdtb"]/kq[hs.lop]["slhs"]
        if hs.dtb >= 5:
            kq[hs.lop]["hsdat"] += 1
            kq[hs.lop]["tongdat"] += hs.dtb
            kq[hs.lop]["dtbdat"]= kq[hs.lop]["tongdat"]/kq[hs.lop]["hsdat"]
            tongdat_all += 1
            dtbdat_all += hs.dtb
        if hs.dtb <5:
            kq[hs.lop]["hschuadat"] += 1
            tongdiemchuadat += hs.dtb

        if hs.dtb > kq[hs.lop]["maxdtb"]:
            kq[hs.lop]["maxdtb"]= hs.dtb
            kq[hs.lop]["dsmax"]=[{"ten":hs.ten,"dtb":hs.dtb}]
        elif kq[hs.lop]["maxdtb"]== hs.dtb:
            kq[hs.lop]["dsmax"].append({"ten":hs.ten,"dtb":hs.dtb})
        if hs.dtb < kq[hs.lop]["mindtb"]:
            kq[hs.lop]["mindtb"]= hs.dtb
            kq[hs.lop]["dsmin"]=[{"ten":hs.ten,"dtb":hs.dtb}]
        elif kq[hs.lop]["mindtb"]== hs.dtb:
            kq[hs.lop]["dsmin"].append({"ten":hs.ten,"dtb":hs.dtb})
    dtb_all = dtbdat_all/tongdat_all
    return {"kq":kq,"dtb_all":dtb_all,"tongdiemchuadat":tongdiemchuadat}



from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class hs_groupby(BaseModel):
    lop:str
    ten:str
    dtb:float
class thongke_groupby(BaseModel):
    ds:list[hs_groupby]
@app.post("/thongke_groupby")
def thongke_groupby(data:thongke_groupby):
    kq={}
    for hs in data.ds:
        if hs.lop not in kq:
            kq[hs.lop]={"hsgioi":0,"hskha":0,"hstb":0,"hsyeu":0,"dsgioi":[],"dskha":[],"dstb":[],"dsyeu":[]}
        if hs.dtb >= 8:
            kq[hs.lop]["hsgioi"]+= 1
            kq[hs.lop]["dsgioi"]=[{"ten":hs.ten,"dtb":hs.dtb}]
        elif kq[hs.lop]["hsgioi"]== hs.dtb:
            kq[hs.lop]["dsgioi"].append({"ten":hs.ten,"dtb":hs.dtb})
        
        if 6.5 <= hs.dtb <8:
            kq[hs.lop]["hskha"]+= 1
            kq[hs.lop]["dskha"]=[{"ten":hs.ten,"dtb":hs.dtb}]
        elif kq[hs.lop]["hskha"]== hs.dtb:
            kq[hs.lop]["dskha"].append({"ten":hs.ten,"dtb":hs.dtb})
        if 5<= hs.dtb < 6.5:
            kq[hs.lop]["hstb"]+= 1
            kq[hs.lop]["dstb"]=[{"ten":hs.ten,"dtb":hs.dtb}]
        elif kq[hs.lop]["hstb"]== hs.dtb:
            kq[hs.lop]["dstb"].append({"ten":hs.ten,"dtb":hs.dtb})
        if hs.dtb <5:
            kq[hs.lop]["hsyeu"]+= 1
            kq[hs.lop]["dsyeu"]=[{"ten":hs.ten,"dtb":hs.dtb}]
        elif kq[hs.lop]["hsyeu"]== hs.dtb:
            kq[hs.lop]["dsyeu"].append({"ten":hs.ten,"dtb":hs.dtb})
    return kq



from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class maxmin(BaseModel):
    ten:str
    lop:str
    dtb:float
class maxmin_rieng(BaseModel):
    ds:list[maxmin]
@app.post("/maxmin_rieng")
def maxmin_rieng(data:maxmin_rieng):
    kq={}
    for hs in data.ds:
        if hs.lop not in kq:
            kq[hs.lop]={"maxdtb":0,"mindtb":999,"dsmax":[],"dsmin":[]}
        if hs.dtb > kq[hs.lop]["maxdtb"]:
            kq[hs.lop]["maxdtb"]=hs.dtb
            kq[hs.lop]["dsmax"]=[{"ten":hs.ten,"dtb":hs.dtb}]
        elif hs.dtb == kq[hs.lop]["maxdtb"]:
            kq[hs.lop]["dsmax"].appens({"ten":hs.ten,"dtb":hs.dtb})
        if hs.dtb <kq[hs.lop]["mindtb"]:
            kq[hs.lop]["mindtb"]=hs.dtb
            kq[hs.lop]["dsmin"]=[{"ten":hs.ten,"dtb":hs.dtb}]
        elif hs.dtb== kq[hs.lop]["mindtb"]:
            kq[hs.lop]["dsmin"].append({"ten":hs.ten,"dtb":hs.dtb})
    return kq



from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class dsmon(BaseModel):
    tenmon:str
    diem:float
class ontonghop(BaseModel):
    lop:str
    ten:str
    ds_mon:list[dsmon]
class ontap(BaseModel):
    ds:list[ontonghop]
@app.post("/ongtonghop123")
def ontonghop987 (data:ontap):
    kq={}
    dsdtbhs=[]
    for hs in data.ds:
        dtbhs =0
        tongdtbhs =0
        tongsomon =0
        for mon in hs.ds_mon:
            tongdtbhs += mon.diem
            tongsomon += 1 
        dtbhs = tongdtbhs/tongsomon
        dsdtbhs.append({"ten":hs.ten,"mon":mon.tenmon,"dtb":dtbhs,"lop":hs.lop})
        if hs.lop not in kq:
            kq[hs.lop]={"dsdtbhs":[],"slhs":0,"tongdtb":0,"dtblop":0,"maxdtb":0,"mindtb":999,"dsmax":[],"dsmin":[],"maxdiem":0,"mindiem":999,"dsmaxdiem":[],"dsmindiem":[]}
        kq[hs.lop]["dsdtbhs"].append({"ten":hs.ten,"dtb":dtbhs})
        kq[hs.lop]["slhs"] += 1
        kq[hs.lop]["tongdtb"] += dtbhs
        kq[hs.lop]["dtblop"] = kq[hs.lop]["tongdtb"]/kq[hs.lop]["slhs"]
        if dtbhs > kq[hs.lop]["maxdtb"] :
            kq[hs.lop]["maxdtb"]= dtbhs
            kq[hs.lop]["dsmax"]=[{"ten":hs.ten,"dtb":dtbhs}]
        elif dtbhs == kq[hs.lop]["maxdtb"]:
            kq[hs.lop]["dsmax"].append({"ten":hs.ten,"dtb":dtbhs})
        if dtbhs < kq[hs.lop]["mindtb"]:
            kq[hs.lop]["mindtb"]= dtbhs
            kq[hs.lop]["dsmin"]=[{"ten":hs.ten,"dtb":dtbhs}]
        elif dtbhs == kq[hs.lop]["mindtb"]:
            kq[hs.lop]["dsmin"].append({"ten":hs.ten,"dtb":dtbhs})
        for mon in hs.ds_mon:
            if mon.diem > kq[hs.lop]["maxdiem"]:
                kq[hs.lop]["maxdiem"]= mon.diem
                kq[hs.lop]["dsmaxdiem"]=[{"ten":hs.ten,"tenmon":mon.tenmon,"diem":mon.diem}]
            elif mon.diem == kq[hs.lop]["maxdiem"]:
                kq[hs.lop]["dsmaxdiem"].append({"ten":hs.ten,"tenmon":mon.tenmon,"diem":mon.diem})
            if mon.diem < kq[hs.lop]["mindiem"]:
                kq[hs.lop]["mindiem"]=mon.diem
                kq[hs.lop]["dsmindiem"]=[{"ten":hs.ten,"tenmon":mon.tenmon,"diem":mon.diem}]
            elif mon.diem == kq[hs.lop]["mindiem"]:
                kq[hs.lop]["dsmindiem"].append({"ten":hs.ten,"tenmon":mon.tenmon,"diem":mon.diem})   
    for lop in kq:
        kq[lop]["dsdtbhs"]=sorted(kq[lop]["dsdtbhs"],key=lambda x: x["dtb"],reverse=True)
                #Muốn sort top N dtb của từng lớp riêng mà trong khởi tạo kq={} k có:
                #cách1: đem dsdtbhs ngoài chứa dữ liệu cần sort đưa vào khởi tạo kq={}
                # xuống dưới cho chạy xong hết ds ở trên tạo thêm biến "lop" trong ds khởi tạo kq={}
                #( vì dsdtbhs bên ngoài cùng cấp giống nhu 1 list đọc lập với kq={} nên bắt buọt tạo tên biến mới)
                # mục đích: để khi sort lấy biến bên trong ra kq[lop]["dsdtbhs"]" thì nó CHỈ LÀ DS CỦA LỚP ĐÓ "mới sort được )
                # NHƯ VẬY THÌ CHỈ SORT RIÊNG TỪNG LỚP , KHÔNG LẤY TOP2 CHUNG CỦA CẢ ALL LỚP 
                #cách 2: sort thẳng vào dsmax và dsmin lưu ý "chỉ trừ khi dsmax và dsmin tính riêng cho từng lơp",rồi lấy top N 
            # Những dữ liệu cần sort mà nằm ngoài khởi tạo kq={} thì "mẹo" tạo ds rồi sort
            # nếu list chứa dict [{},{}] thì lấy theo key để tự lấy value trong sort
            #Nếu là list [] : lấy [0],[1] để python tự lấy giá trị
        kq[lop]["top2"]=kq[lop]["dsdtbhs"][0:2] 
    return {"kq":kq} # k cần return thêm top2 vì kq đã chưa all top2 trong đó vì thêm chỉ dư thừa



from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class hs1(BaseModel):
    ten:str
    ds_diem:list[float]
class hs2 (BaseModel):
    lop:str
    dshs:list[hs1]
class hs3(BaseModel):
    ds:list[hs2]
@app.post("/th_hs_groupby")
def th_hs_groupby(data:hs3):
    kq={}
    tongall=0
    demall=0
    dtball =0
    ds=[]
    for hs in data.ds:   
        tongdtbhs =0
        demdtbhs=0
        dtbhs =0
        for i in hs.dshs:  
            for k in i.ds_diem:        
                tongdtbhs += k
                demdtbhs += 1
                dtbhs = tongdtbhs/demdtbhs
                tongall += k 
                demall += 1
        dtball = tongall /demall
        ds.append({"ten":i.ten,"dtbhs":dtbhs})
        if hs.lop not in kq:
            kq[hs.lop]={"tongdiemlop":0,"demhslop":0,"dtblop":0,"ds":[],"maxdtb":0,"mindtb":999,"dsmax":[],"dsmin":[],"hsdat":0,"hschuadat":0,"tyledat":0,"tylechuadat":0,"dsdat":[]}
        kq[hs.lop]["ds"].append({"ten":i.ten,"dtbhs":dtbhs})
        kq[hs.lop]["tongdiemlop"] += dtbhs
        kq[hs.lop]["demhslop"] += 1
        kq[hs.lop]["dtblop"] = kq[hs.lop]["tongdiemlop"]/kq[hs.lop]["demhslop"]
        if dtbhs > kq[hs.lop]["maxdtb"]:
            kq[hs.lop]["maxdtb"]= dtbhs
            kq[hs.lop]["dsmax"]= [{"ten":i.ten,"dtb":dtbhs}]
        elif kq[hs.lop]["maxdtb"]== dtbhs:
            kq[hs.lop]["dsmax"].append({"ten":i.ten,"dtb":dtbhs})
        if dtbhs < kq[hs.lop]["mindtb"]:
            kq[hs.lop]["mindtb"]=dtbhs
            kq[hs.lop]["dsmin"]= [{"ten":i.ten,"dtb":dtbhs}]
        elif kq[hs.lop]["mindtb"]== dtbhs:
            kq[hs.lop]["dsmin"].append({"ten":i.ten,"dtb":dtbhs})
        if dtbhs >= 5:
            kq[hs.lop]["hsdat"] += 1
            kq[hs.lop]["dsdat"].append({"ten":i.ten,"dtbhs":dtbhs})
        if dtbhs <5:
            kq[hs.lop]["hschuadat"] += 1
    for item in kq:
        kq[item]["tyledat"]= kq[item]["hsdat"]/kq[item]["demhslop"]*100  
        kq[item]["tylechuadat"]=kq[item]["hschuadat"]/kq[item]["demhslop"]*100
        kq[item]["dsdat"]=sorted(kq[item]["dsdat"],key=lambda x: x["dtbhs"],reverse=True)
        kq[item]["top2"]=kq[item]["dsdat"][0:2]
        tonghs2lop = sum(kq[item]["demhslop"]for item in kq)
        for hang, hs in enumerate( kq[item]["dsdat"], start =1):
            hs["hang"]= hang
    return {"tonghs":tonghs2lop,"kq":kq}
    # 2 cách lấy top N:
        #cách 1 : top N lấy chung cho tất cả lớp :
        # sort trong ds chung sau khi append của tất cả lớp lại 
        # ví dụ bài trên thì : ds_all= sorted(ds,key=lambda x: x["dtbhs"],reverse=True)
        #                      Top N = ds_all[0:2]
        # cách 2: top N riêng cho mỗi lớp:
        # sort trong ds chứa riêng cho mỗi lớp: nếu k có trong khởi tạo "ds:[] bằng ds rỗng tránh bị dùng chung ds" thì đưa vào ds trc đó đã append all 
        #- sau đó dòng đưới append lại để gán ds đó vào kq để dễ đem ra return goup cùng "kq[hs.lop]["ds"].append({"ten":i.ten,"dtbhs":dtbhs})"    
        #- xuống cuối dòng ra ngoài tạo biến vào trong kq :"for item in kq:"
        #- sau đó lấy lại mỗi ds riêng của mỗi lớp để sorted "kq[item]["ds"]=sorted(kq[item]["ds"],key=lambda x: x["dtbhs"],reverse=True)"
        #- cuối cùng gán " top N" vào kq mới mục đích return cùng group "kq[item]["top2"]=kq[item]["ds"][0:2]"



from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class hs (BaseModel):
    ten:str
    diem:list[float]
class lop(BaseModel):
    ten_lop:str
    dshs:list[hs]
class truong(BaseModel):
    ds:list[lop]
@app.post("/tonghop_all")
def tonghop_all(data:truong):
    kq={}
    dsdtb1=[]
    for hs in data.ds:
        for i in hs.dshs:
            tongdiemlop =0
            tong1 =0
            dem1= 0
            dtb1 =0
            for k in i.diem:
                tongdiemlop += k
                tong1 += k
                dem1 += 1
            dtb1 = tong1/dem1
            dsdtb1.append({"ten":i.ten,"dtb":dtb1})
            if hs.ten_lop not in kq:
                kq[hs.ten_lop]={"tonghs":0,"tongdiemlop":0,"tongmon":0,"tongdtblop":0,"dtblop":0,"dtbmax":0,"dtbmin":999,"dsmax":[],"dsmin":[],"hsdat":[],"hschuadat":[],"demhsduoi5":0,"dsduoi5":[],"dsdtb1":[],"tyledat":0,"tylechuadat":0}
            kq[hs.ten_lop]["tongmon"] += len(i.diem)
            kq[hs.ten_lop]["tongdiemlop"] += tongdiemlop
            kq[hs.ten_lop]["tonghs"] += 1
            kq[hs.ten_lop]["tongdtblop"] += dtb1
            kq[hs.ten_lop]["dtblop"] = kq[hs.ten_lop]["tongdtblop"]/kq[hs.ten_lop]["tonghs"]
            if dtb1 > kq[hs.ten_lop]["dtbmax"]:
                kq[hs.ten_lop]["dtbmax"]= dtb1 
                kq[hs.ten_lop]["dsmax"]=[{"ten":i.ten,"dtb":dtb1}]
            elif dtb1 == kq[hs.ten_lop]["dtbmax"]:
                kq[hs.ten_lop]["dsmax"].append({"ten":i.ten,"dtb":dtb1})
            if dtb1 < kq[hs.ten_lop]["dtbmin"]:
                kq[hs.ten_lop]["dtbmin"]=dtb1
                kq[hs.ten_lop]["dsmin"]=[{"ten":i.ten,"dtb":dtb1}]
            elif dtb1 == kq[hs.ten_lop]["dtbmin"]:
                kq[hs.ten_lop]["dsmin"].append({"ten":i.ten,"dtb":dtb1})
        
            if dtb1 >= 5:
                kq[hs.ten_lop]["hsdat"].append({"ten":i.ten,"dtb":dtb1})
            if dtb1 <5:
                kq[hs.ten_lop]["hschuadat"].append({"ten":i.ten,"dtb":dtb1})
            for k in i.diem:    
                if k <5:
                    kq[hs.ten_lop]["demhsduoi5"] += 1
            if any (k<5 for k in i.diem): # hàm any tránh lưu tên trùng 
                kq[hs.ten_lop]["dsduoi5"].append({"ten":i.ten})
                # Bản rút gọn của biến cờ : any( k<5 for k in i.diem)
                #mục đích: nó chính là bản rút gọn của biến cờ , duyệt qua từng điểm đúng thỏa dk <5 nhưng trùng tên 1 hs (CHỈ LƯU 1 DÒNG HS)
                # không cần khai báo như biến cờ , tránh trường hợp thỏa dk đúng k<5 nhưng lưu 2 tên trùng nhau cùng 1 kq của 1 hs 
                # tóm gọn : tránh lưu tên trùng 1 hs khi cùng thỏa 1 kq trong dk 
        kq[hs.ten_lop]["dsdtb1"].append({"ten":i.ten,"dtb":dtb1}) 
    for item in kq:
        kq[item]["dsdtb1"]=sorted(kq[item]["dsdtb1"],key=lambda x: x["dtb"],reverse=True) # x: x["dtb"] lưu ý trong x muốn lấy giá trị để sort thì điền "x["key"]" tránh nhầm điền value 
        kq[item]["top2"]= kq[item]["dsdtb1"][:2] # lấy top2 tạm thời
        moc= kq[item]["top2"][-1]["dtb"] # nếu lấy top2 mà có điểm trùng top 2 như 10,9,9 thì trước hết lất top2 tạm thời , sau đó đặt cột mốc lấy "-1" tức là cuối top2 
        for M in kq[item]["dsdtb1"][2:]: # sau khi mấy móc số cuối xong tạo thêm biến "M" mới chạy trong dsdtb1 vừa sort để kiểm tra 
            if M["dtb"]== moc: # đặt dk trong ds có dtb = điểm cột mốc cuối vừa lấy
                kq[item]["top2"].append(M) # nếu bằng thì append lại ds để lấy điẻm bằng cùng top2 
            else: # nếu hết điểm băng thì "dừng"
                break #" dừng"
        kq[item]["tyledat"]=len(kq[item]["hsdat"])/kq[item]["tonghs"]*100 # len(kq[item]["hsdat"]) ở trên lưu theo list nên dùng len() để đếm
        kq[item]["tyledat"]=round(kq[item]["tyledat"],2) # round nghĩa làm tròn công thức round(giá trị , sau dấu phấy lấy "N" số ví dụ lấy 2 số thì bằng 2)
        kq[item]["tylechuadat"]=len(kq[item]["hschuadat"])/kq[item]["tonghs"]*100 # tương tự hsdat
        kq[item]["tylechuadat"]=round(kq[item]["tylechuadat"],2)
    return kq


#put
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app= FastAPI()
class hs (BaseModel):
    ten:str
    tuoi:int
ds=[hs(ten="An",tuoi=18),hs(ten="Bình",tuoi = 19),hs(ten="Cường",tuoi=20)]
@app.put("/suatuoi")
def suatuoi(data:hs):
    for hs in ds:
        if hs.ten ==data.ten:
            hs.tuoi=data.tuoi
            return{"kq":"đã cập nhật","data":hs}
    raise HTTPException(404,"không tìm thấy hs")


from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class hs_1(BaseModel):
    ten:str
    tenmoi:str
    tuoi:int
ds=[hs(ten="An",tuoi=20),hs(ten="Bình",tuoi = 19),hs(ten="Cường",tuoi=20)]
@app.put("/suaten")
def suaten(data:hs_1):
    for hs in ds:
        if hs.ten == data.ten :
            hs.tuoi=data.tuoi
            return {"kq":"đã chỉnh sữa","data":hs}
    raise HTTPException(404,"không tìm thấy hs")


from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class sualist(BaseModel):
    ten:str
    diem:list[float]
ds=[sualist(ten="An",diem=[3,4,5]),sualist(ten="Bình",diem =[4,5,6]),sualist(ten="Cường",diem=[3,6,7])]
@app.put("/sualist")
def sualist(data:sualist):
    for hs in ds:
        if hs.ten == data.ten:
            hs.diem = data.diem
            return {"kq":"đã chỉnh sửa","data":hs}
    raise HTTPException(404,"k tìm thấy hs")



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app=FastAPI()
class sl (BaseModel):
    ten:str
    diem:list[float]
ds=[sl(ten="An",diem=[3,4,5]),sl(ten="Bình",diem =[4,5,6]),sl(ten="Cường",diem=[3,6,7])]
class sua_sl(BaseModel):
    ten:str
    tenmoi:str
    diem:list[float]
@app.put("/sualisttendiem")
def sualist (data:sua_sl):
    for hs in ds:
        if hs.ten == data.ten:
            hs.ten= data.tenmoi
            hs.diem = data.diem
            return {"data":hs,"kq":"xác nhận đã chỉnh sữa"}
    raise HTTPException(404,"không có hs trong ds")

#cách 1: sửa vị trí theo nhập tên
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app=FastAPI()
class sl (BaseModel):
    ten:str
    diem:list[float]
ds=[sl(ten="An",diem=[3,4,5]),sl(ten="Bình",diem =[4,5,6]),sl(ten="Cường",diem=[3,6,7])]
class sua_sl(BaseModel):
    ten:str
    vitri:int
    diemmoi:list[float]
@app.put("/suavitri")
def sualist (data:sua_sl):
    for hs in ds:
        if hs.ten == data.ten:
            hs.diem[data.vitri]=data.diemmoi
            return {"data":hs,"note":"sửa vị trí số 2"}
    raise HTTPException(404,"k tìm thấy hs")


#cách 2: sửa vị trí theo nhập tên
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app=FastAPI()
class sl (BaseModel):
    ten:str
    diem:list[float]
ds=[sl(ten="An",diem=[3,4,5]),sl(ten="Bình",diem =[4,5,6]),sl(ten="Cường",diem=[3,6,7])]
class sua_sl(BaseModel):
    ten:str
    vitri:int
    diemmoi:list[float]
@app.put("/suavitricach2")
def sualist (data:sua_sl):
    for hs in ds:
        if hs.ten == data.ten:
            if data.vitri<0 or data.vitri >len(hs.diem):
                raise HTTPException(404,"vị trí sai")
        else:
            hs.diem[data.vitri]=data.diemmoi
    return hs
     
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()

class themdiem (BaseModel):
    ten:str
    diem:list[float]
ds=[sl(ten="An",diem=[3,4,5]),sl(ten="Bình",diem =[4,5,6]),sl(ten="Cường",diem=[3,6,7])]
class them_diem(BaseModel):
    ten:str
    diemmoi:float
@app.put("/themdiem")
def themdiem (data:them_diem):
    for hs in ds:
        if hs.ten == data.ten:
            hs.diem.append(data.diemmoi)
            return hs
    raise HTTPException (404, "k tìm thấy hs")



    
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()

class xoadiem (BaseModel):
    ten:str
    diem:list[float]
ds=[sl(ten="An",diem=[3,4,5]),sl(ten="Bình",diem =[4,5,6]),sl(ten="Cường",diem=[3,6,7])]
class xoa_diem(BaseModel):
    ten:str
    xoadiem:float
@app.put("/xoadiem")
def xoadiem(data:xoa_diem):
    for hs in ds:
        if hs.ten == data.ten:
            if data.xoadiem in hs.diem:
                hs.diem.remove(data.xoadiem)
                return hs
    raise HTTPException(404,"k tìm thấy điểm có trong hs.diem")



from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class sl (BaseModel):
    ten:str
    tuoi:int
    diem:list[float]
ds=[sl(ten="An",tuoi = 18,diem=[3,4,5]),sl(ten="Bình",tuoi=20,diem =[4,5,6]),sl(ten="Cường",tuoi=21,diem=[3,6,7])]
class tonghop_basic (BaseModel):
    ten:str
    tuoimoi:int 
    vitri:int   
    diemmoi:float 
@app.put("/tonghopbasic")
def tonghop (data:tonghop_basic):
    for sl in ds:
        if data.ten == sl.ten:
            sl.tuoi = data.tuoimoi
            sl.diem[data.vitri]=data.diemmoi
            return sl
    raise HTTPException (404,"thông tin k hợp lệ")




   
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class chiemdiem (BaseModel):
    ten:str
    tuoi:int
    diem:list[float]
ds=[sl(ten="An",tuoi = 18,diem=[3,4,5]),sl(ten="Bình",tuoi=20,diem =[4,5,6]),sl(ten="Cường",tuoi=21,diem=[3,6,7])]
class chiemdiem_basic (BaseModel):
    ten:str
    vitri:int   
    diemmoi:float 
@app.put("/chiemdiem")
def chiemdiem (data:chiemdiem_basic):
    for hs in ds:
        if data.ten == hs.ten:
            hs.diem.insert(data.vitri,data.diemmoi)
            return hs
    raise HTTPException (404,"k tìm thấy hs")




from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class xoavitri (BaseModel):
    ten:str
    tuoi:int
    diem:list[float]
ds=[sl(ten="An",tuoi = 18,diem=[3,4,5]),sl(ten="Bình",tuoi=20,diem =[4,5,6]),sl(ten="Cường",tuoi=21,diem=[3,6,7])]
class xoavitri_basic (BaseModel):
    ten:str
    vitri:int   
@app.put("/xoavitri")
def xoavitri (data:xoavitri_basic):
    for hs in ds:
        if data.ten == hs.ten:
            if data.vitri >= len(hs.diem) or data.vitri <0:
                raise HTTPException (404,"k tìm thấy hs")
            else:
                hs.diem.pop(data.vitri)
            return hs
   


from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class thaydoi(BaseModel):
    ten:str
    tuoi:int
    diem:list[float]
ds=[sl(ten="An",tuoi = 18,diem=[3,4,5]),sl(ten="Bình",tuoi=20,diem =[4,5,6]),sl(ten="Cường",tuoi=21,diem=[3,6,7])]
class thaydoi_1(BaseModel):
    ten:str
    tuoimoi:int
    diemmoi:list[float]
@app.put("/thaythe")
def thaythe(data:thaydoi_1):
    for hs in ds:
        if hs.ten == data.ten:
            hs.tuoi= data.tuoimoi
            hs.diem= data.diemmoi
            return hs
    raise HTTPException(404,"k tìm thấy hs")



from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class thaythe(BaseModel):
    ten:str
    tuoi:int
    diem:list[float]
ds=[sl(ten="An",tuoi = 18,diem=[3,4,5]),sl(ten="Bình",tuoi=20,diem =[4,5,6]),sl(ten="Cường",tuoi=21,diem=[3,6,7])]
class thaythe_1(BaseModel):
    ten:str                     #lưu ý : khi dữ liệu không muốn thay đỏi nhập bên json tại vị trí đo = null , ví dụ diemmoi:null 
    tuoimoi:int |None=None      #nếu ban đầu đã sữa dữ liệu 3,6,7 thành 1,2,3 và tiếp tục gõ null sữa lần nữa thì dữ liệu sẽ cập nhật lần thay đổi gần nhất
    diemmoi:list[float] |None=None  # muốn quay lại dữ liệu cũ thì ctrl+ C CHẠY LẠI hoặc dùng cách khác phức tạo hơn (post/reset hoặc database) hỏi chatgpt  
@app.put("/thaythe")
def thaythe(data:thaythe_1):
    for hs in ds:
        if hs.ten== data.ten:
            if data.tuoimoi is not None:
                hs.tuoi= data.tuoimoi
            if data.diemmoi is not None:
                hs.diem=data.diemmoi
            return hs
    raise HTTPException (404,"thông tin k hợp lệ ")


        

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class dshs(BaseModel):
    ten:str
    tuoi:int
    diem:list[float]
ds=[sl(ten="An",tuoi = 18,diem=[3,4,5]),sl(ten="Bình",tuoi=20,diem =[4,5,6]),sl(ten="Cường",tuoi=21,diem=[3,6,7])]
class dshs_1(BaseModel):
    ten:str                     
    tuoimoi:int |None=None      
    diemmoi:list[float] |None=None    
@app.put("/dshs1")
def thaythe(data:dshs_1):
    for i, hs in enumerate(ds):     #cách tìm vị trí mỗi hs ( i=vị trí, hs= biến chạy trong ds)
        if hs.ten == data.ten:
            return i
    raise HTTPException(404,"k tìm được thông tin")



from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class enumerate_2(BaseModel):
    ten:str
    tuoi:int
    diem:list[float]
ds=[sl(ten="An",tuoi = 18,diem=[3,4,5]),sl(ten="Bình",tuoi=20,diem =[4,5,6]),sl(ten="Cường",tuoi=21,diem=[3,6,7])]
class enumerate_1(BaseModel):
    ten:str                     
    tuoimoi:int |None=None      
    diemmoi:float |None=None    
@app.put("/enumerate_diem")
def thaythe(data:enumerate_1):  
    for i,hs in enumerate(ds):
        if hs.ten==data.ten:
            for j,diem in enumerate(hs.diem): # cách tìm vị trí điểm ở stt bao nhiêu (j= vị trí,diem = biến chạy trong ds)
                if diem==data.diemmoi:# vì để tìm điểm ở vị trí số mấy nên diem = data.diemmoi
                    return {"vị trí hs":i,"vị trí điểm":j}# ra kq vị trí
    raise HTTPException(404,"k tìm thông tin hợp lệ")    
 


from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class sl (BaseModel):
    ten:str
    tuoi:int
    diem:list[float]
ds=[sl(ten="An",tuoi = 18,diem=[3,4,5]),sl(ten="Bình",tuoi=20,diem =[4,5,6]),sl(ten="Cường",tuoi=21,diem=[3,6,7])]
class tonghop_basic (BaseModel):
    ten:str
    tuoimoi:int 
    vitri:int   
    diemmoi:float 
@app.put("/tonghopbasic")
def tonghop (data:tonghop_basic):
    for sl in ds:
        if data.ten == sl.ten:
            sl.tuoi = data.tuoimoi
            sl.diem[data.vitri]=data.diemmoi
            return sl
    raise HTTPException (404,"thông tin k hợp lệ") 



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app=FastAPI()
class th_put(BaseModel):
    ten:str
    tuoi:int
    diem:list[float]
ds=[sl(ten="An",tuoi = 18,diem=[3,4,5]),sl(ten="Bình",tuoi=20,diem =[4,5,6]),sl(ten="Cường",tuoi=21,diem=[3,6,7])]
class th_put1(BaseModel):
    ten:str
    tuoimoi: int | None=None
    diemmoi: float |None=None
    vitri:int |None=None
@app.put("/th_put")
def th_put (data:th_put1):
    for hs in ds:
        if hs.ten == data.ten:
            if data.tuoimoi is not None:
                hs.tuoi= data.tuoimoi
            if data.diemmoi is not None:
                hs.diem[data.vitri]= data.diemmoi
            return hs
    raise HTTPException(404,"thông tin k hợp lệ")




from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class monhoc(BaseModel):
    ten:str
    diem:float
class sl (BaseModel):
    ten:str
    tuoi:int
    monhoc:list[monhoc]
ds=[sl(ten="An",tuoi = 18,monhoc=[monhoc(ten="toan",diem=8)]),sl(ten="Bình",tuoi=20,monhoc=[monhoc(ten="lí",diem=7)]),sl(ten="Cường",tuoi=21,monhoc=[monhoc(ten="sử",diem=9)])]
class hs_nested(BaseModel):
    tenhs:str
    tenmon:str
    diemmoi:float 
@app.put("/nested_put")
def nested_put(data:hs_nested):
    for hs in ds:
        if hs.ten ==data.tenhs:
            for i in hs.monhoc:
                if i.ten == data.tenmon:
                    i.diem=data.diemmoi
                    return hs
                raise HTTPException(404,"không tim thấy môn học")
    raise HTTPException(404,"k tìm thấy hs")





from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field, field_validator
app= FastAPI()
class sl1(BaseModel):
    ten:str
    diem:float
class sl (BaseModel):
    ten:str
    tuoi:int
    monhoc:list[sl1]
ds=[sl(ten="An",tuoi = 18,monhoc=[sl1(ten="toan",diem=8)]),sl(ten="Bình",tuoi=20,monhoc=[sl1(ten="lí",diem=7)]),sl(ten="Cường",tuoi=21,monhoc=[(sl1(ten="sử",diem=9)),(sl1(ten="lí",diem=9)),(sl1(ten="sinh",diem=9))])]
class th_validator1 (BaseModel):
    tenhs:str
    @field_validator("tenhs")
    @classmethod
    def kt_tenhs(cls,tenhs):
        if tenhs.strip()=="":
            raise ValueError("tên không được rỗng")
        return tenhs
    tuoimoi:int
    tenmoncu:str
    tenmonmoi:str
    diemmoi:float
    @field_validator("diemmoi")
    @classmethod
    def kt_diem(cls,diemmoi):
        if diemmoi<0 or diemmoi>10:
            raise ValueError("điểm không hợp lệ")
        return diemmoi
@app.put("/th_validator2")
def th_validator(data:th_validator1):
    for hs in ds:
        if hs.ten==data.tenhs:
            for i in hs.monhoc:
                if i.ten==data.tenmonmoi: # nếu tên môn bằng tên môn mới
                    i.diem=data.diemmoi #diểm = điểm mới
                    break   #dừng vì nếu k dừng là sẽ chạy append ở dưới
            else:   # để if chạy hết rồi mới tới else , nên đưa else ra ngoài 
                hs.monhoc.append(sl1(ten=data.tenmonmoi,diem=data.diemmoi)) # lưu ý : append đúng kểu dữ liệu đã dùng ban đầu tức là "sl1(ten=,diem=)" ở tren ds
            return hs
    raise HTTPException(404,"k tìm được hs")



from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class mh1 (BaseModel):
    ten:str
    tenmon:str
    diem:float
ds=[mh1(ten="My",tenmon="toán",diem=10),mh1(ten="Linh",tenmon="sinh",diem=10),mh1(ten="quỳnh",tenmon="anh",diem=6)]
class mh2(BaseModel):
    tenhs:str
    tenmoncu:str
    tenmonmoi:str
    diemmoi:float
@app.put("/put_nc")
def put_nc(data:mh2):
    for hs in ds:
        print(hs)
        if hs.ten== data.tenhs:
            if hs.tenmon ==data.tenmoncu:
                hs.tenmon = data.tenmonmoi
                hs.diem = data.diemmoi
                return hs 
    raise HTTPException(404,"k tìm thấy môn học")


from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class th1 (BaseModel):
    tenmon:str
    diem:float
class th2(BaseModel):
    ten:str
    tuoi:int
    monhoc:list[th1]
ds=[th2(ten="An",tuoi = 18,monhoc=[th1(tenmon="toan",diem=8)]),th2(ten="Bình",tuoi=20,monhoc=[th1(tenmon="lí",diem=7)]),th2(ten="Cường",tuoi=21,monhoc=[(th1(tenmon="sử",diem=9)),(th1(tenmon="lí",diem=9)),(th1(tenmon="sinh",diem=9))])]
class th3(BaseModel):
    tenhs:str
    tenmoncu:str
    tenmonmoi:str
    diemmoi:float
@app.put("/tonghop_put1")
def check_tonghop_pu1(data:th3):
    for hs in ds:
        if hs.ten==data.tenhs:
            for i in hs.monhoc:
                if i.tenmon == data.tenmoncu:
                    i.tenmon= data.tenmonmoi
                    i.diem= data.diemmoi
                    break
            else:
                hs.monhoc.append(th1(tenmon=data.tenmoncu,diem=data.diemmoi))
            return hs



 
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class th1 (BaseModel):
    tenmon:str
    diem:float
class th2(BaseModel):
    ten:str
    tuoi:int
    monhoc:list[th1]
ds=[th2(ten="An",tuoi = 18,monhoc=[th1(tenmon="toan",diem=8)]),th2(ten="Bình",tuoi=20,monhoc=[th1(tenmon="lí",diem=7)]),th2(ten="Cường",tuoi=21,monhoc=[(th1(tenmon="sử",diem=9)),(th1(tenmon="lí",diem=9)),(th1(tenmon="sinh",diem=9))])]
class thput3(BaseModel):
    tenhs:str
    tenmoncu:str
    tenmonmoi:str
    diemmoi:float
@app.put("/tonghopput3")
def check_tonghop_pu3(data:thput3): # Bài này dùng biến cờ để ghi nhớ dữ liệu đã có hay chưa?
    for hs in ds:
        if hs.ten == data.tenhs:
            tim_mon_cu = False  # biến cờ 
            for i in hs.monhoc:  
                if i.tenmon == data.tenmoncu:
                    i.tenmon = data.tenmonmoi
                    i.diem = data.diemmoi
                    tim_mon_cu = True
                    return hs
            if tim_mon_cu ==False:  #biến cờ
                for i in hs.monhoc:
                    if i.tenmon != data.tenmoncu:   #nếu tên môn (ds) khác với tên môn nhập (tên cũ trong ds) 
                        if data.tenmonmoi == i.tenmon:  #tên môn mới nhập ở json bằng tên môn trong ds
                            raise HTTPException(400,"môn cũ không có nhưng môn mới chuẩn bi thay thế đã có trong ds ")  #code dịch trong () 
            hs.monhoc.append(th1(tenmon=data.tenmonmoi,diem=data.diemmoi)) # ngược lại nếu tenmoncu và temmonmoi đều k có trong ds thì append
            return hs
    raise HTTPException(404,"k tìm thấy học sinh")



from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class put_th(BaseModel):
    tenmon:str
    diem:float
class put_th1(BaseModel):
    ten:str
    monhoc:list[put_th]
ds=[put_th1(ten="Lâm",monhoc=[put_th(tenmon="toán",diem=10)]),put_th1(ten="Huy",monhoc=[put_th(tenmon="Sinh",diem=10)]),put_th1(ten="Nguyên",monhoc=[put_th(tenmon="Anh",diem=10)])]
class tonghop_put_nested(BaseModel):
    tenhs:str
    tenmoncu:str
    tenmonmoi:str
    diemmoi:float
@app.put("/tonghop_put_nested")
def tonghop_put_nested(data:tonghop_put_nested):
    for hs in  ds:
        if hs.ten == data.tenhs:
            tim_mon_cu = False
            for i in hs.monhoc:
                if i.tenmon == data.tenmoncu:
                    i.tenmon = data.tenmonmoi
                    i.diem = data.diemmoi
                    tim_mon_cu = True
                    return hs
            if tim_mon_cu == False:
                for i in hs.monhoc:
                    if data.tenmoncu != i.tenmon:
                        if data.tenmonmoi == i.tenmon:
                            raise HTTPException(400,"tên môn moi đã có trong ds")
                hs.monhoc.append(put_th(tenmon=data.tenmonmoi,diem=data.diemmoi))
                return hs
    raise HTTPException (404,"k tìm thấy tên hs ")   



from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel
app= FastAPI()
class met (BaseModel):
    mon:str
    diem:float
class met1 (BaseModel):
    ten:str
    dsdiem:list[met]
ds=[met1(ten="My",dsdiem=[met(mon="toán",diem=10)]),met1(ten="Nghĩa",dsdiem=[met(mon="sinh",diem=10)]),met1(ten="Bằng",dsdiem=[met(mon="lí",diem=10)])]
class met2 (BaseModel):
    tenhs:str
    monmoi:str
    diemmoi:float
@app.put("/met")
def kt_capnhat(data:met2):
    for hs in ds:
        if hs.ten == data.tenhs:
            for i in hs.dsdiem:
                if i.mon == data.monmoi:
                    i.diem= data.diemmoi
                    return hs
            else:
                hs.dsdiem.append(met(mon=data.monmoi,diem=data.diemmoi))
                return hs
    raise HTTPException(404,"k tìm thấy hs ")



from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class ten (BaseModel):
    ten:str
    tuoi:int
ds=[ten(ten="Tuấn",tuoi=17),ten(ten="Ngọc",tuoi=17),ten(ten="Hòa",tuoi=17),ten(ten="Phát",tuoi=17)]
class ten1 (BaseModel):
    ten_cu:str
    ten_moi:str
@app.put("/ten")
def ten_tonghop (data:ten1):
    for hs in ds:
        if hs.ten == data.ten_cu:
            hs.ten = data.ten_moi
            return hs
    raise HTTPException (404," k  tìm thấy học sinh ")





from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class ten (BaseModel):
    ten:str
    tuoi:int
ds=[ten(ten="Tuấn",tuoi=17),ten(ten="Ngọc",tuoi=17),ten(ten="Hòa",tuoi=17),ten(ten="Phát",tuoi=17)]
class ten1 (BaseModel):
    tenhs:str
    tuoi_moi:int
@app.put("/tuoi_ten1")
def ten_tonghop (data:ten1):  
    for hs in ds:
        if hs.ten == data.tenhs:
            hs.tuoi = data.tuoi_moi
            return hs
    raise HTTPException (404," k tìm thấy hs ")          





from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class ten (BaseModel):
    ten:str
    tuoi:int
ds=[ten(ten="Tuấn",tuoi=17),ten(ten="Ngọc",tuoi=17),ten(ten="Hòa",tuoi=17),ten(ten="Phát",tuoi=17)]
class ten1 (BaseModel):
    ten_cu:str
    ten_moi :str
    tuoi_moi:int
@app.put("/tuoi_ten1_tuoi")
def ten_tonghop (data:ten1): 
    for hs in ds:
        if hs.ten == data.ten_cu:
            hs.ten = data.ten_moi
            hs.tuoi = data.tuoi_moi
            return hs
    raise HTTPException (404,"k tìm thấy hs")


from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app= FastAPI()
class thaylist (BaseModel):
    ten:str
    dsdiem: list[float]
ds=[thaylist(ten="My",dsdiem=[4,6,7]),thaylist(ten="Nghĩa",dsdiem=[4,6,7]),thaylist(ten="Lộc",dsdiem=[4,6,7]),thaylist(ten="Linh",dsdiem=[4,6,7])]
class thaylist1 (BaseModel):
    tenhs:str
    dsdiem_moi : list[float]
@app.put("/thaylist")
def thaylist( data:thaylist1):
    for hs in ds:
        if hs.ten == data.tenhs:
            hs.dsdiem = data.dsdiem_moi
            return hs
    raise HTTPException (status_code=404,detail=" k tìm thấy hs ")


from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app = FastAPI()
class thaymon( BaseModel):
    mon:str
    diem:float
class thaymon1 (BaseModel):
    ten:str
    dsdiem:list[thaymon]
ds=[thaymon1(ten="My",dsdiem=[thaymon(mon="toán",diem=10)]),thaymon1(ten="Lâm",dsdiem=[thaymon(mon="tin học",diem=10)]),thaymon1(ten="Cầm",dsdiem=[thaymon(mon="văn",diem=10)])]
class thaymon2 (BaseModel):
    tenhs:str
    mon_cu:str
    mon_moi:str
    diemmoi:float
@app.put("/thaymon_th")
def thaymon_th (data:thaymon2):
    for hs in ds:
        if hs.ten== data.tenhs:
            for i in hs.dsdiem:
                if i.mon == data.mon_cu:
                    i.mon = data.mon_moi
                    i.diem= data.diemmoi
                    return hs 
            else:
                raise HTTPException(404,"k tìm thấy môn")
    raise HTTPException(404,"k tìm thấy hs ")      




from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app = FastAPI()
class thaymon( BaseModel):
    mon:str
    diem:float
class thaymon1 (BaseModel):
    ten:str
    dsdiem:list[thaymon]
ds=[thaymon1(ten="My",dsdiem=[thaymon(mon="toán",diem=10)]),thaymon1(ten="Lâm",dsdiem=[thaymon(mon="tin học",diem=10)]),thaymon1(ten="Cầm",dsdiem=[thaymon(mon="văn",diem=10)])]
class thaymon2 (BaseModel):
    tenhs:str
    mon_cu:str
    mon_moi:str
    diemmoi:float
@app.put("/themmon_thaydiem")
def thaymon_th (data:thaymon2):
    for hs in ds:
        if hs.ten== data.tenhs:        
            for i in hs.dsdiem:
                if i.mon == data.mon_cu:
                    i.diem= data.diemmoi   
                    return hs 
            hs.dsdiem.append(thaymon(mon=data.mon_moi,diem=data.diemmoi))
            return hs
    raise HTTPException(404,"k tìm thấy hs ")        
    


from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app = FastAPI()
class thaymon( BaseModel):
    mon:str
    diem:float
class thaymon1 (BaseModel):
    ten:str
    dsdiem:list[thaymon]
ds=[thaymon1(ten="My",dsdiem=[thaymon(mon="toán",diem=10),thaymon(mon="CNTT",diem=10)]),thaymon1(ten="Lâm",dsdiem=[thaymon(mon="tin học",diem=10),thaymon(mon="sử",diem=10)]),thaymon1(ten="Cầm",dsdiem=[thaymon(mon="văn",diem=10),thaymon(mon="địa",diem=10)])]
class thaymon2 (BaseModel):
    tenhs:str
    mon_cu:str
@app.put("/xoa_remove")
def xoamon (data:thaymon2): #remove : xóa theo đối tượng (i)
    for hs in ds:
        if hs.ten == data.tenhs:
            for i in hs.dsdiem:
                if i.mon == data.mon_cu:
                    hs.dsdiem.remove(i) #lưu ý : i = thaymon(mon="tin học",diem = 10) khi xóa môn thì xóa luôn điểm, muốn xóa môn ra khỏi list thì phải xóa phần tử (i)
                    return hs
            raise HTTPException(404,"k tìm thấy môn")
    raise HTTPException (404, " k tìm thây hs")


   

from fastapi import FastAPI,HTTPException
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app = FastAPI()
class thaymon( BaseModel):
    mon:str
    diem:float
class thaymon1 (BaseModel):
    ten:str
    dsdiem:list[thaymon]
ds=[thaymon1(ten="My",dsdiem=[thaymon(mon="toán",diem=10),thaymon(mon="CNTT",diem=10)]),thaymon1(ten="Lâm",dsdiem=[thaymon(mon="tin học",diem=10),thaymon(mon="sử",diem=10)]),thaymon1(ten="Cầm",dsdiem=[thaymon(mon="văn",diem=10),thaymon(mon="địa",diem=10)])]
class thaymon2 (BaseModel):
    tenhs:str
    mon_cu:str
    vitri:int
@app.put("/xoa_pop")
def xoa_mon (data:thaymon2):
    for hs in ds:
        if hs.ten == data.tenhs:
            for i in hs.dsdiem:
                if len(hs.dsdiem)<0 or data.vitri >len(hs.dsdiem):
                    raise HTTPException(404,"vị trí k hợp lệ")
            else:
                hs.dsdiem.pop(data.vitri)
                return hs 
    raise HTTPException (404,"k tìm thấy hs")

        


    
from fastapi import FastAPI,HTTPException
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app = FastAPI()
class thaymon( BaseModel):
    mon:str
    diem:float
class thaymon1 (BaseModel):
    ten:str
    dsdiem:list[thaymon]
ds=[thaymon1(ten="My",dsdiem=[thaymon(mon="toán",diem=10),thaymon(mon="CNTT",diem=10)]),thaymon1(ten="Lâm",dsdiem=[thaymon(mon="tin học",diem=10),thaymon(mon="sử",diem=10)]),thaymon1(ten="Cầm",dsdiem=[thaymon(mon="văn",diem=10),thaymon(mon="địa",diem=10)])]
class thaymon2 (BaseModel):
    tenhs:str  
    monmoi:str  
@app.put("/on_enumerate")           #enumerate: tìm vị trí 
def xoa_mon (data:thaymon2):
    for i, hs in enumerate (ds):
        if hs.ten == data.tenhs:
            for j, diem in enumerate (hs.dsdiem):
                if diem.mon == data.monmoi:                   
                    return {"vị trí hs":i , " vị trí môn":j} #tìm vị trí hs và môn 
    raise HTTPException(404," k tìm thấy hs ")




from fastapi import FastAPI,HTTPException
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app = FastAPI()
class thaymon( BaseModel):
    mon:str
    diem:float
class thaymon1 (BaseModel):
    ten:str
    dsdiem:list[thaymon]
ds=[thaymon1(ten="My",dsdiem=[thaymon(mon="toán",diem=10),thaymon(mon="CNTT",diem=10)]),thaymon1(ten="Lâm",dsdiem=[thaymon(mon="tin học",diem=10),thaymon(mon="sử",diem=10)]),thaymon1(ten="Cầm",dsdiem=[thaymon(mon="văn",diem=10),thaymon(mon="địa",diem=10)])]
class thaymon2 (BaseModel):
    tenhs:str  
    monmoi:str  
@app.put("/xoapop_enumerate")
def xoapop_enumerate (data:thaymon2):
    for i, hs in enumerate(ds):
        if hs.ten == data.tenhs:
            for j , diem in enumerate (hs.dsdiem):
                if diem.mon == data.monmoi:
                    mon_da_xoa = hs.dsdiem.pop(j) # Cách ghi log khi xóa dữ liệu để lưu lại kq xóa ( 2 dòng note)
                    print(f"môn:{mon_da_xoa.mon},điểm:{mon_da_xoa.diem}") # Môn= mon_da_xoa.mon VÌ mon_da_xoa như 1 dsdiem có chứa môn và điểm nên lấy luôn 
                    return hs # kết quả trả json chỉ còn lại môn chưa xóa , ở trên có thể ghi 1 dòng "hs.dsdiem.pop(j)" để xóa môn
    raise HTTPException(404," k tìm thấy hs ")




from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app= FastAPI()
class thaymon( BaseModel):
    mon:str
    diem:float
class thaymon1 (BaseModel):
    ten:str
    tuoi:int
    dsdiem:list[thaymon]
ds=[thaymon1(ten="My",tuoi=20,dsdiem=[thaymon(mon="toán",diem=10),thaymon(mon="CNTT",diem=10)]),thaymon1(ten="Lâm",tuoi=20,dsdiem=[thaymon(mon="tin học",diem=10),thaymon(mon="sử",diem=10)]),thaymon1(ten="Cầm",tuoi=20,dsdiem=[thaymon(mon="văn",diem=10),thaymon(mon="địa",diem=10)])]
class thaymon2(BaseModel):
    tenhs:str
@app.delete("/delete_bai1")
def delete_b1 (data:thaymon2):
    for i, hs in enumerate(ds):
        if hs.ten == data.tenhs:
            mon_da_xoa=ds.pop(i) # môn đã xóa 
            return {f"kq:đã xóa thành công, hs đã xoa:{data.tenhs},kq còn lại: {ds}"} # ds: ds đoạn này là ds còn lại 
    raise HTTPException (404," k tìm thấy hs ")


    
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app= FastAPI()
class thaymon( BaseModel):
    mon:str
    diem:float
class thaymon1 (BaseModel):
    ten:str
    tuoi:int
    dsdiem:list[thaymon]
ds=[thaymon1(ten="My",tuoi=20,dsdiem=[thaymon(mon="toán",diem=10),thaymon(mon="CNTT",diem=10)]),thaymon1(ten="Lâm",tuoi=20,dsdiem=[thaymon(mon="tin học",diem=10),thaymon(mon="sử",diem=10)]),thaymon1(ten="Cầm",tuoi=20,dsdiem=[thaymon(mon="văn",diem=10),thaymon(mon="địa",diem=10)])]
class thaymon2(BaseModel):
    tenhs:str
    monmoi:str
@app.delete("/delete_bai2")
def delete_b2 (data:thaymon2):
    for i,hs in enumerate (ds):
        if hs.ten == data.tenhs:
            for k , tim in enumerate (hs.dsdiem):
                if tim.mon == data.monmoi:
                    mon_da_xoa=hs.dsdiem.pop(k)
                    return {f"Đã xóa ,môn :{mon_da_xoa},ds còn lại: {ds}"}
            raise HTTPException(404, " k tìm thấy môn")
    raise HTTPException (404,' k tìm thây hs ')

    
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app= FastAPI()
class thaymon( BaseModel):
    mon:str
    diem:float
class thaymon1 (BaseModel):
    ten:str
    tuoi:int
    dsdiem:list[thaymon]
ds=[thaymon1(ten="My",tuoi=20,dsdiem=[thaymon(mon="toán",diem=10),thaymon(mon="CNTT",diem=10)]),thaymon1(ten="Lâm",tuoi=20,dsdiem=[thaymon(mon="tin học",diem=10),thaymon(mon="sử",diem=10)]),thaymon1(ten="Cầm",tuoi=20,dsdiem=[thaymon(mon="văn",diem=10),thaymon(mon="địa",diem=10)])]
logs =[]
class thaymon2(BaseModel):
    tenhs:str
    monmoi:str
@app.delete("/delete_bai3")
def delete_b3(data:thaymon2):
    # log=[] bắt buột khai bao trước lúc sd hàm , tốt nhất đặt dưới ds vì ds và log dùng chung cho global( global là biến được khai báo ngoài hàm)
    for i,hs in enumerate (ds):
        if hs.ten == data.tenhs:
            for k, tim in enumerate (hs.dsdiem):
                if tim.mon == data.monmoi:
                    mon_da_xoa = hs.dsdiem.pop(k)
                    logs.append(mon_da_xoa)
                    return {f"đã xóa,nhật kí:{logs},còn lại:{ds}"}
            raise HTTPException(404, " k tìm thấy môn")
    raise HTTPException(404," k tìm thây hs")

            
  
# cách xóa theo điều kiện cách 1 theo range 
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app= FastAPI()
class thaymon( BaseModel):
    mon:str
    diem:float
class thaymon1 (BaseModel):
    ten:str
    tuoi:int
    dsdiem:list[thaymon]
ds=[thaymon1(ten="My",tuoi=20,dsdiem=[thaymon(mon="toán",diem=4),thaymon(mon="CNTT",diem=10)]),thaymon1(ten="Lâm",tuoi=20,dsdiem=[thaymon(mon="tin học",diem=3),thaymon(mon="sử",diem=10)]),thaymon1(ten="Cầm",tuoi=20,dsdiem=[thaymon(mon="văn",diem=10),thaymon(mon="địa",diem=2)])]
logs =[]
class thaymon2(BaseModel):
    diemmoi:float
@app.delete("/delete_condition_bai4")
def delete_b4(data:thaymon2):
    for hs in ds:
        for j in range (len(hs.dsdiem)-1,-1,-1):  # j hiện tại là index
            if hs.dsdiem[j].diem < data.diemmoi:    # hs.dsdiem[j].diem : bắt buột vào dsdiem để lấy điểm tại vị trí j , mục đícch ss điểm
                da_xoa_mon = hs.dsdiem.pop(j)   
                logs.append(da_xoa_mon)  
    return{"logs":logs,"còn lại":ds}
            #range(star,stop,step)   
            #star: điểm bắt đầu đếm len(ds) trừ đi 1 vì stt trong python bắt đầu từ "0"
            # stop : điểm dừng , lấy điểm dừng phía sau điểm dừng 1 số 
            # step : bước nhảy, ví dụ lấy từ sau mỗi lần lấy 1 số để tính hoặc khoản cách lấy số đầu đến số sau bằng 2 tức là cách 2 tính 1 lần for 


from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app= FastAPI()
class thaymon( BaseModel):
    mon:str
    diem:float
class thaymon1 (BaseModel):
    ten:str
    tuoi:int
    dsdiem:list[thaymon]
ds=[thaymon1(ten="My",tuoi=20,dsdiem=[thaymon(mon="toán",diem=4),thaymon(mon="CNTT",diem=10)]),thaymon1(ten="Lâm",tuoi=20,dsdiem=[thaymon(mon="tin học",diem=3),thaymon(mon="sử",diem=10)]),thaymon1(ten="Cầm",tuoi=20,dsdiem=[thaymon(mon="văn",diem=10),thaymon(mon="địa",diem=2)])]
logs =[]
class thaymon2(BaseModel):
    diemmoi:float
@app.delete("/delete_condition_bai5")
def delete_b4(data:thaymon2):
    for hs in ds:
        dsxoa=[] # reset lại môn của mỗi hs để lưu vào dsxoa
        for mon in hs.dsdiem:
            if mon.diem < data.diemmoi:
                dsxoa.append(mon)
                logs.append(mon)
        for xoa_mon in dsxoa:
            hs.dsdiem.remove(xoa_mon)
    return {"logs":logs,"ds còn lại":ds}
                



from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class dl_dl(BaseModel):
    tenmon:str
    diem:float
ds=[dl_dl(tenmon="Toán",diem=4),dl_dl(tenmon="Văn",diem=10),dl_dl(tenmon="Anh",diem=4)]
logs=[]
class dl_1 (BaseModel):
    diemmoi:float

@app.delete("/dl_1")
def dl_dl (data:dl_1):
    for i in range(len(ds)-1,-1,-1):
        if ds[i].diem < data.diemmoi:
            xoa_mon=ds.pop(i) #chỉ chứa 1 môn rồi rì sét lại cho mỗi lần xóa
            logs.append(xoa_mon)
    return {"ds xóa ":logs,"ds còn lại":ds}




from fastapi import FastAPI 
from pydantic import BaseModel
app=FastAPI()
class mon (BaseModel):
    tenmon:str
    diem:float
ds=[mon(tenmon="toán",diem=10),mon(tenmon="anh",diem=10),mon(tenmon="sinh",diem=10),mon(tenmon="toán",diem=10),mon(tenmon="toán",diem=10)]
logs =[]
class ten (BaseModel):
    tenmonmoi:str
@app.delete("/dl_ten_range")
def dl_range_nhieuten (data:ten):
    for i in range (len(ds)-1,-1,-1):
        if ds[i].tenmon == data.tenmonmoi:
            xoa_mon= ds.pop(i)
            logs.append({"mon":xoa_mon,"vị trí":i})
    return {"ds xóa":logs}




from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class mon (BaseModel):
    tenmon:str
    diem:float
class ten (BaseModel):
    ten:str
    dsmon:list[mon]
ds=[ten(ten="My",dsmon=[mon(tenmon="anh",diem=10),mon(tenmon="toán",diem=10)]),ten(ten="Linh",dsmon=[mon(tenmon="toán",diem=10),mon(tenmon="văn",diem=10)]),ten(ten="Lâm",dsmon=[mon(tenmon="tin học",diem=10),mon(tenmon="toán",diem=10)])]
class dl_tenmon(BaseModel):
    tenmonmoi:str
@app.delete("/del_tenmon")
def dl_tenmon(data:dl_tenmon):
    for hs in ds:
        for i in range (len(hs.dsmon)-1,-1,-1):
            if hs.dsmon[i].tenmon == data.tenmonmoi:
                xoa_mon = hs.dsmon.pop(i)
                logs.append({"tenhs":hs.ten,"môn":xoa_mon,"vị trí":i})
    return {"ds xóa":logs}  




    

from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class mon (BaseModel):
    tenmon:str
    diem:float
class ten (BaseModel):
    ten:str
    dsmon:list[mon]
ds=[ten(ten="My",dsmon=[mon(tenmon="anh",diem=10),mon(tenmon="toán",diem=3)]),ten(ten="Linh",dsmon=[mon(tenmon="toán",diem=10),mon(tenmon="văn",diem=2)]),ten(ten="Lâm",dsmon=[mon(tenmon="tin học",diem=4),mon(tenmon="toán",diem=10)])]
logs=[]
class dl_tenmon(BaseModel):
    diemmoi:float
@app.delete("/del_diem")
def dl_tenmon(data:dl_tenmon):
    for hs in ds:
        for i in range (len(hs.dsmon)-1,-1,-1):  
            if hs.dsmon[i].diem < data.diemmoi:
                xoa_diem= hs.dsmon.pop(i)
                logs.append({"tenhs":hs.ten,"mon xóa":xoa_diem.tenmon,"vị trí":i,"diem":xoa_diem.diem})
    return{"ds xóa":logs}
              

                        #xoa vị trí 
from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class hs (BaseModel):
    ten:str
    tuoi:int
ds=[hs(ten="My",tuoi=20),hs(ten="Lâm",tuoi=20),hs(ten="Linh",tuoi=20),hs(ten="Tuấn",tuoi=20),hs(ten="kiệt",tuoi=20),hs(ten="Hoàng",tuoi=20)]
log=[]
class dl_hs(BaseModel):
    tenhs:str
@app.delete("/dl_tenhs")
def dl_hs(data:dl_hs):
    for i in range (len(ds)-1,-1,-1):
        if ds[i].ten == data.tenhs:
            xoa_hs = ds.pop(i)
            logs.append({"tenhs":xoa_hs.ten,"vị trí xóa":i})
    return {"ds hs bị xóa":logs,"ds còn lại":ds} 


                    #xoa dtb
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class mon(BaseModel):
    tenmon:str
    diem:float
class hs (BaseModel):
    ten:str
    dsmon:list[mon]
ds=[hs(ten="Lâm",dsmon=[mon(tenmon="toán",diem=3),mon(tenmon="địa",diem=4)]),hs(ten="Ngọc",dsmon=[mon(tenmon="Anh",diem=10),mon(tenmon="toán",diem=5)]),hs(ten="Sương",dsmon=[mon(tenmon="Văn",diem=3),mon(tenmon="Văn",diem=5)])]
logs=[]
class del_dtb (BaseModel):
    dtb_moi : float
@app.delete('/dl_dtb')
def dl_dtb (data:del_dtb):
    for i in range (len(ds)-1,-1,-1):
        tongdiem=0
        for diem in ds[i].dsmon:
            tongdiem += diem.diem
        dtb = tongdiem/len(ds[i].dsmon)
        if dtb < data.dtb_moi:
            xoa_hs = ds.pop(i)
            logs.append({"tên hs":xoa_hs.ten,"dtb":dtb,"vị trí xóa": i})
    return {"ds bị xóa":logs}

                                            #CRUD
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
ds=[hs(ten="My",tuoi=20,dsmon=[mon(tenmon="toán",diem=5)]),hs(ten="Lâm",tuoi=20,dsmon=[mon(tenmon="toán",diem=5)])]
class mon (BaseModel):
    tenmon:str
    diem:float
class ds_hs (BaseModel):
    ten:str
    tuoi:int
    dsmon:list[mon] 

@app.get("/crud_get_ten/{ten}")
def crud_get(ten=str):
    for hs in ds:
        if hs.ten == ten :
            return hs
    
    raise HTTPException(status_code=404,detail=" k tìm thây hs") 


from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class mon (BaseModel):
    tenmon:str
    diem:float
class ds_hs (BaseModel):
    ten:str
    tuoi:int
    dsmon:list[mon] 
class ds1 (BaseModel):
    ds:list[ds_hs]
@app.post("/crud_post")
def crud_post(data:ds1):
    
    for hs in ds:
        ds.append(data)     # đã có ds rồi , muốn từ ds đó thêm học sinh thì trong "(data)"
    return ds



from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class hs (BaseModel):
    ten:str
    tuoi:int
ds=[hs(ten="My",tuoi=20),hs(ten="Linh",tuoi=20),hs(ten="Ngọc",tuoi=20),hs(ten="Lâm",tuoi=20)]
class hs_1 (BaseModel):
    tenmoi:str
@app.put("/crud_put")
def crud_put (data:hs_1):
    for hs in ds:
        if hs.ten == data.tenmoi:
            hs.ten = data.tenmoi
            return hs
    raise HTTPException(404,"k tìm thấy hs ")



from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel
app = FastAPI ()
class ds(BaseModel):
    ten:str
    tuoi:int
ds=[ds(ten="Bình",tuoi=20),ds(ten="Yến",tuoi=20),ds(ten="Hùng",tuoi=20),ds(ten="Ngọc",tuoi=20)]
logs=[]
class ds_1 (BaseModel):
    tenmoi:str
@app.delete("/crud_delete")
def crud_delete (data:ds_1):
    print (ds) # xem dữ liệu
    dsxoa=[]
    for hs in ds:        
        if data.tenmoi == hs.ten:                                 
            dsxoa.append(hs) 
            logs.append(hs)
        for xoa in dsxoa:
            ds.remove(xoa) 
            print("dsxoa",dsxoa)  # xem dữ liệu                   
            return {"hs bị xóa":logs,"ds còn lại":ds}
        
    raise HTTPException(404,"k tìm thây hs ")


    








    



               


                







        






   
   
    
        
       
    

    

    
    
            

            







