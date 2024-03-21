import os
import csv
def annual_salary_for_each_department():
                        it=[]
                        accounting=[]
                        Engineering=[]
                        Finance=[]
                        Hr=[]
                        Marketing=[]
                        Sales=[]
                        with open('Employee Sample Data.csv') as csvfile:
                                        reader=csv.DictReader(csvfile)
                                        for row in reader:
                                                wage=int(row['Annual Salary'])
                                                dep=row['Department']
                                                lis1=[wage, dep]
                                                if lis1[1] == 'IT':
                                                        
                                                        it.append(lis1)
                                                elif lis1[1]=='Accounting':
                                                        accounting.append(lis1)
                                                elif lis1[1]=='Engineering':
                                                        Engineering.append(lis1)
                                                elif lis1[1]=='Finance':
                                                        Finance.append(lis1)
                                                elif lis1[1]=='Human Resources':
                                                        Hr.append(lis1)
                                                elif lis1[1]=='Marketing':
                                                        Marketing.append(lis1)
                                                else:
                                                        Sales.append(lis1)
                                                
                                        #   
                        flattened_it = [val for sublist in it for val in sublist]

                        flattened_accounting = [val for sublist in accounting for val in sublist]

                        flattened_Engineering = [val for sublist in Engineering for val in sublist]

                        flattened_Finance = [val for sublist in Finance for val in sublist]

                        flattened_Hr = [val for sublist in Hr for val in sublist]

                        flattened_Marketing = [val for sublist in Marketing for val in sublist]

                        flattened_Sales = [val for sublist in Sales for val in sublist]



                        sum_it = sum(map(lambda x: int(x), filter(lambda x: str(x).isdigit(), flattened_it)))

                        sum_accounting = sum(map(lambda x: int(x), filter(lambda x: str(x).isdigit(), flattened_accounting)))

                        sum_Engineering = sum(map(lambda x: int(x), filter(lambda x: str(x).isdigit(), flattened_Engineering)))

                        sum_Finance = sum(map(lambda x: int(x), filter(lambda x: str(x).isdigit(), flattened_Finance)))

                        sum_Hr = sum(map(lambda x: int(x), filter(lambda x: str(x).isdigit(), flattened_Hr)))

                        sum_Marketing = sum(map(lambda x: int(x), filter(lambda x: str(x).isdigit(), flattened_Marketing)))

                        sum_Sales = sum(map(lambda x: int(x), filter(lambda x: str(x).isdigit(), flattened_Sales)))
                        print(f'''total payment of IT department is {sum_it} \ntotal payment of Accounting department is {sum_accounting} \ntotal payment of Engineering department is {sum_Engineering} \ntotal payment of Finance department is {sum_Finance} \ntotal payment of HR department is {sum_Hr} \ntotal payment of Marketing department is {sum_Marketing} \ntotal payment of Sales department is {sum_Sales} \n
                        
                        ''')    