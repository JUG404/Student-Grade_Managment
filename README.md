# Student Grade Management System

## Description

This Python application is a simple Student Grade Management System that allows users to store, manage, and analyze student records. Student information is saved in a text file (`grades.txt`) and loaded into a dictionary for processing.

The system supports adding, viewing, searching, updating, deleting, sorting, and analyzing student grades through a command-line interface.

---

## Features

### 1. Read Student Records
Displays all student records stored in the system.

**Command:**
```
read
```

### 2. Add a New Student Record
Appends a new student record to the file.

**Command:**
```
append
```

The user is prompted to enter:
- Student ID
- Student Name
- Student Grade

A backup file is automatically created before adding the new record.

---

### 3. Search for a Student
Allows searching by:

- Student ID
- Student Name

**Command:**
```
search
```

If a student is not found, the user can choose to search again.

---

### 4. Update a Student Grade
Updates the grade of an existing student.

**Command:**
```
update
```

The user must provide:
- Student ID
- New Grade

After updating:
- The file is saved.
- A backup file is created.

---

### 5. Delete a Student Record
Removes a student from the system.

**Command:**
```
delete
```

A backup file is created before deletion.

---

### 6. View and Sort Students
Displays student records sorted by:

1. ID
2. Name
3. Grade

**Command:**
```
sort
```

---

### 7. Compute Grade Statistics
Calculates:

- Highest Grade
- Lowest Grade
- Average Grade

**Command:**
```
stats
```

---

### 8. Display Students Above Average
Shows all students whose grades are above the class average.

**Command:**
```
above average
```

---

### 9. Display Students Below Average
Shows all students whose grades are below the class average.

**Command:**
```
below average
```

---

### 10. Backup System
Creates a backup copy of the student records.

**Backup File:**
```
backup_grades.txt
```

Backups are automatically generated before:
- Adding a record
- Updating a record
- Deleting a record

---

## File Structure

```
project/
│
├── main.py
├── grades.txt
├── backup_grades.txt
└── README.md
```

---

## Data Format

Student records are stored in `grades.txt` using the following format:

```
1001, John Smith, 85
1002, Sarah Johnson, 92
1003, Michael Brown, 78
```

Each line contains:

```
Student ID, Student Name, Grade
```

---

## Dictionary Structure

The program stores student information in the following format:

```python
student_dictionary = {
    "1001": {
        "name": "John Smith",
        "grade": 85
    },
    "1002": {
        "name": "Sarah Johnson",
        "grade": 92
    }
}
```

---

## Program Workflow

1. Load records from `grades.txt`.
2. User enters a command.
3. Program executes the selected operation.
4. Changes are saved back to the file when necessary.
5. The menu continues running until the user enters:

```
exit
```

---

## Available Commands

| Command | Description |
|----------|-------------|
| read | Display all student records |
| append | Add a new student |
| search | Search by ID or name |
| update | Update a student's grade |
| delete | Delete a student record |
| sort | Sort students by ID, name, or grade |
| stats | Display grade statistics |
| above average | Show students above average |
| below average | Show students below average |
| exit | Exit the application |

---

## Requirements

- Python 3.x
- No external libraries required

---

## Running the Program

Execute the Python file:

```bash
python main.py
```

Then enter one of the available commands when prompted.

Example:

```text
What action do you want to take
(read, append, search, update, delete,
sort, stats, above average,
below average or exit?)

append
```

---

## Notes

- Student data is stored permanently in `grades.txt`.
- Backup files help prevent accidental data loss.
- The application uses a dictionary structure for efficient data access and updates.
- The interface is entirely text-based and runs in the terminal.

## Alternative GUI Version

In addition to this command-line version, the project also includes an alternative implementation with a Graphical User Interface (GUI).

The GUI version provides the same functionality as the console application, including:

- Adding student records
- Viewing student records
- Searching for students
- Updating grades
- Deleting records
- Sorting records
- Computing statistics
- Creating backup files

The GUI was developed with the assistance of Artificial Intelligence tools to help design and implement the user interface while preserving the core functionality and logic of the original program.
