from typing import List
from pydantic import BaseModel
import datetime

#AIRTIME PAYMENT

#Custom fields for airtime payment
class CustomFields(BaseModel):
    name: str
    value: str


class AirTranBase(BaseModel):
    amount: int
    serviceID: str
    payment_reference: str
    customfields: list[CustomFields]


class AirTransCreate(AirTranBase):
    pass

class Result(BaseModel):
    amount: int
    provider_reference: str

class AirTrans(AirTranBase):
    result: Result
    response: int
    message: str

    class Config:
        orm_mode = True
#END OF AIRTIME PAYMENT

#DATA PAYMENT
class DataTranBase(BaseModel):
    amount: int
    payment_reference: str
    serviceID: str
    payment_code: str
    customfields: list[CustomFields]


class DataTransCreate(DataTranBase):
    pass

class DataTrans(DataTranBase):
    id: int
    provider_reference: str
    createdAt: datetime.datetime

    class Config:
        orm_mode = True
#END OF DATA PAYMENT


#VERIFY TRANSACTION STATUS
class VerifyAirTrans(BaseModel): #Verify airtime transaction
    payment_reference: str
    provider_reference: str


class VerifyAirCreate(VerifyAirTrans):
    pass

class VerifyAir(VerifyAirTrans):
    amount: int
    serviceID: str
    phone_number: str


    class Config:
        orm_mode = True
    


class VerifyDataTrans(BaseModel): #Verify data transaction
    payment_reference: str
    provider_reference: str

class VerifyDataCreate(VerifyDataTrans):
    pass

class VerifyData(VerifyDataTrans):
    amount: int
    serviceID: str
    payment_code: str
    phone_number: str

    class Config:
        orm_mode = True
#END OF VERIFY TRANSACTION STATUS