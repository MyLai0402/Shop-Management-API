from fastapi import FastAPI,APIRouter
from models import hocsinh
from data import ds
router=APIRouter(prefix="/crud_qlhs",tags=["QLHS"])
@router.post("")
def them_hs(data:hocsinh):
    ds.append(data)
    return {"ds thêm thành công":ds}



                #CRUD_POST ( nhan them hs vao ds)
from models import hs19
router=APIRouter(prefix="/crud_post",tags=["QLHS"])
@router.post("",response_model=hs19)            # bai nay chi nhan nhap them 1 hs 
def crud_post (data:hs19):
    ds.append(data)
    return hs19(id=data.id,ten=data.ten,tuoi=data.tuoi)



                            #crud+nested+validation
from fastapi import HTTPException,FastAPI
from models import Lop1,hs20
from data import ds_nested_crud
router=APIRouter(prefix="/crud_nested_post",tags=["QLHS"])
@router.post("")
def crud_nested_validation(data:hs20):
    
    for hs in ds_nested_crud:
        if hs.id == data.id :              #kiem tra id trung nhau
            raise HTTPException(status_code=400,detail=" id  da ton tai")
        if  hs.ten== data.ten:
            raise HTTPException(status_code=400,detail=" ten da ton tai")
    
    ds_nested_crud.append(data)
    return data


                            #crud_project

    for hs in ds_crud_pr:
        if id == hs.id:
            raise HTTPException(400,"id đã tồn tại")
    if data.diem <0 or data.diem > 10:
        raise HTTPException(404," điểm k hợp lệ")
    ds_crud_pr.append(data)
    return ds_crud_pr




    

    






