const db = require("aa-sqlite");

// La creación de todas las bases de datos (si no existen) se hace en una misma función.

async function crearDBProductora() {
  await db.open("./.data/productora.db");

  // Creacion de la tabla "estudios" en la base de datos

  let existe = false;
  let res = await db.get(
    "SELECT count(*) as contar FROM sqlite_schema WHERE type = 'table' AND name='estudios'"
  );

  if (res.contar > 0) {
    existe = true;
  }

  if (existe === false) {
    await db.run(`
                    CREATE TABLE estudios
        (
                        IdEstudio INTEGER PRIMARY KEY AUTOINCREMENT,
                        Nombre text NOT NULL UNIQUE,
                        FechaFundacion date,
                        Presupuesto integer
                    );
                `);
    console.log("- Tabla estudios creada!");

    await db.run(`
                    INSERT into estudios values 
                    (1, 'Shondaland', '2005-03-27', 234567233),
                    (2, 'Telefe ', '1989-10-20', 5554449002),
                    (3, 'Television 360', '2011-08-18', 345739744),
                    (4, 'Sony Pictures Television', '2002-09-16', 230896544),
                    (5, 'Marvel Studios', '1993-12-07', 943584834),
                    (6, ' Warner Bros', '1923-04-04', 9568439474),
                    (7, 'Paramount Pictures', '1912-08-05', 943583475),
                    (8, 'Original Film One Race Films', '1967-07-18', 983457348),
                    (9, 'Touchstone Pictures', '1984-02-15', 456545765),
                    (10, 'Big Bang Media', '2010-12-26', 9943452323);
                `);
  }

  // // Creacion de la tabla "directores" en la base de datos

  existe = false;
  let sql =
    "SELECT count(*) as contar FROM sqlite_schema WHERE type = 'table' and name = 'directores'";
  res = await db.get(sql, []);
  if (res.contar > 0) existe = true;
  if (!existe) {
    await db.run(
      `CREATE table directores( 
                            IdDirector INTEGER PRIMARY KEY AUTOINCREMENT 
                            , Nombre text NOT NULL 
                            , Apellido text NOT NULL 
                            , FechaNacimiento date 
                            , Nacionalidad text
                            );`
    );
    console.log("- Tabla directores creada!");

    // Agregamos TODOS los datos

    await db.run(
      `insert into directores values
                    (1,'Juan Antonio','Bayona','1975-05-09','España'),
                    (2,'Christopher','Nolan','1970-07-30','Reino Unido'),
                    (3,'Clint','Eastwood','1930-05-31','Estados Unidos'),
                    (4,'Gil','Junger','1954-11-07','Estados Unidos'),
                    (5,'Richard','LaGravenese','1959-10-30','Estados Unidos'),
                    (6,'Donald','Petrie','1954-04-02','Estados Unidos'),
                    (7,'Christian','Ditter','1977-02-29','Alemania'),
                    (8,'Louis','Leterrier','1973-06-17','Francia'),
                    (9,'Shonda','Rhimes','1970-01-13','Estados Unidos'),
                    (10,'Shawn','Levy','1968-07-23','Canada')
                    ;`
    );
  }
// Creación de la tabla "series" en la base de datos

existe = false;
res = await db.get(
  "SELECT count(*) as contar FROM sqlite_schema WHERE type = 'table' AND name='series'",
  []
);

if (res.contar > 0) {
  existe = true;
}

if (!existe) {
  await db.run(`
                    CREATE TABLE series(
                        IdSerie INTEGER PRIMARY KEY AUTOINCREMENT,
                        Nombre TEXT NOT NULL,
                        FechaInicioEmision DATE,
                        CantidadTemporadas INTEGER 
                    );
                `);
  console.log("- Tabla series creada!");
  await db.run(
    `INSERT into series values 
                        (1, 'Greys Anatomy', '2007-03-27', 19), 
                        (2, 'Stranger Things', '2016-07-15', 4),
                        (3, 'Peaky Blinders', '2013-09-12', 6), 
                        (4, 'La Casa de Papel', '2017-05-02', 3), 
                        (5, 'Breaking Bad', '2008-01-20', 5), 
                        (6, 'Game Of Thrones', '2011-04-17', 8), 
                        (7, 'The Walking Dead', '2010-10-31', 11), 
                        (8, 'Casados con Hijos', '2005-04-12', 2), 
                        (9, 'Los Simuladores', '2002-03-20', 2), 
                        (10, 'The Big Bang Theory', '2007-09-24', 12);`
  );
}

// Creacion de la tabla "peliculas" en la base de datos

existe = false;
res = await db.get(
  "SELECT count(*) as contar FROM sqlite_schema WHERE type = 'table' AND name= 'peliculas'",
  []
);

if (res.contar > 0) existe = true;
if (!existe) {
  // como no existe, crea la tabla

  await db.run(
    `CREATE TABLE peliculas (
                        IdPelicula INTEGER PRIMARY KEY AUTOINCREMENT, 
                        Nombre TEXT NOT NULL, 
                        FechaEstreno DATE, 
                        Valoracion REAL CHECK (Valoracion >= 1 AND Valoracion <= 10)
                    );`
  );
  console.log("- Tabla peliculas creada!");

  await db.run(
    `INSERT INTO peliculas values 
                    (1, '10 cosas que odio de ti', '1999-03-31', 7.3),
                    (2, 'Love, Rosie', '2015-08-03', 7.1),
                    (3, 'Como perder a un hombre en 10 dias', '2003-01-27', 6.14),
                    (4, 'Pretty woman', '1990-11-10', 7.1),
                    (5, 'Fast and Fourios X', '2023-05-18', 6.3),
                    (6,'The Impossible',  '2013-01-03', 7.5),
                    (7,'Interstellar', '2014-11-06', 8.6),
                    (8,'Sully', '2016-11-19', 7.4),
                    (9, 'Avengers: EndGame', '2019-04-26', 8.4),
                    (10,'Spider-Man: Sin camino a casa', '2021-12-17', 8.2)
                    ;`
  );
}

// Creacion de la tabla "actores" en la base de datos
existe =false;
res = await db.get(
  "SELECT count(*) as contar FROM sqlite_schema WHERE type = 'table' and name= 'actores'",
  []
);
if (res.contar > 0) 
    existe = true;
    
if (!existe) {
  await db.run(
    `CREATE TABLE actores( 
      CodigoActor INTEGER PRIMARY KEY AUTOINCREMENT,
      Nombre text NOT NULL ,
      Apellido text NOT NULL ,
      FechaNacimiento DATE,
      CantPremios INTEGER
      );
  `);
  console.log("- Tabla actores creada!");
  await db.run(
      `INSERT into actores values	
      (1, 'Naomi', 'Watts', '1968-12-28', '15'),
      (2, 'Matthew', 'McConaughey', '1971-06-09', '28'),
      (3, 'Tom', 'Hanks', '1956-07-09', '41'),
      (4, 'Robert', 'Downey Jr.', '1965-12-07', '35'),
      (5, 'Tom', 'Holland', '1996-09-01', '19'),
      (6, 'Ellen', 'Pompeo', '1969-10-29', '22'),
      (7, 'Millie', 'Bobby Brown', '2002-09-15', '14'),
      (8, 'Cillian', 'Murphy', '1974-09-13', '32'),
      (9, 'Alvaro', 'Morte', '1975-08-09', '21'),
      (10, 'Bryan', 'Cranston', '1956-03-17', '47')`
  );
};


db.close();
}


crearDBProductora();

module.exports = crearDBProductora;
