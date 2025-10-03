# 🎓 Student Management System (Python + CSV)

A **console-based Student Management System** built in Python for managing student data in a department office.  
It replaces paper registers with a CSV-backed solution for admissions, updates, reports, and audits.

---

## 📌 Features
- **Admissions (UC1):** Add new students with validation (no duplicate Roll_No, valid marks & attendance).
- **Search (UC2):** Lookup students by Roll No (exact) or Name (partial).
- **Update (UC3):** Modify marks or attendance with confirmation.
- **Delete (UC4):** Remove a student, moved to `students_deleted.csv` for audit.
- **Reports (UC5):** Generate branch/year-wise reports (avg, top scorer, grade distribution).  
  Reports saved inside `data/reports/`.
- **Bulk Import (UC6):** Import students from a CSV, invalid rows logged in `import_errors.csv`.
- **Sort & Filter (UC7):** Identify top/weak students via sorting/filtering.

---

## 📂 Project Structure
