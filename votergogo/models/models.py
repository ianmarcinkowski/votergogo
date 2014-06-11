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
    country_id = Column(ForeignKey(Country.country_id))

    country = relationship(Country, backref='regions')


class City(Base):
    __tablename__ = 'cities'
    city_id = Column(Integer, primary_key=True)
    name = Column(Text)
    region_id = Column(ForeignKey(Region.region_id))

    region = relationship(Region, backref='cities')


class Address(Base):
    __tablename__ = 'addresses'

    address_id = Column(Ingeger, primary_key=True)

    province_id = Column(ForeignKey(Province.province_id))
    country_id = Column(ForeignKey(Country.country_id))
    city_id = Column(ForeignKey(City.city_id))
    postal_code = Column(Unicode)
    street_number = Column(Unicode(6), nullable=False)
    street_number_suffix = Column(Unicode(5))
    street_name = Column(Unicode(255), nullable=False)
    street_type_abbr = Column(ForeignKey(StreetType.street_type_abbr))
    street_direction = Column(Enum(
            'E', 'N', 'NE', 'NW', 'S', 'SE', 'SW', 'W', 'NO', 'SO', 'O',
            name='street_direction', inherit_schema=True))

    country = relationship(Country)
    province = relationship(Province)
    city = relationship(City)


class PollingStation(Base):
    __tablename__ = 'polling_stations'
    poll_id = Column(Integer, primary_key=True)
    name = Column(Unicode, nullable=False)
    address_id = Column(Integer)


class District(Base):
    __tablename__ = 'districts'
    district_id = Column(Integer, primary_key=True)
    name = Column(Text)


class Contest(Base):
    __tablename__= 'contests'
    contest_id = Column(Integer, primary_key=True)
    district_id = Column(ForeignKey(District.district_id))
    name = Column(Unicode)
    start_date = Column(Date)

    district = relationship(District, backref='contests')


class Contender(Base):
    __tablename__ = 'contenders'
    contender_id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    incumbent = Column(Boolean)
    website = Column(Unicode)


class ContenderAddress(Base):
    __tablename__ = 'contenders_addresses'

    contender_id = Column(ForeignKey(Contender.contender_id),
                          primary_key=True))
    address_id = Column(ForeignKey(Address.address_id),
                        primary_key=True))
    label = Column(Unicode, nullable=False)

    contender = relationship(Customer, backref='addresses')


class Contact(Base):
    __tablename__ = 'contacts'
    contact_id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    label = Column(Boolean)
    website = Column(Unicode)


class PhoneNumbers(Base):
    __tablename__ = 'phone_numbers'
    phone_number_id = Column(Integer, primary_key=True)
    contact_id = Column(ForeignKey(Contact.contact_id),
                        primary_key=True)
    phone_number = Column(Unicode)
    primary = Column(Boolean)

    contact = relationship(Contact, backref='phone_numbers')


class ContenderContacts(Base):
    __tablename__ = 'contenders_contacts'

    contender_id = Column(ForeignKey(Contender.contender_id),
                          primary_key=True))
    contact_id = Column(ForeignKey(Contact.contact_id),
                        primary_key=True))
    label = Column(Unicode, nullable=False)

    contender = relationship(Customer, backref='contacts')
