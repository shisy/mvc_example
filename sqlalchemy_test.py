#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

engine = create_engine('mysql+mysqlconnector://root:dnt.com@172.16.6.208:3306/nova_ha')
DBSession = sessionmaker(bind=engine)
session = DBSession()
new_user = User(id='5', name='Bob')
session.add(new_user)
session.commit()
session.close()