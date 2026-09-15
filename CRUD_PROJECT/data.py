from models import hocsinh,hs_2
ds=[hs_2(ten="My",lop="12A",ds_mon=[hocsinh(tenmon="Toán",diem=10)]),hs_2(ten="Linh",lop="12B",ds_mon=[hocsinh(tenmon="Văn",diem=10)]),hs_2(ten="Ngọc",lop="12A",ds_mon=[hocsinh(tenmon="Anh",diem=10)])]   


from models import put_path_query
dshs=[put_path_query(ten="My",tuoi=20,lop="12A",gioitinh="Nu"),put_path_query(ten="Nghĩa",tuoi=20,lop="12B",gioitinh="Nam"),put_path_query(ten="Nam",tuoi=20,lop="12C",gioitinh="Nam")]


from models import delete_path_query
ds_delete=[delete_path_query(ten="My",lop="12A"),delete_path_query(ten="Nguyên",lop="12A"),delete_path_query(ten="Lê",lop="12A")]


from models import HocSinh
ds_response =[HocSinh(ten="My",tuoi=20,lop="12A"),HocSinh(ten="Linh",tuoi=20,lop="12A"),HocSinh(ten="Nguyên ",tuoi=20,lop="12A")]

from models import hs1,hs2
ds_hide=[hs1(ten="My",lop="12A",tuoi=20,diem=10),hs1(ten="Linh",lop="12A",tuoi=20,diem=6),hs1(ten="Phát",lop="12A",tuoi=20,diem=7)]


from models import hs3
ds_exclude =[hs3(ten="My",tuoi=18,lop="12C",diem=10),hs3(ten="ngọc",tuoi=18,lop="12C",diem=10)]


from models import hs4
ds_include =[hs4(ten="My",tuoi=18,lop=None,diem=5),hs4(ten="Ngọc",tuoi=None,lop="12b",diem=10)]



from models import hs5
ds_unset =[hs5(ten="My",diem=5),hs5(ten="Ngọc",diem=10)]

from models import hs6
ds_default =[hs6(ten="My",tuoi=18,diem=5),hs6(ten="Ngọc",tuoi=10,diem=10)]

                            #RESPONSE MODEL + NESTED +LIST
from models import HS7,DiaChi
ds_all =[HS7(ten="My",tuoi=20,lop="chưa có lớp",diem=10,dia_chi=DiaChi(thanh_pho="HCM",quan="q12")),HS7(ten="Linh",tuoi=20,lop="12A",diem=10,dia_chi=DiaChi(thanh_pho="HCM",quan="1"))]  

                            #RESPONSE MODEL + NESTED +LIST +TRẢ 1 HS

from models import HS8,DC
ds_HS8 =[HS8(ten="Lâm",tuoi=20,lop="chưa có lớp",diem=10,dia_chi=DC(thanh_pho="HCM",quan="Hóc Môn")),HS8(ten="Quỳnh",tuoi=20,lop="12A",diem=10,dia_chi=DC(thanh_pho="HCM",quan="3"))]  


                            #RESPONSE MODEL +NESTED +DICT +TỪ KHÓA 
from models import HS9,D_C
ds_HS9 =[HS9(ten="An Lâm",tuoi=20,lop="chưa có lớp",diem=10,dia_chi=D_C(thanh_pho="HCM",quan="Hóc Môn")),HS9(ten="Quỳnh Chi",tuoi=20,lop="12A",diem=10,dia_chi=D_C(thanh_pho="HCM",quan="3"))]  


                            #RESPONSE Model +NESTED +DICT +TU KHÓA CHỈ LẤY DUY NHẤT HS ĐẦU THỎA TỪ KHÓA
from models import HS10,DICH
ds_HS10 =[HS10(ten="An Lâm",tuoi=20,lop="chưa có lớp",diem=10,dia_chi=DICH(thanh_pho="HCM",quan="Hóc Môn")),HS10(ten="An Chi",tuoi=20,lop="12A",diem=10,dia_chi=DICH(thanh_pho="HCM",quan="3"))]



                            #RESPONSE +DTB
from models import HS11
ds_HS11=[HS11(ten="My",tuoi=20,lop="12A",diem=10,dia_chi="q1"),HS11(ten="Linh",tuoi=20,lop="12A",diem=6,dia_chi="q8"),HS11(ten="Lam",tuoi=20,lop="12A",diem=5,dia_chi="q8"),HS11(ten="Thư",tuoi=20,lop="12A",diem=4,dia_chi="q8")]


                             #RESPONSE MODEL + SUMMARY/DICT
from models import HS13,HS14
ds_HS13 =[HS13(ten="My",diem=8),HS13(ten="Yến",diem=9),HS13(ten="Ngọc",diem=10),HS13(ten="Nhân",diem=6),HS13(ten="Linh",diem=4)]



                            #RESPONSE MODEL + SUMMARY TỔNG HỢP
from models import HS15,HS16
ds_HS15=[HS15(ten="My",tuoi=20,dtb=7),HS15(ten="Ngọc",tuoi=22,dtb=4),HS15(ten="Tuấn",tuoi=20,dtb=3),HS15(ten="Luận",tuoi=20,dtb=9)]


                             #RESPONSE MODEL 
from models import HS17,HS18
ds_HS17=[HS17(ten="My",tuoi=30,dtb=5),HS17(ten="Loan",tuoi=30,dtb=7),HS17(ten="Ngọc",tuoi=30,dtb=9),HS17(ten="Xinh",tuoi=30,dtb=10)]

                            
                            #CRUD_id

from models import crud,Lop
ds_crud=[crud(id=1,ten="My",tuoi=20,diem=3,lop=Lop(ten_lop="12A",phong="p1")),crud(id=2,ten="Keu",tuoi=20,diem=10,lop=Lop(ten_lop="12C",phong="p1")),crud(id=3,ten="Tuấn",tuoi=20,diem=6,lop=Lop(ten_lop="12B",phong="p1"))]



                            #CRUD_TEN
from models import timten
ds_timten=[timten(ten="My Nhu",tuoi=30),timten(ten="nhung",tuoi=30),timten(ten="My mieu",tuoi=30)]


                            # crud+nested+HTTP
from models import hs20,Lop1
ds_nested_crud=[hs20(id=1,ten="My",tuoi=20,lop=Lop1(tenlop="12A",khoi=10)),hs20(id=2,ten="Linh",tuoi=22,lop=Lop1(tenlop="12A2",khoi=10))]



                            #crud_put
from models import put_hs
ds_put=[put_hs(id=1,ten="My",tuoi=20),put_hs(id=2,ten="Khi",tuoi=30),put_hs(id=3,ten="Nhung",tuoi=20),put_hs(id=4,ten="Nhuy",tuoi=20)]



                            #delete
from models import delete_th,delete_2
ds_delete=[delete_th(id=1,ten="My",tuoi=20),delete_th(id=2,ten="Lâm",tuoi=20),delete_th(id=3,ten="Ngân",tuoi=20)]


                            #delete_path
from models import delete_path
ds_de_path=[delete_path(id=1,ten="My",tuoi=20),delete_path(id=2,ten="Lâm",tuoi=20),delete_path(id=3,ten="Ngân",tuoi=20)]


                            #crud_project
from models import crud_pr
ds_crud_pr=[crud_pr(id=1,ten="My",tuoi=20,diem=10),crud_pr(id=2,ten="Linh",tuoi=19,diem=4),crud_pr(id=3,ten="My nhung",tuoi=20,diem=7)]