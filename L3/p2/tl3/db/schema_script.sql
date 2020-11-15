CREATE TABLE cookies(
    key character(36) PRIMARY KEY, 
    value character(36) NOT NULL
);


CREATE TABLE users(
    id serial PRIMARY KEY, 
    name character(70) NOT NULL,
    username character(70) NOT NULL,
    age integer NOT NULL, 
    password character(20) NOT NULL
);

CREATE TABLE trabajos(
    id serial PRIMARY KEY,
    id_usuario integer NOT NULL,
    fecha_inicio date NOT NULL,
    fecha_fin date,
    cargo character(25) NOT NULL,
    observacion character(100),
    CONSTRAINT FK_usuario FOREIGN KEY (id_usuario) REFERENCES users(id)
);

INSERT INTO users (name, age, username, password) 
  VALUES ('Maria Barja',30,'lala','25101990');

SELECT * FROM users;
