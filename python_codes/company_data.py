import csv
import json

with open('mca_maharashtra.csv', 'r', encoding='latin-1') as csv_file:
    csv_reader = csv.reader(csv_file)
    capital = [
        '<=1L',
            '1L to 10L',
            '10L to 1Cr',
            '1Cr to 10Cr',
            '>10Cr'
    ]
    capital_dict = {cap: 0 for cap in capital}
    capital_amount = [
            line[8]
            for line in csv_reader if line[8] is not None
            ][1:]

for i in capital_amount:
    cap_amount = int(float(i))

    if cap_amount <= 100000:
        # companies_with_capital[0] += 1
        capital_dict['<=1L'] += 1
    elif 100000 < cap_amount < 1000000:
        capital_dict['1L to 10L'] += 1
    elif 1000000 <= cap_amount < 10000000:
        capital_dict['10L to 1Cr'] += 1
    elif 10000000 <= cap_amount <= 100000000:
        capital_dict['1Cr to 10Cr'] += 1
    else:
        capital_dict['>10Cr'] += 1

with open("assets/company_data.json", "w") as json_file:
    json.dump(capital_dict,json_file)
