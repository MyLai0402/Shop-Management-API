from fastapi import FastAPI,APIRouter
from models import hocsinh
from data import ds

router = APIRouter(prefix="/crud_qlhs",tags=["QLHS"])
@router.get("/{ten}")
def lay_ds(ten=str):
    dshs=[]
    for hs in ds:
        if ten.lower() in hs.ten.lower():
            dshs.append(hs)
    return {"kq":dshs}



from fastapi import FastAPI,APIRouter
from models import hocsinh,HocSinh
from data import ds
from data import ds_response


router = APIRouter(prefix="/response",tags=["QLHS"])
@router.get("/hs",response_model=list[HocSinh]) # trả hết tất cả class 
def get_response ():
   return ds_response





from fastapi import FastAPI,APIRouter
from models import hocsinh,HocSinh
from data import ds
from data import ds_response
from data import ds_hide
from models import hs1,hs2


router = APIRouter(prefix="/response_1",tags=["QLHS"])
@router.get("/hs",response_model=list[hs2]) # tạo thêm class và các trường cần trả kq 
def hide_hs1():
    return ds_hide



from fastapi import FastAPI,APIRouter
from models import hocsinh,HocSinh
from data import ds
from data import ds_response
from data import ds_hide,ds_exclude
from models import hs1,hs2,hs3


router = APIRouter(prefix="/response_1",tags=["QLHS"])
@router.get("/hs3",response_model=list[hs3],response_model_exclude={"tuoi","diem"}) #trả kq: "Loại" tuoi, diem
def get_exclude ():
    return ds_exclude   


from fastapi import FastAPI,APIRouter
from models import hocsinh,HocSinh
from data import ds
from data import ds_response
from data import ds_hide,ds_exclude,ds_include
from models import hs1,hs2,hs3,hs4


router = APIRouter(prefix="/response_1",tags=["QLHS"])
@router.get("/hs4",response_model=list[hs4],response_model_exclude_none= True) # chỉ trả kq khi nhập giá trị cho feild (nếu trong ds_include field = None thì loại bỏ hết dù có giá trị mặc định vẫn bỏ ) 
def get_include ():
    return ds_include




from fastapi import FastAPI,APIRouter
from models import hocsinh,HocSinh
from data import ds
from data import ds_response
from data import ds_hide,ds_exclude,ds_include,ds_unset
from models import hs1,hs2,hs3,hs4,hs5
router = APIRouter(prefix="/response_1",tags=["QLHS"])
@router.get("/hs5",response_model=list[hs5],response_model_exclude_unset= True)
# unset  trả kq khi giá trị có nhập vào từ đối tượng , còn lại loại bỏ tất cả , nếu k có giá trị nhập vào đối tượng vẩn k bị lỗi
def get_unset():
    return ds_unset




from fastapi import FastAPI,APIRouter
from models import hocsinh,HocSinh
from data import ds
from data import ds_response
from data import ds_hide,ds_exclude,ds_include,ds_unset,ds_default
from models import hs1,hs2,hs3,hs4,hs5,hs6
router = APIRouter(prefix="/response_1",tags=["QLHS"])
@router.get("/hs6",response_model=list[hs6]) 
# k có models_defaults , chỉ trẩ kq khi giá trị nhập vào đối tượng , còn field nào bằng default thì bỏ k trả kq  
def get_default():
    return ds_default



     
                        #RESPONSE MODEL + NESTED+ LIST
from models import HS7,DiaChi
from data import ds_all
router = APIRouter (prefix="/response_all",tags=["QLHS"])
@router.get("/HS7_all",response_model=list[HS7]) # lưu ý:khi trả hết âll hs ds thì response_model=list[thay bằng tên trong ds trong data]
def get_all ():
    return ds_all



                        #RESPONSE MODEL + NESTED+  DICT+ TRẢ VỀ 1HS đầu 
