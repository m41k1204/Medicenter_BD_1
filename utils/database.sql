-- Creación de tablas

CREATE TABLE IF NOT EXISTS persona (
    dni VARCHAR(8),
    nombre VARCHAR(25),
    apellido VARCHAR(25),
    fecha_de_nacimiento DATE
);

CREATE TABLE IF NOT EXISTS gerente (
    pdni VARCHAR(8),
    sueldo DOUBLE PRECISION

);

CREATE TABLE IF NOT EXISTS secretaria (
	pdni VARCHAR(8),
    sueldo DOUBLE PRECISION
);

CREATE TABLE IF NOT EXISTS enfermera (
    pdni VARCHAR(8),
    sueldo DOUBLE PRECISION
);

CREATE TABLE IF NOT EXISTS interno (
    pdni VARCHAR(8),
    sueldo DOUBLE PRECISION
);

CREATE TABLE IF NOT EXISTS doctor (
    pdni VARCHAR(8),
    sueldo DOUBLE PRECISION,
    especialidad VARCHAR(40)
);

CREATE TABLE IF NOT EXISTS paciente (
	pdni VARCHAR(12)
);

CREATE TABLE IF NOT EXISTS pedido (
    codigo VARCHAR(10),
    gdni VARCHAR(8),
    fecha_pedido DATE
);

CREATE TABLE IF NOT EXISTS insumo_medico (
    nro_serial VARCHAR(10),
    material VARCHAR(50),
    marca VARCHAR(40),
    costo_por_unidad DOUBLE PRECISION,
    nombre VARCHAR(50),
    cantidad INTEGER
);

CREATE TABLE IF NOT EXISTS detallePedido (
    im_ns VARCHAR(10),
    pcodigo VARCHAR(10),
    cantidad INTEGER
);

CREATE TABLE IF NOT EXISTS actividad_economica (
    padni VARCHAR(8),
    ddni VARCHAR(8),
    idni VARCHAR(8),
    codigo VARCHAR(10),
    descripcion VARCHAR(500),
    fecha_ae DATE,
    horaInicio TIME,
    monto DOUBLE PRECISION
);

CREATE TABLE IF NOT EXISTS consulta (
    aecodigo VARCHAR(10),
    duracion INTEGER,
    snrodoc VARCHAR(12)
);

