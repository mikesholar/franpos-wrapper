
from fastapi import Header, HTTPException, Depends
from franpos_sdk import FranPOSClient
from .settings import API_KEY

from fastapi import APIRouter, Header, HTTPException, Body

router = APIRouter()

    
        
    

@router.post("/customers")
def import_customers(data: dict = Body(...), ):
    client = routers.settings.get_client()
    return client.import_module.import_customers(data)
