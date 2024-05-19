import unittest
import os
import csv
from pain001.core.core import process_files
from pain001.csv.load_csv_data import load_csv_data
from pain001.csv.validate_csv_data import validate_csv_data


class TestLoadCsvData(unittest.TestCase):

    def setUp(self):
        """Create test files before each test."""
        os.makedirs("tests/data", exist_ok=True)

        # valid_data.csv
        valid_data = [
            [
                "id",
                "date",
                "nb_of_txs",
                "initiator_name",
                "initiator_street_name",
                "initiator_building_number",
                "initiator_postal_code",
                "initiator_town_name",
                "initiator_country_code",
                "payment_information_id",
                "payment_method",
                "batch_booking",
                "requested_execution_date",
                "debtor_name",
                "debtor_street_name",
                "debtor_building_number",
                "debtor_postal_code",
                "debtor_town_name",
                "debtor_country_code",
                "debtor_account_IBAN",
                "debtor_agent_BIC",
                "charge_bearer",
                "payment_id",
                "payment_amount",
                "currency",
                "payment_currency",
                "ctrl_sum",
                "creditor_agent_BIC",
                "creditor_name",
                "creditor_street_name",
                "creditor_building_number",
                "creditor_postal_code",
                "creditor_town_name",
                "creditor_country_code",
                "creditor_account_IBAN",
                "purpose_code",
                "reference_number",
                "reference_date",
                "service_level_code",
                "forwarding_agent_BIC",
                "remittance_information",
                "charge_account_IBAN",
            ],
            [
                "1",
                "2023-03-10T15:30:47.000Z",
                "2",
                "John Doe",
                "John's Street",
                "1",
                "12345",
                "John's Town",
                "DE",
                "Payment-Info-12345",
                "TRF",
                "true",
                "2023-03-12",
                "Acme Corp",
                "Acme Street",
                "2",
                "67890",
                "Acme Town",
                "DE",
                "DE75512108001245126162",
                "BANKDEFFXXX",
                "SLEV",
                "PaymentID6789",
                "150",
                "EUR",
                "EUR",
                "15000",
                "SPUEDE2UXXX",
                "Global Tech",
                "Global Street",
                "3",
                "11223",
                "Global Town",
                "DE",
                "DE68210501700024690959",
                "OTHR",
                "Invoice-98765",
                "2023-03-09",
                "SEPA",
                "SPUEDE2UXXX",
                "Invoice-12345",
                "CHARGE-IBAN-12345",
            ],
            [
                "2",
                "2023-03-11T10:20:18.000Z",
                "3",
                "Jane Smith",
                "Jane's Street",
                "10",
                "67890",
                "Jane's Town",
                "DE",
                "Payment-Info-67890",
                "TRF",
                "true",
                "2023-03-14",
                "Brown Industries",
                "Brown Street",
                "20",
                "45678",
                "Brown Town",
                "DE",
                "DE44500105175407324931",
                "BANKDEFFXXX",
                "SHAR",
                "PaymentID4321",
                "300",
                "EUR",
                "EUR",
                "30000",
                "SPUEDE2UXXX",
                "Green Energy",
                "Green Street",
                "30",
                "78901",
                "Green Town",
                "DE",
                "DE89370400440532013008",
                "OTHR",
                "Invoice-12345",
                "2023-03-13",
                "SEPA",
                "SPUEDE2UXXX",
                "Invoice-67890",
                "CHARGE-IBAN-67890",
            ],
            [
                "3",
                "2023-03-11T11:45:23.000Z",
                "1",
                "Michael Johnson",
                "Michael's Street",
                "15",
                "89101",
                "Michael's Town",
                "DE",
                "Payment-Info-24680",
                "TRF",
                "true",
                "2023-03-13",
                "Alpha Electronics",
                "Alpha Street",
                "25",
                "32165",
                "Alpha Town",
                "DE",
                "DE47500105175711000100",
                "BANKDEFFXXX",
                "SLEV",
                "PaymentID1357",
                "250",
                "EUR",
                "EUR",
                "25000",
                "SPUEDE2UXXX",
                "Beta Chemicals",
                "Beta Street",
                "35",
                "65432",
                "Beta Town",
                "DE",
                "DE44500105175407123457",
                "OTHR",
                "Invoice-24680",
                "2023-03-11",
                "SEPA",
                "SPUEDE2UXXX",
                "Invoice-24680",
                "CHARGE-IBAN-24680",
            ],
            [
                "4",
                "2023-03-12T09:12:34.000Z",
                "2",
                "Emily Wilson",
                "Emily's Street",
                "4",
                "34567",
                "Emily's Town",
                "DE",
                "Payment-Info-36912",
                "TRF",
                "true",
                "2023-03-15",
                "Zeta Services",
                "Zeta Street",
                "8",
                "98765",
                "Zeta Town",
                "DE",
                "DE68120933300112345608",
                "BANKDEFFXXX",
                "SHAR",
                "PaymentID8642",
                "200",
                "EUR",
                "EUR",
                "20000",
                "SPUEDE2UXXX",
                "Theta Solutions",
                "Theta Street",
                "38",
                "54321",
                "Theta Town",
                "DE",
                "DE75512108001245123456",
                "OTHR",
                "Invoice-36912",
                "2023-03-14",
                "SEPA",
                "SPUEDE2UXXX",
                "Invoice-36912",
                "CHARGE-IBAN-36912",
            ],
        ]
        with open("tests/data/valid_data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(valid_data)

        # invalid_data.csv
        invalid_data = [
            [
                "id",
                "date",
                "nb_of_txs",
                "initiator_name",
                "initiator_street_name",
                "initiator_building_number",
                "initiator_postal_code",
                "initiator_town_name",
                "initiator_country_code",
                "payment_information_id",
                "payment_method",
                "batch_booking",
                "requested_execution_date",
                "debtor_name",
                "debtor_street_name",
                "debtor_building_number",
                "debtor_postal_code",
                "debtor_town_name",
                "debtor_country_code",
                "debtor_account_IBAN",
                "debtor_agent_BIC",
                "charge_bearer",
                "payment_id",
                "payment_amount",
                "currency",
                "payment_currency",
                "ctrl_sum",
                "creditor_agent_BIC",
                "creditor_name",
                "creditor_street_name",
                "creditor_building_number",
                "creditor_postal_code",
                "creditor_town_name",
                "creditor_country_code",
                "creditor_account_IBAN",
                "purpose_code",
                "reference_number",
                "reference_date",
                "service_level_code",
                "forwarding_agent_BIC",
                "remittance_information",
                "charge_account_IBAN",
            ],
            [
                "1",
                "not-a-date",
                "2",
                "John Doe",
                "John's Street",
                "1",
                "12345",
                "John's Town",
                "DE",
                "Payment-Info-12345",
                "TRF",
                "true",
                "2023-03-12",
                "Acme Corp",
                "Acme Street",
                "2",
                "67890",
                "Acme Town",
                "DE",
                "DE75512108001245126162",
                "BANKDEFFXXX",
                "SLEV",
                "PaymentID6789",
                "150",
                "EUR",
                "EUR",
                "15000",
                "SPUEDE2UXXX",
                "Global Tech",
                "Global Street",
                "3",
                "11223",
                "Global Town",
                "DE",
                "DE68210501700024690959",
                "OTHR",
                "Invoice-98765",
                "2023-03-09",
                "SEPA",
                "SPUEDE2UXXX",
                "Invoice-12345",
                "CHARGE-IBAN-12345",
            ],
        ]
        with open(
            "tests/data/invalid_data.csv", "w", newline=""
        ) as file:
            writer = csv.writer(file)
            writer.writerows(invalid_data)

        # empty.csv
        open("tests/data/empty.csv", "w").close()

        # single_column.csv
        single_column = [["id"], ["1"], ["2"], ["3"]]
        with open(
            "tests/data/single_column.csv", "w", newline=""
        ) as file:
            writer = csv.writer(file)
            writer.writerows(single_column)

        # single_row.csv
        single_row = [
            [
                "id",
                "date",
                "nb_of_txs",
                "initiator_name",
                "initiator_street_name",
                "initiator_building_number",
                "initiator_postal_code",
                "initiator_town_name",
                "initiator_country_code",
                "payment_information_id",
                "payment_method",
                "batch_booking",
                "requested_execution_date",
                "debtor_name",
                "debtor_street_name",
                "debtor_building_number",
                "debtor_postal_code",
                "debtor_town_name",
                "debtor_country_code",
                "debtor_account_IBAN",
                "debtor_agent_BIC",
                "charge_bearer",
                "payment_id",
                "payment_amount",
                "currency",
                "payment_currency",
                "ctrl_sum",
                "creditor_agent_BIC",
                "creditor_name",
                "creditor_street_name",
                "creditor_building_number",
                "creditor_postal_code",
                "creditor_town_name",
                "creditor_country_code",
                "creditor_account_IBAN",
                "purpose_code",
                "reference_number",
                "reference_date",
                "service_level_code",
                "forwarding_agent_BIC",
                "remittance_information",
                "charge_account_IBAN",
            ],
            [
                "1",
                "2023-03-10T15:30:47.000Z",
                "2",
                "John Doe",
                "John's Street",
                "1",
                "12345",
                "John's Town",
                "DE",
                "Payment-Info-12345",
                "TRF",
                "true",
                "2023-03-12",
                "Acme Corp",
                "Acme Street",
                "2",
                "67890",
                "Acme Town",
                "DE",
                "DE75512108001245126162",
                "BANKDEFFXXX",
                "SLEV",
                "PaymentID6789",
                "150",
                "EUR",
                "EUR",
                "15000",
                "SPUEDE2UXXX",
                "Global Tech",
                "Global Street",
                "3",
                "11223",
                "Global Town",
                "DE",
                "DE68210501700024690959",
                "OTHR",
                "Invoice-98765",
                "2023-03-09",
                "SEPA",
                "SPUEDE2UXXX",
                "Invoice-12345",
                "CHARGE-IBAN-12345",
            ],
        ]
        with open("tests/data/single_row.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(single_row)

    def tearDown(self):
        """Delete test files after each test."""
        files = [
            "tests/data/valid_data.csv",
            "tests/data/invalid_data.csv",
            "tests/data/empty.csv",
            "tests/data/single_column.csv",
            "tests/data/single_row.csv",
        ]
        for file in files:
            if os.path.exists(file):
                os.remove(file)

    def test_load_valid_csv(self):
        file_path = "tests/data/valid_data.csv"
        data = load_csv_data(file_path)
        self.assertEqual(len(data), 4)
        self.assertEqual(data[0]["id"], "1")

    def test_load_empty_csv(self):
        file_path = "tests/data/empty.csv"
        with self.assertRaises(ValueError):
            load_csv_data(file_path)

    def test_load_csv_with_invalid_data(self):
        file_path = "tests/data/invalid_data.csv"
        data = load_csv_data(file_path)
        self.assertFalse(validate_csv_data(data))

    def test_load_single_row_csv(self):
        file_path = "tests/data/single_row.csv"
        data = load_csv_data(file_path)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["id"], "1")

    def test_load_single_column_csv(self):
        file_path = "tests/data/single_column.csv"
        data = load_csv_data(file_path)
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0]["id"], "1")


