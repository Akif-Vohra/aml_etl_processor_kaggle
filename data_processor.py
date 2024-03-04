import os
import sqlite3
import csv


class ETLProcessor:
    def __init__(self, input_file, db_file):
        self.input_file = input_file
        self.db_file = db_file

    def create_database(self):
        if os.path.exists(self.db_file):
            answer = input(
                "Running this file will delete previous sqlite"
                " database and reload it. Press Y to continue: ")
            if answer.lower() != 'y':
                return

        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()

        # Create a table to store the data
        c.execute(
            '''CREATE TABLE IF NOT EXISTS transactions
            (Time TEXT, Date TEXT, Sender_account TEXT, Receiver_account TEXT, 
            Amount REAL, Payment_currency TEXT, Received_currency TEXT, 
            Sender_bank_location TEXT, Receiver_bank_location TEXT, 
            Payment_type TEXT, Is_laundering INTEGER, Laundering_type TEXT)''')

        conn.commit()
        conn.close()

    def extract_transform_load(self):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()

        with open(self.input_file, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for index, row in enumerate(csv_reader):
                if index > 100000:
                    break
                print("Loaded {0} row".format(index))
                values = tuple(row.values())
                c.execute("INSERT INTO transactions VALUES "
                          "(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values)

        conn.commit()
        conn.close()


if __name__ == "__main__":
    input_file = "SAML-D.csv"
    db_file = "transactions.db"

    etl_processor = ETLProcessor(input_file, db_file)
    etl_processor.create_database()
    etl_processor.extract_transform_load()
