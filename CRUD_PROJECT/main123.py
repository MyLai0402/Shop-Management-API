from fastapi import FastAPI,APIRouter
from models import hocsinh,hs_2,sua_mon,put_path_query,delete_path_query,HocSinh
from data import ds,dshs,ds_delete
from data import ds_response,ds_hide,ds_exclude,ds_include,ds_unset,ds_default,ds_all,ds_HS8,ds_HS9,ds_HS10,ds_HS13,ds_HS15,ds_HS17,ds_crud,ds_timten,ds_nested_crud,ds_put,ds_delete,ds_de_path,ds_crud_pr
from models import hs1,hs2,hs3,hs4,hs5,hs6,HS7,DiaChi,HS8,DC,HS9,D_C,HS10,DICH,HS13,HS14,HS15,HS16,HS17,HS18,crud,Lop,timten,hs19,Lop1,hs20,put_hs,sua,delete_th,delete_2,delete_path,crud_pr

from get import router as get_router  
from post import router as post_router
from put import router as put_router
from delete import router as delete_router
from query import router as query_router
from path import router as path_router

app123=FastAPI()
app123.include_router(get_router)
app123.include_router(post_router)
app123.include_router(put_router)
app123.include_router(delete_router)
app123.include_router(query_router)
app123.include_router(path_router)   
