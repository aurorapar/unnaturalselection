import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from base import Base

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

MAX_USERNAME_LENGTH = 50


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    phone_number = Column(Integer, nullable=False)
    user_uuid = Column(String(36), nullable=False)
    join_date = Column(Integer, nullable=False)  # use time.time() ?
    last_login = Column(Integer)
    last_played = Column(Integer)
    platform_id = Column(String(50))
    username = Column(String(MAX_USERNAME_LENGTH))

    inventory_id = Column(Integer, ForeignKey("inventory.id"), nullable=False)
    inventory = relationship("Inventory", backref=backref("user"), uselist=False)

    def __repr__(self):
        return "<User(name='%s', phone_number='%s', uuid='%s')>" % (
            self.username, self.phone_number, self.user_uuid
        )

    def __init__(self, code=None, *args, **kwargs):
        self.name = None

