from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from config.dbconnect import Base
import datetime
from sqlalchemy.orm import relationship

class Telcos(Base):
    __tablename__ = "telcos"
    id = Column(Integer, autoincrement=True)
    name = Column(String(10))
    serviceID = Column(String(10), primary_key=True, index=True, unique=False)


class AirtimeTransaction(Base):
    __tablename__ = "airtime_transaction"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    amount = Column(Integer, nullable=False)
    provider_reference = Column(String(15)) #Should be generated automatically
    payment_reference = Column(String(15), unique=True, nullable=False)
    serviceID = Column(String(10), ForeignKey("telcos.serviceID"), nullable=False, index=True, unique=False)
    phone_number = Column(String(15), nullable=False)
    createdAt = Column(DateTime, default=datetime.datetime.now)

class GetAirtimeService(Base):
    __tablename__ = "get_airtime_telcos"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(10))
    serviceID = Column(String(10), ForeignKey("telcos.serviceID"), nullable=False, index=True, unique=False)
    package = Column(String(10))

class GetDataPlans(Base):
    __tablename__ = "get_data_plans"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    serviceID = Column(String(10), ForeignKey("telcos.serviceID"), nullable=False, index=True, unique=False)
    name = Column(String(10), nullable=False)
    package = Column(String(10), nullable=False)
    payment_code = Column(String(15), nullable=False, primary_key=True, index=True, unique=False)
    amount = Column(Integer, nullable=False)

class DataTransaction(Base):
    __tablename__ = "data_transaction"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    amount = Column(Integer, nullable=False)
    provider_reference = Column(String(15)) #Should be generated automatically
    payment_reference = Column(String(15), unique=True, nullable=False)
    serviceID = Column(String(10), ForeignKey("telcos.serviceID"), nullable=False, index=True, unique=False)
    phone_number = Column(String(15), nullable=False)
    payment_code = Column(String(15), ForeignKey("get_data_plans.payment_code"), nullable=False, index=True, unique=False)
    createdAt = Column(DateTime, default=datetime.datetime.now)
    # payment_code = relationship("GetDataPlans")
