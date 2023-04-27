# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import csv
import os

# Define a few state variables
trans_file_name =""
trans_out_file_name = ""
skip_rows = []
skip_rows_def = [0]
header_row = 1
ticker_column_name = ""
ticker_column_name_def = "Symbol"
tickers = []
tickers_def = ["FB", "META"]

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def get_trans_file():
    global trans_file_name
    while (True):
        trans_file_name = input("Please provide full path to CSV file with all transactions: ")
        if "" != trans_file_name:
            print('transaction file name: ' + trans_file_name)
            break
        print('Sorry, empty transaction csv filename....')
        continue

    global header_row
    header_row_str = input("Header Row # ?, Enter for default (" + str(header_row) + ") ")
    if "" != header_row_str:
        header_row = int(header_row_str)
    print('Using Header Row # : ' + str(header_row))

    global ticker_column_name
    ticker_column_name = input("Column name for the ticker symbols ?, Enter for default(" + ticker_column_name_def +") ")
    if "" == ticker_column_name:
        ticker_column_name = ticker_column_name_def
    print('Using Column name for the ticker symbols: ' + ticker_column_name)

    global skip_rows
    skip_rows = [int(x) for x in input("Please enter row numbers to skip, separated by space, Enter for default(" + str(skip_rows_def) + ") ").split()]
    if  len(skip_rows) == 0:
        skip_rows = skip_rows_def
    print(skip_rows)

def get_tickers():
    global tickers
    tickers = input("Please enter ticket symbols separated by space, Enter for default(" + str(tickers_def) + ") ").split()
    if  len(tickers) == 0:
        tickers = tickers_def
    print("Filtering for symbols " + str(tickers))

def dump_file(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(row)
                line_count += 1
        print(f'Processed {line_count} lines.')

def filter_transactions(trans_file_name: str, ticker_column_name: str, header_row: int, skip_rows: list):
    dirname = os.path.dirname(trans_file_name)
    basename, extname = os.path.splitext(os.path.basename(trans_file_name))
    global trans_out_file_name
    trans_out_file_name = dirname + '/' + basename + '_out' + extname
    print('Transactions output file ', trans_out_file_name)
    with open(trans_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        with open(trans_out_file_name, mode='w') as trans_out_file:
            csv_writer = csv.writer(trans_out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            line_count = 0
            for row in csv_reader:
                if line_count == header_row:
                    print(f'Column names are {", ".join(row)}')
                    ticker_index = row.index(ticker_column_name)
                    csv_writer.writerow(row)
                elif line_count not in skip_rows:
                    print(row)
                    if row[ticker_index] in tickers:
                        csv_writer.writerow(row)
                line_count += 1
            print(f'Processed {line_count} lines.')
            ""

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_trans_file()
    get_tickers()
    filter_transactions(trans_file_name, ticker_column_name, header_row, skip_rows)
    dump_file(trans_out_file_name)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
