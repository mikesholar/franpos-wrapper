
from fastapi import Header, HTTPException, Depends
from franpos_sdk import FranPOSClient
from .settings import API_KEY

from fastapi import APIRouter, Header, HTTPException, Path

router = APIRouter()

    
        
    

@router.get("/orders/{days}/{type}/{from_date}")
def get_order_dump(days: int, type: str, from_date: str, ):
    client = routers.settings.get_client()
    return client.datadump.get_orders(days, type, from_date)

@router.get("/customers/{days}/{type}/{from_date}")
def get_customer_dump(days: int, type: str, from_date: str, ):
    client = routers.settings.get_client()
    return client.datadump.get_customers(days, type, from_date)

@router.get("/orderitems/{days}/{type}/{from_date}")
def get_order_items_dump(days: int, type: str, from_date: str, ):
    client = routers.settings.get_client()
    return client.datadump.get_order_items(days, type, from_date)

@router.get("/v1/orders/{days}/{page}/{from_date}/{location_id}")
def get_v1_orders(days: int, page: int, from_date: str, location_id: int, ):
    client = routers.settings.get_client()
    return client.datadump.get_v1_orders(days, page, from_date, location_id)
