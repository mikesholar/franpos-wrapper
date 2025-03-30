
from fastapi import APIRouter, Header, HTTPException, Query, Body
from franpos_sdk import FranPOSClient

router = APIRouter()

def get_client(api_key: str):
    if not api_key:
        raise HTTPException(status_code=401, detail="API key required")
    return FranPOSClient(api_key=api_key)

@router.get("/queue")
def get_walkin_queue(api_key: str = Header(...)):
    client = get_client(api_key)
    return client.walkin.get_queue()

@router.post("/{company_id}/checkIn")
def check_in(company_id: int, data: dict = Body(...), api_key: str = Header(...)):
    client = get_client(api_key)
    return client.walkin.check_in(company_id, data)

@router.post("/{company_id}/isCheckedIn")
def is_checked_in(company_id: int, data: dict = Body(...), api_key: str = Header(...)):
    client = get_client(api_key)
    return client.walkin.is_checked_in(company_id, data)

@router.post("/{company_id}/secondaryContacts/{customer_id}")
def secondary_contacts(company_id: int, customer_id: int, data: dict = Body(...), api_key: str = Header(...)):
    client = get_client(api_key)
    return client.walkin.secondary_contacts(company_id, customer_id, data)

@router.post("/{company_id}/serviceProviders")
def service_providers(company_id: int, data: dict = Body(...), api_key: str = Header(...)):
    client = get_client(api_key)
    return client.walkin.service_providers(company_id, data)

@router.get("/{company_id}/settings")
def get_walkin_settings(company_id: int, api_key: str = Header(...)):
    client = get_client(api_key)
    return client.walkin.get_settings(company_id)

@router.post("/{company_id}/simpleServices")
def post_simple_services(company_id: int, data: dict = Body(...), api_key: str = Header(...)):
    client = get_client(api_key)
    return client.walkin.simple_services(company_id, data)

@router.post("/{company_id}/services")
def post_services(company_id: int, data: dict = Body(...), api_key: str = Header(...)):
    client = get_client(api_key)
    return client.walkin.services(company_id, data)

@router.get("/company/workinghours")
def get_working_hours(api_key: str = Header(...)):
    client = get_client(api_key)
    return client.walkin.get_working_hours()

@router.get("/booking/appointments")
def get_appointments(api_key: str = Header(...)):
    client = get_client(api_key)
    return client.walkin.get_appointments()

@router.get("/employee/schedules")
def get_schedules(api_key: str = Header(...)):
    client = get_client(api_key)
    return client.walkin.get_schedules()
