import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'chinook.db')

connection = sqlite3.connect(db_path)
cursor = connection.cursor()


def get_profit():
    query = "SELECT SUM(UnitPrice * Quantity) FROM invoice_items;"
    cursor.execute(query)
    result = cursor.fetchall()
    print(f'Общая прибыль по таблице invoice_items составляет {result[0][0]}.')


def get_repeating_firstnames():
    query = "SELECT FirstName, COUNT(FirstName) FROM customers GROUP BY FirstName HAVING COUNT(FirstName) > 1;"
    cursor.execute(query)
    result = cursor.fetchall()
    print('Повторяющиеся FirstName:')
    for res in result:
        print(f'{res[0]} {res[1]}')


get_profit()
get_repeating_firstnames()


connection.close()
