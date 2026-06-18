# Database Integration - Hands-On 2

## Writing SQL Queries - DML, Joins & Aggregations

## Overview

This project implements **Hands-On 2** of the **Digital Nurture 5.0 - Database Integration** module. The objective is to practice SQL Data Manipulation Language (DML), filtering queries, joins, aggregate functions, grouping, and HAVING clauses using the **Student Course Registration System** database.

---

## Database

```sql
USE college_db;
```

The project uses the following tables:

* Departments
* Students
* Courses
* Enrollments
* Professors

---

# Task 1: Insert, Update and Delete Data

Implemented the following DML operations:

* Inserted sample data into all five tables.
* Added two additional student records.
* Updated a student's grade from **C** to **B**.
* Deleted enrollment records with **NULL** grades.
* Verified table row counts using `COUNT(*)`.

### SQL Concepts Used

* INSERT
* UPDATE
* DELETE
* WHERE
* COUNT()

---

# Task 2: Single Table Queries and Filtering

Implemented queries using:

* SELECT
* WHERE
* ORDER BY
* BETWEEN
* LIKE
* GROUP BY

### Queries Performed

* Retrieve students enrolled in 2022.
* Display courses having credits greater than 3.
* List professors with salaries between 80,000 and 95,000.
* Find students whose email ends with `@college.edu`.
* Count students grouped by enrollment year.

---

# Task 3: Multi-Table Joins

Implemented SQL JOIN operations across multiple tables.

### Queries Performed

* Student name with department name.
* Student enrollments with course names and grades.
* Students not enrolled in any course.
* Number of students enrolled in each course.
* Departments with professor names and salaries.

### SQL Concepts Used

* INNER JOIN
* LEFT JOIN
* Multi-table JOIN
* CONCAT()
* GROUP BY

---

# Task 4: Aggregations and Grouping

Implemented aggregate queries to generate summary reports.

### Queries Performed

* Total enrollments per course.
* Average professor salary by department.
* Departments with budget greater than 600000.
* Grade distribution for course CS101.
* Departments having more than two enrolled students using HAVING.

### SQL Concepts Used

* COUNT()
* AVG()
* ROUND()
* GROUP BY
* HAVING
* COUNT(DISTINCT)

---

## Topics Covered

* SQL Data Manipulation Language (DML)
* Data Filtering
* Sorting Records
* Pattern Matching using LIKE
* Aggregate Functions
* GROUP BY and HAVING
* INNER JOIN
* LEFT JOIN
* Multi-table JOIN Queries

---

## Technologies Used

* MySQL 8.x
* SQL
* MySQL Workbench

---

## Learning Outcomes

After completing this hands-on, the following concepts were practiced:

* Performing CRUD operations using SQL.
* Writing filtering and sorting queries.
* Combining multiple tables using JOINs.
* Using aggregate functions for reporting.
* Grouping records and filtering aggregated data using HAVING.
* Building real-world SQL queries for relational databases.


