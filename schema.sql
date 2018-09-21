DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS sessions;
DROP TABLE IF EXISTS subjects;

CREATE TABLE users (
	id TEXT PRIMARY KEY,
	username TEXT NOT NULL,
	email TEXT NOT NULL,
	dateCreated TEXT NOT NULL
);

CREATE TABLE sessions (
	id TEXT PRIMARY KEY,
	owner_id TEXT NOT NULL,
	subject TEXT NOT NULL,
	dateCreated TEXT NOT NULL,
	startTime TEXT NOT NULL,
	endTime TEXT NOT NULL
);

CREATE TABLE subjects (
	id INT PRIMARY KEY,
	owner_id TEXT NOT NULL,
	parent TEXT,
	dateCreated TEXT NOT NULL
);

INSERT INTO users (id, username, email, dateCreated) VALUES ('749f09bade8aca755660eeb17792da880218d4fbdc4e25fbec279d7fe9f65d70', 'admin', 'admin@timesheet.com', 'epoch');
