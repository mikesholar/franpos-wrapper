
from franpos_sdk import FranPOSClient
from fastapi import HTTPException

API_KEY = "KEY HERE"


def get_client():
    if not API_KEY:
        raise HTTPException(status_code=401, detail="API key not configured")
    return FranPOSClient(api_key=API_KEY)
