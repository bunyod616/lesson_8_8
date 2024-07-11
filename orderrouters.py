from fastapi import APIRouter

orderrouter =APIRouter(
    prefix='/orders'
)

@orderrouter.get('/')
async def get_orders():
    return {'message': 'Welcome to the orders endpoint!'}

@orderrouter.get('/c')
async def create_order():
    return {'message': 'Order created successfully!'}