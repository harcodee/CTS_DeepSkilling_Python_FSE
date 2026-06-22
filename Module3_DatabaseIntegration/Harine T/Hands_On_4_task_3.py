import mysql.connector
from mysql.connector import Error
import time

try:
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Har7bts1nefftech",
        database="college_db",
        use_pure=True
    )

    if conn.is_connected():
        print("Connected successfully!")

except Error as e:
    print("Database connection failed:")
    print(e)
    exit()

cursor = conn.cursor()
# ==========================================
# Task 56 - Simulate the N+1 Problem
# ==========================================

print("=" * 60)
print("TASK 56 - N+1 QUERY PROBLEM")
print("=" * 60)

query_count = 1

start = time.time()

cursor.execute("SELECT * FROM enrollments")
enrollments = cursor.fetchall()

for row in enrollments:
    student_id = row[1]

    cursor.execute(
        "SELECT first_name, last_name FROM students WHERE student_id=%s",
        (student_id,)
    )

    cursor.fetchone()
    query_count += 1

end = time.time()

n_plus_one_time = end - start

print(f"Queries Executed : {query_count}")
print(f"Execution Time   : {n_plus_one_time:.6f} seconds")


# ==========================================
# Task 57 - Solve using JOIN
# ==========================================

print("\n" + "=" * 60)
print("TASK 57 - USING SINGLE JOIN")
print("=" * 60)

start = time.time()

cursor.execute("""
SELECT
    e.enrollment_id,
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
    ON e.student_id = s.student_id
JOIN courses c
    ON e.course_id = c.course_id;
""")

rows = cursor.fetchall()

end = time.time()

join_time = end - start

print("Queries Executed : 1")
print(f"Execution Time   : {join_time:.6f} seconds")

print("\nEnrollment Details")

for row in rows:
    print(row)


# ==========================================
# Task 58 - Compare Performance
# ==========================================

print("\n" + "=" * 60)
print("TASK 58 - PERFORMANCE COMPARISON")
print("=" * 60)

print(f"N+1 Query Time : {n_plus_one_time:.6f} seconds")
print(f"JOIN Query Time: {join_time:.6f} seconds")

if join_time != 0:
    print(f"JOIN is approximately {n_plus_one_time / join_time:.2f}x faster")


# ==========================================
# Task 59 - Documentation
# ==========================================

print("\n" + "=" * 60)
print("TASK 59")
print("=" * 60)

print("""
N+1 Query Problem

For N enrollments:
    Total Queries = N + 1

Example:

10 enrollments  -> 11 queries
100 enrollments -> 101 queries
1000 enrollments -> 1001 queries
10000 enrollments -> 10001 queries

Using JOIN:
Only ONE query is executed irrespective of the number of enrollments.

This reduces:
✔ Database round trips
✔ Execution time
✔ Server load
✔ Network overhead
""")

cursor.close()
conn.close()