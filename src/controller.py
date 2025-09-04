from fastapi import Request
from src.dtos import *
from src.database import cursor,connection
temp_db = []


# def get_all_students(request:Request,id):
#     try:
#         try:
#             id:int = request.query_params.get("id","No Id Found")
#         except Exception as e1:
#             return e
#         filteredData = list(filter(lambda x:x["id"]==int(id),temp_db))
#         return filteredData
#     except Exception as e:
#         return e


def show_products(request:Request):
    data = temp_db
    filtered_data = list(filter(lambda price:price["price"]>50,data))
    return filtered_data
    
def add_products(request:Request,body:Item):
    newData = {
        **body.model_dump(),
        "id": len(temp_db)+1    
    }
    sql = "INSERT INTO products (title, description, price, count) VALUES (%s, %s, %s, %s)"

    val = (newData["title"], newData["description"], newData["price"], newData["count"])
    connection.commit()
    cursor.execute(sql,val)
    temp_db.append(newData)
    return temp_db