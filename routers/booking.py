
from fastapi import Header, HTTPException, Depends
from franpos_sdk import FranPOSClient
from .settings import API_KEY

from fastapi import APIRouter, Header, HTTPException, Query

router = APIRouter()

    
        
    

@router.get("/all")
def get_all_bookings(location_id: int = Query(...), ):
    client = routers.settings.get_client()
    return client.booking.get_all(location_id)
