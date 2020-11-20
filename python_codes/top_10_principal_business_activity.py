import csv
import json

if __name__ == '__main__':
    # Reading and extracting information from csv file
    with open('mca_maharashtra.csv', 'r', encoding='latin-1') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Dictionary is created to store business activity with numbers
        registration_dict = {}
        for line in csv_reader:
            if line[6] == 'DATE_OF_REGISTRATION':
                continue
            else:
                year = line[6]
                year = year[6:]
                if year == "2015":
                    a = line[11]
                    registration_dict[a] = registration_dict.get(a, 1)+1

    # Two arrays created to store business activity and
    # number of registrations from the dictionary
    principal_business_activity = []
    registrations = [registration_dict[k] for k in registration_dict]
    registrations.sort(reverse=True)
    registrations = registrations[:11]
    for k in registrations:
        activity = [
            key for key, value in registration_dict.items() if value == k
            ]
        principal_business_activity.append(activity)
    # extract string from p_b_a_2 to a new 1D List
    p_b_a_2 = [
        principal_business_activity[i][0]
        for i in range(len(principal_business_activity))
        ]
    final_obj = {}
    for i in range(len(p_b_a_2)):
        final_obj[p_b_a_2[i]] = registrations[i]

    with open("assets/top_10_principal_business_activity.json", "w") as json_file:
        json.dump(final_obj,json_file)
