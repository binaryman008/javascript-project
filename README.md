# dataproject-javascript

## Aim
To convert raw open data into plots, that tell a story on the state of company registration in Maharashtra and serve it into a html file.

## How to get the data
The data can be downloaded from [here](https://data.gov.in/resources/company-master-data-maharashtra-upto-21st-april-2018)

## Requirements for the project
Python3.5+ is the requirement to run this project

## Running the project
There are 4 problem statements :-
### 1. Plot a bar chart on the "Authorized Capital"
   * We need to plot the graph of authorized capitals of different companies according to amount.
   * run `python python_codes/company_data.py` in terminal to generate its json file.

### 2. Bar Plot of company registration by year
   * From the column, DATE_OF_REGISTRATION parse out the registration year. Using this data, plot a bar plot of the number of company registrations, vs. year.
   * run `python python_codes/company_registration_by_year.py` in terminal to generate its json file.

### 3. Top registrations by "Principal Business Activity" for the year 2015
   * Here we need to show top 10 principal business activities by companies in Maharashtra.
   * run `python python_codes/top_10_principal_business_activity.py` in terminal to generate its json file.
  
### 4. Plot a Grouped Bar Plot by aggregating registrations counts over
   * Year of Registration
   * Principal business activity (here we pick 5 activities and plot the graph against them).
   * run `python python_codes/stacked_bar_plot.py` in terminal to generate its json file.
   
open the current directory in the terminal and run the command `python -m http.server`. Now open any browser and open the [http://0.0.0.0:8000/](http://0.0.0.0:8000/) and open chart.html