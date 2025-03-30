
from fastapi import APIRouter, Header, HTTPException, Query, Body
from franpos_sdk import FranPOSClient

router = APIRouter()

def get_client(api_key: str):
    if not api_key:
        raise HTTPException(status_code=401, detail="API key required")
    return FranPOSClient(api_key=api_key)

@router.post("/location")
def create_location(data: dict = Body(...), api_key: str = Header(...)):
    client = get_client(api_key)
    return client.company.create_location(data)

@router.post("/update")
def update_company(data: dict = Body(...), api_key: str = Header(...)):
    client = get_client(api_key)
    return client.company.update(data)

@router.get("/getLoyaltyProgram")
def get_loyalty_program(api_key: str = Header(...)):
    client = get_client(api_key)
    return client.company.get_loyalty_program()

@router.get("/GetChildLocation")
def get_child_location(api_key: str = Header(...)):
    client = get_client(api_key)
    return client.company.get_child_location()

@router.get("/formfields")
def get_form_fields(api_key: str = Header(...)):
    client = get_client(api_key)
    return client.company.get_form_fields()
