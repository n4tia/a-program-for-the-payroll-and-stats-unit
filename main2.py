import csv
import lib1
import os
import business_unit
import dep_name
#import palindrome

file_name=os.path.dirname(os.path.abspath(__file__))+"//Employee Sample Data.csv"
my_data=lib1.data_temp_file(file_name)
############

menu = '''
create a menu
1.wage slips
'''
menu2 = '''
create a menu
1. range
2.total pay
'''

get_menu_choice = int(input(menu))
get_menu_choice2=int(input(menu2))

#############
country=[]
years_of_service=[]
for index, row in enumerate(my_data):
            country.append(row[11])
for index, row in enumerate(my_data):
            years_of_service.append(row[8])

country.sort()
years_of_service.sort()


#################

if get_menu_choice==1:
        if get_menu_choice2==1:
                #ask user for starting range
                starting_range=int(input('Please enter starting range for wages:'))
                #ask user for ending range
                ending_range=int(input('Please enter ending range for wages:'))


                data=[]
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
                                #add variables to list
                                lis=[name, wage, dep, city]
                                #compare variable wage to user inputs
                                if starting_range<lis[1] and ending_range>lis[1]:
                                        #add correctvalues to new list
                                        data.append(lis)
                                
                                
                print(data)

                #####

                #ask user if they want to save
                
                option_to_save=input('Do you want to save this information to a file? (Y/N)').upper()

                if option_to_save == 'Y':
                        with open('employees_within_range.txt', 'w+') as newfile:
                                s=''.join(map(str, data))
                                for line in s:

                                        newfile.write(line)
                                        
                                print("File written successfully")
                        newfile.close()
                else:
                        print('')
        
        
        

        if get_menu_choice2==2:

                menu_total_pay='''1 - Display total payment of annual salary for each department \n2 - Display total payment of annual salary for each business unit \n3 - Display employees with palindrome first names \n
                                                '''
                total_pay_userinput=int(input(menu_total_pay))


                ############## 2.1
                if total_pay_userinput==1:
                        dep_name.annual_salary_for_each_department()


                ############## 2.2
                elif total_pay_userinput==2:
                        business_unit.annual_salary_for_each_business_unit()
                        
                ############## 2.3
                elif total_pay_userinput==3:
                        data=[]
                        with open('Employee Sample Data.csv') as csvfile:
                                reader=csv.DictReader(csvfile)
                                for row in reader:
                                        name=row['Full Name'].lower()
                                        data.append(name)
                        separated_names=[words for segments in data for words in segments.split()]
                        first_names=separated_names[::2]
                        palindrome=list(filter(lambda x: (x == "".join(reversed(x))), first_names))
                        print(palindrome)
                        
                        option_to_save=input('Do you want to save this information to a file? (Y/N)').upper()
                
                        if option_to_save == 'Y':
                                with open('employees_with_palindromes.txt', 'w+') as newfile:
                                        s=''.join(map(str, str(palindrome)))
                                        for line in s:
                                                newfile.write(line)
                                        
                                        print("File written successfully")
                                        newfile.close()
                        else:
                                print('')   