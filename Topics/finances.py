import csv


with open('government-finance-statistics-general-government-year-ended-june-2019-csv.csv') as file:
    file_reader = csv.DictReader(file, delimiter=',')
    count = 0
    for line in file_reader:
        if line['STATUS'] == 'FINAL':
            count += 1
    print(count)
