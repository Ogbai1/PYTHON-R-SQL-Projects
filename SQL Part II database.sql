CREATE database TASK3;
USE TASK3;
CREATE TABLE employee(
employeeID INT NOT NULL,
name VARCHAR(8),
surname VARCHAR(8) NOT NULL,
department VARCHAR(25) NOT NULL,
salary INT (6) NOT NULL,
address VARCHAR(30),
PRIMARY KEY (employeeID)
);

 INSERT INTO employee(employeeID, name, surname, department, salary, address)
 VALUES ('44547','Smith','Ken','Computer Science', '95000', '10 Knnnedy Street'),
 ('44541','Bill','Sum','Electrical','55000', '11 Knnnedy Street '),
 ('47778','Sam', 'John','Humanities','44000','12 Knnnedy Street '),
 ('48147', 'Erik','Saron','Mechanical','80000','13 Knnnedy Street '),
 ('411547', 'Melisa', 'Aeron', 'Information Technology', '65000','14 Knnnedy Street '),
 ('48898', 'Jena', 'Cozby','Civil', '50000', '15 Knnnedy Street '),
 ('49999', 'Andy', 'Smith ', 'Human Resources', '40000', '16 Knnnedy Street'),
 ('50505', 'Michael', ' Bill', 'Financ', ' 30000', '17 Knnnedy Street '),
 ('42779', 'Foster', 'Bill', 'Marketing','12000', ' 18 Knnnedy Street '),
 ('41888', 'Andrew','Baiden',' Geology', '85000','19 Knnnedy Street ');
 
 Explain employee;
 SELECT*FROM employee;
 
 CREATE TABLE department(
departmentID INT NOT NULL,
dept_name VARCHAR(30),
Budget INT (7) NOT NULL,
address VARCHAR(20) NOT NULL,
email VARCHAR(30) NOT NULL,
Telephone INT (11) NOT NULL,
PRIMARY KEY (departmentID)
);
 INSERT INTO department(departmentID, dept_name, Budget, address, email, telephone)
 VALUES ('1','Computer Science','100000','2 Bk Street',' Space@gmail.com', '12144'),
 ('2','Electrical','80000','3 Bk Street', 'humanitis@gmail.com', '12145'),
 ('3','Humanities','50000','4 Bk Street', 'micahel@gmail.com', '12146'),
 ('4', 'Mechanical','40000','5 Bk Street', 'Sp121@gmail.com', '12147'),
 ('5','Information Technology', '90000','6 Bk Street', 'Sp113@gmail.com','12148'),
 ('6','Civil', '60000', '7 Bk Street', 'Sp115@gmail.com', '12149');
 
 SELECT*FROM department;

ALTER TABLE employee RENAME COLUMN department TO section;
ALTER TABLE employee RENAME COLUMN address TO location;

UPDATE employee SET salary = replace(salary, '55000', '50000');
SELECT*FROM employee;

SELECT employee.employeeID, department.dept_name, employee.name
FROM employee 
INNER JOIN department ON employee.salary=department.budget;

SELECT salary FROM employee
where salary > '48000';

SELECT salary, count(*) FROM employee
INNER JOIN department
ON employee.salary=department.budget
WHERE (salary < '50000');

SELECT
	employeeID, 
	Surname
FROM
	employee
ORDER BY
	salary DESC;

SELECT *
FROM department 
WHERE budget <= '80000' and budget >='50000';


 

 
