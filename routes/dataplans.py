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

#GET DATA PLAN BY SERVICEID
@router.get("/dataplan/{serviceID}")
def get_data_plan(serviceID: str, db: Session = Depends(get_db)):
    return crud.get_data_plan(serviceID=serviceID, db=db)


#GET ALL DATA PLANS
@router.get("/dataplans")
def get_data_plans(db: Session = Depends(get_db), skip: int = 0, limit: int = 50):
    getdata =  crud.get_data_plans(db=db, skip=skip, limit=limit)
    return {
        "result": [
            {
                "name": "mtn",
                "serviceID": "MTN-DATA",
                "items": [
                    {
                        "name": "10GB",
                        "paymentCode": "MTN10GB",
                        "amount": 2000
                    },
                    {
                        "name": "15GB",
                        "paymentCode": "MTN15GB",
                        "amount": 2500
                    },
                    {
                        "name": "20GB",
                        "paymentCode": "MTN20GB",
                        "amount": 5000
                    },
                    {
                        "name": "30GB",
                        "paymentCode": "MTN30GB",
                        "amount": 9000
                    }
                ]
            },
            {
                "name": "airtel",
                "serviceID": "AIRTEL-DATA",
                "items": [
                    {
                        "name": "10GB",
                        "paymentCode": "AIRTEL10GB",
                        "amount": 2000
                    },
                    {
                        "name": "15GB",
                        "paymentCode": "AIRTEL15GB",
                        "amount": 2500
                    },
                    {
                        "name": "20GB",
                        "paymentCode": "AIRTEL20GB",
                        "amount": 5000
                    },
                    {
                        "name": "30GB",
                        "paymentCode": "AIRTEL30GB",
                        "amount": 9000
                    }
                ]
            },
            {
                "name": "glo",
                "serviceID": "GLO-DATA",
                "items": [
                    {
                        "name": "10GB",
                        "paymentCode": "GLO10GB",
                        "amount": 2000
                    },
                    {
                        "name": "15GB",
                        "paymentCode": "GLO15GB",
                        "amount": 2500
                    },
                    {
                        "name": "20GB",
                        "paymentCode": "GLO20GB",
                        "amount": 5000
                    },
                    {
                        "name": "30GB",
                        "paymentCode": "GLO30GB",
                        "amount": 9000
                    }
                ]
            },
            {
                "name": "9mobile",
                "serviceID": "9MOBILE-DATA",
                "items": [
                    {
                        "name": "10GB",
                        "paymentCode": "9MOBILE10GB",
                        "amount": 2000
                    },
                    {
                        "name": "15GB",
                        "paymentCode": "9MOBILE15GB",
                        "amount": 2500
                    },
                    {
                        "name": "20GB",
                        "paymentCode": "9MOBILE20GB",
                        "amount": 5000
                    },
                    {
                        "name": "30GB",
                        "paymentCode": "9MOBILE30GB",
                        "amount": 9000
                    }
                ]
            },
        ],
        "response": 0,
        "message": "success"
    }