from fastapi import FastAPI,APIRouter
from models import hocsinh
from data import ds

router = APIRouter(prefix="/crud_qlhs",tags=["QLHS"])
@router.get("/")                        # query sử dụng cho get , có thể để trong mục get.py
def tim (ten:str ="",tuoi:int =0):      # ="" và =0 : nghĩa là không cần nhập 1 trong 2 ô điều được
    dshs=[]
    for hs in ds:
        
        if ten.lower() in hs.ten.lower() and hs.tuoi== tuoi :
            dshs.append(hs)
        elif ten.lower() == hs.ten.lower() and tuoi == 0:
            dshs.append(hs.ten)
        elif ten.lower() == "" and hs.tuoi == tuoi:
            dshs.append({"tenhs":hs.ten,"tuoi":hs.tuoi})
    if len(dshs)>0:
        return dshs       
    if len(dshs)==0:
            return {"kq":"k tìm thấy hs"}
    # có thể dùng biến flag(cờ)
    


from fastapi import FastAPI,APIRouter
from models import hocsinh
from data import ds

router = APIRouter(prefix="/crud_qlhs",tags=["QLHS"])
@router.get("/tim_khoang_tuoi")                        
def tim_khoang_tuoi (tuoi_min:int =0,tuoi_max:int=100):
    dshs=[]
    for hs in ds:
        if tuoi_min <= hs.tuoi<= tuoi_max:
            dshs.append(hs)
    if len(dshs)>0:
        return dshs   
    return {"kq":" k tìm thấy hs "} 




from fastapi import FastAPI,APIRouter
from models import hocsinh
from data import ds

router = APIRouter(prefix="/crud_qlhs",tags=["QLHS"])
@router.get("/tim_khoantuoi_ten")                        
def tim_khoantuoi_ten (ten:str,tuoi_min:int =0,tuoi_max:int=100):
    dshs=[]
    for hs in ds:
        print (hs)
        if ten.lower() in hs.ten.lower() and tuoi_min <= hs.tuoi<= tuoi_max:
            dshs.append(hs)
    if len(dshs)>0:
        return dshs   
    return {"kq":" k tìm thấy hs "} 



                                #Tìm top2 đồng hạng và pagination(phân trang)
from fastapi import FastAPI,APIRouter
from models import hocsinh
from data import ds

router = APIRouter(prefix="/crud_qlhs",tags=["QLHS"])
@router.get("/onlai_th")                        
def onlai_th (ten:str="",page:int=1,page_size:int=2):   #page:trang 1,2,3 , page_size:trang 1 chứa 3 hs hoặc 2 sản phẩm tùy vào sl đề cho
    ds_sorted=sorted(ds,key=lambda hs: hs.tuoi,reverse=True)
    top2=ds_sorted[:2]
    moc=top2[-1].tuoi
    for M in ds_sorted[2:]:
        if M.tuoi ==moc:
            top2.append(M)
        else:
            break
    skip=(page-1)*page_size     # thường ngta cho biết page_size để tính công thức skip
    return {"top2":top2[skip:skip+page_size],"dstop2":top2,"dssorted":ds_sorted}     


from fastapi import FastAPI,APIRouter
from models import hocsinh
from data import ds


router = APIRouter(prefix="/crud_qlhs",tags=["QLHS"])
@router.get("/query_2if")                        
def onlai_th (keu_sx:str="ten",reverse:bool = False): #lưu ý: keu_sx:str="ten" nghĩa là khai biến "str"sx theo "tên" hoặc "tuổi"
    if keu_sx == "ten":           # lưu ý : chỉ được dùng sort đặt dk , KHÔNG ĐƯỢC DÙNG "SORTED" VÌ SORTED LÀ 1 HÀM
        ds_sorted=sorted(ds,key=lambda hs: hs.ten,reverse=reverse)
    elif keu_sx == "tuoi":
        ds_sorted=sorted(ds,key=lambda hs: hs.tuoi,reverse=reverse)
    else:
        return{"kq":"kq k hợp lệ"}
    return ds_sorted




                                #Query
from fastapi import FastAPI,APIRouter,Query #công cụ mới : Query(...,gt=,lt=) 
from models import hocsinh
from data import ds
router = APIRouter(prefix="/crud_qlhs",tags=["QLHS"])
@router.get("/query_para") 
def query_para(reverse:bool=False,ten:str=Query("",min_length=2,max_length=20),page:int=Query(1,ge=1),page_size:int=Query(10,ge=1,le=50)):
    # "ten:str=Query("",min_length=2,max_length=20)":
                #  "" nghĩa là bắt buôc nhập nếu k nhập báo lỗi, nếu nhập ví dụ =1 mà bên swagger k nhập thì mặc định =1
    dshs=[]
    for hs in ds:
        if ten.lower()in hs.ten.lower():#có thể viết hs.ten==tennhưng khi cần tìm tên có chứa trùng chuỗi vd "An Lan","An Bình" thì dùng lower() để kt        
            dshs.append(hs)
    ds_sorted=sorted(dshs,key=lambda hs: hs.ten,reverse=reverse) # nên lấy ds vừa lộc để sorted
    skip=(page-1)*page_size
    pagination=ds_sorted[skip:skip+page_size]
    return {"pagination":pagination,"ds_sorted":ds_sorted,"lộc hs":dshs}
    # bài này còn xét theo pattern(mục đích kt dữ liệu đầu vào diễn ra trước khi chạy hàm) vì rộng nên học sau
    # Query kt Query Parameter trc khi vào hàm
    # field_validator kt body(model) trc khi vào hàm     



    


     








            
               
     