
def eliminar_registro(data):
	employee_id = input("Digite el ID del empleado que desea eliminar: ")

	# Buscar el empleado por ID
	employee = next((item for item in data if item['Id'] == employee_id), None)

	if employee:
		print("Datos del empleado encontrado:")
		print(employee)

		confirm = input("¿Desea eliminar este registro? (s/n): ")
		if confirm.lower() == 's':
			data.remove(employee)  # Eliminar el empleado de la lista
			print("Registro eliminado.")
		else:
			print("Operación cancelada.")
	else:
		print("Empleado no encontrado.")