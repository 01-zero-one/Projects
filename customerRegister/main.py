import sys
import pandas as pd

customer_info = []

def Menu_Control():
    menu = '''
    1. Add customer
    2. View all customers
    3. Search customer
    4. Exit
    '''

    while True:
        print(menu)
        try:
            ans = input('Please Enter A Number From 1 TO 4: ')
            if ans == '1':
                # Logic for adding a customer
                print("Adding Customer")
                add_Info()
                print("Customer has been Added To Database")
            elif ans == '2':
                # Logic for viewing customers
                print("Viewing all customers...")
                allCustomerInfo()
            elif ans == '3':
                # Logic for searching a customer
                print('''
                Searching For Customer
                Please Enter Name Or Email To Identify Customer
                ''')
                customerSearch()
            elif ans == '4':
                print("Goodbye!")
                sys.exit()
            else:
                print("❗ Please enter a number between 1 and 4.")
        except ValueError:
            print("⚠️ Information entered is not valid. Please enter a number.")


def add_Info():
    cus_name = input('Enter name of the customer: ')
    cus_email = input('Enter email of the customer: ')
    cus_phone = input('Enter phone number of the customer: ')

    info = dict(name=cus_name, email=cus_email, phone=cus_phone)
    customer_info.append(info)

    df = pd.DataFrame(customer_info)
    df.to_excel('HospitalManagementData.xlsx', index=False)

def allCustomerInfo():
    df = pd.read_excel('HospitalManagementData.xlsx')
    print(df)

def customerSearch():
    cus_name = input('Enter name of the customer: ')
    cus_email = input('Enter email of the customer: ')

    df = pd.read_excel('HospitalManagementData.xlsx')

    if cus_name or cus_email:
        if cus_name != '':
            print(df[df['name'] == cus_name])
        elif cus_email != '':
            print(df[['email'] == cus_email])
    else:
        print('Please Enter Appropriate Information')

if __name__ == "__main__":
    Menu_Control()