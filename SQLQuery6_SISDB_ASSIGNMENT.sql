CREATE DATABASE SISDB;
use SISDB;
CREATE TABLE Students (
    student_id INT PRIMARY KEY IDENTITY(1,1),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    date_of_birth DATE,
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(15)
);

CREATE TABLE Teacher (
    teacher_id INT PRIMARY KEY IDENTITY(1,1),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);


CREATE TABLE Courses (
    course_id INT PRIMARY KEY IDENTITY(1,1),
    course_name VARCHAR(100),
    credits INT,
    teacher_id INT FOREIGN KEY REFERENCES Teacher(teacher_id)
);

CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY IDENTITY(1,1),
    student_id INT FOREIGN KEY REFERENCES Students(student_id),
    course_id INT FOREIGN KEY REFERENCES Courses(course_id),
    enrollment_date DATE
);
CREATE TABLE Payments (
    payment_id INT PRIMARY KEY IDENTITY(1,1),
    student_id INT FOREIGN KEY REFERENCES Students(student_id),
    amount DECIMAL(10, 2),
    payment_date DATE
);

INSERT INTO Students (first_name, last_name, date_of_birth, email, phone_number)
VALUES
('Johny', 'Does', '1995-08-15', 'johny.does@example.com', '12345678909'),
('Jane', 'Smith', '1993-05-23', 'jane.smith@example.com', '0987654321'),
('Michael', 'Johnson', '1992-11-02', 'michael.johnson@example.com', '1112223333'),
('Emily', 'Davis', '1994-04-11', 'emily.davis@example.com', '4445556666'),
('David', 'Brown', '1990-12-17', 'david.brown@example.com', '7778889999'),
('Sophia', 'Wilson', '1991-06-25', 'sophia.wilson@example.com', '1231231234'),
('Chris', 'Miller', '1994-09-08', 'chris.miller@example.com', '9876543210'),
('Amanda', 'Taylor', '1992-03-19', 'amanda.taylor@example.com', '5556667777'),
('Oliver', 'Anderson', '1995-01-30', 'oliver.anderson@example.com', '8889990000'),
('Ethan', 'Thomas', '1996-07-14', 'ethan.thomas@example.com', '1112224444');

INSERT INTO Teacher (first_name, last_name, email)
VALUES
('Sarah', 'Smith', 'sarah.smith@example.com'),
('James', 'Williams', 'james.williams@example.com'),
('Linda', 'Brown', 'linda.brown@example.com'),
('Robert', 'Jones', 'robert.jones@example.com'),
('Michael', 'Garcia', 'michael.garcia@example.com'),
('William', 'Rodriguez', 'william.rodriguez@example.com'),
('David', 'Martinez', 'david.martinez@example.com'),
('Richard', 'Hernandez', 'richard.hernandez@example.com'),
('Charles', 'Lopez', 'charles.lopez@example.com'),
('Thomas', 'Gonzalez', 'thomas.gonzalez@example.com');

INSERT INTO Courses (course_name, credits, teacher_id)
VALUES
('Mathematics 101', 3, 1),
('Physics 101', 4, 2),
('Chemistry 101', 3, 3),
('Biology 101', 3, 4),
('Computer Science 101', 4, 5),
('History 101', 2, 6),
('Psychology 101', 3, 7),
('Sociology 101', 3, 8),
('Political Science 101', 2, 9),
('English 101', 3, 10);

INSERT INTO Payments (student_id, amount, payment_date)
VALUES
(1, 500.00, '2024-09-01'),
(2, 300.00, '2024-09-02'),
(3, 200.00, '2024-09-03'),
(4, 400.00, '2024-09-04'),
(5, 350.00, '2024-09-05'),
(6, 250.00, '2024-09-06'),
(7, 450.00, '2024-09-07'),
(8, 600.00, '2024-09-08'),
(9, 700.00, '2024-09-09'),
(10, 100.00, '2024-09-10');

INSERT INTO Enrollments (student_id, course_id, enrollment_date)
VALUES
(1, 1, '2024-09-01'),
(2, 2, '2024-09-02'),
(3, 3, '2024-09-03'),
(4, 4, '2024-09-04'),
(5, 5, '2024-09-05'),
(6, 6, '2024-09-06'),
(7, 7, '2024-09-07'),
(8, 8, '2024-09-08'),
(9, 9, '2024-09-09'),
(10, 10, '2024-09-10');

INSERT INTO Students (first_name, last_name, date_of_birth, email, phone_number)
VALUES ('John', 'Doe', '1995-08-15', 'john.doe@example.com', '1234567890');

INSERT INTO Enrollments (student_id, course_id, enrollment_date)
VALUES (1, 3, '2024-09-15');
SELECT * FROM Students WHERE student_id = 1;
INSERT INTO Students (first_name, last_name, date_of_birth, email, phone_number)
VALUES ('John', 'Doe', '1995-08-15', 'john.doe@example.com', '1234567890');
INSERT INTO Enrollments (student_id, course_id, enrollment_date)
VALUES (2, 2, '2024-09-15');

UPDATE Teacher
SET email = 'new.email@example.com'
WHERE teacher_id = 1;

DELETE FROM Enrollments
WHERE student_id = 1 AND course_id = 3;

UPDATE Courses
SET teacher_id = 3
WHERE course_id = 2;


DELETE FROM Enrollments WHERE student_id = 1;
DELETE FROM Students WHERE student_id = 1;


