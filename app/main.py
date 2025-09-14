from fastapi import FastAPI, HTTPException
from . import crud
from .models import UserCreate, ProductCreate, OrderCreate, User, Product, Order
from .schemas import ResponseModel
from typing import List

app = FastAPI(title="E-commerce API", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "E-commerce API is running!"}

# User endpoints
@app.post("/users/", response_model=ResponseModel)
async def create_user_endpoint(user: UserCreate):
    user_id = crud.create_user(user)
    if user_id:
        return ResponseModel(
            success=True,
            message="User created successfully",
            data={"user_id": user_id}
        )
    raise HTTPException(status_code=400, detail="Error creating user")

@app.get("/users/", response_model=List[User])
async def get_users_endpoint():
    users = crud.get_users()
    return users

@app.get("/users/{user_id}", response_model=User)
async def get_user_endpoint(user_id: int):
    user = crud.get_user(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}", response_model=ResponseModel)
async def update_user_endpoint(user_id: int, user_data: dict):
    success = crud.update_user(user_id, user_data)
    if success:
        return ResponseModel(success=True, message="User updated successfully")
    raise HTTPException(status_code=404, detail="User not found or update failed")

@app.delete("/users/{user_id}", response_model=ResponseModel)
async def delete_user_endpoint(user_id: int):
    success = crud.delete_user(user_id)
    if success:
        return ResponseModel(success=True, message="User deleted successfully")
    raise HTTPException(status_code=404, detail="User not found or delete failed")

# Product endpoints
@app.post("/products/", response_model=ResponseModel)
async def create_product_endpoint(product: ProductCreate):
    product_id = crud.create_product(product)
    if product_id:
        return ResponseModel(
            success=True,
            message="Product created successfully",
            data={"product_id": product_id}
        )
    raise HTTPException(status_code=400, detail="Error creating product")

@app.get("/products/", response_model=List[Product])
async def get_products_endpoint():
    products = crud.get_products()
    return products

@app.get("/products/{product_id}", response_model=Product)
async def get_product_endpoint(product_id: int):
    product = crud.get_product(product_id)
    if product:
        return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.put("/products/{product_id}", response_model=ResponseModel)
async def update_product_endpoint(product_id: int, product_data: dict):
    success = crud.update_product(product_id, product_data)
    if success:
        return ResponseModel(success=True, message="Product updated successfully")
    raise HTTPException(status_code=404, detail="Product not found or update failed")

@app.delete("/products/{product_id}", response_model=ResponseModel)
async def delete_product_endpoint(product_id: int):
    success = crud.delete_product(product_id)
    if success:
        return ResponseModel(success=True, message="Product deleted successfully")
    raise HTTPException(status_code=404, detail="Product not found or delete failed")

# Order endpoints
@app.post("/orders/", response_model=ResponseModel)
async def create_order_endpoint(order: OrderCreate):
    order_id = crud.create_order(order)
    if order_id:
        return ResponseModel(
            success=True,
            message="Order created successfully",
            data={"order_id": order_id}
        )
    raise HTTPException(status_code=400, detail="Error creating order")

@app.get("/orders/", response_model=List[Order])
async def get_orders_endpoint():
    orders = crud.get_orders()
    return orders

@app.get("/orders/{order_id}", response_model=Order)
async def get_order_endpoint(order_id: int):
    order = crud.get_order(order_id)
    if order:
        return order
    raise HTTPException(status_code=404, detail="Order not found")