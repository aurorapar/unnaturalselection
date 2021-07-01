import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.append(parentdir)

from base import Base

from sqlalchemy import Column, Integer, String


class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True)

    def __init__(self, code=None, *args, **kwargs):
        self.name = None


