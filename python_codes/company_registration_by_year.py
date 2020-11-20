import csv
import json

if __name__ == '__main__':

    # Reading and extracting information from csv file
    with open('mca_maharashtra.csv', 'r', encoding='latin-1') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Creating a dictionary to store year
        # and count of registrations each year
        year_dict = {}
        for line in csv_reader:
            if line[6] == 'DATE_OF_REGISTRATION':
                continue
            else:
                string = line[6]
                string = string[6:]
                year_dict[string] = year_dict.get(string, 1) + 1

    # Creating arrays to store years and number of registrations
    year_array = [k for k in year_dict]
    year_array.sort()
    year_array.remove('')
    year_array_2 = [year_array[i] for i in range(101, 112)]
    registrations = [year_dict[i] for i in year_array_2]
    year_dict_short = {i:year_dict[i] for i in year_array_2}
    with open("assets/company_registration_by_year.json", "w") as json_file:
        json.dump(year_dict_short,json_file)
