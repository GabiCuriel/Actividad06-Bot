create database demo_bot;

use demo_bot;

create table otonio(
    id_otonio int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    consejos longtext not null)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table invierno(
    id_invierno int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    consejos longtext not null)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table primavera(
    id_primavera int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    consejos longtext not null)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table verano(
    id_verano int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    consejos longtext not null)ENGINE=InnoDB DEFAULT CHARSET=latin1;

insert into otonio(id_otonio,consejos)values
    (01, 'Si quieres usar tu chaqueta de cuero sin parecer Gatubela, combinala con algo muy suave como el encaje.'),
    (02, 'Una prenda a cuadros hace que cualquier look se vea apropiado para la época.'),
    (03, 'Botas: altas, cortas, con tacones o flats, todas son maravillosas y pueden ser utilizadas desde los primeros días de frio.');

insert into invierno(id_invierno,consejos)values
    (01, 'Es de suma importancia protegerse la cabeza contra el frío, el viento y la humedad con un buen gorro que tape hasta las orejas.'),
    (02, 'En todos los casos, las botas de invierno deben ser impermeables, de lo contrario incumplirán su función de aislante térmico.'),
    (03, 'El consejo de oro para salir de forma abrigada y funcional durante el invierno consiste en colocarse la ropa en capas.');

insert into primavera(id_primavera,consejos)values 
    (01, 'Debes enfocarte en los colores y patrones brillantes para darle un poco de estilo a tu atuendo.'),
    (02, 'Llena tu guardarropa de colores neutros.'),
    (03, 'Ten en cuenta que los patrones florales siempre están de moda durante la primavera.');

insert into verano(id_verano,consejos)values
    (01, 'Los vestidos largos son muy elegantes y cuanto más anchos más frescos.'),
    (02, 'Los chalecos largos con muy estilosos y ligeros para el verano.'),
    (03, 'Los pantalones palazzo, ya sean largos o por encima de las rodillas, son de un estilo increíble.');

CREATE TABLE users(
    username varchar(20) NOT NULL PRIMARY KEY,
    password varchar(32) NOT NULL,
    privilege integer NOT NULL DEFAULT -1,
    status integer NOT NULL DEFAULT 1,
    name varchar(150) NOT NULL,
    email varchar(100) NOT NULL,
    other_data varchar(50) NOT NULL,
    user_hash varchar(32) NOT NULL,
    change_pwd integer NOT NULL DEFAULT 1,
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE sessions(
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE logs( 
    id_log integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    ip varchar(16) NOT NULL,
    access timestamp NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO users (username, password, privilege, status, name, email, other_data, user_hash, change_pwd)
VALUES ('admin',MD5(concat('admin', 'kuorra_key')), 0, 1, 'Admin', 'admin@gmail.com','TIC:SI', MD5(concat('admin', 'kuorra_key', '2016/06/04')), 0),
('guess',MD5(concat('guess', 'kuorra_key')), 1, 1, 'Guess', 'guess@gmail.com','TIC:SI', MD5(concat('guess', 'kuorra_key','2016/06/04')), 0);

show tables;
SELECT * FROM users;
SELECT * FROM sessions;
select * from otonio;
select * from invierno;
select * from primavera;
select * from verano;

describe otonio;
describe invierno;
describe primavera;
describe verano;

CREATE USER 'bot'@'localhost' IDENTIFIED BY 'bot.2019';
GRANT ALL PRIVILEGES ON demo_bot.* TO 'bot'@'localhost';
FLUSH PRIVILEGES;