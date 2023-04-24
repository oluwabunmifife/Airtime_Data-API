#FastAPI imports
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

#Submodules
from config import crud
from models import tables
from models.tables import GetAirtimeService
from schemas import module
from config.dbconnect import SessionLocal, engine

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#GET ALL AIRTIME PLANS
@router.get("/airtimetelcos")
def get_airtime_telcos(db: Session = Depends(get_db), skip: int = 0, limit: int = 50):
    gettelco = crud.get_airtime_telcos(db=db, skip=skip, limit=limit)

    #ALTERNATIVE RESPONSE
    # return {
    #     "result": [
    #     {
    #         "name": "mtn",
    #         "serviceID": "MTN"
    #     },
    #     {
    #         "name": "airtel",
    #         "serviceID": "AIRTEL"
    #     },
    #     {
    #         "name": "glo",
    #         "serviceID": "GLO"
    #     },
    #     {
    #         "name": "9mobile",
    #         "serviceID": "9MOBILE"
    #     }
    #     ],
    #     "response": 0,
    #     "message": "Successful"
    # }
    return {
        "result": [
            gettelco
        ],
        "response": 0,
        "message": "Successful"
    }

#GET AIRTIME PLAN BY SERVICEID
@router.get("/airtimetelco/{serviceID}")
def get_airtime_telcos(serviceID: str, db: Session = Depends(get_db)):
    return crud.get_airtime_telco(serviceID=serviceID, db=db)


