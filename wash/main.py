# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import csv
import os

# Define a few state variables
all_trans_file_name = ""
sale_trans_file_name = ""
trans_file_name =""
skip_rows = []
header_row = 0
ticker_column_name = "Symbol"

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
    while (True):
        header_row_str = input("Header Row # ? ")
        if "" != header_row_str:
            header_row = int(header_row_str)
            print('Header Row # : ' + str(header_row))
            break
        print('Sorry missing Header Row #....')
        continue

    global ticker_column_name
    while (True):
        ticker_column_name = input("Column name for the ticker symbols ?  ")
        if "" != ticker_column_name:
            print('Column name for the ticker symbols: ' + ticker_column_name)
            break
        print('Sorry missing Column name for the ticker symbols....')
        continue

    global skip_rows
    skip_rows = [int(x) for x in input("Please enter row numbers to skip, separated by space: ").split()]
    if  len(skip_rows) != 0:
        print(skip_rows)

def get_files():
    global all_trans_file_name
    all_trans_file_name = input("Please provide full path to CSV file with all transactions: ")
    if "" == all_trans_file_name:
        print('Sorry missing all transactions CSV file')
        exit(1)
    global sale_trans_file_name
    sale_trans_file_name = input("Please provide full path to CSV file with RSU sale transactions: ")
    if "" == sale_trans_file_name:
        print('Sorry missing RSU sale transactions CSV file')
        exit(1)
    print('All Transactions: ' + all_trans_file_name)
    print('Sale transactions: ' + sale_trans_file_name)

def get_tickers():
    global tickers
    while (True):
        tickers = input("Please enter ticket symbols separated by space: ").split()
        if  len(tickers) != 0:
            print(tickers)
            return
        print('Sorry no tickers to filter, please specify the symbols of equities to filter')

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


def process_all_transactions(all_trans_file_name):
    dirname       = os.path.dirname(all_trans_file_name)
    basename, extname = os.path.splitext(os.path.basename(all_trans_file_name))
    all_trans_out_file_name = dirname + '/' + basename + '_out' + extname
    print('All trans output file ',all_trans_out_file_name)
    with open(all_trans_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        with open(all_trans_out_file_name, mode='w') as all_out_file:
            csv_writer = csv.writer(all_out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            line_count = 0
            for row in csv_reader:
                if line_count == 1:
                    print(f'Column names are {", ".join(row)}')
                    csv_writer.writerow(row)
                elif line_count != 0:
                    print(row)
                    if row[2] in tickers:
                        csv_writer.writerow(row)
                line_count += 1
            print(f'Processed {line_count} lines.')

def process_sale_transactions(sale_trans_file_name):
    dirname           = os.path.dirname(sale_trans_file_name)
    basename, extname = os.path.splitext(os.path.basename(sale_trans_file_name))
    sale_trans_out_file_name = dirname + '/' + basename + '_out' + extname
    print('Sale trans output file ',sale_trans_out_file_name)
    with open(sale_trans_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        with open(sale_trans_out_file_name, mode='w') as sale_out_file:
            csv_writer = csv.writer(sale_out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            line_count = 0
            for row in csv_reader:
                if line_count == 1:
                    print(f'Column names are {", ".join(row)}')
                    csv_writer.writerow(row)
                elif line_count != 0:
                    print(row)
                    if row[0] in tickers:
                        csv_writer.writerow(row)
                line_count += 1
            print(f'Processed {line_count} lines.')

def filter_transactions(trans_file_name: str, ticker_column_name: str, header_row: int, skip_rows: list):
    dirname = os.path.dirname(trans_file_name)
    basename, extname = os.path.splitext(os.path.basename(trans_file_name))
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
#    get_files()
    get_trans_file()
    get_tickers()
 #   process_all_transactions(all_trans_file_name)
 #   process_sale_transactions(sale_trans_file_name)
 #   filter_transactions(all_trans_file_name, "Symbol", 1, [0])
 #   filter_transactions(sale_trans_file_name, "Symbol", 1, [0])
    filter_transactions(trans_file_name, ticker_column_name, header_row, skip_rows)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
