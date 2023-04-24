from fastapi import FastAPI
from routes import airtimepayment, airtimetelco, datapayment, dataplans, verify
from config.dbconnect import engine
from models import tables

app = FastAPI()

tables.Base.metadata.create_all(bind=engine)

app.include_router(airtimepayment.router)
app.include_router(airtimetelco.router)
app.include_router(datapayment.router)
app.include_router(dataplans.router)
app.include_router(verify.router)