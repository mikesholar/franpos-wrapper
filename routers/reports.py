
from fastapi import APIRouter, Header, HTTPException, Query, Body
from franpos_sdk import FranPOSClient

router = APIRouter()


def get_client(api_key: str):
    if not api_key:
        raise HTTPException(status_code=401, detail="API key required")
    return FranPOSClient(api_key=api_key)


@router.post("/tickets")
def get_tickets(data: dict = Body(...), api_key: str = Header(...)):
    client = get_client(api_key)
    return client.reports.get_tickets(data)


@router.post("/v1/tickets")
def get_tickets_v1(data: dict = Body(...), api_key: str = Header(...)):
    client = get_client(api_key)
    return client.reports.get_tickets_v1(data)


@router.post("/v2/tickets")
def get_tickets_v2(data: dict = Body(...), api_key: str = Header(...)):
    client = get_client(api_key)
    return client.reports.get_tickets_v2(data)


@router.post("/timeClocks")
def post_time_clocks(data: dict = Body(...), api_key: str = Header(...)):
    client = get_client(api_key)
    return client.reports.post_time_clocks(data)


@router.get("/timeClocks")
def get_time_clocks(
    start_date: str, end_date: str,
    page_index: int = 1, page_size: int = 100,
    return_deleted: bool = False, skip_time_zone_conversion: bool = False,
    api_key: str = Header(...)
):
    client = get_client(api_key)
    return client.reports.get_time_clocks(start_date, end_date, page_index, page_size, return_deleted, skip_time_zone_conversion)


@router.post("/cashRegisters")
def get_cash_registers(data: dict = Body(...), api_key: str = Header(...)):
    client = get_client(api_key)
    return client.reports.get_cash_registers(data)
