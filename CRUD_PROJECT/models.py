from pydantic import BaseModel

class hocsinh(BaseModel):
    tenmon:str
    diem:float 
class hs_2 (BaseModel):
    ten:str
    lop:str
    ds_mon:list[hocsinh]
class sua_mon(BaseModel):
    diemmoi:float
    tenmonmoi:str



class put_path_query(BaseModel):
    ten:str    |None=None  
    tuoi:int   |None=None
    lop:str     |None=None 
    gioitinh:str    |None=None



class delete_path_query (BaseModel):
    ten:str     |None=None
    lop:str     |None=None



class HocSinh(BaseModel):
    ten:str
    tuoi:int
    lop:str




class hs1 (BaseModel):
    ten:str
    lop:str
    tuoi:int
    diem:float
class hs2(BaseModel):
    ten:str
    lop:str



            #cách ẩn 1-2 field ngắn gọn nhanh
class hs3 (BaseModel):
    ten:str
    tuoi:int
    lop:str
    diem:float



class hs4 (BaseModel):
    ten:str
    tuoi:int    |None=None
    lop:str     |None=None
    diem:float
    

class hs5 (BaseModel):
    ten:str
    tuoi:int =18 
    lop:str ="12A"   
    diem:float    


class hs6 (BaseModel):
    ten:str
    tuoi:int  
    lop:str ="chưa có lớp"   
    diem:float



                        #RESPONSE MODEL + NESTED+ DICT + LIST
class DiaChi (BaseModel):
    thanh_pho:str
    quan:str |None=None
class HS7 (BaseModel):
    ten:str
    tuoi:int
    lop:str="chưa có lớp" 
    diem:float| None=None
    dia_chi:DiaChi

                        #RESPONSE MODEL +NESTED + LIST + TRẢ 1 HS 
class DC (BaseModel):
    thanh_pho:str
    quan:str |None=None
class HS8 (BaseModel):
    ten:str
    tuoi:int
    lop:str="chưa có lớp" 
    diem:float| None=None
    dia_chi:DC

                        #RESPONSE MODEL +NESTED + DICT + TRẢ TỪ KHÓA

class D_C (BaseModel):
    thanh_pho:str
    quan:str |None=None
class HS9 (BaseModel):
    ten:str
    tuoi:int
    lop:str="chưa có lớp" 
    diem:float| None=None
    dia_chi:D_C


                        #RESPONSE MODEL +NESTED +DICT + TRẢ TỪ KHÓA VỚI "CHỈ DUY NHẤT 1 HS ĐẦU THỎA DK TÙ KHÓA "

class DICH (BaseModel):
    thanh_pho:str
    quan:str |None=None
class HS10 (BaseModel):
    ten:str
    tuoi:int
    lop:str="chưa có lớp" 
    diem:float| None=None
    dia_chi:DICH



                        #RESPONSE +DTB
class HS11 (BaseModel):
    ten:str
    tuoi:int
    lop:str
    diem:float |None=None
    dia_chi:str
class HS12 (BaseModel):
    ten:str
    lop:str
    diem :float |None=None
    dtb:float
    xep_loai:str



                        #RESPONSE MODEL + SUMMARY/DICT
class HS13 (BaseModel):
    ten:str
    diem:float
    lop : str |None=None
class HS14 (BaseModel):
    tong_hs :int    |None=None
    hs_gioi: int    |None=None
    hs_yeu:int  |None=None



                        #RESPONSE MODEL + SUMMARY TỔNG HỢP
class HS15 (BaseModel):
    ten:str
    tuoi:int
    dtb:float
class HSDiem (BaseModel):           # thêm hsdiem để đúng class HS16 để khi trả kq max và min về đủ dsmax và dsmin
    ten:str
    dtb:float
class HS16 (BaseModel):
    tonghs:int
    max_dtb:list[HSDiem]
    min_dtb:list[HSDiem]
    tong_dtb:float
    hs_dat:int
    hs_chuadat:int

                                #RESPONSE MODEL 

class HS17 (BaseModel):
    ten:str
    tuoi:int
    dtb:float
class DSDiem (BaseModel):
    ten:str
    diem : float
    xeploai:str
class HS18(BaseModel):
    tonghs:int
    hsgioi:list[DSDiem]
    hskha:list[DSDiem]
    hstb:list[DSDiem]
    hsyeu:list[DSDiem]




                                #CRUD_id
class Lop(BaseModel):
    ten_lop:str
    phong:str
class crud (BaseModel):
    id:int
    ten:str
    tuoi:int
    diem:float
    lop:Lop

                                #CRUD_TEN
class timten  (BaseModel):
    ten:str
    tuoi:int


                                #CRUD_POST
class hs19 (BaseModel):
    id:int
    ten:str
    tuoi:int


                                #crud+nested+validation
class Lop1 (BaseModel):
    tenlop:str
    khoi:int
class hs20 (BaseModel):
    id:int
    ten:str
    tuoi:int
    lop:Lop1



                            # crud+ put
class put_hs(BaseModel):
    id:int
    ten:str
    tuoi:int
class sua (BaseModel):
    idmoi:int
    tenmoi:str
    tuoimoi:int




                                #delete
class delete_th (BaseModel):
    id:int
    ten:str
    tuoi:int
class delete_2 (BaseModel):
    idmoi:int
                            #delete_path
class delete_path (BaseModel):
    id:int
    ten:str
    tuoi:int



                            #crud_project
class crud_pr (BaseModel):
    id:int
    ten:str
    tuoi:int    
    diem:float




   
   