from fastapi import FastAPI, Request
from src.controller import *
from src.dtos import *


app = FastAPI()


@app.get("/products")
def getProducts(request:Request):
    return show_products(request)

@app.post("/products")
def addProducts(request: Request,body: Item):
    return add_products(request,body)

    