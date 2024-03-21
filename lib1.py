import csv
import os
#file_name=os.path.dirname(os.path.abspath(__file__))+"//Employee Sample Data.csv"
def r(rg):
    with open('Employee Sample Data.csv') as csvfile:
                            #create a dictionary object for each row and map each row value to a column name 
                            reader=csv.DictReader(csvfile)
                            for row in reader:
                                    #assign values to variables
                                    #######
                                    name=row['Full Name']
                                    wage=int(row['Annual Salary'])
                                    dep=row['Department']
                                    city=row['City']
                                    #######
                                    unit=row['Business Unit']
                    
def data_temp_file(file_name):
    with open(file_name, 'r') as csv_file:
        csv_reader=csv.reader(csv_file)
        data=[]
        for row in csv_reader:
            data.append(row)

    return(data)
'''
def get_listing(my_data, iindex):
    for items in my_data:
        department_list = []
        if items[int(iindex)] not in department_list:
            department_list.append(items[int(iindex)])
    return
'''