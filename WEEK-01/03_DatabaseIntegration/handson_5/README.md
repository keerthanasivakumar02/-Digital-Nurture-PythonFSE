# Hands-On 5 – MongoDB: Document Modelling, CRUD & Aggregation

## 📚 Module

**Digital Nurture 5.0 – Python Full Stack Engineer**

**Module 3:** Database Integration – PostgreSQL, MySQL & MongoDB



---

## 🎯 Objective

The objective of this hands-on is to understand MongoDB document modelling, perform CRUD operations, build aggregation pipelines, and improve query performance using indexes.

---

## 🛠 Technologies Used

- MongoDB Community Server 8.0
- MongoDB Compass
- MongoDB Shell (mongosh)
- BSON Documents

---

## 📂 Files Included

```text
Handson_5/
│── mongo_output.txt
│── README.md
```

---

## 📌 Tasks Completed

### Task 1 – Create Collection and Insert Documents

- Created the `college_nosql` database.
- Created the `feedback` collection.
- Inserted 10 feedback documents.
- Included multiple courses, ratings, semesters, and tags.
- Inserted one document without the `attachments` field to demonstrate MongoDB's schema-less design.
- Verified the inserted documents using `countDocuments()`.

---

### Task 2 – CRUD Operations

#### Read Operations

- Retrieved all feedback documents with rating 5.
- Retrieved CS101 feedback containing the `challenging` tag.
- Used projection to display only selected fields.

#### Update Operations

- Added the `needs_review` field for feedback with ratings less than 3.
- Added the `reviewed` tag to documents marked for review.

#### Delete Operation

- Deleted feedback documents belonging to the `2021-EVEN` semester.

---

### Task 3 – Aggregation Pipeline

Implemented aggregation pipelines to generate analytical reports.

Operations performed:

- Filtered documents using `$match`.
- Grouped records by `course_code`.
- Calculated average ratings using `$avg`.
- Counted total feedback using `$sum`.
- Sorted results using `$sort`.
- Renamed and rounded average ratings using `$project` and `$round`.
- Used `$unwind` to analyze tag frequency.
- Created an index on `course_code`.
- Verified index usage using `explain("executionStats")`, confirming `IXSCAN`.

---

## 📖 MongoDB Concepts Practiced

- Documents & Collections
- BSON Data Types
- CRUD Operations
- Aggregation Pipeline
- `$match`
- `$group`
- `$project`
- `$sort`
- `$unwind`
- Array Queries
- Index Creation
- Query Optimization
- IXSCAN vs COLLSCAN
- Embedding vs Referencing

---

## 🎯 Learning Outcomes

After completing this hands-on, I was able to:

- Create MongoDB databases and collections.
- Insert flexible BSON documents.
- Perform CRUD operations efficiently.
- Use projections to retrieve specific fields.
- Update and delete documents based on conditions.
- Build aggregation pipelines for reporting and analysis.
- Analyze array data using `$unwind`.
- Create indexes to improve query performance.
- Verify index usage through `executionStats`.
- Understand MongoDB's flexible schema design and document modelling.

---

## 🚀 Key Skills Gained

- MongoDB Database Management
- Document Modelling
- CRUD Operations
- Aggregation Framework
- Query Optimization
- Indexing
- Performance Analysis
- MongoDB Compass
- MongoDB Shell (mongosh)

---

## ✅ Status

✔ Hands-On 5 Completed Successfully

---

## 👩‍💻 Author

**Keerthana Sivakumar**