UPDATE Payments
SET amount = 550.00
WHERE payment_id = 2;

SELECT s.first_name, s.last_name, SUM(p.amount) AS total_payments
FROM Students s
JOIN Payments p ON s.student_id = p.student_id
WHERE s.student_id = 3  -- Replace with the specific student ID
GROUP BY s.first_name, s.last_name;

SELECT c.course_name, COUNT(e.student_id) AS total_students
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name;

SELECT s.first_name, s.last_name
FROM Students s
LEFT JOIN Enrollments e ON s.student_id = e.student_id
WHERE e.course_id IS NULL;

SELECT s.first_name, s.last_name, c.course_name
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id;

SELECT t.first_name, t.last_name, c.course_name
FROM Teacher t
JOIN Courses c ON t.teacher_id = c.teacher_id;

SELECT s.first_name, s.last_name, e.enrollment_date
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
WHERE c.course_id = 1;  -- Replace with the specific course ID

SELECT s.first_name, s.last_name
FROM Students s
LEFT JOIN Payments p ON s.student_id = p.student_id
WHERE p.payment_id IS NULL;

SELECT c.course_name
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
WHERE e.course_id IS NULL;

SELECT e.student_id, COUNT(e.course_id) AS total_courses
FROM Enrollments e
GROUP BY e.student_id
HAVING COUNT(e.course_id) > 1;

SELECT e1.student_id, s.first_name, s.last_name, COUNT(e1.course_id) AS course_count
FROM Enrollments e1
JOIN Students s ON e1.student_id = s.student_id
JOIN Enrollments e2 ON e1.student_id = e2.student_id
GROUP BY e1.student_id, s.first_name, s.last_name
HAVING COUNT(e1.course_id) > 1;

SELECT t.first_name, t.last_name
FROM Teacher t
LEFT JOIN Courses c ON t.teacher_id = c.teacher_id
WHERE c.course_id IS NULL;
 
 select * from Teacher;
 SELECT t.first_name, t.last_name
FROM Teacher t
LEFT JOIN Courses c ON t.teacher_id = c.teacher_id
WHERE c.course_id IS NULL;

SELECT s.first_name, s.last_name, e.enrollment_date
FROM Students s
INNER JOIN Enrollments e ON s.student_id = e.student_id
INNER JOIN Courses c ON e.course_id = c.course_id
WHERE c.course_name = 'Mathematics 101';  -- Replace with the specific course name




SELECT AVG(student_count) AS avg_students_per_course
FROM (SELECT COUNT(e.student_id) AS student_count
      FROM Enrollments e
      GROUP BY e.course_id) AS enrollment_counts;

SELECT s.first_name, s.last_name, p.amount
FROM Payments p
JOIN Students s ON p.student_id = s.student_id
WHERE p.amount = (SELECT MAX(amount) FROM Payments);

SELECT c.course_name, COUNT(e.student_id) AS enrollment_count
FROM Courses c
JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name
HAVING COUNT(e.student_id) = (SELECT MAX(enrollment_count)
                               FROM (SELECT COUNT(student_id) AS enrollment_count
                                     FROM Enrollments
                                     GROUP BY course_id) AS subquery);

SELECT t.first_name, t.last_name, SUM(p.amount) AS total_payments
FROM Teacher t
JOIN Courses c ON t.teacher_id = c.teacher_id
JOIN Enrollments e ON c.course_id = e.course_id
JOIN Payments p ON e.student_id = p.student_id
GROUP BY t.first_name, t.last_name;

SELECT s.first_name, s.last_name
FROM Students s
WHERE NOT EXISTS (SELECT c.course_id
                  FROM Courses c
                  WHERE NOT EXISTS (SELECT e.course_id
                                    FROM Enrollments e
                                    WHERE e.course_id = c.course_id
                                    AND e.student_id = s.student_id));
SELECT t.first_name, t.last_name
FROM Teacher t
WHERE NOT EXISTS (SELECT c.course_id
                  FROM Courses c
                  WHERE c.teacher_id = t.teacher_id);

SELECT AVG(DATEDIFF(YEAR, date_of_birth, GETDATE())) AS avg_age
FROM Students;

SELECT c.course_name
FROM Courses c
WHERE NOT EXISTS (SELECT e.course_id
                  FROM Enrollments e
                  WHERE e.course_id = c.course_id);

SELECT s.first_name, s.last_name, c.course_name, SUM(p.amount) AS total_payments
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
JOIN Payments p ON s.student_id = p.student_id
GROUP BY s.first_name, s.last_name, c.course_name;

SELECT s.first_name, s.last_name, COUNT(p.payment_id) AS payment_count
FROM Students s
JOIN Payments p ON s.student_id = p.student_id
GROUP BY s.first_name, s.last_name
HAVING COUNT(p.payment_id) > 1;

SELECT s.first_name, s.last_name, SUM(p.amount) AS total_payments
FROM Students s
JOIN Payments p ON s.student_id = p.student_id
GROUP BY s.first_name, s.last_name;

SELECT c.course_name, COUNT(e.student_id) AS student_count
FROM Courses c
JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name;

SELECT s.first_name, s.last_name, AVG(p.amount) AS avg_payment
FROM Students s
JOIN Payments p ON s.student_id = p.student_id
GROUP BY s.first_name, s.last_name;







SELECT t.first_name, t.last_name
FROM Teacher t
LEFT JOIN Courses c ON t.teacher_id = c.teacher_id
WHERE c.course_id IS NULL;
