from xml.etree.ElementTree import iterparse

from gleifpy.schemas import CompanySchema

TAGS = ('LEI', 'LegalName', 'City', 'Country', 'AdditionalAddressLine', 'EntityLegalFormCode',  # 'EntityStatus',
        'FirstAddressLine',
        'LegalJurisdiction', 'OtherLegalForm', 'PostalCode', 'Region')


def gleif_data(filename: str) -> CompanySchema:
    context = iterparse(filename, events=("start", "end"))

    context = iter(context)

    event, root = next(context)

    prefix = '{http://www.gleif.org/data/schema/leidata/2016}'
    end_tag = 'LEIRecord'

    company_dict = {}
    for index, (event, elem) in enumerate(context):
        if elem.tag[len(prefix):] in TAGS:
            if event == 'start':
                company_dict[elem.tag[len(prefix):]] = elem.text

        elif event == "end" and elem.tag == prefix + end_tag:
            yield CompanySchema(**company_dict)

        root.clear()
        elem.clear()


if __name__ == "__main__":
    for com in gleif_data('../gle.xml'):
        print(com)
