from fastapi import FastAPI,APIRouter,HTTPException
from models import hocsinh,hs_2
from data import ds
router=APIRouter(prefix="/crud_qlhs",tags=["QLHS"])
@router.put("")
def sua_hs(data:hs_2):
    for hs in ds:
        for i ,hs in enumerate (ds):
            if hs.ten == data.tenmoi:
                ds[i].ten = data.tenmoi
                return hs
    raise HTTPException(404,"k tìm thấy hs")


                            #put_ kết hơp parameter và nhận body class
from fastapi import FastAPI,APIRouter,HTTPException
from models import hocsinh,hs_2
from data import ds
router=APIRouter(prefix="/crud_put_cn",tags=["QLHS"])
@router.put("/put_cn/{ten}")
def put_cn(data:hs_2,ten:str):
    for hs in ds:
        if hs.ten == ten:
            hs.tuoi= data.tuoimoi
            hs.lop = data.lopmoi
            return hs
    else:
        raise HTTPException(status_code=404,detail="k tìm thây hs")



from fastapi import FastAPI,APIRouter,HTTPException
from models import hocsinh,hs_2
from data import ds
router=APIRouter(prefix="/put_parameter_body",tags=["QLHS"])
@router.put("/put_cn/{ten},{tuoi},{lop}")
def put_paramester_body(data:hs_2,ten:str,lop:str,tuoi:int):
    for hs in ds:
        if hs.ten==ten and hs.tuoi==tuoi and hs.lop==lop:
            hs.ten=data.tenmoi
            hs.lop= data.lopmoi
            hs.tuoi= data.tuoimoi
            return hs
    raise HTTPException(status_code=404,detail=" k tìm thấy hs ")



                #dạng 4: dùng enumerate , và trước vị trí là một danh sách mới xd được vị trí " công thức mẫu: ds[i]"
from fastapi import FastAPI,APIRouter,HTTPException
from models import hocsinh,hs_2
from data import ds
router=APIRouter(prefix="/put_enumerate",tags=["QLHS"])
@router.put("/put_enumerate/{ten}")
def put_ten(data:hs_2,ten:str):
    for i,hs in enumerate(ds):
        if hs.ten == ten:
            ds[i].tuoi = data.tuoimoi               # phải là ds[i] vì trước vị trí thì là một danh sách để xác định vị trí 
            ds[i].lop = data.lopmoi                 # lưu ý : không được dùng hs[i] vì hs là biến k xác định dc
            return ds[i]
    raise HTTPException(status_code=404,detail="k tìm thây hs")




                        #dạng 5:enumerate_parameter_body_nhiều dk
from fastapi import FastAPI,APIRouter,HTTPException
from models import hocsinh,hs_2
from data import ds
router=APIRouter(prefix="/put_enumerate_pr_dk",tags=["QLHS"])
@router.put("/put_enumerate/{ten}/{lop}")
def put_enum_pr_dk(data:hs_2,ten:str,lop:str):
    for i,hs in enumerate(ds):
        if hs.ten == ten and hs.lop == lop:
            ds[i].ten = hs.ten
            ds[i].tuoi = data.tuoimoi
            ds[i].lop = data.lopmoi
            return ds[i]
    raise HTTPException(status_code=404, detail=" k tìm thấy hs ")






                        #dạng6: 

from fastapi import FastAPI,APIRouter,HTTPException
from models import hocsinh,hs_2
from data import ds
router=APIRouter(prefix="/put_enumerate_pr_dk",tags=["QLHS"])
@router.put("/put_enumerate/{lop}")                 #lop =>: path prameter
def put_enum_pr_dk(data:hs_2,lop:str):              #lop =>: body swagger , data: nhận dữ liệu class body        
    kq=[]
    for hs in ds:
        if hs.lop == lop:
            hs.tuoi = data.tuoimoi
            kq.append({"tên hs":hs.ten,"tuôi": hs.tuoi})
    if len(kq)==0:
        raise HTTPException(status_code=404, detail=" k tìm thấy lop")
    return kq





                        #dạng7: lưu ý append trong danh sách riêng của học sinh chứ k phải append vào ds
                        # Nên: "hs.ds_mon" nghĩa là thêm môn vào ds môn của riêng hs đó , chứ k được append vào ds

