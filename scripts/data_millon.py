import pandas as pd
from faker import Faker
import random

fake = Faker()

personas = []
unique_documents = set()

# Creacion de personas --------------------------------------------------------

for i in range(6000):
    while True:
        nrodocumento = fake.unique.random_number(digits=8)
        if nrodocumento not in unique_documents:
            unique_documents.add(nrodocumento)
            break
    nombre = fake.first_name()
    apellido = fake.last_name()
    fecha_de_nacimiento = fake.date_of_birth(minimum_age=30, maximum_age=60)
    personas.append({
        'dni': nrodocumento,
        'nombre': nombre,
        'apellido': apellido,
        'fecha_de_nacimiento': fecha_de_nacimiento
    })

df = pd.DataFrame(personas)
df.to_csv('personas_mil.csv', index=False)
print('personas creadas')


# Creacion de doctor --------------------------------------------------------

doctores = []
especialidades = [
    'Cardiología','Dermatología','Endocrinología',
    'Gastroenterología','Geriatría','Hematología',
    'Inmunología','Infectología','Medicina Interna',
    'Nefrología','Neumología','Neurología',
    'Obstetricia y Ginecología','Oncología','Oftalmología',
    'Otorrinolaringología','Pediatría','Psiquiatría',
    'Radiología','Reumatología','Urología',
    'Cirugía General','Cirugía Cardiovascular','Cirugía Plástica',
    'Cirugía Torácica','Cirugía Vascular','Medicina de Emergencias',
    'Medicina Física y Rehabilitación','Medicina del Deporte','Medicina del Trabajo'
]


for i in range(1000):

    sueldo = round(random.uniform(30000, 300000), 2)
    especialidad = random.choice(especialidades)

    doctores.append({
        'pdni': personas[i]['dni'],
        'sueldo': sueldo,
        'especialidad': especialidad
    })

df = pd.DataFrame(doctores)
df.to_csv('doctor_mil.csv', index=False)
print('doctor exitoso')

# Creacion de interno -------------------------------------------------------

internos = []

for i in range(1000,2000):
    sueldo = round(random.uniform(1025, 3000), 2)

    internos.append({
        'pdni': personas[i]['dni'],
        'sueldo': sueldo
    })

df = pd.DataFrame(internos)
df.to_csv('internos_mil.csv', index=False)
print('internos exitoso')

# Creacion de enfermera -----------------------------------------------------

enfermeras = []

for i in range(2000, 3000):
    sueldo = round(random.uniform(3000, 6000), 2)

    enfermeras.append({
        'pdni': personas[i]['dni'],
        'sueldo': sueldo
    })

df = pd.DataFrame(enfermeras)
df.to_csv('enfermeras_mil.csv', index=False)
print('enfermeras exitoso')

# Creacion de secretaria ----------------------------------------------------

secretarias = []

for i in range(3000, 4000):

    sueldo = round(random.uniform(2000, 5000), 2)

    secretarias.append({
        'pdni': personas[i]['dni'],
        'sueldo': sueldo
    })

df = pd.DataFrame(secretarias)
df.to_csv('secretarias_mil.csv', index=False)
print('secretarias exitoso')

# Creacion de gerente ------------------------------------------------------

gerentes = []

for i in range(4000, 5000):

    sueldo = round(random.uniform(15000, 30000), 2)

    gerentes.append({
        'pdni': personas[i]['dni'],
        'sueldo': sueldo,
    })

df = pd.DataFrame(gerentes)
df.to_csv('gerentes_mil.csv', index=False)
print('gerentes exitoso')


# Creacion de paciente -----------------------------------------------------

pacientes = []

for i in range(5000, 6000):
    nrodocumento = personas[i]['dni']

    pacientes.append({
        'pdni': nrodocumento
    })

df = pd.DataFrame(pacientes)
df.to_csv('pacientes_mil.csv', index=False)
print('pacientes exitoso')


# Creacion de insumos medicos
insumos_medicos = []
insumos_codigos = set()

for i in range(1000):
    while True:
        codigo = fake.unique.random_number(digits=10)
        if codigo not in insumos_codigos:
            insumos_codigos.add(codigo)
            break
    material = fake.word()
    marca = fake.company()
    costo_por_unidad = round(random.uniform(10, 100), 2)
    nombre_insumo = fake.word()
    cantidad = random.randint(1, 100)

    insumos_medicos.append({
        'nro_serial': codigo,
        'material': material,
        'marca': marca,
        'costo_por_unidad': costo_por_unidad,
        'nombre': nombre_insumo,
        'cantidad': cantidad
    })

df = pd.DataFrame(insumos_medicos)
df.to_csv('insumos_medicos_mil.csv', index=False)
print('insumos_medicos exitoso')

# Creacion de Pedido
pedidos = []

for i in range(1000):
    while True:
        codigo = fake.unique.random_number(digits=10)
        if codigo not in insumos_codigos:  # ensure unique order codes
            insumos_codigos.add(codigo)
            break
    fecha_pedido = fake.date_this_year()
    nrodocumento = random.choice(gerentes)['pdni']

    pedidos.append({
        'codigo': codigo,
        'gdni': nrodocumento,
        'fecha_pedido': fecha_pedido
    })

