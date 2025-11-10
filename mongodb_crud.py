// STEP 1 — Create a Database (Optional, switches context)
use college;

// STEP 2 — Create a Collection
db.createCollection("students");

// -------------------------------
// C → CREATE Operation (Insert)
// -------------------------------

// Insert a Single Document
db.students.insertOne({
  roll_no: 1,
  name: "Advay",
  dept: "AIDS",
  marks: 89
});

// Insert Multiple Documents
db.students.insertMany([
  { roll_no: 2, name: "Om", dept: "IT", marks: 45 },
  { roll_no: 3, name: "Manisha", dept: "ENTC", marks: 78 },
  { roll_no: 4, name: "Riya", dept: "CS", marks: 91 }
]);

// -------------------------------
// R → READ Operation
// -------------------------------

// View all documents
db.students.find();

// View formatted documents
db.students.find().pretty();

// Find student with specific roll number
db.students.find({ roll_no: 2 });

// -------------------------------
// U → UPDATE Operation
// -------------------------------

// Update one student’s marks
db.students.updateOne(
  { roll_no: 2 },
  { $set: { marks: 75 } }
);

// Verify the update
db.students.find({ roll_no: 2 });

// -------------------------------
// D → DELETE Operation
// -------------------------------

// Delete one document
db.students.deleteOne({ roll_no: 3 });

// Verify deletion
db.students.find();
