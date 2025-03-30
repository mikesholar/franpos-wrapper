
from fastapi import Header, HTTPException, Depends
from franpos_sdk import FranPOSClient
from .settings import API_KEY

from fastapi import APIRouter, Header, HTTPException, Query

router = APIRouter()

    
        
    

@router.get("/dictionary/{entity_name}")
def get_dictionary(entity_name: str, ):
    client = routers.settings.get_client()
    return client.common.get_dictionary(entity_name)

@router.get("/getOrderIdAndAuthNo")
def get_order_auth():
    client = routers.settings.get_client()
    return client.common.get_order_auth()

@router.get("/getCategory/{name}/{location_id}")
def get_category(name: str, location_id: int, ):
    client = routers.settings.get_client()
    return client.common.get_category(name, location_id)

@router.get("/getLocationsInfo")
def get_locations_info():
    client = routers.settings.get_client()
    return client.common.get_locations_info()

@router.get("/generateApiKey/{location_code}")
def generate_api_key(location_code: str, ):
    client = routers.settings.get_client()
    return client.common.generate_api_key(location_code)
