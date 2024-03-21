import os
import csv
def annual_salary_for_each_business_unit():
    data=[]
    Corporate=[]
    Speciality_Products=[]
    Research=[]
    Manufacturing=[]
    with open('Employee Sample Data.csv') as csvfile:
        reader=csv.DictReader(csvfile)

                                    
        for row in reader:
            units_list=['Corporate', 'Speciality Products', 'Research & Development', 'Manufacturing']
            unit=row['Business Unit']
            wage=int(row['Annual Salary'])
            lis=[unit, wage]
            data.append(lis)

            if lis[0]=='Corporate':
                Corporate.append(lis)
            elif lis[0]=='Speciality Products':
                Speciality_Products.append(lis)
            elif lis[0]=='Research & Development':
                Research.append(lis)
            elif lis[0]=='Manufacturing':
                Manufacturing.append(lis)

    #Corporate
    flattened_Corporate = [val for sublist in Corporate for val in sublist]

    sum_Corporate = sum(map(lambda x: int(x), filter(lambda x: str(x).isdigit(), flattened_Corporate)))

    #Speciality Products
    flattened_Products = [val for sublist in Speciality_Products for val in sublist]

    sum_Products = sum(map(lambda x: int(x), filter(lambda x: str(x).isdigit(), flattened_Products)))

    #Research
    flattened_Research = [val for sublist in Research for val in sublist]

    sum_Research = sum(map(lambda x: int(x), filter(lambda x: str(x).isdigit(), flattened_Research)))

    #Manufacturing
    flattened_Manufacturing = [val for sublist in Manufacturing for val in sublist]

    sum_Manufacturing = sum(map(lambda x: int(x), filter(lambda x: str(x).isdigit(), flattened_Manufacturing)))


    print(f'Annual salary of {units_list[0]} unit is {sum_Corporate}, \nAnnual salary of {units_list[1]} unit is {sum_Products}, \nAnnual salary of {units_list[2]} unit is {sum_Research}, \nAnnual salary of {units_list[3]} unit is {sum_Manufacturing}. ')