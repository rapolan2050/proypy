import matplotlib.pyplot as plt

def generate_bar_chart(labels, values, departments):
    fig, ax = plt.subplots()
    for i, department in enumerate(departments):
        ax.bar(labels, values[i], label=department)
    plt.title('Distribución de Edades por Departamento')
    plt.xlabel('Edad')
    plt.ylabel('Número de Empleados')
    plt.legend()
    plt.show()


def generate_pie_chart(labels, values, title):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct="%0.1f %%")
    ax.axis('equal')
    ax.set_title(title)
    plt.show()
