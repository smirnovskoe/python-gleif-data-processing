from pydantic import BaseModel, Field


class CompanySchema(BaseModel):
    lei: str = Field(default=None, alias='LEI')
    legal_name: str = Field(default=None, alias='LegalName')
    first_address_line: str = Field(default=None, alias='FirstAddressLine')
    additional_address_line: str = Field(default=None, alias='AdditionalAddressLine')
    city: str = Field(default=None, alias='City')
    region: str = Field(default=None, alias='Region')
    country: str = Field(default=None, alias='Country')
    postal_code: str = Field(default=None, alias='PostalCode')
    legal_jurisdiction: str = Field(default=None, alias='LegalJurisdiction')
    entity_legal_form_code: str = Field(default=None, alias='EntityLegalFormCode')
    other_legal_form: str = Field(default=None, alias='OtherLegalForm')
