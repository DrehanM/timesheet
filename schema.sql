DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS sessions;
DROP TABLE IF EXISTS subjects;

CREATE TABLE users (
	id BIGINT PRIMARY KEY,
	username TEXT NOT NULL,
	dateCreated INT,
	numSessions INT
);

CREATE TABLE sessions (
	id INT PRIMARY KEY,
	owner TEXT NOT NULL,
	subject TEXT NOT NULL,
	dateCreated INT NOT NULL,
	startTime INT NOT NULL,
	endTime INT NOT NULL
);

CREATE TABLE subjects (
	id INT PRIMARY KEY,
	owner TEXT NOT NULL,
	parent TEXT,
	dateCreated INT NOT NULL
);

INSERT INTO users (id, username) VALUES (438398031073640448, 'admin');
