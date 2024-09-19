import read_csv
import add_rows
import charts
import del_rows
from collections import Counter

def utils():
    data = read_csv.read_csv('example.csv')
    updated_data = add_rows.update_rows(data)
    add_rows.write_csv(updated_data, 'example.csv')

# Define funcion para alistar los datos para el gráfico edad vs depto Sales
def datos_filtrados(data):
    sales_data = list(filter(lambda item: item['Department'] == 'Sales', data))
    ages = [int(item['Age']) for item in sales_data]
    age_counts = Counter(ages)
    labels = list(age_counts.keys())
    values = list(age_counts.values())
    return labels, values

# Mediante esta opcion se llama para la generación de gráficos
def option_1(data):
    labels, values = datos_filtrados(data)
    charts.generate_pie_chart(labels, values, "Gráfico de edades por departamento de Ventas")

# Preparación de datos para el segundo gráfico  edad  x departamento
def datos_edad_departamento(data):
    age_department_counts = Counter((int(item['Age']), item['Department']) for item in data)
    departments = list(set(department for _, department in age_department_counts.keys()))
    ages_values = {}
    for department in departments:
        ages_values[department] = [age_department_counts[(age, department)] for age in range(18, 65)]
    return ages_values, departments

# En esta opción se llama  el gráfico de barras
def option_2(data):
    age_values, departments = datos_edad_departamento(data)
    labels = range(18, 65)  # Edades de 18 a 64
    values_per_department = []

    for department in departments:
        values_per_department.append(age_values[department])

    # Generar gráfico de barras usando la función del módulo charts
    charts.generate_bar_chart(labels, values_per_department, departments)

# Opcion que simplemente pregunta si desea continuar o  quiere salir
def back_main():
    while True:
        return_to_menu = input("Presiona 'v' para volver al menú principal o 's' para salir: ")
        if return_to_menu.lower() == 'v':
            break  # Volver al menú principal
        elif return_to_menu.lower() == 's':
            return  #

# Menu principal donde le damos las opciones para solicitar al usuario
def main_menu():
    data = read_csv.read_csv('example.csv')  # Leer los datos una vez
    while True:
        print("\n Menú Principal:  ")
        print("1. Mostrar gráfico edades por depto Ventas")
        print("2. Mostrar gráfico edad vs departments")
        print("3. Mostrar registros")
        print("4. Actualizar o crear registros empleados")
        print("5. Eliminar registro empleado")
        print("6. Salir")

        choice = input("Elige una opción (1-6): ")

        if choice == '1':
            option_1(data)
        elif choice == '2':
            option_2(data)
        elif choice == '3':
            read_csv.print_data(data)
            back_main()
        elif choice == '4':
            data = add_rows.update_rows(data)  # Actualizar datos
            add_rows.write_csv(data, 'example.csv')
        elif choice == '5':
            data = del_rows.eliminar_registro(data)
        elif choice == '6':
            print("----------GRACIAS POR ELEGIRNOS RECUERDE GUARDE CAMBIOS---------------")
            exit()
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main_menu()