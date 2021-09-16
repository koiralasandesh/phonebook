Introduction

The phonebook is a simple python program that simulates a simple phonebook to save people’s name and phone numbers. The program takes user input as execution arguments and saves the names and phone numbers to SQLite database. The program is built with security in mind. Every function is built to be secure against various outside attacks. The program also has a logging feature to log all essential program flow. 

The program directory follows the following structure:

 
				|---- main		main executable
				|	
 sandesh_assignment11----|------logs/logs	program logs
				|
				|----db/users.db	SQLite database 


The main program executable can be executed as:
    
	./main <COMMAND> “<ARGUMRNT>” “<ARGUMENT>”

The command is the user command to add, delete or list Contacts and the argument is the required argument for the command.

The program allows following command:

	ADD “<Person>” “<Telephone #>” 	- Add a new person to the database 
	DEL “<Person>” 			- Remove someone from the database by name 
	DEL “<Telephone #>” 		- Remove someone by telephone # 
	LIST					- Produce a list of the members of the database
	LOG					- Produce system log 

The program accepts any following combination of Names.

	Firstname
	Firstname Lastname
	Firstname Middename Lastname
	Firstname Middlename-Lastname
	Lastname, Firstname
	Lastname, Firstname Middlename
	Lastname, Firstname-Middlename

The character count for any combination must be >2 and <40.


Installation

The program is portable and does not require any installation. However, the program is written in python and requires python v3.0 or higher to execute. The program uses sqlite3 to store user data. Hence sqlite3 must also be present in your system. There is a huge chance all dependencies already exist in your system. 

1.	Check if python is already installed using following command:

	which python3

If the following command returns the path to a python executable. Skip to step 3.
If the command does not return anything, Go to step 2.

2.	Install python3.

Input the following command to install python3 on Debian based Linux.

	sudo apt install python3

Accept all confirmation. Go to step3 once done.

3.	Check if SQLite3 exists in your system:

	which sqlite3

If the following command returns the path to a sqlite executable. No further installation is required. 
If the command does not return anything, Go to step 4.
4.	Install sqlite for Debian based systems using following command:

	sudo apt install sqlite3

The program automatically creates a database file in the “db” directory if one doesn’t exist in the system. The program uses the existing file if there already exists a database file in the directory. Similarly, the program checks for log file in the “logs” directory and creates one if it doesn’t exist. If a log file does exist, it appends the logs to same file.  

Please verify to make sure the program is executable. If the program is not executable, please type following command from the directory to make the file executable:

	chmod +x main

Alternately the program can also be executed with the python interpreter. To run the program with python interpreter, for every command, run it as:

	python3 main <COMMAND> “<ARGUMRNT>” “<ARGUMENT>”
Execution

This page assumes you made the program file executable following the command in the above page. The program takes user input via command line during invocation. From the directory containing the python executable, the program must be executed as such:

	./main <COMMAND> “<ARGUMRNT>” “<ARGUMENT>”

The program prints help text to stderr if the program is executed with incorrect command or arguments. If incorrect arguments are passed to correct command, it displays help for the command. The command also returns 0 for all successful executions like addition of phone numbers and deletions. It returns 1 for all incomplete or unsuccessful execution.

The program accepts the following commands. The commands are case insensitive.

	ADD “<Person>” “<Telephone #>” 	- Add a new person to the database 
	DEL “<Person>” 			- Remove someone from the database by name 
	DEL “<Telephone #>” 		- Remove someone by telephone # 
	LIST					- Produce a list of the members of the database
	LOG					- Produce system log 

Few examples of commands are as follows:

	./main add “Sandesh Koirala” “(682)674-1234”
	./main del “Sandesh Koirala”
	./main del “(682)674-1234”
	./main list
	./main log


Assumptions

1.	This is a portable App. Does not require complex installation procedure.

The only assumptions made in this project is that this is a portable program. The program does not require extensive setup except to set the program’s execute bit.

2.	Uses SQLite instead of MySQL to eliminate complex database setup process during grading.

For this assignment, the program uses SQLite database to eliminate extensive setup process required to use Full Functional Database like MySQL. 

3.	The program does not have any user authentication. 


Pros

1.	Portability
The portability is a huge advantage of the program. The program can readily be copied from one machine to another without difficult installation procedure. If the database file is found in the correct directory, the program runs in any system and appends new data to the existing database. If no database is found, the program creates one without any input from the user.

2.	Prepared Database Queries
Using database allows for use of database APIs. Hence, all database queries are parametrized queries. Eliminating the SQL Injection Attack Vulnerabilities.


Cons

1.	No database authentication
SQLite apparently does not support database authentication. Although the database file exists as binary and cannot be directly modified, the database is not authenticated. However, if complete database was implemented, it would not be too difficult to implement authentication. 

2.	No user authentication
The program does not have any user authentication feature. Hence, it assumes that any user with permission to access the program can list the database, delete records, and view system log.

Bonus

The program uses SQLite as a database and all database queries are parameterized.