from models import HS8,DC
from data import ds_HS8
router =APIRouter(prefix="/one_hs",tags=["QLHS"])
@router.get("/HS8_ONE",response_model=HS8)      # lưu ý : khi trả kq: 1 hs hay dict thì response_model= tổng tên class "HS8"
def get_HS8_One():
    return ds_HS8[0]    #trả kq 1 hs đầu


from models import HS9,D_C
from data import ds_HS9
router =APIRouter(prefix="/tukhoa",tags=["QLHS"])
@router.get("/tukhoa",response_model=list[HS9])
def get_tukhoa_response (tu_khoa:str):
    kq=[]
    for hs in ds_HS9:
        if tu_khoa.lower() in hs.ten.lower():
            kq.append(hs)
    return kq



                          #RESPONSE Model +NESTED +DICT +TU KHÓA CHỈ LẤY DUY NHẤT HS ĐẦU THỎA TỪ KHÓA

from models import HS10,DICH
from data import ds_HS10
router =APIRouter(prefix="/tukhoa",tags=["QLHS"])
@router.get("/tukhoa",response_model=HS10)
def get_tukhoa_response_one(tu_khoa:str):   
    for hs in ds_HS10:
        if tu_khoa.lower() in hs.ten.lower():
            return hs   # vì chỉ lấy duy nhất hs đầu thỏa điều kiện từ khóa nên chỉ return thôi không cần append để lấy all như bài trên        



                       # RESPONSE +DTB
from models import HS11,HS12
from data import ds_HS11
router = APIRouter (prefix="/DTB",tags=["QLHS"])
@router.get("/DTB_RESPONSE", response_model=list[HS12])
def DTB_RESPONSE():
   
    kq=[]
    for hs in ds_HS11:
        
        if hs.diem >=8 :
            xep_loai ="HS GIỎI"
            kq.append({"ten":hs.ten,"lop":hs.lop,"diem":hs.diem,"dtb":hs.diem,"xep_loai":"GIỎI"})
        elif 6.5 <= hs.diem <8 :
            xep_loai ="HS KHÁ"
            kq.append({"ten":hs.ten,"lop":hs.lop,"diem":hs.diem,"dtb":hs.diem,"xep_loai":"KHÁ"})
        elif 5 <= hs.diem <6.5:
            xep_loai ="HS TB"
            kq.append({"ten":hs.ten,"lop":hs.lop,"diem":hs.diem,"dtb":hs.diem,"xep_loai":"TB"})
        else:
            xep_loai ="YẾU"
            kq.append({"ten":hs.ten,"lop":hs.lop,"diem":hs.diem,"dtb":hs.diem,"xep_loai":"YẾU"})
    return kq

#lưu ý : khi muốn trả kq theo class HS12 thì phần append phải đủ và đúng all chính tả bên field của HS12
# có thể sd 1 class vẩn được ( nếu 1 class thì data nhập vào k ghi xếp loại vì response vẩn trả theo list[ds], k báo lỗi hay thếu, cách làm tương tự 2 class )



                                #RESPONSE + SUMMARY
from models import HS13,HS14
from data import ds_HS13
router =APIRouter(prefix="/summary",tags=["QLHS"])
@router.get("/summary",response_model=list[HS14])
def get_summary():
    tong_hs =len(ds_HS13)
    dem8 =0
    dem5 =0
    kq=[]
    for hs in ds_HS13:   
        if hs.diem >=8:        
            dem8 += 1
            hs_gioi = dem8
        elif hs.diem <5:
            dem5 += 1
            hs_yeu=dem5   
    kq.append({"tong_hs":tong_hs,"hs_gioi":hs_gioi,"hs_yeu":hs_yeu})
    return kq


