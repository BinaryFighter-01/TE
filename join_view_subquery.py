-- Create Department table
CREATE TABLE Department (
    deptid INT PRIMARY KEY,
    deptname VARCHAR(50)
);

-- Create Employee table with foreign key
CREATE TABLE Employee (
    empid INT PRIMARY KEY,
    empname VARCHAR(50),
    deptid INT,
    salary INT,
    FOREIGN KEY (deptid) REFERENCES Department(deptid)
);

-- Insert sample departments
INSERT INTO Department VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Management'),
(4, 'Finance');

-- Insert sample employees
INSERT INTO Employee VALUES
(101, 'Advay', 2, 500000),
(102, 'Durva', 1, 600000),
(103, 'Anish', 3, 300000),
(104, 'Aryan', NULL, 200000),
(105, 'Anjali', 4, 800000);

-- INNER JOIN: Show employees with matching departments
SELECT empname, deptname
FROM Employee
INNER JOIN Department ON Employee.deptid = Department.deptid;

-- LEFT JOIN: Show all employees, even if department is missing
SELECT empname, deptname
FROM Employee
LEFT JOIN Department ON Employee.deptid = Department.deptid;

-- RIGHT JOIN: Show all departments, even if no employee is assigned
SELECT empname, deptname
FROM Employee
RIGHT JOIN Department ON Employee.deptid = Department.deptid;

-- CROSS JOIN: Combine all employees with all departments
SELECT empname, deptname
FROM Employee
CROSS JOIN Department;

-- SELF JOIN: Find colleagues in the same department
SELECT e1.empname AS employee, e2.empname AS colleague
FROM Employee e1, Employee e2
WHERE e1.deptid = e2.deptid AND e1.empid <> e2.empid;

-- SUBQUERY: Employees earning above average salary
SELECT empname, salary
FROM Employee
WHERE salary > (SELECT AVG(salary) FROM Employee);

-- SUBQUERY: Employees from IT department
SELECT empname
FROM Employee
WHERE deptid IN (
    SELECT deptid FROM Department WHERE deptname = 'IT'
);

-- SUBQUERY with EXISTS: Employees in Finance department
SELECT empname
FROM Employee e
WHERE EXISTS (
    SELECT * FROM Department d
    WHERE d.deptid = e.deptid AND d.deptname = 'Finance'
);

-- CREATE VIEW: Employee details with department info
CREATE VIEW emp_details AS
SELECT e.empname, e.empid, d.deptid, e.salary
FROM Employee e
LEFT JOIN Department d ON d.deptid = e.deptid;

-- Query the view for employees with high salaries
SELECT * FROM emp_details
WHERE salary > 500000;
