use("college_nosql")

db.feedback.drop()

db.createCollection("feedback")

db.feedback.insertMany([
    [{
  "_id": {
    "$oid": "6a394db13b15a7e49caf9454"
  },
  "student_id": 1,
  "course_code": "CS101",
  "semester": "2022-ODD",
  "rating": 5,
  "comments": "Excellent teaching. Would recommend.",
  "tags": [
    "interactive",
    "well-structured",
    "good-examples"
  ],
  "submitted_at": "2022-11-30T10:15:00Z",
  "attachments": [
    {
      "filename": "notes.pdf",
      "size_kb": 240
    }
  ]
},
{
  "_id": {
    "$oid": "6a394e183b15a7e49caf9456"
  },
  "student_id": 2,
  "course_code": "CS101",
  "semester": "2022-ODD",
  "rating": 4,
  "comments": "Good explanations and practical sessions.",
  "tags": [
    "interactive",
    "practical"
  ],
  "submitted_at": "2022-12-01T09:30:00Z",
  "attachments": [
    {
      "filename": "assignment1.pdf",
      "size_kb": 180
    }
  ]
},
{
  "_id": {
    "$oid": "6a394e283b15a7e49caf9458"
  },
  "student_id": 3,
  "course_code": "CS101",
  "semester": "2023-EVEN",
  "rating": 3,
  "comments": "Course was informative but needs more examples.",
  "tags": [
    "theory",
    "examples"
  ],
  "submitted_at": "2023-04-15T11:20:00Z",
  "attachments": [
    {
      "filename": "feedback.docx",
      "size_kb": 90
    }
  ]
},
{
  "_id": {
    "$oid": "6a394e333b15a7e49caf945a"
  },
  "student_id": 4,
  "course_code": "CS102",
  "semester": "2022-EVEN",
  "rating": 5,
  "comments": "Excellent lab sessions and support.",
  "tags": [
    "labs",
    "supportive"
  ],
  "submitted_at": "2022-11-20T10:45:00Z",
  "attachments": [
    {
      "filename": "labnotes.pdf",
      "size_kb": 250
    }
  ]
},
{
  "_id": {
    "$oid": "6a394e403b15a7e49caf945c"
  },
  "student_id": 5,
  "course_code": "CS102",
  "semester": "2023-ODD",
  "rating": 2,
  "comments": "Need more practical examples.",
  "tags": [
    "difficult"
  ],
  "submitted_at": "2023-09-10T14:00:00Z"
},
{
  "_id": {
    "$oid": "6a394e4a3b15a7e49caf945e"
  },
  "student_id": 6,
  "course_code": "CS103",
  "semester": "2023-EVEN",
  "rating": 4,
  "comments": "Interesting subject with useful projects.",
  "tags": [
    "projects",
    "interesting"
  ],
  "submitted_at": "2023-11-12T13:15:00Z",
  "attachments": [
    {
      "filename": "project.pdf",
      "size_kb": 310
    }
  ]
},
{
  "_id": {
    "$oid": "6a394e583b15a7e49caf9460"
  },
  "student_id": 7,
  "course_code": "CS104",
  "semester": "2022-ODD",
  "rating": 5,
  "comments": "Highly engaging classes.",
  "tags": [
    "engaging",
    "interactive"
  ],
  "submitted_at": "2022-10-25T08:45:00Z",
  "attachments": [
    {
      "filename": "slides.pdf",
      "size_kb": 200
    }
  ]
},
{
  "_id": {
    "$oid": "6a394e623b15a7e49caf9462"
  },
  "student_id": 8,
  "course_code": "CS103",
  "semester": "2022-EVEN",
  "rating": 1,
  "comments": "Course needs improvement.",
  "tags": [
    "slow",
    "theory"
  ],
  "submitted_at": "2022-12-18T16:30:00Z",
  "attachments": [
    {
      "filename": "remarks.txt",
      "size_kb": 20
    }
  ]
},
{
  "_id": {
    "$oid": "6a394e6c3b15a7e49caf9464"
  },
  "student_id": 9,
  "course_code": "CS105",
  "semester": "2023-ODD",
  "rating": 4,
  "comments": "Good content and assignments.",
  "tags": [
    "assignments",
    "content"
  ],
  "submitted_at": "2023-08-18T15:20:00Z",
  "attachments": [
    {
      "filename": "assignment.pdf",
      "size_kb": 150
    }
  ]
},
{
  "_id": {
    "$oid": "6a394e7d3b15a7e49caf9466"
  },
  "student_id": 10,
  "course_code": "CS104",
  "semester": "2023-EVEN",
  "rating": 5,
  "comments": "Very well organized and easy to follow.",
  "tags": [
    "organized",
    "clear"
  ],
  "submitted_at": "2023-12-05T10:10:00Z",
  "attachments": [
    {
      "filename": "certificate.pdf",
      "size_kb": 280
    }
  ]
}]
])