from models import HS15,HS16
from data import ds_HS15
router=APIRouter(prefix="/summary",tags=["QLHS"])
@router.get("",response_model=HS16)
def tong_hop():
    tonghs=len(ds_HS15)  
    tong_dtb=0
    max_dtb =0
    min_dtb=999
    max_ten=""
    min_ten=""
    dsmax=[]
    dsmin=[]
    hs_dat=0
    hs_chuadat=0
    for i in ds_HS15:    
        tong_dtb += i.dtb
        if i.dtb >max_dtb:
            max_dtb=i.dtb
            max_ten= i.ten
            dsmax=[]
            dsmax.append({"ten":i.ten,"dtb":i.dtb})
        elif i.dtb == max_dtb:
            dsmax.append({"ten":i.ten,"dtb":i.dtb})
        if i.dtb <min_dtb:
            min_dtb=i.dtb
            min_ten=i.ten
            dsmin=[]
            dsmin.append({"ten":i.ten,"dtb":i.dtb})
        elif i.dtb == min_dtb:
            dsmin.append({"ten":i.ten,"dtb":i.dtb})
        if i.dtb >=5:
            hs_dat += 1
        elif i.dtb <5:
            hs_chuadat += 1
    return HS16(tonghs=tonghs,max_dtb=dsmax,min_dtb=dsmin,tong_dtb=tong_dtb,hs_dat=hs_dat,hs_chuadat= hs_chuadat) 
    # SUMMARY  trả kq như model HS16 , xem mẫu return trên áp dụng cho all return trả kq theo summary model

                            #RESPONSE MODEL

from models import HS17,HS18
from data import ds_HS17
router = APIRouter(prefix="/summary2",tags=["QLHS"])
@router.get("",response_model=HS18)
def tonghop_summary ():
    tonghs=len(ds_HS17)
    xeploai=""
    dsgioi=[]
    dskha=[]
    dstb=[]
    dsyeu=[]
    for k in ds_HS17:
        if k.dtb >=8:
            xeploai ="hsgioi"
            dsgioi.append({"ten":k.ten,"diem":k.dtb,"xeploai":xeploai})
        elif 6.5 <= k.dtb <8:
            xeploai="hskha"
            dskha.append({"ten":k.ten,"diem":k.dtb,"xeploai":xeploai})
        elif 5<= k.dtb < 6.5:
            xeploai ="hstb"
            dstb.append({"ten":k.ten,"diem":k.dtb,"xeploai":xeploai})
        else:
            xeploai ="hsyeu"
            dsyeu.append({"ten":k.ten,"diem":k.dtb,"xeploai":xeploai})   
    return HS18(tonghs=tonghs,hsgioi=dsgioi,hskha=dskha,hstb=dstb,hsyeu=dsyeu)

                            #CRUD_id
from fastapi import Path ,HTTPException
from models import crud,Lop
from data import ds_crud
router =APIRouter(prefix="/crud_th/{id}",tags=["QLHS"])         #{id}:path
@router.get("",response_model=crud)
def crud_th(id:int):
    for i in ds_crud:
        if id == i.id:
            return i
    raise HTTPException(status_code=404,detail="k tìm thấy id ")


                             #CRUD_TEN
from fastapi import Query,HTTPException
from models import timten
from data import ds_timten
router=APIRouter(prefix="/crud_timten")
@router.get("",response_model=list[timten],tags=["QLHS"])
def crud_timten(ten:str=Query(min_length=1)):
    dshs=[]
    for hs in ds_timten:
        if ten.lower() in hs.ten.lower():
            dshs.append({"ten":hs.ten,"tuoi":hs.tuoi})
    if len(dshs)==0:
        raise HTTPException(status_code=404,detail="k tim thay ten hs")
    return dshs



                            #crud_project
from models import crud_pr
from data import ds_crud_pr 
router=APIRouter(prefix="/crud_pr",tags=["QLHS"])
@router.get("")
def crud_pr (tuoi:int | None = None):
    ds=[]
    for hs in ds_crud_pr:
        if tuoi is None:
            return ds_crud_pr
        if tuoi == hs.tuoi:
            ds.append(hs)
    return ds

                            #crud+path
from fastapi import HTTPException
from models import crud_pr
from data import ds_crud_pr 
router=APIRouter(prefix="/crud_path",tags=["QLHS"])
@router.get("/{id}")
def crud_path (id:int):
    for hs in ds_crud_pr:
        if id == hs.id:
            return hs 
    raise HTTPException(404,"k tìm thấy hs")




    
    






           


    
            


