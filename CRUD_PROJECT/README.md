# FastAPI CRUD Project

Project thực hành xây dựng REST API bằng FastAPI, tổ chức các chức năng CRUD thành các module riêng biệt.

## Chức năng

- GET: lấy danh sách và tìm kiếm dữ liệu
- POST: thêm dữ liệu
- PUT: cập nhật dữ liệu
- DELETE: xóa dữ liệu
- Path Parameter
- Query Parameter
- Request Body
- Pydantic Model
- Validation
- HTTPException
- Response Model
- Swagger API testing

## Cấu trúc

- `main123.py`: file chính, kết nối các router
- `get.py`: các API GET
- `post.py`: các API POST
- `put.py`: các API PUT
- `delete.py`: các API DELETE
- `query.py`: xử lý Query Parameter
- `path.py`: xử lý Path Parameter
- `models.py`: Pydantic models
- `data.py`: dữ liệu mẫu

## Công nghệ

- Python
- FastAPI
- Pydantic
- Uvicorn
