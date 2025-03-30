
from fastapi import Header, HTTPException, Depends
from franpos_sdk import FranPOSClient
from .settings import API_KEY

from fastapi import APIRouter, Header, HTTPException, Body

router = APIRouter()

    
        
    

@router.post("/importschedules")
def import_schedules(data: dict = Body(...), ):
    client = routers.settings.get_client()
    return client.employee.import_schedules(data)

@router.post("/create")
def create_employee(data: dict = Body(...), ):
    client = routers.settings.get_client()
    return client.employee.create(data)

@router.post("/update")
def update_employee(data: dict = Body(...), ):
    client = routers.settings.get_client()
    return client.employee.update(data)

@router.post("/createservice")
def create_service(data: dict = Body(...), ):
    client = routers.settings.get_client()
    return client.employee.create_service(data)

@router.post("/updateservices")
def update_services(data: dict = Body(...), ):
    client = routers.settings.get_client()
    return client.employee.update_services(data)