from fastapi import FastAPI,APIRouter,HTTPException
from models import hocsinh,hs_2,sua_mon
from data import ds
router=APIRouter(prefix="/put_enumerate_pr_dk",tags=["QLHS"])
@router.put("/put_monhoc/{tenmon}")                 
def put_monhoc(data:sua_mon,ten:str,tenmon:str):
    
    for hs in ds:
        if hs.ten == ten:
            tim_mon= False
            for i in hs.ds_mon:
                if i.tenmon == tenmon:
                    i.diem = data.diemmoi
                    tim_mon=True
                    break           
            if tim_mon==False :
                hs.ds_mon.append({"môn":data.tenmonmoi,"diem":data.diemmoi})       
                return {"kq":hs.ds_mon}   
    raise HTTPException (404," k tìm thây hs")




                                #Dạng8:put + nhiều path +nhiều query + body class  
from fastapi import FastAPI,APIRouter,HTTPException
from models import hocsinh,hs_2,sua_mon,put_path_query
from data import ds,dshs
router=APIRouter(prefix="/put_path_query",tags=["QLHS"])    
@router.put("/lop/{lop}/hoc_sinh/{ten}")      #path :cố định , tìm đúng tên , băt buột bên swagger phải nhập           
def put_path_query(ten:str,lop:str,tuoi:int|None=None,gioitinh:str|None=None,data:put_path_query|None=None):    #query ,body class 
    for hs in dshs:
        if hs.ten ==ten and hs.lop==lop:
            if tuoi is not None:
                hs.tuoi=tuoi
            if gioitinh is not None:
                hs.gioitinh = gioitinh
            if data is not None:  # if data: để xét cả data, if hs."" mục đích xét riêng lẻ tránh ghi đè khi muốn thay đổi thông tin phần path query
                if data.ten is not None:    # tên có trong path bắt buôc nhập tại path swagger, nhưng k bắt buột nhập ở body
                    hs.ten =data.ten
                if data.tuoi is not None:
                    hs.tuoi =data.tuoi
                if data.lop is not None:    # lop có trong path bắt buôc nhập tại path swagger, nhưng k bắt buột nhập ở body
                    hs.lop =data.lop
                if data.gioitinh is not None:
                    hs.gioitinh =data.gioitinh
        return hs
    raise HTTPException(404,"k tìm thây hs")
# ứng dụng thực tế: tìm đúng tên và lớp(cố định) , tiếp theo cập nhật và sửa được thông tin của tất cả trường và trả đúng kq thông tin của hs đó 
# có thể sữa luôn cả path ( tên và lớp ) cố định 
#text swagger:body không bị đè hoặc muốn giữ lại giá trị trên path hoặc query thì gõ "null" sẽ giữ lại kết quả cũ, hoặc muốn giữ trường nào thì"null" trường đó 


                                    #crud_put
from fastapi import HTTPException
from models import put_hs,sua
from data import ds_put
router=APIRouter(prefix="/put_ds",tags=["QLHS"])
@router.put("/suatuoi")
def suatuoi (data:sua):
    for hs in ds_put:
        if hs.id == data.idmoi:
            hs.ten = data.tenmoi
            hs.tuoi = data.tuoimoi
            return hs
    raise HTTPException(404,"k tim thay hs")


                                    #crud_project
from fastapi import HTTPException
from models import crud_pr
from data import ds_crud_pr
router=APIRouter(prefix="/crud_pr",tags=["QLHS"])
@router.put("/{id}")
def crud_post(id:int |None=None,data:crud_pr |None=None ):
    tim_hs= False
    for hs in ds_crud_pr:
        if id == hs.id :
            hs.ten = data.ten
            hs.diem =data.diem
            hs.tuoi = data.tuoi
            tim_hs=True
            return hs
        if data.diem < 0 or data.diem > 10:
            raise HTTPException(400,"diem k hợp lệ")   
    if tim_hs ==False:
        if id != hs.id:
            raise HTTPException(404," k tìm thấy hs ")   
    return hs     


    








                        
    


       









