from django.core.management.base import BaseCommand, CommandError
from school_data_app.models import School

from xml.etree import ElementTree
from ares_util.ares import call_ares
import requests

class Command(BaseCommand):
    help = 'Parse Data about czech schools and save them to DB'

    def add_arguments(self, parser):
        # Argument pro vypnutí validace
        parser.add_argument(
            '--validate',
            action='store_true',
            help='Start validating company_id through ares API',
        )

    def handle(self, *args, **kwargs):
        # Stažení XML dat, kvůli veliksoti souboru používám stream=True
        url = 'https://rejstriky.msmt.cz/opendata/vrejcelk.xml'
        xml_response = requests.get(url=url, stream=True)
        # Parsne XMl data pro následnou manipulaci
        events = ElementTree.iterparse(xml_response.raw)

        # Data representujicí jednu školu
        data = {}

        # Projdeme každý element a uloží užitečná data
        for event, elem in events:

            if elem.tag == 'RedPlnyNazev':
                data['full_name'] = elem.text
            elif elem.tag == 'RedRUAINKod':
                data['ruian_code'] = elem.text
            elif elem.tag == 'RedAdresa1':
                data['address_1'] = elem.text
            elif elem.tag == 'RedAdresa2':
                data['address_2'] = elem.text
            elif elem.tag == 'RedAdresa3':
                data['address_3'] = elem.text
            elif elem.tag == 'ReditelJmeno':
                data['principal_name'] = elem.text
            elif elem.tag == 'ICO':
                data['company_id'] = elem.text
            elif elem.tag == 'PravniForma':
                data['legal_form'] = elem.text

            # PravniSubjekt je poslední tag, který každá škola má
            if elem.tag == 'PravniSubjekt':
                
                if kwargs['validate']:
                    # Validace IČO školy pomocí ares
                    ares_valid_data = call_ares(data['company_id'])
                else:
                    ares_valid_data = True

                if ares_valid_data:

                    if kwargs['validate']:
                        #Validace jména adresy školy pomocí ares
                        if not ares_valid_data['legal']['company_name'] == data['full_name']:
                            print(data['full_name'] + ' Is Not Valid')
                            continue
                        elif not ares_valid_data['legal']['legal_form'] == data['legal_form']:
                            print(data['legal_form'] + ' Is Not Valid')
                            continue
                        elif not ares_valid_data['address']['street'] == data['address_1']:
                            print(data['address_1'] + ' Is Not Valid')
                            continue
                    
                    # Uloží Školu do DB
                    school = School(**data)
                    school.save()
                    print('SAVED')
                else:
                    print('************************')
                    print('FAILED')
                    print('************************')
                    continue

        print('***********************')
        print('Data Collected!')
        print('***********************')