df = pd.DataFrame(pedidos)
df.to_csv('pedidos_mil.csv', index=False)
print('pedido exitoso')

# Creacion de detallePedido
detallePedido = []
insumos_utilizados = set()

def escogerPedido():
    return random.choice(pedidos)['codigo']

def escogerInsumoMedico():
    while True:
        insumoMedico = random.choice(insumos_medicos)
        if insumoMedico['nro_serial'] not in insumos_utilizados:
            insumos_utilizados.add(insumoMedico['nro_serial'])
            return insumoMedico['nro_serial']

for i in range(1000):
    pcodigo = escogerPedido()
    insumoMedico = escogerInsumoMedico()
    cantidad = random.randint(1, 100)

    detallePedido.append({
        'im_ns': insumoMedico,
        'pcodigo': pcodigo,
        'cantidad': cantidad
    })

df = pd.DataFrame(detallePedido)
df.to_csv('detallePedido_mil.csv', index=False)
print('detallePedido exitoso')

# Creacion de actividad_economica ----------------------------

actividad_economica = []
used_codigos = set()
used_fecha_hora = {}

for i in range(2000):
    while True:
        codigo = fake.unique.random_number(digits=10)
        if codigo not in used_codigos:
            used_codigos.add(codigo)
            break

    pnrodoc = random.choice(pacientes)['pdni']
    dnrodoc = random.choice(doctores)['pdni']
    inrodoc = random.choice(internos)['pdni']
    descripcion = ''

    while True:
        fecha_ae = fake.date_this_year()
        horaInicio = fake.time()
        if fecha_ae not in used_fecha_hora:
            used_fecha_hora[fecha_ae] = {horaInicio}
            break
        elif horaInicio not in used_fecha_hora[fecha_ae]:
            used_fecha_hora[fecha_ae].add(horaInicio)
            break
    monto = round(random.uniform(10000, 40000), 2)


    actividad_economica.append({
        'pdni': pnrodoc,
        'ddni': dnrodoc,
        'idni': inrodoc,
        'codigo': codigo,
        'descripcion': descripcion,
        'fecha_ae': fecha_ae,
        'horainicio': horaInicio,
        'monto':monto
    })

df = pd.DataFrame(actividad_economica)
df.to_csv('actividad_economica_mil.csv', index=False)
print('actividad_economica exitoso')

# Creacion de operacion -----------------------------------

operaciones = []

for i in range(1000):
    aecodigo = actividad_economica[i]['codigo']
    enrodoc = random.choice(enfermeras)['pdni']
    tipo_operacion = fake.word()

    operaciones.append({
        'aecodigo':aecodigo,
        "edni":enrodoc,
        "tipo_operacion":tipo_operacion
    })


df = pd.DataFrame(operaciones)
df.to_csv('operaciones_mil.csv', index=False)
print('operacion exitoso')

# Creacion de consulta

consulta = []

for i in range(1000,2000):
    aecodigo = actividad_economica[i]['codigo']
    n = i-1000
    snrodoc = secretarias[n]['pdni']
    tipo_operacion = fake.word()

    consulta.append({
        'aecodigo':aecodigo,
        "sdni":snrodoc,
        "duracion":30
    })


df = pd.DataFrame(consulta)
df.to_csv('consulta_mil.csv', index=False)
print('consulta exitoso')

# Creacion de utiliza 

utiliza = []
used_combinations = set()

for i in range(5000):
    
    while True:
        enrodoc = random.choice(enfermeras)['pdni']
        ocodigo = random.choice(operaciones)['aecodigo']
        im_ns = random.choice(insumos_medicos)['nro_serial']
        combination = (ocodigo, im_ns, enrodoc)
        
        if combination not in used_combinations:
            used_combinations.add(combination)
            break

    cantidad = random.randint(1, 15)

    utiliza.append({
        'ocodigo': ocodigo,
        'im_ns': im_ns,
        'cantidad': cantidad,
        'edni': enrodoc,
    })

df = pd.DataFrame(utiliza)
df.to_csv('utiliza_mil.csv', index=False)
print('utiliza exitoso')

# Creacion de pago

pago = []
used_codigos = set()

for i in range(2000):
    aecodigo = actividad_economica[i]['codigo']
    while True:
        codigo = fake.unique.random_number(digits=10)
        if codigo not in used_codigos:
            used_codigos.add(codigo)
            break
    monto = actividad_economica[i]['monto']
    tipo_de_pago = fake.random_element(elements=('Tarjeta de Credito', 'Tarjeta de Debito', 
                                                  'Seguro', 'Efectivo'))
    fecha_pago = fake.date_this_year() 

    pago.append({
        'codigo': codigo,
        'aecodigo': aecodigo,
        'monto': monto,
        'tipo_de_pago': tipo_de_pago,
        'fecha_de_pago': fecha_pago
    })

df = pd.DataFrame(pago)
df.to_csv('pago_mil.csv', index=False)
print('pago exitoso')
