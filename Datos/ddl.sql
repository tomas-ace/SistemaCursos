CREATE TABLE Alumno (
    Legajo INT AUTO_INCREMENT,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Fecha_Nac DATE,
    DNI VARCHAR(15) UNIQUE,
    Telefono VARCHAR(20),
    Email VARCHAR(100),
    PRIMARY KEY (Legajo)
);


CREATE TABLE Curso (
    IdCurso INT AUTO_INCREMENT,
    Descripcion VARCHAR(100) NOT NULL,
    Duracion INT,
    PRIMARY KEY (IdCurso)
);
CREATE TABLE Clase (
    IdClase INT AUTO_INCREMENT,
    Anio YEAR,
    Horario TIME,
    Estado VARCHAR(20),
    IdCurso INT NOT NULL,
    PRIMARY KEY (IdClase),
    FOREIGN KEY (IdCurso) REFERENCES Curso(IdCurso)
);

CREATE TABLE Inscripcion (
    IdInscripcion INT AUTO_INCREMENT,
    Fecha_Inscripcion DATE NOT NULL,
    Estado VARCHAR(20),
    Legajo INT NOT NULL,
    IdClase INT NOT NULL,
    PRIMARY KEY (IdInscripcion),
    FOREIGN KEY (Legajo) REFERENCES Alumno(Legajo),
    FOREIGN KEY (IdClase) REFERENCES Clase(IdClase)
);

CREATE TABLE Asistencia (
    Fecha DATE NOT NULL,
    IdInscripcion INT NOT NULL,
    Estado VARCHAR(20),
    PRIMARY KEY (Fecha, IdInscripcion),
    FOREIGN KEY (IdInscripcion) REFERENCES Inscripcion(IdInscripcion)
);


CREATE TABLE Nota (
    IdNota INT AUTO_INCREMENT,
    Fecha DATE NOT NULL,
    Nota DECIMAL(4,2) NOT NULL,
    Descripcion VARCHAR(255),
    IdInscripcion INT NOT NULL,
    PRIMARY KEY (IdNota),
    FOREIGN KEY (IdInscripcion) REFERENCES Inscripcion(IdInscripcion)
);