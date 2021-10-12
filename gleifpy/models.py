from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ForeignCompany(Base):
    __tablename__ = "gleif_com"

    id = Column(Integer, primary_key=True)

    lei = Column(String)
    legal_name = Column(String)
    first_address_line = Column(String)
    additional_address_line = Column(String)
    country = Column(String)
    city = Column(String)
    region = Column(String)
    postal_code = Column(String)
    legal_jurisdiction = Column(String)
    entity_legal_form_code = Column(String)
    other_legal_form = Column(String)

    def __repr__(self):
        return f"ForeignCompany(lei={self.lei}, legal_name={self.legal_name}, country={self.country}, " \
               f"city={self.city}, first_address={self.first_address_line})"
