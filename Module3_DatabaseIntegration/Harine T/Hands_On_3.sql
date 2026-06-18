USE college_db;
-- =======================================
-- Task 1: SUBQUERIES
-- =======================================
-- 35 
SELECT s.student_id = CONCAT(s.first_name,' ',s.last_name) AS student_name
FROM students s JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id,s.first_name,s.last_name
HAVING COUNT(e.course_id) >
(
    SELECT AVG(course_count)
    FROM
    (
        SELECT COUNT(course_id) AS course_count
        FROM enrollments
        GROUP BY student_id
    ) AS avg_table
);

-- 36
SELECT c.course_name
FROM courses c WHERE EXISTS
(SELECT * FROM enrollments e WHERE e.course_id = c.course_id)
AND NOT EXISTS(
SELECT * FROM enrollments e WHERE e.course_id = c.course_id AND e.grade <> 'A');

-- 37
SELECT p.prof_name, p.department_id, p.salary FROM professors p WHERE p.salary = 
( SELECT MAX(salary) FROM professors WHERE department_id = p.department_id);

-- 38
SELECT * FROM
(
    SELECT d.dept_name, ROUND(AVG(p.salary),2) AS avg_salary
    FROM departments d
    JOIN professors p
    ON d.department_id = p.department_id
    GROUP BY d.department_id, d.dept_name
) AS dept_avg
WHERE avg_salary > 85000;

-- =======================================
-- Task 2: CREATING AND USING VIEWS
-- =======================================

-- 39
CREATE VIEW vw_student_enrollment_summary AS
SELECT
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    d.dept_name,
    COUNT(e.course_id) AS total_courses,
    ROUND(
        AVG(
            CASE
                WHEN e.grade = 'A' THEN 4
                WHEN e.grade = 'B' THEN 3
                WHEN e.grade = 'C' THEN 2
                WHEN e.grade = 'D' THEN 1
                WHEN e.grade = 'F' THEN 0
            END
        ),
        2
    ) AS GPA
FROM students s
JOIN departments d
ON s.department_id = d.department_id
LEFT JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, student_name, d.dept_name;

-- 40
CREATE VIEW vw_course_stats AS
SELECT
    c.course_name,
    c.course_code,
    COUNT(e.student_id) AS total_enrollments,
    ROUND(
        AVG(
            CASE
                WHEN e.grade = 'A' THEN 4
                WHEN e.grade = 'B' THEN 3
                WHEN e.grade = 'C' THEN 2
                WHEN e.grade = 'D' THEN 1
                WHEN e.grade = 'F' THEN 0
            END
        ),
        2
    ) AS avg_gpa
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name, c.course_code;

-- 41
SELECT *
FROM vw_student_enrollment_summary
WHERE GPA > 3.0;

-- 42
UPDATE vw_student_enrollment_summary
SET GPA = 4.0
WHERE student_id = 1;

-- 43
DROP VIEW IF EXISTS vw_student_enrollment_summary;
DROP VIEW IF EXISTS vw_course_stats;

CREATE VIEW vw_student_enrollment_summary AS
SELECT
    student_id,
    first_name,
    last_name,
    department_id,
    enrollment_year
FROM students
WHERE enrollment_year >= 2022
WITH CHECK OPTION;

-- ===========================================
-- Task 3: STORED PROCEDURES AND TRANSACTIONS
-- ===========================================

-- 44
DELIMITER $$

CREATE PROCEDURE sp_enroll_student(
    IN p_student_id INT,
    IN p_course_id INT,
    IN p_enrollment_date DATE
)
BEGIN
    IF EXISTS (
        SELECT 1
        FROM enrollments
        WHERE student_id = p_student_id
        AND course_id = p_course_id
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Student is already enrolled in this course';
    ELSE
        INSERT INTO enrollments
        (student_id, course_id, enrollment_date)
        VALUES
        (p_student_id, p_course_id, p_enrollment_date);
    END IF;
END $$

DELIMITER ;

-- 45
CREATE TABLE department_transfer_log(
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    old_department INT,
    new_department INT,
    transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
DELIMITER $$

CREATE PROCEDURE sp_transfer_student(
    IN p_student_id INT,
    IN p_new_department INT
)
BEGIN
    DECLARE old_dept INT;

    START TRANSACTION;

    SELECT department_id
    INTO old_dept
    FROM students
    WHERE student_id = p_student_id;

    UPDATE students
    SET department_id = p_new_department
    WHERE student_id = p_student_id;

    INSERT INTO department_transfer_log
    (student_id, old_department, new_department)
    VALUES
    (p_student_id, old_dept, p_new_department);

    COMMIT;
END $$

DELIMITER ;

-- 46
START TRANSACTION;

UPDATE students
SET department_id = 99
WHERE student_id = 1;

INSERT INTO department_transfer_log
(student_id, old_department, new_department)
VALUES
(1,1,99);

ROLLBACK;

SELECT *
FROM students
WHERE student_id = 1;

-- 47
START TRANSACTION;

INSERT INTO enrollments
(student_id, course_id, enrollment_date, grade)
VALUES
(2,2,'2024-06-18','A');

SAVEPOINT first_insert;

-- This will fail if course_id 99 does not exist
INSERT INTO enrollments
(student_id, course_id, enrollment_date, grade)
VALUES
(3,99,'2024-06-18','A');

ROLLBACK TO first_insert;

COMMIT;

SELECT *
FROM enrollments
WHERE student_id = 2
AND course_id = 2;

