
from fastapi import Header, HTTPException, Depends
from franpos_sdk import FranPOSClient

import routers.settings
from .settings import API_KEY

from fastapi import APIRouter, Query, Header, Body, HTTPException

router = APIRouter()


@router.get("/{customer_id}")
def get_customer_by_id(customer_id: int, location_id: int = Query(...), ):
    client = routers.settings.get_client()
    return client.customer.get_by_id(customer_id, location_id)


@router.get("/by-company/")
def get_customers_by_company(page: int = Query(1), ):
    client = routers.settings.get_client()
    return client.customer.get_by_company(page)


@router.post("/analysis-report/")
def customer_analysis_report(data: dict = Body(...), ):
    client = routers.settings.get_client()
    return client.customer.analysis_report(data)


@router.post("/analysis-summary/")
def customer_analysis_summary(data: dict = Body(...), ):
    client = routers.settings.get_client()
    return client.customer.analysis_summary(data)


@router.get("/search/")
def search_customers(query: str = Query(...), filter_type: str = "email", ):
    client = routers.settings.get_client()
    return client.customer.search(query, filter_type)


@router.get("/searchByCellPhoneOrEmail/")
def search_by_contact(query: str = Query(...), ):
    client = routers.settings.get_client()
    return client.customer.search_by_contact(query)


@router.post("/getOrCreate/")
def get_or_create_customer(data: dict = Body(...), ):
    client = routers.settings.get_client()
    return client.customer.get_or_create(data)


@router.get("/history/{customer_id}/{type}")
def get_customer_history(customer_id: int, type: str, ):
    client = routers.settings.get_client()
    return client.customer.get_history(customer_id, type)


@router.post("/put/")
def put_customer(data: dict = Body(...), ):
    client = routers.settings.get_client()
    return client.customer.put(data)


@router.post("/")
def create_customer(data: dict = Body(...), ):
    client = routers.settings.get_client()
    return client.customer.create(data)


@router.post("/houseaccount/create/")
def create_house_account(data: dict = Body(...), ):
    client = routers.settings.get_client()
    return client.customer.create_house_account(data)


@router.post("/send-auth-code/")
def send_auth_code(data: dict = Body(...), ):
    client = routers.settings.get_client()
    return client.customer.send_auth_code(data)
