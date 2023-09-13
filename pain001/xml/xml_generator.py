# Copyright (C) 2023 Sebastien Rousseau.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# XML generator function that creates the XML file from the CSV data
# and the mapping dictionary between XML tags and CSV columns names and
# writes it to a file in the same directory as the CSV file


import sys
from jinja2 import Environment, FileSystemLoader
from pain001.xml.create_root_element import create_root_element
from pain001.xml.generate_updated_xml_file_path import (
    generate_updated_xml_file_path,
)
from pain001.xml.generate_xml import (
    create_xml_v3,
    create_xml_v4,
    create_xml_v9,
)

from pain001.xml.validate_via_xsd import validate_via_xsd

# Import the XML libraries
import xml.etree.ElementTree as ET


def xml_generator( 
    data,
    payment_initiation_message_type,
    xml_file_path,
    xsd_file_path,
):
    # Create the root element and set its attributes
    root = create_root_element(payment_initiation_message_type)

    # Define a mapping between the XML types and the XML generators
    xml_generators = {
        "pain.001.001.03": create_xml_v3,
        "pain.001.001.04": create_xml_v4,
        "pain.001.001.09": create_xml_v9,
    }

    # Check if the provided payment_initiation_message_type exists in
    # the mapping
    if payment_initiation_message_type in xml_generators:
        # Get the corresponding XML generation function for the XML type
        # xml_generator = xml_generators[payment_initiation_message_type]

        # Check if data is not empty
        if not data:
            print("Error: No data to process.")
            sys.exit(1)

        # Create a Jinja2 environment
        env = Environment(loader=FileSystemLoader('.'))

        # Load the Jinja2 template
        template = env.get_template(xml_file_path)

        # Prepare the data for rendering
        if payment_initiation_message_type == "pain.001.001.03":
            xml_data_pain001_001_03 = {
                'id': data[0]['id'],
                'date': data[0]['date'],
                'nb_of_txs': data[0]['nb_of_txs'],
                'initiator_name': data[0]['initiator_name'],
                'initiator_street_name': data[0]['initiator_street_name'],
                'initiator_building_number': data[0]['initiator_building_number'],
                'initiator_postal_code': data[0]['initiator_postal_code'],
                'initiator_town_name': data[0]['initiator_town_name'],
                'initiator_country_code': data[0]['initiator_country_code'],
                'payment_id': data[0]['payment_id'],
                'payment_method': data[0]['payment_method'],
                'batch_booking': data[0]['batch_booking'],
                'requested_execution_date': data[0]['requested_execution_date'],
                'debtor_name': data[0]['debtor_name'],
                'debtor_street_name': data[0]['debtor_street_name'],
                'debtor_building_number': data[0]['debtor_building_number'],
                'debtor_postal_code': data[0]['debtor_postal_code'],
                'debtor_town_name': data[0]['debtor_town_name'],
                'debtor_country_code': data[0]['debtor_country_code'],
                'debtor_account_IBAN': data[0]['debtor_account_IBAN'],
                'debtor_agent_BIC': data[0]['debtor_agent_BIC'],
                'charge_bearer': data[0]['charge_bearer'],
                'transactions': [
                    {
                        'payment_id': row['payment_id'],
                        'payment_amount': row.get('payment_amount', ''),
                        'payment_currency': row.get('payment_currency', ''),
                        'charge_bearer': row['charge_bearer'],
                        'creditor_agent_BIC': row['creditor_agent_BIC'],
                        'creditor_name': row['creditor_name'],
                        'creditor_street_name': row['creditor_street_name'],
                        'creditor_building_number': row['creditor_building_number'],
                        'creditor_postal_code': row['creditor_postal_code'],
                        'creditor_town_name': row['creditor_town_name'],
                        'creditor_country_code': row['creditor_country_code'],
                        'creditor_account_IBAN': row['creditor_account_IBAN'],
                        'purpose_code': row['purpose_code'],
                        'reference_number': row['reference_number'],
                        'reference_date': row['reference_date'],
                    }
                    for row in data[1:]
                ],
            }
        elif payment_initiation_message_type == "pain.001.001.04":
            xml_data_pain001_001_04 = {
                'id': data[0]['id'],
                'date': data[0]['date'],
                'nb_of_txs': data[0]['nb_of_txs'],
                'initiator_name': data[0]['initiator_name'],
                'initiator_street': data[0]['initiator_street_name'],
                'initiator_building_number': data[0]['initiator_building_number'],
                'initiator_postal_code': data[0]['initiator_postal_code'],
                'initiator_town': data[0]['initiator_town_name'],
                'initiator_country': data[0]['initiator_country_code'],

                'payment_information_id': data[0]['payment_id'],
                'payment_method': data[0]['payment_method'],
                'batch_booking': data[0]['batch_booking'],
                'requested_execution_date': data[0]['requested_execution_date'],

                'debtor_name': data[0]['debtor_name'],
                'debtor_street': data[0]['debtor_street_name'],
                'debtor_building_number': data[0]['debtor_building_number'],
                'debtor_postal_code': data[0]['debtor_postal_code'],
                'debtor_town': data[0]['debtor_town_name'],
                'debtor_country': data[0]['debtor_country_code'],
                'debtor_account_IBAN': data[0]['debtor_account_IBAN'],
                'debtor_agent_BICFI': data[0]['debtor_agent_BIC'],
                'debtor_agent_account_IBAN': data[0]['debtor_agent_account_IBAN'],
                'instruction_for_debtor_agent': data[0]['instruction_for_debtor_agent'],
                'charge_bearer': data[0]['charge_bearer'],
                'charge_account_IBAN': data[0]['charge_account_IBAN'],
                'charge_agent_BICFI': data[0]['charge_agent_BICFI'],
                'payment_instruction_id': data[0]['payment_instruction_id'],
                'payment_end_to_end_id': data[0]['payment_end_to_end_id'],
                'payment_currency': data[0]['payment_currency'],
                'payment_amount': data[0]['payment_amount'],
                'creditor_agent_BIC': data[0]['creditor_agent_BIC'],
                'creditor_name': data[0]['creditor_name'],
                'creditor_street': data[0]['creditor_street'],
                'creditor_building_number': data[0]['creditor_building_number'],
                'creditor_postal_code': data[0]['creditor_postal_code'],
                'creditor_town': data[0]['creditor_town'],
                'creditor_account_IBAN': data[0]['creditor_account_IBAN'],
                'purpose_code': data[0]['purpose_code'],
                'reference_number': data[0]['reference_number'],
                'reference_date': data[0]['reference_date'],

                'transactions': [{
                    'payment_instruction_id': row['payment_id'],
                    'payment_end_to_end_id': row['reference_number'],
                    'payment_currency': row.get('payment_currency','EUR'),
                    'payment_amount': row.get('payment_amount', ''),
                    'charge_bearer': row['charge_bearer'],
                    'creditor_agent_BIC': row['creditor_agent_BIC'],
                    'creditor_name': row['creditor_name'],
                    'creditor_street': row['creditor_street_name'],
                    'creditor_building_number': row['creditor_building_number'],
                    'creditor_postal_code': row['creditor_postal_code'],
                    'creditor_town': row['creditor_town_name'],
                    'creditor_account_IBAN': row['creditor_account_IBAN'],
                    'purpose_code': row['purpose_code'],
                    'reference_number': row['reference_number'],
                    'reference_date': row['reference_date']
                }
                for row in data[1:]]
            }

        # Check if the payment initiation message type is "pain.001.001.03"
        if payment_initiation_message_type == "pain.001.001.03":
            xml_data = xml_data_pain001_001_03
        elif payment_initiation_message_type == "pain.001.001.04":
            xml_data = xml_data_pain001_001_04
        else:
            # If it's not supported, print an error message and exit the program
            print(f"The payment initiation message type {payment_initiation_message_type} is not supported at this time.")
            sys.exit(1)

        # Render the template
        xml_content = template.render(**xml_data)

        # Generate updated XML file path
        updated_xml_file_path = generate_updated_xml_file_path(xml_file_path, payment_initiation_message_type)

        # Write the XML content to the file without extra spacing
        with open(updated_xml_file_path, "w") as xml_file:
            xml_file.write(xml_content)

        print(f"A new XML file has been created at {updated_xml_file_path}")

        # Validate the updated XML file against the XSD schema
        is_valid = validate_via_xsd(updated_xml_file_path, xsd_file_path)
        if not is_valid:
            print("Error: Invalid XML data.")
            sys.exit(1)
        else:
            print(f"The XML has been validated against {xsd_file_path}")

        # Validate the updated XML file against the XSD schema
        is_valid = validate_via_xsd(updated_xml_file_path, xsd_file_path)
        if not is_valid:
            print("Error: Invalid XML data.")
            sys.exit(1)
        else:
            print(f"The XML has been validated against {xsd_file_path}")


    else:
        # Handle the case when the payment_initiation_message_type is
        # not valid
        print(
            "Error: Invalid XML message type:",
            payment_initiation_message_type,
        )
        sys.exit(1)