import sqlite3
from datetime import datetime


class DataAnalyzer:
    def __init__(self, db_file):
        self.db_file = db_file

    def query_database(self, query):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute(query)
        data = c.fetchall()
        conn.close()
        return data

    def total_deposits_between_dates(self, start_date, end_date):
        query = (f"SELECT SUM(Amount) FROM transactions WHERE "
                 f"Date BETWEEN '{start_date}' AND '{end_date}'")
        total_deposits = self.query_database(query)[0][0]
        return total_deposits if total_deposits else 0

    def total_deposits_by_bank_and_currency(self, bank_location, currency):
        query = (f"SELECT SUM(Amount) FROM transactions WHERE Sender_"
                 f"bank_location = '{bank_location}' AND "
                 f"Payment_currency = '{currency}'")
        total_deposits = self.query_database(query)[0][0]
        return total_deposits if total_deposits else 0

    def total_transactions(self):
        query = "SELECT COUNT(*) FROM transactions"
        total_transactions = self.query_database(query)[0][0]
        return total_transactions

    def average_transaction_amount(self):
        query = "SELECT AVG(Amount) FROM transactions"
        average_amount = self.query_database(query)[0][0]
        return average_amount if average_amount else 0

    def transactions_by_laundering_type(self):
        query = ("SELECT Laundering_type, COUNT(*) "
                 "FROM transactions GROUP BY Laundering_type")
        data = self.query_database(query)
        laundering_types = {row[0]: row[1] for row in data}
        return laundering_types


# Example usage
if __name__ == "__main__":
    db_file = "transactions.db"

    analyzer = DataAnalyzer(db_file)
    print("Total deposits between 2022-10-07 and 2022-10-08:",
          analyzer.total_deposits_between_dates('2022-10-07', '2022-10-08'))
    print("Total deposits from UK bank in UK pounds:",
          analyzer.total_deposits_by_bank_and_currency("UK", "UK pounds"))
    print("Total transactions:", analyzer.total_transactions())
    print("Average transaction amount:", analyzer.average_transaction_amount())
    print("Transactions by laundering type:",
          analyzer.transactions_by_laundering_type())
