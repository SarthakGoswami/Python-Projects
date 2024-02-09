import mysql.connector

con = mysql.connector.connect(host='localhost',user='root',password='123456789',database='empd')

# function to check if employee with given id exists or not
def check_employee(employee_id):
     
    #  query to select all rows from employee table
    sql = 'select * from empd where Id=%s'

    # making curson buffered to make rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_id,)

    # executing the sql query
    c.execute(sql,data)

    # rowcount method to find number of rows wth given values
    r = c.rowcount

    if r==1:
        return True
    else:
        return False


# function to add employee
def add_employee():
    Id = input('Enter Employee id: ')

    # checking if employee with given id already exists or not
    if (check_employee(Id)==True):
        print('Employee already exist! \n Try Again!! \n')
        menu()
    
    else:
        Name = input('Enter Employee Name: ')
        Post = input('Enter Employee Post: ')
        Salary = input('Enter Employee Salary: ')
        data = (id,Name,Post,Salary)

        # inserting employee details in the employee table
        sql = 'insert into empd values(%s,%s,%s,%s)'
        c = con.cursor()

        # executing the sql query
        c.execute(sql,data)

        # commit() method to make changes in the table
        con.commit()
        print('Employee Added Successfully')
        menu()


# function to remove employee with given id
def remove_employee():
    Id = input('Enter Employee id: ')

    # checking if employee with given id exist or not
    if(check_employee(Id)==False):
        print("Employee does not exist! \n Try Again!! \n")
        menu()
    
    else:
        # query to delete employee from table
        sql = 'delete from empd where Id=%s'
        data = (Id,)
        c = con.cursor()

        # executing the sql query
        c.execute(sql,data)

        # commit() method to make changes in the table
        con.commit()
        print('Employee Removed')
        menu()


# function to promote employee
def promote_employee():
    Id = input('Enter Employee id: ')

    # checking if employee with given id ecists or not
    if (check_employee(Id)==False):
        print('Employee does not exist! \n Try Again!! \n')
        menu()
    else:
        Amount = int(input('Enter increase in salary: '))

        # query to fetch salary of employee with given id
        sql = 'select Salary from empd where Id=%s'
        data = (Id,)
        c = con.cursor()

        # executing the sql query
        c.execute(sql,data)
        
        # fetching salary of employee with given id
        r = c.fetchone()
        t = r[0] + Amount

        # query to update salary of employee with given id
        sql = 'update empd set Salary=%s where Id=%s'
        d = (t,Id)

        # executing the sql query
        c.execute(sql,d)

        # commit() method to make changes in the table
        con.commit()
        print('Employee Promoted')
        menu()


# function to display all employees from employee table
def display_employees():
    # query to select all rows from employee table
    sql = 'select * from empd'
    c = con.cursor()

    # executing sql query
    c.execute(sql)

    # fetching all details of all the employee
    r = c.fetchall()
    for i in r:
        print('Employee Id: ', i[0])
        print('Employee Name: ', i[1])
        print('Employee Post: ', i[2])
        print('Employee Salary: ', i[3])
        print('-----------------------------\
        -------------------------------------\
        -----------------------------------')
    menu()


# menu function to display the menu
def menu():
    print('Welcome to Employee Management Record')
    print('Press ')
    print('1 to Add Employee')
    print('2 to Remove Employee')
    print('3 to Promote Employee')
    print('4 to Display Employees')
    print('5 to Exit')

    # taking choice from user
    ch = int(input('Enter Your Choice: '))
    if ch == 1:
        add_employee()
    elif ch == 2:
        remove_employee()
    elif ch == 3:
        promote_employee()
    elif ch == 4:
        display_employees()
    elif ch == 5:
        exit(0)
    else:
        print('Invalid Choice')
        menu()

menu()