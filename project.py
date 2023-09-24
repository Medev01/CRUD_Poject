import database


PROMPT = """
Hi there what do you want to do : 
    1) add a student 
    2) add many students 
    3) see the all students 
    4) see the first Note 
    5) see the first Three Students 
    6) lock up for student by his name 
    7) exit 

Your selection : 
"""

def main():

    connection = database.con
    database.create_tables(connection)

    while (user_input := input(PROMPT)) != "7":

        if user_input == "1":
            name = input("ENTER STUDENT NAME : ")     
            mail = input("ENTER STUDENT MAIL : ")
            note = float(input('ENTER STUDENT NOTE : '))
            database.ADD_student(connection,name, mail, note)

        elif user_input == "2":
            data =  get_list_of_infos()
            database.add_many_stds(connection, data)

        elif user_input == "3": 
            students = database.see_all_students(connection)
            for student in students:
                print(student, end='\n')   

        elif user_input == "4":
            database.First_note(connection)

        elif user_input == "5":
            first_three_std = database.the_first_three(connection)
            for item in first_three_std:
                print(item, end='\n')

        elif user_input == "6": 
            name = input('ENTER STUDENT NAME  : ')
            database.lock_up_std_by_name(connection, name)

        elif user_input == "7":
            break

        else:
            print('invalid input, try again')



def get_list_of_infos():
    data = []
    tup = tuple()
    cnt = 0
    num = int(input('how many students do you want to add: '))
    while True :
        name = input("ENTER STUDENT NAME : ")     
        mail = input("ENTER STUDENT MAIL : ")     
        note = float(input('ENTER STUDENT NOTE : '))
        tup += (name,mail,note)
        data.append(tup)
        cnt += 1
        if num == cnt:
            break

    return data

main()



    
        


