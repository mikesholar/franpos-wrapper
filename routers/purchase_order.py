
from fastapi import Header, HTTPException, Depends
from franpos_sdk import FranPOSClient
from .settings import API_KEY

from fastapi import APIRouter, Header, HTTPException, Query, Body

router = APIRouter()

    
        
    

@router.post("/create")
def create_po(data: dict = Body(...), ):
    client = routers.settings.get_client()
    return client.purchase_order.create(data)

@router.post("/delete")
def delete_po(data: dict = Body(...), ):
    client = routers.settings.get_client()
    return client.purchase_order.delete(data)

@router.get("/all")
def get_all():
    client = routers.settings.get_client()
    return client.purchase_order.get_all()

@router.get("/{po_id}")
def get_by_id(po_id: int, ):
    client = routers.settings.get_client()
    return client.purchase_order.get_by_id(po_id)
