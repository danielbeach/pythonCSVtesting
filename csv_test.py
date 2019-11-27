from time import time


def open_csv_file(file_location: str) -> object:
    with open(file_location, 'r') as f:
        data = f.readlines()
    for line in data:
        split_line(line)


def split_line(line: str) -> None:
    column_data = line.split(',')
    print(column_data)


if __name__ == '__main__':
    t1 = time()
    open_csv_file(file_location='PortfoliobyBorrowerLocation-Table 1.csv')
    t2 = time()
    print('The total time taken was {t} seconds'.format(t=str(t2-t1)))


from time import time


def open_csv_file(file_location: str) -> object:
    with open(file_location, 'r') as f:
        line = True
        while line:
            line = f.readline()
            split_line(line)


def split_line(line: str) -> None:
    column_data = line.split(',')
    print(column_data)


if __name__ == '__main__':
    t1 = time()
    open_csv_file(file_location='PortfoliobyBorrowerLocation-Table 1.csv')
    t2 = time()
    print('The total time taken was {t} seconds'.format(t=str(t2-t1)))


from time import time
import csv


def open_csv_file(file_location: str) -> object:
    with open(file_location) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            print(row)


if __name__ == '__main__':
    t1 = time()
    open_csv_file(file_location='PortfoliobyBorrowerLocation-Table 1.csv')
    t2 = time()
    print('The total time taken was {t} seconds'.format(t=str(t2-t1)))


from time import time
import pandas


def open_csv_file(file_location: str) -> object:
    dataframe = pandas.read_csv(file_location)
    for index, row in dataframe.iterrows():
        print(row['Location'], row['Balance (in billions)'], row['Borrowers (in thousands)'])

if __name__ == '__main__':
    t1 = time()
    open_csv_file(file_location='PortfoliobyBorrowerLocation-Table 1.csv')
    t2 = time()
    print('The total time taken was {t} seconds'.format(t=str(t2-t1)))


from time import time
import dask.dataframe as dd


def open_csv_file(file_location: str) -> object:
    df = dd.read_csv(file_location)
    for index, row in df.iterrows():
        print(row['Location'], row['Balance (in billions)'], row['Borrowers (in thousands)'])

if __name__ == '__main__':
    t1 = time()
    open_csv_file(file_location='PortfoliobyBorrowerLocation-Table 1.csv')
    t2 = time()
    print('The total time taken was {t} seconds'.format(t=str(t2-t1)))