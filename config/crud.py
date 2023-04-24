from sqlalchemy.orm import Session

#To generate random payment reference
import random
import string
import secrets
import datetime

from models import tables
from schemas import module

#GET ALL AIRTIME PLANS
def get_airtime_telcos(db: Session, skip: int = 0, limit: int = 50):
    return db.query(tables.GetAirtimeService).offset(skip).limit(limit).all()

#GET AIRTIME PLAN BY SERVICEID
def get_airtime_telco(serviceID: str, db: Session):
    return db.query(tables.GetAirtimeService).filter(tables.GetAirtimeService.serviceID==serviceID).all()

#Get data plan by serviceID
def get_data_plan(serviceID: str, db: Session):
    return db.query(tables.GetDataPlans).filter(tables.GetDataPlans.serviceID == serviceID).all()

#Get all data plans
def get_data_plans(db: Session, skip: int = 0, limit: int = 50):
    return db.query(tables.GetDataPlans).offset(skip).limit(limit).all()

#MAKE AIRTIME PAYMENT
def airtime_transaction(data: module.AirTransCreate, db:Session):
    #USING SECRETS.CHOICE, GENERATE A RANDOM STRING OF 10 CHARACTERS
    provider_reference = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
              for i in range(10))

    phone = data.customfields
    for i in phone:
        number = i.value

    db_data = tables.AirtimeTransaction(amount=data.amount, provider_reference=provider_reference, payment_reference=data.payment_reference,
                                        serviceID=data.serviceID, phone_number=number, createdAt=datetime.datetime.now())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

#MAKE DATA PAYMENT
def data_transaction(data: module.DataTransCreate, db:Session):
    #USING SECRETS.CHOICE, GENERATE A RANDOM STRING OF 10 CHARACTERS
    provider_reference = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
              for i in range(10))
    
    phone = data.customfields
    for i in phone:
        number = i.value

    db_data = tables.DataTransaction(amount=data.amount, provider_reference=provider_reference, payment_reference=data.payment_reference,
                                     serviceID=data.serviceID, payment_code=data.payment_code, phone_number=number, createdAt=datetime.datetime.now())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

