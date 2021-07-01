import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from base import Base

from sqlalchemy import Column, Integer, String, Boolean, SmallInteger


class Registration(Base):
    __tablename__ = 'registration'

    uuid = Column(String(36), primary_key=True)
    phone_number = Column(String(16), nullable=False)
    creation_date = Column(Integer, nullable=False)
    registered = Column(Boolean, nullable=False)
    otp = Column(SmallInteger, nullable=False)

    def __repr__(self):
        return "<Registration(uuid='%s', phone_number='%s', creation_dat='%s', registered='%i')>" % (
            self.uuid, self.phone_number, self.creation_date, self.registered
        )


