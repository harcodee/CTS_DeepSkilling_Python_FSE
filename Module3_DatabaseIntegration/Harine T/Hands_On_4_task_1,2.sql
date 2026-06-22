USE college_db;

-- ==========================================
-- Task 1: BASELINE PERFORMANCE - NO INDEXES
-- ==========================================
-- 48
EXPLAIN
SELECT s.first_name, s.last_name, c.course_name
FROM enrollments e JOIN students s
ON s.student_id = e.student_id JOIN courses c
ON c.course_id = e.course_id WHERE s.enrollment_year = 2022;

-- Task 49:
-- EXPLAIN shows a Full Table Scan (type = ALL) on the students table.
-- Since enrollment_year has no index, MySQL scans all student records
-- before applying the WHERE condition.

-- Task 50:
-- Estimated rows examined:
-- students    : 10
-- enrollments : 1 (per matching student using student_id index)
-- courses     : 1 (using PRIMARY KEY)
-- The query uses:
-- students    -> ALL (Full Table Scan)
-- enrollments -> ref
-- courses     -> eq_ref

-- ==========================================
-- Task 2: ADD INDEXES AND COMPARE PLANS
-- ==========================================
-- 51
CREATE INDEX idx_students_enrollment_year
ON students(enrollment_year);

EXPLAIN
SELECT s.first_name, s.last_name, c.course_name
FROM enrollments e JOIN students s
ON s.student_id = e.student_id JOIN courses c
ON c.course_id = e.course_id WHERE s.enrollment_year = 2022;

-- 52
CREATE UNIQUE INDEX idx_enrollment_student_course
ON enrollments(student_id, course_id);

-- 53
CREATE INDEX idx_course_code
ON courses(course_code);

-- 54
EXPLAIN
SELECT s.first_name, s.last_name, c.course_name
FROM enrollments e JOIN students s
ON s.student_id = e.student_id JOIN courses c
ON c.course_id = e.course_id WHERE s.enrollment_year = 2022;

-- 55
CREATE INDEX idx_enrollment_student
ON enrollments(student_id);


