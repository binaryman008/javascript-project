import csv
import json


if __name__ == '__main__':

    # Reading and extracting information from csv file
    with open('mca_maharashtra.csv', 'r', encoding='latin-1') as csv_file:
        ACTIVITIES_LIST = [
            "Agriculture and Allied Activities",
            "Trading",
            "Manufacturing (Metals & Chemicals, and products thereof)",
            "Finance",
            "Construction"
            ]
        csv_reader = csv.reader(csv_file)

        # Creating a dictionary to store 5 business activities in values
        # with year as the key
        pba_dict = {}
        for line in csv_reader:
            if line[6] == 'DATE_OF_REGISTRATION':
                continue
            else:
                year = line[6]
                year = year[6:]
                if year == "":
                    continue
                if int(year) >= 1990 and int(year) < 2000:
                    if year not in pba_dict:
                        pba_dict[year] = [0, 0, 0, 0, 0]
                    else:
                        for i in range(len(ACTIVITIES_LIST)):
                            if line[11] == ACTIVITIES_LIST[i]:
                                pba_dict[year][i] += 1
    with open("assets/stacked_plot.json", "w") as json_file:
        json.dump(pba_dict,json_file)