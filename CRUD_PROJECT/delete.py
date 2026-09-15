from fastapi import APIRouter,HTTPException
from data import ds
router = APIRouter(prefix="/crud_qlhs",tags=["QLHS"])
@router.delete("/{ten}")
def xoa_ten (ten:str):  # lưu ý : get(path và query), delete(có thể dùng path "ten:str", cũng có thể truyền dữ liệu từ body " data:hs_2")
    for i,hs in enumerate(ds):
        if hs.ten == ten:
            ds.pop(i)
            return {"đã xóa":hs,"ds còn lại":ds}
    raise HTTPException(404,"k tìm thấy hs")




                #delete_path_query những bài delete tốt nhất nên có is None và not is None vì dễ bị trùng dk
from fastapi import APIRouter,HTTPException
from data import ds_delete
from models import delete_path_query
router=APIRouter(prefix="/crud_qlhs",tags=["QLHS"])
@router.delete("/delete_path_query")
def xoa (data:delete_path_query |None=None,ten:str|None=None,lop:str|None=None):
    if ten is None and lop is None and data is None:
                raise HTTPException (400,"không tìm thấy dữ liệu") 
    logs=[] # đặt logs vào trong mục đích để khi xóa lưu tất cả thôg tin vào và xóa 1 lần cho gọn 
    dslop=[]
    dsten=[]
    
    for i,hs in enumerate(ds_delete):
        if ds_delete[i].ten == ten and ds_delete[i].lop == lop:   
            logs.append(hs)     # <= append logs xóa 1 lần cho gọn
        elif ten is None and ds_delete[i].lop ==lop:
            dslop.append(hs)
            logs.append(hs)    # <= append logs xóa 1 lần cho gọn
        elif  data is not None and ds_delete[i].ten == data.ten :
            dsten.append(hs)
            logs.append(hs)     # <= append logs xóa 1 lần cho gọn
    for xoa in logs:
        ds_delete.remove(xoa)
    if len(logs)==0:
        raise HTTPException(404,"k tìm thấy tên và lớp")  
    return{"logs":logs,"ds còn":ds_delete}
        # bài này có thể làm xóa remove dễ hơn nhưng tập làm quen xóa vị trí và append cho quen 
        
                
            
                        #delete_th
from fastapi import HTTPException
from models import delete_th,delete_2
from data import ds_delete
logs=[]
router=APIRouter(prefix="/crud_delete_th",tags=["QLHS"])
@router.delete("/delete_th")
def delete (data:delete_2):
    for i,hs in enumerate(ds_delete):
        if data.idmoi == hs.id:
            xoa_hs=ds_delete.pop(i)
            logs.append(xoa_hs)
            return{"đã xóa":logs,"còn lại":ds_delete}
    raise HTTPException(status_code=404,detail=" k tìm thấy id cần xóa ")
             

                        #delete_path
from fastapi import HTTPException
from models import delete_path
from data import ds_de_path
logs=[]
router=APIRouter(prefix="/crud_delete_th",tags=["QLHS"])
@router.delete("/delete_th/{id}")
def delete (id:int):
    for hs in ds_de_path:
        if id == hs.id:
            xoa_hs= ds_de_path.remove(hs)
            logs.append(xoa_hs)
            return{"xóa":logs,"còn lại":ds_de_path}
    raise HTTPException(404,"k tìm thấy hs")

                        #delete_crud
from models import crud_pr
from data import ds_crud_pr
router =APIRouter(prefix="/crud_delete",tags=["QLHS"])
logs=[]
@router.delete("/{id}")
def crud_delete (id:int):
    for i,hs in enumerate(ds_crud_pr):
        if id == hs.id:
            xoa_hs = ds_crud_pr.pop(i)
            logs.append(xoa_hs)
            return {"xóa":logs,"còn lại":ds_crud_pr}
    raise HTTPException(404,"l tìm thây hs")




          
