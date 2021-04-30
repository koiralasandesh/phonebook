import sys
import sqlite3


def add_user(argv):
    #print(argv)
    if len(argv) > 2 or len(argv) < 2:
        show_help()
        exit(1)
    print("maybe_added")
    exit(0)


def show_help():
    sys.stderr.write('''
        ---------------------------------------------------------------------------------
        Please Provide input in the following format:

        ADD <Name> <Telephone #>        Adds the person to database
        DEL <Name>                      Deletes the person to database
        DEL <Telephone #>               Deletes  the record with provided telephone number
        LIST                            Produces the list of all records in database
        ---------------------------------------------------------------------------------
    ''')


if __name__ == '__main__':
    # print(sys.argv)
    conn = sqlite3.connect("db/users.db")
    if len(sys.argv) > 4 or len(sys.argv) < 2:
        show_help()
        exit(1)
    command = sys.argv[1].lower()
    if command == "add":
        add_user(sys.argv[2:])
    if command == "del":
        remove_user(sys.argv[2:])
    if command == "list":
        list_users()
    sys.stderr.write("Unknown Command!")
    show_help()
    exit(1)
