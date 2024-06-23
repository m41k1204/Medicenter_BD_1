import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Function to generate a random date
def random_date(start, end):
    return start + timedelta(days=random.randint(0, int((end - start).days)))

# Generate data for 1000 rows
data = []
for _ in range(1000):
    nrodocumento = fake.unique.random_number(digits=12)
    tipodocumento = fake.random_element(elements=('DNI', 'Passport', 'ID Card'))
    nombre = fake.first_name()
    apellido = fake.last_name()
    fecha_de_nacimiento = fake.date_of_birth(minimum_age=18, maximum_age=90)
    
    # Generate some random salaries
    sueldo = round(random.uniform(30000, 150000), 2)
    
    # Specialization for doctors
    especialidad = fake.random_element(elements=('Cardiology', 'Neurology', 'Pediatrics', 'General'))

    # Random dates for orders
    fecha_pedido = fake.date_this_year()

    # Generate other random data
    codigo = fake.unique.random_number(digits=10)
    material = fake.word()
    marca = fake.company()
    costo_por_unidad = round(random.uniform(10, 1000), 2)
    nombre_insumo = fake.word()
    cantidad = random.randint(1, 100)

    # Activity economic data
    descripcion = fake.text(max_nb_chars=200)
    fecha_ae = fake.date_this_year()
    horaInicio = fake.time()

    # Random values for operations and payments
    tipo_operacion = fake.word()
    monto = round(random.uniform(100, 5000), 2)
    tipo_de_pago = fake.random_element(elements=('Credit Card', 'Cash', 'Debit Card', 'Insurance'))
    fecha_pago = fake.date_this_year()

    # Append data to the list
    data.append({
        'nrodocumento': nrodocumento,
        'tipodocumento': tipodocumento,
        'nombre': nombre,
        'apellido': apellido,
        'fecha_de_nacimiento': fecha_de_nacimiento,
        'sueldo': sueldo,
        'especialidad': especialidad,
        'codigo': codigo,
        'fecha_pedido': fecha_pedido,
        'material': material,
        'marca': marca,
        'costo_por_unidad': costo_por_unidad,
        'nombre_insumo': nombre_insumo,
        'cantidad': cantidad,
        'descripcion': descripcion,
        'fecha_ae': fecha_ae,
        'horaInicio': horaInicio,
        'tipo_operacion': tipo_operacion,
        'monto': monto,
        'tipo_de_pago': tipo_de_pago,
        'fecha_pago': fecha_pago
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv('database_population.csv', index=False)

print("CSV file 'database_population.csv' created successfully.")


