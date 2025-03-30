
from fastapi import FastAPI
from routers import (
    customers, walkin, company, reports, datadump,
    purchase_order, employee, common, import_module, booking, pos
)

location = 202676

app = FastAPI(title="FranPOS API Wrapper", version="1.0.0")

app.include_router(customers.router, prefix="/customers", tags=["Customers"])
app.include_router(walkin.router, prefix="/walkin", tags=["Walk-in"])
app.include_router(company.router, prefix="/company", tags=["Company"])
app.include_router(reports.router, prefix="/reports", tags=["Reports"])
app.include_router(datadump.router, prefix="/datadump", tags=["Data Dump"])
app.include_router(purchase_order.router, prefix="/purchase_order", tags=["Purchase Orders"])
app.include_router(employee.router, prefix="/employee", tags=["Employees"])
app.include_router(common.router, prefix="/common", tags=["Common"])
app.include_router(import_module.router, prefix="/import", tags=["Import"])
app.include_router(booking.router, prefix="/booking", tags=["Booking"])
app.include_router(pos.router, prefix="/pos", tags=["POS"])
