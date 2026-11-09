Sistema de Gestión Académica para Cursos
Tomas Acevedo
Aplicación de escritorio desarrollada en Python con Tkinter y SQLite para administrar la actividad académica de una institución que dicta cursos.

El sistema centraliza los datos de alumnos, cursos, clases e inscripciones, y permite registrar y consultar notas y asistencias.
Tecnologías
- Python
- Tkinter para la interfaz gráfica.
- SQLite para almacenar la información.


Funcionalidades
Alumnos
- Registrar alumnos.
- Consultar el listado de alumnos.
- Modificar sus datos personales.
- Consultar el historial de cursadas.
- Consultar notas y asistencias de cada inscripción.
- Inscribir a un alumno en una clase.
- Dar de baja una inscripción.
Cursos y clases
- Registrar y consultar cursos.
- Modificar los datos de un curso.
- Crear clases asociadas a un curso, indicando año y turno.
- Consultar las clases mediante filtros por curso y estado.
- Consultar los alumnos de una clase y filtrar por estado.
- Cerrar una clase y calcular el resultado final de las inscripciones que continúan En Curso.
Notas
- Registrar notas para los alumnos de una clase.
- Consultar las notas registradas.
- Modificar una nota mientras la clase está activa.
- Calcular el promedio de cada inscripción.
Asistencias
- Tomar lista para una clase.
- Consultar y corregir asistencias mientras la clase está activa.
- Calcular el porcentaje de asistencia de cada inscripción.
- Cambiar automáticamente a Libre cuando las inasistencias superan el límite establecido.
- Registrar automáticamente como Ausente a los alumnos que ya están en estado Libre o Baja al tomar una nueva lista.
Panel principal
Muestra un resumen con la cantidad de alumnos, cursos, inscripciones activas y clases activas.


Estructura del proyecto
SistemaCursos/
├── Datos/
│   ├── cursos_db.db
│   ├── ddl.sql
│   └── *_dao.py
├── Dominio/
│   └── modelos del sistema
├── Presentacion/
│   └── ventanas y componentes Tkinter
├── Servicios/
│   └── validaciones y reglas de negocio
├── ventana_principal.py
└── README.md
La aplicación está organizada en capas:
- Presentación: ventanas, formularios, tablas y controles de Tkinter.
- Servicios: validaciones y reglas de negocio.
- Datos: consultas SQL y acceso a SQLite.
- Dominio: clases que representan las entidades del sistema.
Requisitos
- Python 3 instalado.
- Tkinter disponible en la instalación de Python.
- No requiere conexión a Internet.
