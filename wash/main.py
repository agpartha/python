# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import csv
import os

# Define a few state variables
all_trans_file_name = ""
sale_trans_file_name = ""
tickers = []


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


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

def get_tickers():
    global tickers
    tickers = input("Please enter ticket symbols separated by space: ").split()

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(os.getlogin())
    get_files()
    get_tickers()
    print('All Transactions: ' + all_trans_file_name)
    print('Sale transactions: ' + sale_trans_file_name)
    print(tickers)
    process_all_transactions(all_trans_file_name)
    process_sale_transactions(sale_trans_file_name)
#    dump_file(all_trans_file_name)
#    dump_file(sale_trans_file_name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
