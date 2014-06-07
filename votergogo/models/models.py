from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode
    )
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Country(Base):
    __tablename__ = 'countries'
    country_id = Column(Unicode, primary_key=True)


class Region(Base):
    __tablename__ = 'regions'
    region_id = Column(Unicode, primary_key=True)
    country_id = Column(Unicode, nullable=False)
    country = relationship(Country, backref='regions')


class City(Base):
    __tablename__ = 'cities'
    city_id = Column(Integer, primary_key=True)
    name = Column(Text)
    region_id = Column(Unicode)
    region = relationship(Region, backref='districts')


class Address(Base):
    __tablename__ = 'addresses'
    address_id = Column(Ingeger, primary_key=True)
    address_1 = Column(Unicode, nullable=False)
    address_2 = Column(Unicode)
    address_3 = Column(Unicode)
    postal_code = Column(Unicode)
    city_id = Column(Unicode)


class PollingStation(Base):
    __tablename__ = 'polling_stations'
    poll_id = Column(Integer, primary_key=True)
    name = Column(Unicode, nullable=False)
    address_id = Column(Integer)


class District(Base):
    __tablename__ = 'electoral_regions'
    district_id = Column(Integer, primary_key=True)
    name = Column(Text)
    region_id = Column(Unicode)
    region = relationship(Region, backref='districts')


class Election(Base):
    __tablename__= 'elections'
    election_id = Column(Integer, primary_key=True)
    district_id = Column(Integer)
    name = Column(Unicode)
    start_date = Column(Date)

    district = relationship(District, backref='elections')


class Candidate(Base):
    __tablename__ = 'candidates'
    candidate_id = Column(Ingeger, primary_key=True)
    name = Column(Unicode)
    district_id = Column(Integer)
    district = relationship(District, backref='candidates')


