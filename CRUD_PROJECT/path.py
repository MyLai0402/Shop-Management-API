from fastapi import FastAPI,APIRouter,Query ,HTTPException
from models import hocsinh
from data import ds
router = APIRouter(prefix="/path",tags=["path"])
@router.get("/tim/{ten}")
def tim_hs(ten:str):
    for hs in ds:
        if hs.ten==ten:
            return hs  
    raise HTTPException(status_code=404,detail="k tìm thây hs ")

                                        #1path
from fastapi import FastAPI,APIRouter,Query ,HTTPException
from models import hocsinh
from data import ds

router = APIRouter(prefix="/path",tags=["path"])
@router.get("/tim/tuoi/{tuoi}")
def tim_hs(tuoi:int):
    kq=[]
    for hs in ds:
        print(hs)          
        if hs.tuoi==tuoi:
            kq.append(hs) 
    if len(kq)==0:
        raise HTTPException(status_code=404,detail="k tìm thây hs ")
    return kq



                                            #2path
from fastapi import FastAPI,APIRouter,Query ,HTTPException
from models import hocsinh
from data import ds

router = APIRouter(prefix="/path",tags=["path"])
@router.get("/tim/{tuoi}/{lop}")
def tim_hs(tuoi:int,lop:str):
    kq=[]
    for hs in ds:
        print(hs.ten,hs.tuoi,hs.lop)         
        if hs.tuoi==tuoi and hs.lop== lop:
            kq.append(hs) 
    if len(kq)==0:
        raise HTTPException(status_code=404,detail="k tìm thây hs ")
    return kq



                                            #3path

from fastapi import FastAPI,APIRouter,Query ,HTTPException
from models import hocsinh
from data import ds

router = APIRouter(prefix="/path",tags=["path"])
@router.get("/tim/{ten}/{tuoi}/{lop}")                 
def tim_hs(ten:str,tuoi:int,lop:str):
    kq=[]
    for hs in ds:
        print(hs.ten,hs.tuoi,hs.lop)         
        if hs.ten==ten and hs.tuoi==tuoi and hs.lop== lop:
            kq.append(hs) 
    if len(kq)==0:
        raise HTTPException(status_code=404,detail="k tìm thây hs ") 
    return kq
    