CREATE TABLE IF NOT EXISTS operacion (
    aecodigo VARCHAR(10),
    edni VARCHAR(8),
    tipo_operacion VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS utiliza (
    ocodigo VARCHAR(10),
    im_ns VARCHAR(10),
    cantidad INTEGER,
    edni VARCHAR(8)
);

CREATE TABLE IF NOT EXISTS pago (
    codigo VARCHAR(10),
    aecodigo VARCHAR(10),
    monto DOUBLE PRECISION,
    tipo_de_pago VARCHAR(25),
    fecha_pago DATE
);

-- Key constraints

-- Persona
ALTER TABLE persona ADD CONSTRAINT pk_persona_dni PRIMARY KEY (dni);

-- Gerente
ALTER TABLE gerente ADD CONSTRAINT pk_gerente_dni PRIMARY KEY (pdni);
ALTER TABLE gerente ADD CONSTRAINT fk_gerente_persona_dni 
	FOREIGN KEY (pdni) REFERENCES persona(dni);

-- Paciente
ALTER TABLE paciente ADD CONSTRAINT pk_paciente_dni PRIMARY KEY (pdni);
ALTER TABLE paciente ADD CONSTRAINT fk_paciente_persona_nrodoc 
	FOREIGN KEY (pdni) REFERENCES persona(dni);

-- Enfermera 
ALTER TABLE enfermera ADD CONSTRAINT pk_enfermera_pdni PRIMARY KEY (pdni);
ALTER TABLE enfermera ADD CONSTRAINT fk_enfermera_persona_nrodoc 
	FOREIGN KEY (pdni) REFERENCES persona(dni);
	
-- Interno 
ALTER TABLE interno ADD CONSTRAINT pk_interno_pdni PRIMARY KEY (pdni);
ALTER TABLE interno ADD CONSTRAINT fk_interno_persona_nrodoc 
	FOREIGN KEY (pdni) REFERENCES persona(dni); 

-- Doctor
ALTER TABLE doctor ADD CONSTRAINT pk_doctor_pdni PRIMARY KEY (pdni);
ALTER TABLE doctor ADD CONSTRAINT fk_doctor_persona_nrodoc 
	FOREIGN KEY (pdni) REFERENCES persona(dni);
	
-- Secretaria
ALTER TABLE secretaria ADD CONSTRAINT pk_secretaria_nrodoc PRIMARY KEY (pdni);
ALTER TABLE secretaria ADD CONSTRAINT fk_secretaria_persona_pdni
	FOREIGN KEY (pdni) REFERENCES persona(dni);

-- Pedido
ALTER TABLE pedido ADD CONSTRAINT pk_pedido_codigo PRIMARY KEY (codigo);
ALTER TABLE pedido ADD CONSTRAINT fk_pedido_gerente_gdni 
	FOREIGN KEY (gdni) REFERENCES gerente(pdni);

-- Insumo médico
ALTER TABLE insumo_medico ADD CONSTRAINT pk_insumomedico_ns PRIMARY KEY (nro_serial); 

-- detalle Pedido
ALTER TABLE detallePedido ADD CONSTRAINT pk_detallePedido_nroserial PRIMARY KEY (im_ns);
ALTER TABLE detallePedido ADD CONSTRAINT fk_detallePedido_insumomedico_nroserial
	FOREIGN KEY (im_ns) REFERENCES insumo_medico(nro_serial);
ALTER TABLE detallePedido ADD CONSTRAINT fk_detallePedido_pedido_codigo 
	FOREIGN KEY (pcodigo) REFERENCES pedido(codigo);

-- actividad_economica
ALTER TABLE actividad_economica ADD CONSTRAINT pk_actividadEconomica_codigo PRIMARY KEY (codigo);
ALTER TABLE actividad_economica ADD CONSTRAINT fk_actividadEconomica_paciente_nrodocumento 
	FOREIGN KEY (padni) REFERENCES paciente(pdni);
ALTER TABLE actividad_economica ADD CONSTRAINT fk_actividadEconomica_doctor_nrodocumento 
	FOREIGN KEY (ddni) REFERENCES doctor(pdni);
ALTER TABLE actividad_economica ADD CONSTRAINT fk_actividadEconomica_interno_nrodocumento 
	FOREIGN KEY (idni) REFERENCES interno(pdni);

-- consulta
ALTER TABLE consulta ADD CONSTRAINT fk_consulta_actividadEconomica 
	FOREIGN KEY (aecodigo) 
REFERENCES actividad_economica(codigo);
ALTER TABLE consulta ADD CONSTRAINT pk_consulta_aecodigo 
	PRIMARY KEY (aecodigo);

-- operacion
ALTER TABLE operacion ADD CONSTRAINT fk_operacion_actividadEconomica 
	FOREIGN KEY (aecodigo) REFERENCES actividad_economica(codigo);
ALTER TABLE operacion ADD CONSTRAINT fk_operacion_enfermera_edni
	FOREIGN KEY (edni) REFERENCES enfermera(pdni);
ALTER TABLE operacion ADD CONSTRAINT pk_operacion_actividadEconomica_codigo 
	PRIMARY KEY (aecodigo);

-- utiliza
ALTER TABLE utiliza ADD CONSTRAINT fk_utiliza_operacion
	FOREIGN KEY (ocodigo) REFERENCES operacion(aecodigo);
ALTER TABLE utiliza ADD CONSTRAINT fk_utiliza_enfermera_edni
	FOREIGN KEY (edni) REFERENCES enfermera(pdni);
ALTER TABLE utiliza ADD CONSTRAINT fk_utiliza_insumoMedico_nroserial
	FOREIGN KEY (im_ns) REFERENCES insumo_medico(nro_serial);
ALTER TABLE utiliza ADD CONSTRAINT pk_utiliza_ocodigo_edni_imns
	PRIMARY KEY (ocodigo, edni, im_ns);
	
-- pago
ALTER TABLE pago ADD CONSTRAINT fk_pago_actividadEconomica
	FOREIGN KEY (aecodigo) REFERENCES actividad_economica(codigo);
ALTER TABLE pago ADD CONSTRAINT pk_pago_codigo
	PRIMARY KEY (codigo);
 
-- Unique Constraints

ALTER TABLE actividad_economica ADD CONSTRAINT uniqe_fechaae_horainicio
UNIQUE (fecha_ae, horainicio)