class TestProcessFiles(unittest.TestCase):
    def test_successful_execution(self):
        process_files(
            "pain.001.001.03",
            "tests/data/template.xml",
            "tests/data/template.xsd",
            "tests/data/template.csv",
        )

    def test_valid_xml_message_type(self):
        process_files(
            "pain.001.001.03",
            "tests/data/template.xml",
            "tests/data/template.xsd",
            "tests/data/template.csv",
        )


class TestValidateCsvData(unittest.TestCase):
    def test_validate_csv_with_valid_data(self):
        data = [
            {
                "id": "1",
                "date": "2023-03-10T15:30:47.000Z",
                "nb_of_txs": "2",
                "initiator_name": "John Doe",
                "initiator_street_name": "John's Street",
                "initiator_building_number": "1",
                "initiator_postal_code": "12345",
                "initiator_town_name": "John's Town",
                "initiator_country_code": "DE",
                "payment_information_id": "Payment-Info-12345",
                "payment_method": "TRF",
                "batch_booking": "true",
                "requested_execution_date": "2023-03-12",
                "debtor_name": "Acme Corp",
                "debtor_street_name": "Acme Street",
                "debtor_building_number": "2",
                "debtor_postal_code": "67890",
                "debtor_town_name": "Acme Town",
                "debtor_country_code": "DE",
                "debtor_account_IBAN": "DE75512108001245126162",
                "debtor_agent_BIC": "BANKDEFFXXX",
                "charge_bearer": "SLEV",
                "payment_id": "PaymentID6789",
                "payment_amount": "150",
                "currency": "EUR",
                "payment_currency": "EUR",
                "ctrl_sum": "15000",
                "creditor_agent_BIC": "SPUEDE2UXXX",
                "creditor_name": "Global Tech",
                "creditor_street_name": "Global Street",
                "creditor_building_number": "3",
                "creditor_postal_code": "11223",
                "creditor_town_name": "Global Town",
                "creditor_country_code": "DE",
                "creditor_account_IBAN": "DE68210501700024690959",
                "purpose_code": "OTHR",
                "reference_number": "Invoice-98765",
                "reference_date": "2023-03-09",
                "service_level_code": "SEPA",
                "forwarding_agent_BIC": "SPUEDE2UXXX",
                "remittance_information": "Invoice-12345",
                "charge_account_IBAN": "CHARGE-IBAN-12345",
            }
        ]
        self.assertTrue(validate_csv_data(data))

    def test_validate_csv_with_invalid_data(self):
        data = [
            {
                "id": "1",
                "date": "not-a-date",
                "nb_of_txs": "2",
                "initiator_name": "John Doe",
                "initiator_street_name": "John's Street",
                "initiator_building_number": "1",
                "initiator_postal_code": "12345",
                "initiator_town_name": "John's Town",
                "initiator_country_code": "DE",
                "payment_information_id": "Payment-Info-12345",
                "payment_method": "TRF",
                "batch_booking": "true",
                "requested_execution_date": "2023-03-12",
                "debtor_name": "Acme Corp",
                "debtor_street_name": "Acme Street",
                "debtor_building_number": "2",
                "debtor_postal_code": "67890",
                "debtor_town_name": "Acme Town",
                "debtor_country_code": "DE",
                "debtor_account_IBAN": "DE75512108001245126162",
                "debtor_agent_BIC": "BANKDEFFXXX",
                "charge_bearer": "SLEV",
                "payment_id": "PaymentID6789",
                "payment_amount": "150",
                "currency": "EUR",
                "payment_currency": "EUR",
                "ctrl_sum": "15000",
                "creditor_agent_BIC": "SPUEDE2UXXX",
                "creditor_name": "Global Tech",
                "creditor_street_name": "Global Street",
                "creditor_building_number": "3",
                "creditor_postal_code": "11223",
                "creditor_town_name": "Global Town",
                "creditor_country_code": "DE",
                "creditor_account_IBAN": "DE68210501700024690959",
                "purpose_code": "OTHR",
                "reference_number": "Invoice-98765",
                "reference_date": "2023-03-09",
                "service_level_code": "SEPA",
                "forwarding_agent_BIC": "SPUEDE2UXXX",
                "remittance_information": "Invoice-12345",
                "charge_account_IBAN": "CHARGE-IBAN-12345",
            }
        ]
        self.assertFalse(validate_csv_data(data))


if __name__ == "__main__":
    unittest.main()
