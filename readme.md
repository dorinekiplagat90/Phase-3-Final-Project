# Student Course Registration System (CLI Application)

**Author:** Dorine Kiplagat

## Introduction
The **Student Course Registration System** is a command-line application developed to manage students, courses, and enrollments in a simplified academic environment. It provides core functionalities similar to a real-world college registration system, including adding students, creating courses, enrolling students, and viewing or modifying their schedules.  

The system is built using **Python**, **SQLAlchemy ORM**, and **SQLite**, with **Click** for a clean and user-friendly command-line interface (CLI). It demonstrates essential concepts of database modeling, many-to-many relationships, and modular CLI design.

---

## Purpose
The primary objectives of this project are:

- To simulate a minimal student registration system  
- To learn and implement ORM-based data modeling  
- To demonstrate many-to-many relationships using an association table  
- To manage CRUD (Create, Read, Update, Delete) operations through a CLI  
- To create a modular, maintainable, and extendable application  

This project is ideal for academic learning, portfolio development, and understanding backend system architecture.

---

## System Features

### 1. Student Management
- Add new students with name and email  
- Prevent duplicate emails  
- List all students with the number of registered courses  

### 2. Course Management
- Add courses with code, title, and credits  
- Prevent duplicate course codes  
- List all courses  

### 3. Enrollment Management
- Enroll students into courses  
- Drop courses from schedules  
- View a student's full course schedule  

### 4. Administrative Tools
- Initialize the database  
- Seed the database with sample data  
- Display clean tabular output  

---

## Database Design

The system uses **SQLAlchemy ORM** with SQLite, supporting many-to-many relationships between students and courses.

**Models:**

1. **Student**
   - `id`: primary key  
   - `name`: student name  
   - `email`: unique student email  

2. **Course**
   - `id`: primary key  
   - `code`: unique course code  
   - `title`: course title  
   - `credits`: number of credit units  

3. **Enrollment**
   - `student_id`: foreign key referencing `Student.id`  
   - `course_id`: foreign key referencing `Course.id`  
   - Represents the many-to-many relationship between students and courses  

---

## CLI Features

- Human-readable commands using **Click**  
- Modular commands for students, courses, and enrollments  
- Input validation and helpful error messages  
- View student schedules in a clean tabular format  

---

## Getting Started

### 1. Clone the repository
```bash
git clone <repository-url>
cd student-course-registration