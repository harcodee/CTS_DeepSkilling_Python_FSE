// ===========================================================
// Hands-On 5 : MongoDB – Document Modelling, CRUD & Aggregation
// ===========================================================

// ===========================================================
// Task 60 : Create Database
// ===========================================================

use("college_nosql")


// ===========================================================
// Task 61 : Create Collection
// ===========================================================

db.createCollection("feedback")


// ===========================================================
// Task 62 : Insert Documents
// ===========================================================

db.feedback.insertMany([

{
    student_id:1,
    course_code:"CS101",
    semester:"2022-ODD",
    rating:5,
    comments:"Excellent teaching. Would recommend.",
    tags:["interactive","challenging","well-structured","good-examples"],
    submitted_at:new Date("2022-11-30T10:15:00Z"),
    attachments:[
        {
            filename:"notes.pdf",
            size_kb:240
        }
    ]
},

{
    student_id:2,
    course_code:"CS101",
    semester:"2022-ODD",
    rating:4,
    comments:"Good explanations and practical sessions.",
    tags:["interactive","practical"],
    submitted_at:new Date("2022-12-01T09:30:00Z"),
    attachments:[
        {
            filename:"assignment1.pdf",
            size_kb:180
        }
    ]
},

{
    student_id:3,
    course_code:"CS101",
    semester:"2023-EVEN",
    rating:3,
    comments:"Course was informative but needs more examples.",
    tags:["theory","examples"],
    submitted_at:new Date("2023-04-15T11:20:00Z"),
    attachments:[
        {
            filename:"feedback.docx",
            size_kb:90
        }
    ]
},

{
    student_id:4,
    course_code:"CS102",
    semester:"2022-EVEN",
    rating:5,
    comments:"Excellent lab sessions and support.",
    tags:["labs","supportive"],
    submitted_at:new Date("2022-11-20T10:45:00Z"),
    attachments:[
        {
            filename:"labnotes.pdf",
            size_kb:250
        }
    ]
},

{
    student_id:5,
    course_code:"CS102",
    semester:"2023-ODD",
    rating:2,
    comments:"Need more practical examples.",
    tags:["difficult"],
    submitted_at:new Date("2023-09-10T14:00:00Z")
},

{
    student_id:6,
    course_code:"CS103",
    semester:"2023-EVEN",
    rating:4,
    comments:"Interesting subject with useful projects.",
    tags:["projects","interesting"],
    submitted_at:new Date("2023-11-12T13:15:00Z"),
    attachments:[
        {
            filename:"project.pdf",
            size_kb:310
        }
    ]
},

{
    student_id:7,
    course_code:"CS104",
    semester:"2021-EVEN",
    rating:5,
    comments:"Highly engaging classes.",
    tags:["engaging","interactive"],
    submitted_at:new Date("2022-10-25T08:45:00Z"),
    attachments:[
        {
            filename:"slides.pdf",
            size_kb:200
        }
    ]
},

{
    student_id:8,
    course_code:"CS103",
    semester:"2022-EVEN",
    rating:1,
    comments:"Course needs improvement.",
    tags:["slow","theory"],
    submitted_at:new Date("2022-12-18T16:30:00Z"),
    attachments:[
        {
            filename:"remarks.txt",
            size_kb:20
        }
    ]
},

{
    student_id:9,
    course_code:"CS105",
    semester:"2023-ODD",
    rating:4,
    comments:"Good content and assignments.",
    tags:["assignments","content"],
    submitted_at:new Date("2023-08-18T15:20:00Z"),
    attachments:[
        {
            filename:"assignment.pdf",
            size_kb:150
        }
    ]
},

{
    student_id:10,
    course_code:"CS104",
    semester:"2023-EVEN",
    rating:5,
    comments:"Very well organized and easy to follow.",
    tags:["organized","clear"],
    submitted_at:new Date("2023-12-05T10:10:00Z"),
    attachments:[
        {
            filename:"certificate.pdf",
            size_kb:280
        }
    ]
}

])


// ===========================================================
// Task 63
// One document intentionally omits attachments
// (student_id = 5)
// ===========================================================


// ===========================================================
// Task 64
// Verify Inserts
// ===========================================================

db.feedback.countDocuments()


// ===========================================================
// Task 65
// READ
// Find all feedback documents where rating is 5.
// ===========================================================

db.feedback.find(
{
    rating:5
}
)


// ===========================================================
// Task 66
// READ
// Find feedback for CS101 where tags contain "challenging"
// ===========================================================

db.feedback.find(
{
    course_code:"CS101",
    tags:"challenging"
}
)


// ===========================================================
// Task 67
// Projection
// Display only student_id, course_code and rating
// ===========================================================

db.feedback.find(
{},
{
    _id:0,
    student_id:1,
    course_code:1,
    rating:1
}
)


// ===========================================================
// Task 68
// Update all documents having rating <=3
// Add needs_review:true
// ===========================================================

db.feedback.updateMany(
{
    rating:{
        $lte:3
    }
},
{
    $set:{
        needs_review:true
    }
}
)


// ===========================================================
// Task 69
// Push "reviewed" into tags array
// ===========================================================

db.feedback.updateMany(
{
    needs_review:true
},
{
    $push:{
        tags:"reviewed"
    }
}
)


// ===========================================================
// Task 70
// Delete feedback where semester is 2021-EVEN
// ===========================================================

db.feedback.deleteMany(
{
    semester:"2021-EVEN"
}
)


// ===========================================================
// Task 71
// Aggregation Pipeline
// Average rating & total feedback for semester 2022-ODD
// ===========================================================

db.feedback.aggregate([

{
    $match:{
        semester:"2022-ODD"
    }
},

{
    $group:{
        _id:"$course_code",
        average_rating:{
            $avg:"$rating"
        },
        total_feedback:{
            $sum:1
        }
    }
},

{
    $sort:{
        average_rating:-1
    }
}

])


// ===========================================================
// Task 72
// Project rounded average rating
// ===========================================================

db.feedback.aggregate([

{
    $group:{
        _id:"$course_code",
        avg_rating:{
            $avg:"$rating"
        }
    }
},

{
    $project:{
        _id:1,
        average_rating:{
            $round:["$avg_rating",1]
        }
    }
}

])


// ===========================================================
// Task 73
// Unwind tags and count frequency
// ===========================================================

db.feedback.aggregate([

{
    $unwind:"$tags"
},

{
    $group:{
        _id:"$tags",
        frequency:{
            $sum:1
        }
    }
},

{
    $sort:{
        frequency:-1
    }
}

])


// ===========================================================
// Task 74
// Create Index
// Verify using explain()
// ===========================================================

db.feedback.createIndex(
{
    course_code:1
}
)

db.feedback.find(
{
    course_code:"CS101"
}
).explain("executionStats")