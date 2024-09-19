import csv
import random
import read_csv
import code_ram

# ---------------------------- update  Employee------------------------
def update_rows(data):
    id_employee = input('Enter the employee ID: ')
    found_employee = False
    for employee in data:
        if employee['Id'] == id_employee:
            salary = input('Enter the new salary: ')
            employee['Salary'] = salary
            phone = int(input('Digite el telefono:   '))
            employee['Phone'] = phone
            found_employee = True
            break

    if not found_employee:
        print("Employee ID not Found")
        choice = input("Do you want to: \n1.Add New Employee \n2.Continue looking \n3.Exit\n")
        if choice == '1':
            new_employee = add_employee(data)
            data = new_employee
        elif choice == '2':
            data = update_rows(data)
        elif choice == '3':
            exit()
        else:
            print("Invalid Choice")
            data = update_rows(data)

    return data


#----------------------FUNCIÓN QUE CREA REGISTRO DE EMPLEADOS-------------------------------
def add_employee(data):
    name = input('Enter the employee name: ')
    age = int(input('Enter the employee age: '))
    department = input('Enter the employee department \n (Sales/Human Relations/Design/Accounting/Finance/Management: ')
    salary = input('Enter the employee salary: ')
    phone = int(input('Enter the employee phone: '))
    id_employee = code_ram.generar_id_persona(department)
    new_employee = {
        'Id': id_employee,
        'Name': name,
        'Age': age,
        'Department': department,
        'Salary': salary,
        'Phone': phone
        }
    data.append(new_employee)
    print("New employee added successfully.")
    return data

# --------------FUNCION SE ENCARGA DE  ESCRIBIR Y GUARDAR LOS DATOS ACTUALIZADOS Y CREADOS------------'''
def write_csv(data, path):
    fieldnames = data[0].keys()
    with open(path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

if __name__ == '__main__':
    data = read_csv.read_csv('example.csv')
    updated_data = update_rows(data)
    write_csv(updated_data, 'example.csv')