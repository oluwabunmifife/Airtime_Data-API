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


@router.post("/airtimepayment", status_code=200)
def airpayment(airtimepay: module.AirTransCreate, db: Session = Depends(get_db)):
    try:
        new = crud.airtime_transaction(db=db, data=airtimepay)
        if new:
            response = 0
            message = "Transaction successful"
        else:
            response = 3
            message = "Transaction failed"
        return {
            "result": {
                "amount": new.amount,
                "provider_reference": new.provider_reference
            },
            "response": response,
            "message": message
        }
    except:
        return {
            "message": "Duplicate transaction"
        }