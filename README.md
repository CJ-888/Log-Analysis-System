# Log-Analysis-System

**•	Introduction:**
  This report explains how the implementation of a cybersecurity log analysis system used to detect suspicious activity within a system log was done. The main goal is to analyse authentication logs and identify failed login attempts, brute-force attacks and unauthorized access attempts. 

**•	Investigation:**
Modern systems are vulnerable to cyber threats, for instance, brute-force attacks, unauthorized attempts to gain access, and credential stuffing. Log analysis is vital in detecting and treating these threats. This project aims to study the extent to which parsing of authentication logs can be done to find traces of failed and unauthorized access attempts.

**•	Analysis:**
The system processes authentication logs containing records in a format of:
User, Status, Timestamp

**•	Test Cases & Results:**
The system correctly identified failed login attempts, displayed login history per user, and handled errors gracefully.

 
**•	Key Insights Derived:**

-Tracking failed login attempts per user to detect any brute force attempts 
-Monitoring successful and unsuccessful logins to determine legitimate access
-Identifying the login frequency of users 

**•	Design:**

There are 3 primary classes in the system:

1.	LOG READER: Gathers and saves authentication logs in a list after reading them from a file.

2.	LOG ANALYSER: Monitors login timestamps, counts unsuccessful login attempts, and analyses login attempts. 

3.	Report Generator: Produces a report that summarises user activity and unsuccessful login attempts.


**•	Execution:**
 Python is used to implement the system using: Reading log data from a file is part of file handling. Log entries are broken down into their component parts (user, status, and timestamp) via string processing. Dictionary Data Structures: Keeps track of login timestamps and the number of unsuccessful login attempts. Functionality is encapsulated into distinct classes using object-oriented design. 


**•	Workflow for Code**
•	1. Use Log Reader to load logs from a file. 
•	2. Use Log Analyzer to examine login attempts. 
•	3. Use Report Generator to create a security report.

