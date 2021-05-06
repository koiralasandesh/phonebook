# import os
import sys
import sqlite3
import re
import logging


def compile_name_regex():
    name_pattern = re.compile(
        r"^((([A-Za-z]+)(\')?)?([A-Za-z]+))(\,? ([A-Za-z]+)(((\')?)?([A-Za-z]+))( ?)(-?)([A-Za-z]+)(.?))?$")
    return name_pattern


def compile_number_regex():
    number_pattern = re.compile(r"^(\d{3})? ?(\+?\d{1,2})? ?(\(?\d{2,3}\)?)? ?-?(\d{3}?(\s?-?.?))?\d{4,5}$")
    return number_pattern


def add_user(argv):
    # print(argv)
    if len(argv) > 2 or len(argv) < 2:
        user_input = " ".join(argv)
        logging.warning("invalid add command - <" + user_input + ">")
        show_help()
        exit(1)
    name_regex = compile_name_regex()
    number_regex = compile_number_regex()
    name_result = name_regex.match(argv[0])
    number_result = number_regex.match(argv[1])
    if name_result and number_result:
        add_sql = 'INSERT INTO users VALUES (?,?);'
    else:
        sys.stderr.write("Invalid Input!")
        logging.error("invalid user not added - <" + argv[0] + "> <" + argv[1] + ">")
        exit(1)
    # print(add_sql)
    c = conn.cursor()
    try:
        data_tuple = (argv[0], argv[1])
        c.execute(add_sql, data_tuple)
        conn.commit()
        conn.close()
        logging.info("user added - <" + argv[0] + "> <" + argv[1] + ">")
        exit(0)
    except IOError as e:
        sys.stderr.write(e)
        logging.error("could not write to database - <" + add_sql + ">")
        exit(1)


def remove_user(argv):
    if len(argv) > 1 or len(argv) < 1:
        user_input = " ".join(argv)
        logging.warning("invalid del command - <" + user_input + ">")
        show_help()
        exit(1)
    name_regex = compile_name_regex()
    number_regex = compile_number_regex()
    name_result = name_regex.match(argv[0])
    number_result = number_regex.match(argv[0])
    if name_result or number_result:
        remove_sql = 'DELETE FROM users WHERE name=? OR phone=?;'
    else:
        sys.stderr.write("Invalid Input!")
        logging.error("invalid user not deleted - <" + argv[0] + ">")
        exit(1)
    c = conn.cursor()
    try:
        data_tuple = (argv[0], argv[0])
        c.execute(remove_sql, data_tuple)
        conn.commit()
        if conn.total_changes > 0:
            logging.info("user removed - <" + argv[0] + ">")
            conn.close()
            exit(0)
        else:
            logging.info("user DNE del - <" + argv[0] + ">")
            conn.close()
            exit(1)
    except IOError as e:
        sys.stderr.write(e)
        logging.error("could not write to database - " + remove_sql)
        exit(1)


def list_users():
    fetch_sql = 'SELECT * FROM users;'
    c = conn.cursor()
    rows = None
    try:
        c.execute(fetch_sql)
        rows = c.fetchall()
        conn.close()
    except IOError as e:
        sys.stderr.write(e)
        exit(1)
    print("Name\t\t\t\t\t\tPhone")
    print("___________\t\t\t\t\t___________")
    for row in rows:
        print(row[0] + "\t\t\t\t" + row[1])

    exit(0)


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except IOError as e:
        sys.stderr.write(e)
        logging.critical("could not connect to db - <" + e + ">")
        exit(1)
    return conn


def show_help():
    sys.stderr.write('''
---------------------------------------------------------------------------------
Please Provide input in the following format:

ADD <Name> <Telephone #>        Adds the person to database
DEL <Name>                      Deletes the person to database
DEL <Telephone #>               Deletes  the record with provided telephone number
LIST                            Produces the list of all records in database
LOG                             Print system logs
---------------------------------------------------------------------------------
    ''')


def create_table():
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE IF NOT EXISTS users (
                                        name CHAR(30) NOT NULL,
                                        phone CHAR(15) NOT NULL
                                        );'''
                  )
    except IOError as e:
        sys.stderr.write(e)
        logging.critical("could not create db table - <" + e + ">")
        exit(1)


def show_log():
    logging.info("log printed")
    logs = open("logs/logs", "r")
    for log in logs:
        print(log)


if __name__ == '__main__':
    # print(sys.argv)
    logging.basicConfig(filename="logs/logs",
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)
    conn = create_connection("db/users.db")
    create_table()
    if len(sys.argv) > 4 or len(sys.argv) < 2:
        show_help()
        user_input = " ".join(sys.argv[1:])
        logging.warning("number of arguments do not match- <" + user_input + ">")
        exit(1)
    command = sys.argv[1].lower()
    if command == "add":
        add_user(sys.argv[2:])
    if command == "del":
        remove_user(sys.argv[2:])
    if command == "list":
        list_users()
    if command == "help":
        show_help()
        exit(0)
    if command == "log":
        show_log()
        exit(0)
    sys.stderr.write("Unknown Command!")
    show_help()
    logging.warning("unknown command passed - <" + command + ">")
    exit(1)
