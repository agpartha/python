# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import csv
import os

# Define a few state variables
all_trans_file = ""
sale_trans_file = ""
tickers = []


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def get_files():
    global all_trans_file
    all_trans_file = input("Please provide full path to CSV file with all transactions: ")
    if "" == all_trans_file:
        print('Sorry missing all transactions CSV file')
        exit(1)
    global sale_trans_file
    sale_trans_file = input("Please provide full path to CSV file with RSU sale transactions: ")
    if "" == sale_trans_file:
        print('Sorry missing RSU sale transactions CSV file')
        exit(1)

def get_tickers():
    global tickers
    tickers = input("Please enter ticket symbols separated by space: ").split()

def dump_file(filename):
    with open(filename) as csv_file:
#       with open("/Users/anandpartha/Downloads/all_trans_filtered_file.csv", mode='w') as all_out_file:
#            with open("/Users/anandpartha/Downloads/sale_trans_filtered_file.csv", mode='w') as sale_out_file:
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(os.getlogin())
    get_files()
    get_tickers()
    print('All Transactions: ' + all_trans_file)
    print('Sale transactions: ' + sale_trans_file)
    print(tickers)
    dump_file(all_trans_file)
    dump_file(sale_trans_file)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
