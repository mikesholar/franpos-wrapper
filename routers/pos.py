
from fastapi import Header, HTTPException, Depends
from franpos_sdk import FranPOSClient
from .settings import API_KEY

from fastapi import APIRouter, Header, HTTPException, Query

router = APIRouter()

    
        
    

@router.get("/settings")
def get_pos_settings(location_id: int = Query(...), ):
    client = routers.settings.get_client()
    return client.pos.get_settings(location_id)
