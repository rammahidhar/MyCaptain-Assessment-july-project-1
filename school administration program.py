#school admistration project

import csv

def write_into_csv(info_list):
    with open('student_info.csv','a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() == 0: 
            writer.writerow(["name", "age", "contact number", "email ID"])
            
            write.writrow(info_list)

if __name__ == '__main__':            
    condition = True
    student_num = 1

    while(condition):
       student_info = input("enter student information for student #{} following format(name age contact_number email_ID): ").format(student_num)
    
    
    #split
    student_info_list = student_info.split(' ')
    
    
    print("\nThe entered information is -\nName: {}\nAge: {}\nContact_number: {}\nE-mail ID: {}"
            .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
    
   choice_check = input("is the information correct? (yes/no): ")
    
   if choice check == "yes":
     write_into_csv(student_info_list)
    
    condition_check = input("enter (yes/no) if you want to enter information for another students: ")
    if condition_check == "yes":
        condition = True
        student_num =student_num + 1
    elif condition_check == "no":    
        condition = false
    
    elif choice_check == "no"
        print("\nPlease re-enter the values!")    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            