#FastAPI imports
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

#Submodules
from config import crud
from models import tables
from schemas import module
from config.dbconnect import SessionLocal, engine

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/verify_airtime")
def check_airtransaction(verify: module.VerifyAirCreate, db: Session = Depends(get_db)):
    try:
        amount = db.query(tables.AirtimeTransaction).filter(tables.AirtimeTransaction.payment_reference==verify.payment_reference).first().amount
        provider_reference = db.query(tables.AirtimeTransaction).filter(tables.AirtimeTransaction.payment_reference==verify.payment_reference).first().provider_reference

        if amount == None and provider_reference == None:
            return {
                "response": 3,
                "message": "Transaction failed or not found"
            }
        else:

            return {
                "result": {
                    "amount": amount,
                    "provider_reference": provider_reference,
                },
                "response": 0,
                "message": "Transaction successful"
            }
    except:
        return {
            "response": 3,
            "message": "Transaction failed or not found"
        }
@router.post("/verify_data")
def check_datatransaction(verify: module.VerifyDataCreate, db: Session = Depends(get_db)):
    try:

        amount = db.query(tables.DataTransaction).filter(tables.DataTransaction.payment_reference==verify.payment_reference).first().amount
        provider_reference = db.query(tables.DataTransaction).filter(tables.DataTransaction.payment_reference==verify.payment_reference).first().provider_reference
        return {
            "result": {
                "amount": amount,
                "provider_reference": provider_reference,
            },
            "response": 0,
            "message": "Transaction successful"
        }
    except:
        return {
            "response": 3,
            "message": "Transaction failed or not found"
        }