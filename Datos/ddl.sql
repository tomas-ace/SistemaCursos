CREATE TABLE Alumno (
    Legajo INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT NOT NULL,
    Apellido TEXT NOT NULL,
    Fecha_Nac TEXT,
    DNI TEXT UNIQUE,
    Telefono TEXT,
    Email TEXT
);

CREATE TABLE Curso (
    IdCurso INTEGER PRIMARY KEY AUTOINCREMENT,
    Descripcion TEXT NOT NULL,
    Duracion INTEGER
);

CREATE TABLE Clase (
    IdClase INTEGER PRIMARY KEY AUTOINCREMENT,
    Anio INTEGER,      -- SQLite no tiene YEAR, usamos INTEGER
    Turno TEXT,      -- SQLite no tiene TIME, usamos TEXT (HH:MM:SS)
    Estado TEXT,
    IdCurso INTEGER NOT NULL,
    FOREIGN KEY (IdCurso) REFERENCES Curso(IdCurso)
);

CREATE TABLE Inscripcion (
    IdInscripcion INTEGER PRIMARY KEY AUTOINCREMENT,
    Fecha_Inscripcion TEXT NOT NULL,
    Estado TEXT,
    Legajo INTEGER NOT NULL,
    IdClase INTEGER NOT NULL,
    FOREIGN KEY (Legajo) REFERENCES Alumno(Legajo),
    FOREIGN KEY (IdClase) REFERENCES Clase(IdClase)
);

CREATE TABLE Asistencia (
    Fecha TEXT NOT NULL,
    IdInscripcion INTEGER NOT NULL,
    Estado TEXT,
    PRIMARY KEY (Fecha, IdInscripcion),
    FOREIGN KEY (IdInscripcion) REFERENCES Inscripcion(IdInscripcion)
);

CREATE TABLE Nota (
    IdNota INTEGER PRIMARY KEY AUTOINCREMENT,
    Fecha TEXT NOT NULL,
    Nota REAL NOT NULL, -- SQLite usa REAL para números con decimales
    Descripcion TEXT,
    IdInscripcion INTEGER NOT NULL,
    FOREIGN KEY (IdInscripcion) REFERENCES Inscripcion(IdInscripcion)
);
